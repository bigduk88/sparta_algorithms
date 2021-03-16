num = int(input())

nums = []
for i in range(num):
    nums.append(int(input()))

nums = sorted(nums)

for i in range(num):
    print(nums[i])

    