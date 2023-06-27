'''
304 迴圈倍數總和
請使用迴圈敘述撰寫一程式，讓使用者輸入一個正整數a，
利用迴圈計算從1到a之間，所有5之倍數數字總和。
'''

a = int(input())
sum = 0

for num in range(1, a + 1):
  if num % 5 == 0:
    sum += num

print(sum)
