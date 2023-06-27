'''
604 眾數
請撰寫一程式，讓使用者輸入十個整數作為樣本數，
輸出眾數 (樣本中出現最多次的數字)及其出現的次數。

提示：假設樣本中只有一個眾數。
'''

num = [eval(input()) for i in range(10)]
count = [num.count(i) for i in num]

for i in range(10):
  if count[i] == max(count):
    print(num[i])
    print(count[i])
    break


# num = [int(input()) for i in range(10)]
# m=max(num, key = num.count)
# print(m)
# print(num.count(m))

