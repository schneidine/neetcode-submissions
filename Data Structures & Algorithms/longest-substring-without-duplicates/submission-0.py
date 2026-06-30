class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # CREATE HASHSET, ADD ALL ELEMENTS TO HASHSET W INDEX, 
        # THEN IF U CATCH A DUPLICATE IN OUR WINDOW WE GOTTA JUMP LEFT TO
        # THAT POSITION
        if not s:
            return 0
        
        left = 0 
        result = 0 
        seen = {}

        for right in range (len(s)):

            char = s[right]

            if char not in seen:
                seen[char] = right
            else:
                if seen[char]>=left:
                    # update left index if needed
                    left = seen[char]+1

                # update last seen of this variable
                seen[char] = right
            
            result = max(result, right-left+1)
        
        return result
                


            