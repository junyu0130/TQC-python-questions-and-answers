'''
604 眾數
請撰寫一程式，讓使用者輸入十個整數作為樣本數，
輸出眾數 (樣本中出現最多次的數字)及其出現的次數。

提示：假設樣本中只有一個眾數。
'''

nums = [int(input()) for i in range(10)]
count = [nums.count(nums[i]) for i in range(10)]

# print(nums)
# print(count)

print(nums[count.index(max(count))])
print(max(count))
