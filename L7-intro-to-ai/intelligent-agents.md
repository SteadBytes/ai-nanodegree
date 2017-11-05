# Intelligent Agents
Intelligence should be defined in the context of a task or problem domain.

Intelligent Agent = takes actions to maximise its expected utility given a desired goal
* This is rational behaviour and requires the agent to behave optimally

Optimal behaviour is **not always possible** due to constraints in the problem such as running time, partially observable environment, computational limits. 

Use **bounded optimality** as a practical and feasible way of defining intelligence:
* Route finding agent to always find a route **within 5 miles** of the optimal.
* Chess playing agent to win **60%** of the time against a human player.

**Agent** = Intelligent system/software
* i.e a Roomba
**Environment** = Problem Domain
* i.e floor, obstacles **not** paintings on wall
**State** = Information stored and used that are necessary to accomplish task
* i.e current position, areas already cleaned etc
* **Goal State** = state that would be acceptable for the finished task.

**Perception** = agent sensing the properties of the environment
**Action** = useful output in order to change the state of the environment
**Cognition** = process by which an agent decides which action to take based on its perceived inputs

Perception and action are more relevant with agents interacting in the real world - automated cars etc.

**Reactive/Behaviour Based Agents** = agents directly associate actions with perceptions or very simple pre-programmed behaviours.
* Complex behaviour can be achieved by layering simple reactive control in a hierarchy

Some agents perform non-trivial processing to make 'decisions' - game playing agents/path finders etc
* Further classification can be done based on type of processing - i.e. knowledge based agents, planning agents, learning agents etc
