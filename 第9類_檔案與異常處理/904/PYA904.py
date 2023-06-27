'''
904 資料計算
請撰寫一程式，讀取read.txt（每一列的格式為名字和身高、體重，以空白分隔）
並顯示檔案內容、所有人的平均身高、平均體重以及最高者、最重者。

提示：輸出浮點數到小數點後第二位。
請注意：資料夾或程式碼中所提供的檔案路徑，不可進行變動，read.txt檔案需為UTF-8編碼格式。
'''

data = []

with open("read.txt", "r") as file:
  for line in file:
    print(line)
    name, height, weight = line.strip().split(' ')
    data.append((name, int(height), int(weight)))

  # print(data)
  # print(max(data, key=lambda x: x[1]))

  tellest = max(data, key=lambda x: x[1])
  heaviest = max(data, key=lambda x: x[2])
  print(f"Average height: {sum([i[1] for i in data]) / len(data):.2f}")
  print(f"Average weight: {sum([i[2] for i in data]) / len(data):.2f}")
  print("The tallest is {} with {:.2f}cm".format(tellest[0], tellest[1]))
  print("The heaviest is {} with {:.2f}kg".format(heaviest[0], heaviest[2]))

# """
# Average height: _
# Average weight: _
# The tallest is _ with _cm
# The heaviest is _ with _kg
# """
