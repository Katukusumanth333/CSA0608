nums1=[2,3,2]
nums2=[1,2]
answer1 = len([i for i in nums1 if i in nums2])
answer2 = len([i for i in nums2 if i in nums1])
result = [answer1, answer2]
print(result)
