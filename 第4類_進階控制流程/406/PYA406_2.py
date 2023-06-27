'''
406 不定數迴圈-BMI計算
請撰寫一程式，以不定數迴圈的方式輸入身高(cm)與體重(kg)，
計算出BMI之後再根據以下對照表，印出BMI及相對應的BMI代表意義 (State)。
假設此不定數迴圈輸入-9999則會結束此迴圈。

標準如下表所示:
BMI值	            代表意義
BMI < 18.5	        under weight
18.5 <= BMI < 25	normal
25.0 <= BMI < 30	over weight
30 <= BMI	        fat

提示:BMI=體重(kg) / 身高^2(m)，輸出浮點數到小數點後第二位。 不需考慮男性或女性標準。
'''

while True:
    h = int(input())
    if h == -9999 or h < 0:
        break
    w = int(input())
    if w == -9999 or w < 0:
        break

    bmi = w / (h / 100)**2

    print(f"BMI: {bmi:.2f}")
    if bmi < 18.5:
        print("State: under weight")
    elif 18.5 <= bmi < 25:
        print("State: normal")
    elif 25.0 <= bmi < 30:
        print("State: over weight")
    elif bmi >= 30:
        print("State: fat")

"""
fat
over weight
normal
under weight
BMI: _
State: _
"""
