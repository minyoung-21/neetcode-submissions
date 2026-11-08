class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k%=n
        count = index = current = 0

        while count < n:
            prev = nums[current]
            start = current
            print(current)
            while True:
                index = (current + k) % n
                nums[index], prev =  prev, nums[index]
                current = index
                count += 1
                #print(current, prev)
                #get here more often if k and n has mod that is 0
                # ex) k = 3, n = 6
                if current == start:
                    break

            # 
            current += 1