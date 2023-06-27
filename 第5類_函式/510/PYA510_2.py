'''
510 費氏數列
請撰寫一程式，計算費氏數列 (Fibonacci numbers)，
使用者輸入一正整數num (num >= 2)，
並將它傳遞給名為compute()的函式，此函式將輸出費氏數列前num個的數值。

提示：費氏數列的某一項數字是其前兩項的和，而且第0項為0，第一項為1，表示方式如下：
F[0] = 0
F[1] = 1
F[n] = F[n-1] + F[n-2]
'''

def fib(num):
  if num <= 1:
    return num
  else:
    return fib(num - 1) + fib(num - 2)

def compute(num):
  for i in range(num):
    print(f"{fib(i)}", end=' ')

num = int(input())

compute(num)
