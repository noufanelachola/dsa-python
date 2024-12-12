class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        low = 0
        high = min(len(s) for s in strs)
        
        def isPrefix(length):
            prefix = strs[0][:length]
            
            for s in strs:
                if s[:length] != prefix:
                    return False
            return True
        
        while low <= high:
            mid = (low+high)//2

            if isPrefix(mid):
                low = mid+1
            else :
                high = mid-1

        return strs[0][:high]


s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))