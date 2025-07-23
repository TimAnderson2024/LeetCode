class Solution(object):
    def topKFrequent(self, nums, k):
        hashmap = {}
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)

        freq_map = [[] for _ in range(0, len(nums) + 1)]
        for num, freq in hashmap.items():
            freq_map[freq].append(num)

        top_k = []
        for freq in reversed(freq_map):
            for num in freq:
                top_k.append(num)
                if len(top_k) == k:
                    return top_k
