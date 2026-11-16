
def minOperations(nums: list[int], x: int) -> int:
    n = len(nums)
    target = sum(nums) - x

    if target < 0:
        return -1

    if target == 0:
        return n

    current_sum = 0
    max_len = 0
    left = 0

    for right in range(n):
        current_sum += nums[right]

        while current_sum > target:
            current_sum -= nums[left]
            left += 1

        if current_sum == target:
            max_len = max(max_len, right - left + 1)

    return -1 if max_len == 0 else n - max_len


# Test cases
print(minOperations([1, 1, 4, 2, 3], 5))  # 2
print(minOperations([5, 6, 7, 8, 9], 4))  # -1
print(minOperations([3, 2, 20, 1, 1, 3], 10))  # 5
print(minOperations([1, 1], 2))  # 2
