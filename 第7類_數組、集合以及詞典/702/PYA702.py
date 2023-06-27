'''
702 數組合併排序
請撰寫一程式，輸入並建立兩組數組，各以-9999為結束點 (數組中不包含-9999)。
將此兩數組合併並從小到大排序之，顯示排序前的數組和排序後的串列。
'''

t1 = []
t2 = []

print("Create tuple1:")
while True:
  num = eval(input())
  if num == -9999:
    break
  else:
    t1.append(num)

print("Create tuple2:")
while True:
  num = eval(input())
  if num == -9999:
    break
  else:
    t2.append(num)

print("Combined tuple before sorting:", tuple(t1 + t2))
print("Combined list after sorting:", sorted(t1 + t2))

"""
Combined tuple before sorting: _
Combined list after sorting: _
"""
