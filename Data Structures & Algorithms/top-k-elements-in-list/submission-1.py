class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        element_count = {}
        ret_list = []
        for number in nums:
            if number in element_count:
                element_count[number] += 1
            else:
                element_count[number] = 1
        element_count = dict(sorted(element_count.items(), key=lambda item: item[1], reverse = True))
        list_keys = list(element_count.keys())
        print(list_keys)

        for key in range(k):
            ret_list.append(list_keys[key])

        return ret_list




