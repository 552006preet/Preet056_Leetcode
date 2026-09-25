class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        
        def dfs(s):
            res = {""}
            cur = set()
            i = 0

            while i < len(s):
                if s[i] == ',':
                    cur |= res
                    res = {""}
                    i += 1

                elif s[i] == '{':
                    j = i
                    balance = 0

                    while j < len(s):
                        if s[j] == '{':
                            balance += 1
                        elif s[j] == '}':
                            balance -= 1

                        if balance == 0:
                            break
                        j += 1

                    words = dfs(s[i + 1:j])

                    res = {a + b for a in res for b in words}
                    i = j + 1

                else:
                    j = i
                    while j < len(s) and s[j].isalpha():
                        j += 1

                    word = s[i:j]
                    res = {a + word for a in res}
                    i = j

            return cur | res

        return sorted(dfs(expression))