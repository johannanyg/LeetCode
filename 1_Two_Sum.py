from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_list = []
        for idx in range(len(nums)):
            for i in range(idx+1,len(nums)):
                add = nums[idx]+nums[i]
                if add == target:
                    index_list = [idx,i]
                    return index_list
        return []
    

####### local run ########################
'''
def main():

    nums = [2, 11, 7, 15]
    target = 9

    solution = Solution()

    result = solution.twoSum(nums, target)
    print("Result:", result)

if __name__=="__main__":
    main()
    '''
