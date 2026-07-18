class Solution:
    def longestValidParentheses(self, s: str) -> int:

         #st means stack
         #m_len means maximum_length
        st = [-1]
        m_len = 0

        for i in range(len(s)):
            if s[i] == "(":
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    m_len = max(m_len, i - st[-1])
        return m_len







            
        