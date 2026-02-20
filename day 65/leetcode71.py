class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False

        st = []

        for ch in s:   # list(s) ki need nahi
            # sirf opening bracket push karo
            if ch == '(' or ch == '[' or ch == '{':
                st.append(ch)
            else:
                if len(st) == 0:
                    return False

                top = st.pop()

                if top == '(' and ch != ')':
                    return False
                if top == '[' and ch != ']':
                    return False
                if top == '{' and ch != '}':
                    return False

        if len(st) == 0:
            return True
        return False


# VS Code me run karne ke liye
obj = Solution()
print(obj.isValid("()"))     # True
print(obj.isValid("([)]"))   # False
print(obj.isValid("{[]}"))   # True