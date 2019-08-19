'''Given a string, find the length of the longest substring without repeating characters.'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if s == ' ':
            return 1

        
        # store char from substring, referenced to check repeating chars
        # also will be used to index the repeating char, next index from repeating index will start the new substring
        arr = []
        
        # two pointers, to keep trace of start and end of substring
        strt = 0
        end = -1
        
        substr_len = 0

        # one pass
        for i in s:
            if i in arr:
                # add substring length
                substr_len = end-strt+1 if end-strt+1 > substr_len else substr_len
                #substr_len.append(end-strt+1)
                # update start pointer for new substring
                strt += arr.index(i) + 1 
                # delete all elements that occurred before repeating char
                del arr[0:arr.index(i)+1]
                
            arr.append(i)
            end += 1
        
        #substr_len.append(end-strt+1)
        substr_len = end-strt+1 if end-strt+1 > substr_len else substr_len

        return substr_len

a = Solution()
print(a.lengthOfLongestSubstring("pwwekw"))