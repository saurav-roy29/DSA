def solution(nums, target):
    start = 0
    end = len(nums)-1

    while start <= end:
        res = nums[start] + nums[end]
        if res < target:
            start+=1
        elif res > target:
            end-=1
        else:
            return ([start+1, end+1])

if __name__ == "__main__":
    numbers = [2,7,11,15]
    target = 9
    print(solution(numbers, target))
