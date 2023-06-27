'''
910 學生基本資料
請撰寫一程式，要求使用者讀入read.dat (以UTF-8編碼格式讀取)，
第一列為欄位名稱，第二列之後是個人記錄。
請輸出檔案內容並顯示男生人數和女生人數 (根據"性別"欄位，0為女性、1為男性)。

請注意：資料夾或程式碼中所提供的檔案路徑，不可進行變動，read.dat檔案為UTF-8編碼格式。
'''

f_name = "read.dat"
data = []
with open(f_name, 'r', encoding = 'utf8') as file:
  for i, line in enumerate(file):
    print(line)

    if i > 0:
      no, name, sex, dept = line.strip().split(' ')
      data.append((no, name, int(sex), dept))

print("Number of males: {}".format(len(list(filter(lambda x:x[2] == 1, data)))))
print("Number of females: {}".format(len(list(filter(lambda x:x[2] == 0, data)))))

"""
Number of males: _
Number of females: _
"""