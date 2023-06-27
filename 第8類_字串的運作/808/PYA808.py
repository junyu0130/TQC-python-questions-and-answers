'''
808 社會安全碼
請撰寫一程式，提示使用者輸入一個社會安全碼SSN，格式為ddd-dd-dddd，d表示數字。
若格式完全符合 (正確的SSN)則顯示 "Valid SSN"，否則顯示 "Invalid SSN"。
'''
ssn = input().split('-')

# print(ssn)
if ssn[0].isdigit() and len(ssn[0]) == 3 and\
   ssn[1].isdigit() and len(ssn[1]) == 2 and\
   ssn[2].isdigit() and len(ssn[2]) == 4:
   print("Valid SSN")
else: print("Invalid SSN")

"""
Valid SSN
Invalid SSN
"""
