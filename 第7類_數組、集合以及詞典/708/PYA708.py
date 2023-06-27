'''
708 詞典合併
請撰寫一程式，自行輸入兩個詞典
(以輸入鍵值"end"作為輸入結束點，詞典中將不包含鍵值"end")，
將此兩詞典合併，並根據key值字母由小到大排序輸出，如有重複key值，後輸入的key值將覆蓋前一key值。
'''
d1 = {}
d2 = {}
d3 = {}

print("Create dict1:")
while True:
    #Key: (後方有一空白格)
    key = input("Key: ")
    if key == 'end':    break
    #Value: (後方有一空白格)
    d1[key] = input("Value: ")

print("Create dict2:")
while True:
    key = input("Key: ")
    if key == 'end':    break
    d2[key] = input("Value: ")

d3.update(d1)
d3.update(d2)

for key in sorted(d3.keys()):
    print("{}: {}".format(key, d3[key]))
