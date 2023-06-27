'''
908 單字次數計算
請撰寫一程式，要求使用者輸入檔名read.txt，以及檔案中某單字出現的次數。
輸出符合次數的單字，並依單字的第一個字母大小排序。
(單字的判斷以空白隔開即可)

請注意：資料夾或程式碼中所提供的檔案路徑，不可進行變動，read.txt檔案需為UTF-8編碼格式。
'''
# from typing import Counter

data = dict()
# data = {}
f_name = input()
n = int(input())

with open(f_name, 'r') as file:
  for line in file:
    words = line.strip().split(' ')
    for word in words:
      if word in data:
        data[word] += 1
      else:
        data[word] = 1

  for word in sorted([word for word, freq in data.items() if freq == n]):
    print(word)
