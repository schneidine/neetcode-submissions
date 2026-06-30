class Solution:
    # This solution is incorrect since I did not verify the frequency of the letters.
    def isAnagram(self, s: str, t: str) -> bool:        
        # Edge cases
        if not s or not t:
            return False

        # create a dictionary    
        word1 = {}
        word2= {}

        # Add first world to dictionary
        for letter in s:
            if letter in word1:
                word1[letter] += 1
            else:
                word1[letter] = 1

        # add all the letters of one word to the dictionary
        for l in t:
            if l in word2:
                word2[l] += 1
            else:
                word2[l] = 1

        if word1 == word2:
            return True
        else:
            return False