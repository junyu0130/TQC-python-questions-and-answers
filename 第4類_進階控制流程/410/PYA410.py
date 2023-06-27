'''
410 繪製等腰三角形
請撰寫一程式，依照使用者輸入的n，畫出對應的等腰三角形。
'''
n = eval(input())

for i in range(n):
  for j in range(n - i - 1, 0, -1):
    print(' ', end='')
  for k in range(1, 2 * i + 2):
    print('*', end='')
  print()

'''
for i in range(n):
  print('.' * (n - i - 1), '*' * (2 * i + 1), sep='')
'''
