class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = [0] * 26
        count2 = [0] * 26

        for char in s1:
            count1[ord(char) - ord('a')] += 1
        
        window_size = len(s1)

        for ind in range(len(s2)):
            count2[ord(s2[ind]) - ord('a')] += 1

            if ind >= window_size:
                count2[ord(s2[ind-window_size]) - ord('a')] -= 1

            if count1 == count2:
                return True
        return False