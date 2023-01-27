
"""
# Örnek harf ve sayı dizisi oluşturma
letters = ['A', 'B', 'C', 'D']
numbers = [1, 2, 3, 4]

randomseyler = [(letters,:2),(numbers,2:5)]


# Sadece sayısal bölümü temel alarak artan sırada bir yeni dizi oluşturma
sorted_numbers = sorted(numbers)

# Yeniden sıralanmış dizinin ekranda gösterilmesi
print(sorted_numbers)

def main():

    student_id_a = "S50123"
    student_id_b = "S41235"

    if int(student_id_a[1:])> int(student_id_b[1:]):
        print(student_id_a)
        print(student_id_b)
    else:
        print(student_id_b)
        print(student_id_a)

if __name__ == "__main__":
    main()

 The freshman of the students of a University is composed of
 two parts: a letter and a sequence of numbers. Write a
 program that, starting from two serial codes, shows them
 on the screen in ascending order based on the numerical
 part only. Tip: Use the default functions of the Python
 language.

"""
import random
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3, 4, 5]
for _ in range (1):
    random.shuffle(list1)
    first_letter=list1[0]
    random.shuffle(list2)
    a=''
    for i in list2:
        a+=f'{i}'
    random.shuffle(list1)
    first_letter_2 = list1[0]
    random.shuffle(list2)
    b = ''
    for i in list2:
        b += f'{i}'

    listemsi = (first_letter+a, first_letter_2+b)
    print(listemsi)

if int(a[1:]) > int(b[1:]):
     print("The first element is larger than the second element.")
else:
    print(31)



