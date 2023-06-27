'''
302 迴圈偶數連加
請使用迴圈敘述撰寫一程式，讓使用者輸入兩個正整數a、b (a < b)，
利用迴圈計算從a開始的偶數連加到b的總和。
例如：輸入a=1、b=100，則輸出結果為2550（2 + 4 + … + 100 = 2550）。
'''

a = int(input())
b = int(input())
sum = 0

for num in range(a, b + 1):
  if num % 2 == 0:
    sum += num

print(sum)
