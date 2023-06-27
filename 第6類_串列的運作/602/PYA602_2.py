'''
602 撲克牌總和
請撰寫一程式，讓使用者輸入52張牌中的5張，計算並輸出其總和。

提示：J、Q、K以及A分別代表11、12、13以及1。
'''

hand = []

for i in range(5):
  poker = input()

  if poker == 'J':
    hand.append(11)
  elif poker == 'Q':
    hand.append(12)
  elif poker == 'K':
    hand.append(13)
  elif poker == 'A':
    hand.append(1)
  else:
    hand.append(int(poker))

print(sum(hand))
