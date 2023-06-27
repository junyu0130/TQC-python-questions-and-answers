'''
302 迴圈偶數連加
請使用迴圈敘述撰寫一程式，讓使用者輸入兩個正整數a、b (a < b)，
利用迴圈計算從a開始的偶數連加到b的總和。
例如：輸入a=1、b=100，則輸出結果為2550（2 + 4 + … + 100 = 2550）。
'''
a = eval(input())
b = eval(input())
add = 0
# TODO
for i in range(a, b + 1):
  if i % 2 == 0:
    add += i

print(add)

#print(sum(filter(lambda x: x % 2 == 0, range(a, b + 1))))