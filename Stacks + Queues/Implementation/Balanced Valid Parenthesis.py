class Solution:

    def isValid(self, s: str) -> bool:
        """
        T.C. : O(n)
        S.C. : O(n)
        """
        st = []
        for i in s:
            if i == "(":
                st.append(')')
            elif i == "{":
                st.append("}")
            elif i == "[":
                st.append("]")
            elif ((len(st) == 0) or (st.pop() != i)):
                return False
        return len(st) == 0
