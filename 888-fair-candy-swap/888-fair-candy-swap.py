class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        optimal_sum = int((sum(aliceSizes) + sum(bobSizes)) / 2)
        print('optimal_sum')
        print(optimal_sum)
        if sum(aliceSizes) > sum(bobSizes):
            diff_sum = sum(aliceSizes) - optimal_sum
            large_arr = aliceSizes
            small_arr = bobSizes
            first = True
        else:
            diff_sum = sum(bobSizes) - optimal_sum
            large_arr = bobSizes
            small_arr = aliceSizes
            first = False
        print('diff_sum')
        print(diff_sum)
            
        # target_element = optimal_sum - diff_sum
        # print('target_element')
        print('large_arr')
        print(large_arr)
        print(small_arr)
        
        for element in large_arr:
            if element - diff_sum in small_arr:
                print(element)
                print(diff_sum)
                if not first:
                    return [element - diff_sum, element]
                return [element, element - diff_sum]
            
        