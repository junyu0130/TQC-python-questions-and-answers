'''
706 全字母句
全字母句 (Pangram)是英文字母表所有的字母都出現至少一次 (最好只出現一次)的句子。
請撰寫一程式，要求使用者輸入一正整數k (代表有k筆測試資料)，
每一筆測試資料為一句子，程式判斷該句子是否為Pangram，並印出對應結果True (若是)或False (若不是)。

提示：不區分大小寫字母
'''
k = eval(input())
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in range(k):
  string = input()
  flag = True

  for ch in alphabet:
    if ch not in string.lower():
      flag = False
      break

  print(flag)
