class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        """
        T.C. : O(n+k)
        S.C. : O(n)
        """
        st = []
        for i in nums:
            while st and k > 0 and st[-1] > i:
                st.pop()
                k -= 1
            st.append(i)
        while st and k > 0:
            st.pop()
            k -= 1
        if not st:
            return "0"
        ans = ""
        while st:
            ans += st.pop()
        ans = ans.rstrip("0")
        return ans[::-1] if ans else "0"
