# perturbations = self.rescale( dist.probs, adv_dist.probs )
                    # perturbations = [ self.apply_budget_constraint(x, y, z[0] ).cpu().numpy() for (x,y,z) in zip(dist.probs, perturbations, remaining_budget)  ]
                    # perturbations = Categorical(probs = torch.tensor(perturbations,  device = 'cuda') )

                    # dist_agent, value_agent = self.acmodel(sb.obs)
                    # dist_adv, value = self.acmodel_adversary( sb.inputs_adversary )
                    # dist = self.rescale( dist_agent.probs, dist_adv.probs )
                    #print('raw: ' + str(dist.probs) )
                    #scaled_dist = dist.probs / (dist_agent.probs * dist.probs).sum() 
                    #print('scaled: ' + str(scaled_dist) )
                    # si on a que raw_preds >= 0 partout
                    # (avec une sortie exp ou relu par exemple), il suffit de ramener la somme à 1
                    # pour générer une distribution (perturbed_probas = raw_probas * scaled_preds).
                    # print(dist.log_prob( sb.action ))
                    # print(sb.log_prob)
                    #policy_loss = policy_loss.mean()
                    #format_constraint =  1 - torch.sum( dist_agent.probs * dist.probs, 1 )
                    #print(format_constraint) #+ 0.005 * format_constraint

   
    # def _hypothetical_transition(self, policy_action):
    #     reward = -1
    #     done = False

    #     next_pos = self.agent_pos + self.ACTION_DIR_VEC[policy_action] #add the new (x,y) coordinates to the current position

    #     if self._is_oob(next_pos): # check if out-of-box
    #         next_pos = self.agent_pos

    #     next_cell = self.grid.get(*next_pos)

    #     if next_cell != None and next_cell.type == "goal":
    #         done = True
    #         reward = 20

    #     if next_cell != None and next_cell.type == "lava":
    #         done = True
    #         reward = -20

    #     reward = reward / 20

    #     return next_pos, reward, done

    # def _get_transition_porbabilities(self, action):

    #     """
    #     Method called in step_policy() to get the possible next states, rewards, dones and their probas.
    #     Returns lists respectively containing a transition proba, its next state, its reward and if it is a terminal state.
        
    #     The stochasticity is defined as the agent following its selected action with probability 1 - delta
    #     and taking any of the 3 other possible actions with proba delta/3.
    #     """

        #print(acmodel)

        # with torch.no_grad():
        #     if self.acmodel.recurrent:
        #         dist, value, memory = self.acmodel(preprocessed_obs, self.memory * self.mask.unsqueeze(1))
        #     else:
        #         dist, value = self.acmodel(preprocessed_obs)

        # print(dist)

        # chosen_proba = 1 - self.delta
        # random_proba = (  self.delta / 3  )  # Since we have 4 actions, each non-selected action has p=delta/3 of being sampled
        # transition_probas = [random_proba] * 4
        # transition_probas[action] = chosen_proba
        
        # states, rewards, dones = [] * 4, [] * 4, [] * 4
        # for possible_action in self.pol_action_space:
        #     next_pos, reward, done = self._hypothetical_transition(possible_action)
        #     states[possible_action] = next_pos
        #     rewards[possible_action] = reward
        #     dones[possible_action] = done

        #transition_probas = [0.25, 0.25, 0.25, 0.25 ]

        #return transition_probas #, states, rewards, dones


    # def _make_transition(self, adversary_perturbation):

    #     states, state_idxs, probas = self._get_transitions(action)

    #     perturbed_probas, perturbations = self._get_adversarial_perturbation( states, state_idxs, probas  )

    #     sampled_idx = np.random.choice(len(perturbed_probas), p=perturbed_probas)

    #     """
    #     TODO:
    #     1. Ensure adversary_perturbation is not over budget and generates a distribution
    #        (i.e. adversary_perturbation * self.probas sums up to 1)
    #     2. Sample the next state and reward from the perturbed transition probas. Return them.
    #     """

    #     return agent_pos, reward, done

    # @property
    # def torch_adv_state(self):
    #     torch_state = torch.tensor(self.agent_pos, dtype=float)
    #     torch_probas = torch.tensor(self.probas, dtype=float)
    #     torch_budget = torch.tensor([self.remaining_budget], dtype=float)
    #     return torch.hstack( [torch_state, torch_probas, torch_budget] )

    # def gen_adv_obs(self):
    #     obs = {  "state": self.torch_adv_state, "remaining_budget": self.remaining_budget  }
    #     return obs

    # def gen_pol_obs(self):
    #     obs = {"position": self.agent_pos }
    #     return obs
