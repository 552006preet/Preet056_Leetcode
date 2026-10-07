class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(string):
            count = 0

            for ch in string:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                if count < 0:
                    return False

            return count == 0

        level = {s}

        while level:
            valid = []

            for string in level:
                if isValid(string):
                    valid.append(string)

            if valid:
                return valid

            next_level = set()

            for string in level:
                for i in range(len(string)):
                    if string[i] not in '()':
                        continue

                    new_string = string[:i] + string[i + 1:]
                    next_level.add(new_string)

            level = next_level

        return [""]