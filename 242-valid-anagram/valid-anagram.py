class Solution(object):
    def isAnagram(self, s, t):

        anagram = True
        frequency_str1 = {}
        frequency_str2 = {}
        
        if len(t) != len(s):
            return False

        for ch in s:
            count = 0
            if ch not in frequency_str1:
                count += 1
                frequency_str1[ch] = count
            else:
                frequency_str1.update({ch:frequency_str1.get(ch)+1})

        for ch in t:
            count = 0
            if ch not in frequency_str2:
                count += 1
                frequency_str2[ch] = count
            else:
                frequency_str2.update({ch:frequency_str2.get(ch)+1})

        return frequency_str1 == frequency_str2

        #return anagram