class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        group = [1]
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                group[-1] += 1
            else:
                group.append(1)

        ans = 0
        for i in range(0, len(group) - 1):
            ans += min(group[i], group[i+1])

        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.countBinarySubstrings('110'))
    # print(s.judge('11'))

