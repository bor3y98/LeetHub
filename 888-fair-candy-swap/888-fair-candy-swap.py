class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum1=sum(aliceSizes)
        total_sum = sum1 + sum(bobSizes)
        median = total_sum/2
        dict_alices = {}
        dict_bob = {}
        for item in aliceSizes:
            dict_alices[item-sum1]=item
        print(dict_alices)
        for item in bobSizes:
            dict_bob[item]=int(item-median)

            if dict_bob[item] in dict_alices:
                print(dict_bob[item])
                print(dict_alices[dict_bob[item]])

                return[dict_alices[dict_bob[item]],item]