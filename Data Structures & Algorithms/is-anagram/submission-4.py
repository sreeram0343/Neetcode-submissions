class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):  #First checking the length of two strings are equal
            return False      #If not equal, then returning False

        countS, countT = {}, {}   # Creating two empty dictionaries to count the number of characters in each string

        for i in range(len(s)):   #iterate in range of total characters in the string

            countS[s[i]] = 1 + countS.get(s[i], 0)    # Incrementing the value of dict{} by one for each character
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:     # Now iterating each charaters in a String
            if countS[c] != countT.get(c, 0):  # Checking whether the characters of String S is equals to String T
                return False 


        return True #Returning the booleans respectively


# The Time complexity of this solution is O(N) + O(N) + O(1):
            # Time complexity = O(2N + 1)  =  O(N)
                  