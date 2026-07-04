class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}  #creating an empty dictionary to store the frequency of nums with their key values

        for num in nums:  #iterating for each number in the numbers list

            if num in freq:  # checking whether the number is already in the freq dict{}
                freq[num] += 1  # if yes, increment it by 1

            else:

                freq[num] = 1  #else, keep it same as one

        result = []    # creating an emoty array to showcasing endresults 

        for _ in range(k):  #iterating k times to get the highest values upto k times 

            max_freq = max(freq, key = freq.get)  # to find the highest repeated number

            result.append(max_freq) # appending the highest value with the results

            del freq[max_freq] # removing the Highest number to get the next highest and the loop continues upto k times


        return result            


#the time complexity here is - O(n + k*m)




        
        