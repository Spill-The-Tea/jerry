class NagHashTable():
    def __init__(self):
        self.dict = {1: "!",
                     2: "?",
                     3: "!!",
                     4: "??",
                     5: "!?",
                     6: "?!",
                     7: "□",
                     10: "=",
                     13: "∞",
                     14: "⩲",
                     15: "⩱",
                     16: "±",
                     17: "∓",
                     18: "+-",
                     19: "-+",
                     22: "⨀",
                     23: "⨀",
                     32: "⟳",
                     33: "⟳",
                     36: "→",
                     37: "→",
                     40: "↑",
                     41: "↑",
                     44: "=/∞",
                     45: "∞/=",
                     132: "⇆",
                     133: "⇆"
                    }

    def nag_to_str(self,nag):
        try:
            return self.dict[nag]
        except KeyError:
            return ""