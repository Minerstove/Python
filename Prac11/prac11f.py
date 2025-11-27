class OneToOneCorrespondence:
    def __init__(self, *pairs):
        self.agent_to_spy = {}
        self.spy_to_agent = {}

        for agent, spy in pairs:
            if agent in self.agent_to_spy or spy in self.spy_to_agent:
                raise ValueError()
            self.agent_to_spy[agent] = spy
            self.spy_to_agent[spy] = agent

    def get_right(self, v):
        # v is an agent name
        if v not in self.agent_to_spy:
            raise ValueError()
        return self.agent_to_spy[v]

    def get_left(self, v):
        # v is a spy name
        if v not in self.spy_to_agent:
            raise ValueError()
        return self.spy_to_agent[v]
    
    def set_pair(self, l, r):
        # l = agent, r = spy
        if l in self.agent_to_spy or r in self.spy_to_agent:
            raise ValueError()
        self.agent_to_spy[l] = r
        self.spy_to_agent[r] = l
        return None
    
    def remove_pair_with_left(self, v):
        # v is an agent name
        if v not in self.agent_to_spy:
            raise ValueError()
        spy = self.agent_to_spy.pop(v)
        del self.spy_to_agent[spy]
        return None
    
    def remove_pair_with_right(self, v):
        # v is a spy name
        if v not in self.spy_to_agent:
            raise ValueError()
        agent = self.spy_to_agent.pop(v)
        del self.agent_to_spy[agent]
        return None