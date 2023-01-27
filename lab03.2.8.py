"""
A supermarket rewards its customers with shopping vouchers whose
amount depends on the amount of money spent on food. For example,
if you spend $50, you get a shopping voucher equal to 8% of the
amount you spent. The table below shows the percentage used to
calculate the shopping voucher relative to different amounts.
Write a program that calculates and displays the value of the
shopping voucher given to the customer, based on the amount of
money he or she spent on the purchase of groceries. [P3.40]
Money spent
Less than $ 10
From $ 10 to $ 60
From more than $ 60 to $ 150 From more than $ 150 to $ 210
More than $ 210
Percentage of the voucher
No voucher 8% 10% 12% 14%
"""

money = int(input("Kaç para harcadınız?: "))

if money > 210:
    last_money = (money - ((money*14)/100))
elif money > 150 and money < 210:
    last_money = (money - ((money*12)/100))
elif money > 60 and money < 150:
    last_money = (money - ((money * 10) / 100))
elif money > 10 and money < 60:
    last_money = (money - ((money * 8) / 100))
else:
    last_money = money

print(last_money)