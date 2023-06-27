'''
504 次方計算
請撰寫一程式，讓使用者輸入兩個整數，
接著呼叫函式compute()，此函式接收兩個參數a、b，並回傳a^b的值。
'''

def compute(a, b):
  return a**b

x = eval(input())
y = eval(input())

print(compute(x, y))
