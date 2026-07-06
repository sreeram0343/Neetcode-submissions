from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Step 1: Count frequency of each number
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1


        # Step 2: Create frequency buckets
        bucket = [[] for _ in range(len(nums) + 1)]


        # Step 3: Group numbers according to their frequency
        for num, count in freq.items():
            bucket[count].append(num)


        # Step 4: Collect elements from highest frequency
        result = []

        for count in range(len(bucket) - 1, 0, -1):

            for num in bucket[count]:
                result.append(num)

                if len(result) == k:
                    return result