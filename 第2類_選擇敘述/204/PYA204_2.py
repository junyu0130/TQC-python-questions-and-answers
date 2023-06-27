'''
204 算術運算
請使用選擇敘述撰寫一程式，讓使用者輸入兩個整數a、b，
然後再輸入一算術運算子(+、-、*、/、//、%)，輸出經過運算後的結果。
'''
a = int(input())
b = int(input())
op = input()

if op == '+':
  print(f"{a + b}")
elif op == '-':
  print(f"{a - b}")
elif op == '*':
  print(f"{a * b}")
elif op == '/':
  print(f"{a / b}")
elif op == '//':
  print(f"{a // b}")
elif op == '%':
  print(f"{a % b}")
else:
  print(None)
