'''
608 最大最小值索引
請撰寫一程式，讓使用者建立一個3*3的矩陣，
其內容為從鍵盤輸入的整數（不重複），接著輸出矩陣最大值與最小值的索引。
'''

arr = [int(input()) for i in range(9)]

print(f"Index of the largest number {max(arr)} is: ({arr.index(max(arr)) // 3}, {arr.index(max(arr)) % 3})")
print(f"Index of the smallest number {min(arr)} is: ({arr.index(min(arr)) // 3}, {arr.index(min(arr)) % 3})")

"""
Index of the largest number _ is: (_, _)
Index of the smallest number _ is: (_, _)
"""
