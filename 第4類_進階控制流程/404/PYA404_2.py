'''
404 數字反轉判斷
請撰寫一程式，讓使用者輸入一個正整數，
將此正整數以反轉的順序輸出，並判斷如輸入0，則輸出為0。
'''

nums = list(input())

nums.reverse()

for num in nums:
  print(num, end='')
