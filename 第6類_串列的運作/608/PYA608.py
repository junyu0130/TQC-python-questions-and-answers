'''
608 最大最小值索引
請撰寫一程式，讓使用者建立一個3*3的矩陣，
其內容為從鍵盤輸入的整數（不重複），接著輸出矩陣最大值與最小值的索引。
'''
num = [eval(input()) for i in range(9)]
arr = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

k = 0
for i in range(3):
  for j in range(3):
    arr[i][j] = num[k]
    k += 1

for i in range(3):
  for j in range(3):
    if arr[i][j] == max(num):
      print("Index of the largest number {} is: ({}, {})".format(max(num), i, j))
      break

for i in range(3):
  for j in range(3):
    if arr[i][j] == min(num):
      print("Index of the smallest number {} is: ({}, {})".format(min(num), i, j))
      break

"""
Index of the largest number _ is: (_, _)
Index of the smallest number _ is: (_, _)
"""
