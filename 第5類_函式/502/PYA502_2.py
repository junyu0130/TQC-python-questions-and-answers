'''
502 乘積
請撰寫一程式，將使用者輸入的兩個整數作為參數
傳遞給一個名為compute(x, y)的函式，此函式將回傳x和y的乘積。
'''

def compute(x, y):
  return x * y

num = [int(input()) for i in range(2)]

print(compute(num[0], num[1]))
