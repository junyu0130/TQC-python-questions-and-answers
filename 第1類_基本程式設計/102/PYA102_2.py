'''
102 浮點數格式化輸出
請撰寫一程式，輸入四個分別含有小數1到4位的浮點數，
然後將這四個浮點數以欄寬為7、欄與欄間隔一個空白字元、每列印兩個的方式，
先列印向右靠齊，再列印向左靠齊，左右皆以直線 |（Vertical bar）作為邊界。

提示：輸出浮點數到小數點後第二位。
'''
num = [eval(input()) for i in range(4)]

# 靠右對齊
print(f"|{num[0]:7.2f} {num[1]:7.2f}|")
print(f"|{num[2]:7.2f} {num[3]:7.2f}|")

# 靠左對齊
print(f"|{num[0]:<7.2f} {num[1]:<7.2f}|")
print(f"|{num[2]:<7.2f} {num[3]:<7.2f}|")
