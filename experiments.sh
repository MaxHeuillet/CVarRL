#!/bin/bash



python3 /home/mheuillet/Desktop/CARL2/rl-starter-files/train.py --algo ppo --model experiment5_1_0.05_0.5 --budget 1 --stochasticity 0.05 --cost 0.5 --frames 5000000 --save-interval 10
python3 /home/mheuillet/Desktop/CARL2/rl-starter-files/evaluate.py --model experiment5_1_0.05_0.5 --cost 0.5 --stochasticity 0.05 --type 5m --episodes 100000

python3 /home/mheuillet/Desktop/CARL2/rl-starter-files/train.py --algo ppo --model experiment5_5_0.05_0.5 --budget 5 --stochasticity 0.05 --cost 0.5 --frames 5000000 --save-interval 10
python3 /home/mheuillet/Desktop/CARL2/rl-starter-files/evaluate.py --model experiment5_5_0.05_0.5 --cost 0.5 --stochasticity 0.05 --type 5m --episodes 100000

python3 /home/mheuillet/Desktop/CARL2/rl-starter-files/train.py --algo ppo --model experiment5_10_0.05_0.5 --budget 10 --stochasticity 0.05 --cost 0.5 --frames 5000000 --save-interval 10
python3 /home/mheuillet/Desktop/CARL2/rl-starter-files/evaluate.py --model experiment5_10_0.05_0.5 --cost 0.5 --stochasticity 0.05 --type 5m --episodes 100000

python3 /home/mheuillet/Desktop/CARL2/rl-starter-files/train.py --algo ppo --model experiment5_25_0.05_0.5 --budget 25 --stochasticity 0.05 --cost 0.5 --frames 5000000 --save-interval 10
python3 /home/mheuillet/Desktop/CARL2/rl-starter-files/evaluate.py --model experiment5_25_0.05_0.5 --cost 0.5 --stochasticity 0.05 --type 5m --episodes 100000

python3 /home/mheuillet/Desktop/CARL2/rl-starter-files/train.py --algo ppo --model experiment5_50_0.05_0.5 --budget 50 --stochasticity 0.05 --cost 0.5 --frames 5000000 --save-interval 10
python3 /home/mheuillet/Desktop/CARL2/rl-starter-files/evaluate.py --model experiment5_50_0.05_1 --cost 0.5 --stochasticity 0.05 --type 5m --episodes 100000

python3 /home/mheuillet/Desktop/CARL2/rl-starter-files/train.py --algo ppo --model experiment5_100_0.05_0.5 --budget 100 --stochasticity 0.05 --cost 0.5 --frames 5000000 --save-interval 10
python3 /home/mheuillet/Desktop/CARL2/rl-starter-files/evaluate.py --model experiment5_100_0.05_0.5 --cost 0.5 --stochasticity 0.05 --type 5m --episodes 100000

python3 /home/mheuillet/Desktop/CARL2/rl-starter-files/train.py --algo ppo --model experiment5_300_0.05_0.5 --budget 300 --stochasticity 0.05 --cost 0.5 --frames 5000000 --save-interval 10
python3 /home/mheuillet/Desktop/CARL2/rl-starter-files/evaluate.py --model experiment5_300_0.05_0.5 --cost 0.5 --stochasticity 0.05 --type 5m --episodes 100000





#python3 /home/mheuillet/Desktop/CARL2/rl-starter-files/train.py --algo ppo --model experiment3_1_0.15_0.7 --budget 1 --stochasticity 0.15 --cost 0.7 --frames 5000000 --save-interval 10
#python3 /home/mheuillet/Desktop/CARL2/rl-starter-files/evaluate.py --model experiment3_1_0.15_0.7 --cost 0.7 --stochasticity 0.15 --type 2m --episodes 100000
#python3 /home/mheuillet/Desktop/CARL2/rl-starter-files/evaluate.py --model experiment3_1_0.15_0.7 --cost 0.7 --stochasticity 0.15 --type 5m --episodes 100000

#python3 /home/mheuillet/Desktop/CARL2/rl-starter-files/train.py --algo ppo --model experiment3_5_0.15_0.7 --budget 5 --stochasticity 0.15 --cost 0.7 --frames 5000000 --save-interval 10
#python3 /home/mheuillet/Desktop/CARL2/rl-starter-files/evaluate.py --model experiment3_5_0.15_0.7 --cost 0.7 --stochasticity 0.15 --type 2m --episodes 100000
#python3 /home/mheuillet/Desktop/CARL2/rl-starter-files/evaluate.py --model experiment3_5_0.15_0.7 --cost 0.7 --stochasticity 0.15 --type 5m --episodes 100000

