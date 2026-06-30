class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #  Edge cases - one string or no strings
        if (len(strs) == 0):
            return [[""]]

        if len(strs) == 1:
            return [[strs[0]]]

        # This Solution - Find out the frequency of each character, store in array
        # and make that array the key to a hash function, and array of agreeable values the value

        mydict = {} # create a new dictionary/hashmap

        for s in strs:
            # create array of 0 values
            arr = [0] *26
            
            # fill the frequency array for this string
            for char in s:
                arr[ord(char)-ord('a')] +=1

            # if the array isn't in ther add it and update its value to be the string
            if tuple(arr) not in mydict:
                mydict[tuple(arr)] = [s]
            else: 
                mydict[tuple(arr)].append(s) # if it is in there, append the new string to the value

        # return a list of our dictionary's values
        return list(mydict.values())
            


        