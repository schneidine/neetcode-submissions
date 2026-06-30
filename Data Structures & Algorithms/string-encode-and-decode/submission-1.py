class Solution:
    # Encode each string into string with delimiter and num of chars to come
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        i=0
        for word in strs:
            encoded = encoded+str(len(word))+"$"+strs[i]
            i+=1

        return encoded

    def decode(self, s: str) -> List[str]:
        strs=[]
        i=0

        while i < len(s):
            word = ""
            length = ""
            while s[i] != "$":
                length += s[i]
                i+= 1
            # should be at delimiter i  
            charLen = int(length)
            word = s[i+1:i+charLen+1]
            strs.append(word)
            i+=charLen+1

        return strs