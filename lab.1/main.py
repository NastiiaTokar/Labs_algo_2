def is_monotonic(nums):
    increasing = decreasing = True
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            decreasing = False
        elif nums[i] < nums[i - 1]:
            increasing = False
    return increasing or decreasing

test_cases = [
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1, 2, 2, 3, 2, 4],
        [1, 1, 1, 1, 1],
        [10],
        [1, 3, 2]
    ]
    
for case in test_cases:
        result = is_monotonic(case)
        print(f"Масив {case} є монотонним: {result}")
