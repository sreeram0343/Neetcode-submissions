class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        for num in nums:

            if num in freq:
                freq[num] += 1

            else:

                freq[num] = 1

        result = []

        for _ in range(k):

            max_freq = max(freq, key = freq.get)

            result.append(max_freq)

            del freq[max_freq]


        return result            





        
        