#python3 /home/mheuillet/Desktop/CARL2/rl-starter-files/train.py --algo ppo --model experiment3_10_0.15_0.7 --budget 10 --stochasticity 0.15 --cost 0.7 --frames 5000000 --save-interval 10
#python3 /home/mheuillet/Desktop/CARL2/rl-starter-files/evaluate.py --model experiment3_10_0.15_0.7 --cost 0.7 --stochasticity 0.15 --type 2m --episodes 100000
#python3 /home/mheuillet/Desktop/CARL2/rl-starter-files/evaluate.py --model experiment3_10_0.15_0.7 --cost 0.7 --stochasticity 0.15 --type 5m --episodes 100000

#python3 /home/mheuillet/Desktop/CARL2/rl-starter-files/train.py --algo ppo --model experiment3_25_0.15_0.7 --budget 25 --stochasticity 0.15 --cost 0.7 --frames 5000000 --save-interval 10
#python3 /home/mheuillet/Desktop/CARL2/rl-starter-files/evaluate.py --model experiment3_25_0.15_0.7 --cost 0.7 --stochasticity 0.15 --type 2m --episodes 100000
#python3 /home/mheuillet/Desktop/CARL2/rl-starter-files/evaluate.py --model experiment3_25_0.15_0.7 --cost 0.7 --stochasticity 0.15 --type 5m --episodes 100000

#python3 /home/mheuillet/Desktop/CARL2/rl-starter-files/train.py --algo ppo --model experiment3_50_0.15_0.7 --budget 50 --stochasticity 0.15 --cost 0.7 --frames 5000000 --save-interval 10
#python3 /home/mheuillet/Desktop/CARL2/rl-starter-files/evaluate.py --model experiment3_50_0.15_0.7 --cost 0.7 --stochasticity 0.15 --type 2m --episodes 100000
#python3 /home/mheuillet/Desktop/CARL2/rl-starter-files/evaluate.py --model experiment3_50_0.15_0.7 --cost 0.7 --stochasticity 0.15 --type 5m --episodes 100000

#python3 /home/mheuillet/Desktop/CARL2/rl-starter-files/train.py --algo ppo --model experiment3_100_0.15_0.7 --budget 100 --stochasticity 0.15 --cost 0.7 --frames 5000000 --save-interval 10
#python3 /home/mheuillet/Desktop/CARL2/rl-starter-files/evaluate.py --model experiment3_100_0.15_0.7 --cost 0.7 --stochasticity 0.15 --type 2m --episodes 100000
#python3 /home/mheuillet/Desktop/CARL2/rl-starter-files/evaluate.py --model experiment3_100_0.15_0.7 --cost 0.7 --stochasticity 0.15 --type 5m --episodes 100000

#python3 /home/mheuillet/Desktop/CARL2/rl-starter-files/train.py --algo ppo --model experiment3_300_0.15_0.7 --budget 300 --stochasticity 0.15 --cost 0.7 --frames 5000000 --save-interval 10
#python3 /home/mheuillet/Desktop/CARL2/rl-starter-files/evaluate.py --model experiment3_300_0.15_0.7 --cost 0.7 --stochasticity 0.15 --type 2m --episodes 100000
#python3 /home/mheuillet/Desktop/CARL2/rl-starter-files/evaluate.py --model experiment3_300_0.15_0.7 --cost 0.7 --stochasticity 0.15 --type 5m --episodes 100000

#python3 /home/mheuillet/Desktop/CARL2/rl-starter-files/train.py --algo ppo --model experiment3_1000_0.15_0.7 --budget 1000 --stochasticity 0.15 --cost 0.7 --frames 5000000 --save-interval 10
#python3 /home/mheuillet/Desktop/CARL2/rl-starter-files/evaluate.py --model experiment3_1000_0.15_0.7 --cost 0.7 --stochasticity 0.15 --type 2m --episodes 100000
#python3 /home/mheuillet/Desktop/CARL2/rl-starter-files/evaluate.py --model experiment3_1000_0.15_0.7 --cost 0.7 --stochasticity 0.15 --type 5m --episodes 100000





