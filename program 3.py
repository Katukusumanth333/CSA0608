nums = [1,2,1]
n = len(nums)
result=0
for i in range(n):
    distinct = set()
    for j in range(i,n):
        distinct.add(nums[j])
        distinct_count = len(distinct)
        result += distinct_count**2
print(result)
