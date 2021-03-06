import argparse
import time
import torch
from torch_ac.utils.penv import ParallelEnv
import numpy as np; np.random.seed(0)
import seaborn as sns; sns.set_theme()
import utils
import pickle as pkl
import gzip
import os



# Parse arguments

parser = argparse.ArgumentParser()

parser.add_argument("--model", required=True,
                    help="name of the trained model (REQUIRED)")
parser.add_argument("--stochasticity", required=True,
                    help="amount of stochasticity")
parser.add_argument("--type", required=True,
                    help="whether with 2m or 5m trajectories in the training")
parser.add_argument("--cost", required=True,
                    help="cost for each moove")
parser.add_argument("--episodes", type=int, default=100,
                    help="number of episodes of evaluation (default: 100)")
parser.add_argument("--seed", type=int, default=0,
                    help="random seed (default: 0)")
parser.add_argument("--procs", type=int, default=16,
                    help="number of processes (default: 16)")
parser.add_argument("--argmax", action="store_true", default=False,
                    help="action with highest probability is selected")
parser.add_argument("--worst-episodes-to-show", type=int, default=10,
                    help="how many worst episodes to show")
parser.add_argument("--memory", action="store_true", default=False,
                    help="add a LSTM to the model")
parser.add_argument("--text", action="store_true", default=False,
                    help="add a GRU to the model")
args = parser.parse_args()

# Set seed for all randomness sources

utils.seed(args.seed)

# Set device

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Device: {device}\n")

# Load environments

envs = []
height = None
width = None
for i in range(args.procs):
    env = utils.make_env( 1, args.cost, args.seed + 10000 * i)
    height = env.height
    width = env.width
    envs.append(env)
env = ParallelEnv(envs)
print("Environments loaded\n")


# Load agent

model_dir = utils.get_model_dir(args.model)
agent = utils.Agent(env.observation_space, env.action_space, model_dir, type = args.type,
                    device=device, argmax=args.argmax, num_envs=args.procs,
                    use_memory=args.memory, use_text=args.text)
print("Agent loaded\n")

# Initialize logs

logs = {"num_frames_per_episode": [], "return_per_episode": []}

# Run agent

start_time = time.time()



obss = env.reset()

log_done_counter = 0
log_episode_return = torch.zeros(args.procs, device=device)
log_episode_num_frames = torch.zeros(args.procs, device=device)

position_history = []

while log_done_counter < args.episodes:

    agent_pos, _ = env._get_infos() 
    position_history.extend(agent_pos)
    actions = agent.get_actions(  agent_pos, args.stochasticity)
    
    state_dist =   [ [1,1,1,1] ] * len(actions)
    final_dist = [ [1,1,1,1] ] * len(actions)
    obss, rewards, dones, _ = env.step(actions, final_dist, state_dist, None , None)
    #agent.analyze_feedbacks(rewards, dones)

    log_episode_return += torch.tensor(rewards, device=device, dtype=torch.float)
    log_episode_num_frames += torch.ones(args.procs, device=device)

    for i, done in enumerate(dones):
        if done:
            log_done_counter += 1
            logs["return_per_episode"].append(log_episode_return[i].item())
            logs["num_frames_per_episode"].append(log_episode_num_frames[i].item())

    mask = 1 - torch.tensor(dones, device=device, dtype=torch.float)
    log_episode_return *= mask
    log_episode_num_frames *= mask

    print(log_done_counter)

end_time = time.time()

# Print logs

num_frames = sum(logs["num_frames_per_episode"])
fps = num_frames/(end_time - start_time)
duration = int(end_time - start_time)
return_per_episode = utils.synthesize(logs["return_per_episode"])
num_frames_per_episode = utils.synthesize(logs["num_frames_per_episode"])

print("F {} | FPS {:.0f} | D {} | R:????mM {:.2f} {:.2f} {:.2f} {:.2f} | F:????mM {:.1f} {:.1f} {} {}"
      .format(num_frames, fps, duration,
              *return_per_episode.values(),
              *num_frames_per_episode.values()))

# Print worst episodes

n = args.worst_episodes_to_show
if n > 0:
    print("\n{} worst episodes:".format(n))

    indexes = sorted(range(len(logs["return_per_episode"])), key=lambda k: logs["return_per_episode"][k])
    for i in indexes[:n]:
        print("- episode {}: R={}, F={}".format(i, logs["return_per_episode"][i], logs["num_frames_per_episode"][i]))

# get trajectory heat-maps

width = width - 2
height = height - 2

position_history = [ x.tolist() for x in position_history ]

map = np.zeros ( (width, height) )

for x in range(width):
    for y in range(height):
        map[ x, y ] = position_history.count( [x+1,y+1] )

with gzip.open( os.path.join('/home/mheuillet/Desktop/CARL2', '{}_{}_{}.pkl.gz'.format(args.model, args.stochasticity, args.type) )  ,'wb') as f:
    pkl.dump(map,f)