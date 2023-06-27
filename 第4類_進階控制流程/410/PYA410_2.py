'''
410 繪製等腰三角形
請撰寫一程式，依照使用者輸入的n，畫出對應的等腰三角形。
'''

n = int(input())

for i in range(n):
  for j in range(n - i - 1):
    print(' ', end='')
  for k in range(2 * i + 1):
    print('*', end='')
  print()
