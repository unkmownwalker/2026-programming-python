nums_input = input("nums = ").strip()
target = int(input("target = ").strip())
nums_str = nums_input.strip('[]')
nums = [int(x.strip()) for x in nums_str.split(',')]
n=len(nums)
for i in range(0,n):
    for j in range(i+1,n):
        if nums[i]+nums[j]==target:
            a=i
            b=j
output=[]
output.append(a)
output.append(b)
print(output)
#用哈希表，字典降低复杂度