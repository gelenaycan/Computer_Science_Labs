"""
Write a program that reads three numbers and displays
the message "increasing" if they are in strictly
increasing order, "decreasing" if they are in
strictly decreasing order, and "neither" if
they are in neither increasing nor decreasing
order. "Strictly increasing" means that each
value must be greater than the previous one
(similar meaning has the term decreasing):
the sequence 3 4 4, thus, it is not “increasing”.
"""

x = int(input("Bir x değeri girin: "))
y = int(input("Bir y değeri girin: "))
z = int(input("Bir z değeri girin: "))



if x > y > z :
    print("Verdiniz değerler ", x, y, z, "ve bunlar kesinlikle azalan değerlerdir..")
elif x < y < z:
    print("Kesinlikle azalan.")
else:
    print("Hiçbiri.")

#chatgpt sonucu aşağıda

def check_order(a,b,c):
    if a < b < c:
        return "increasing"
    elif a > b > c:
        return "decreasing"
    else:
        return "neither"

print(check_order(1, 2, 3))
print(check_order(3, 2, 1))
print(check_order(1, 2, 2))
print(check_order(2, 2, 2))
print(check_order(3, 1, 2)) 