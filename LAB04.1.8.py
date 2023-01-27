"""

HATALI SONUÇ ALINDI TEKRAR KONTROL ET!!!!!!

Write a basic program in python reading a sequence of integer numbers (the sequence ends with an empty line) and, after each acquisition, compute and shows only the adjacent duplicate numbers.
Example: if the input sequence at step IV are the values 1 3 3 4 5 5 6 6 6 3, the program shall output the adjacent numbers repeated at least two times; at the end of the sequence of equal numbers (after acquiring the first different number), it shall print:
I. Nothing at the first input (1), as it is the first value.
II. Nothing at the second input (3), as the adjacent values 1 and 3 are not duplicates (equal).
III. Nothing after the third input (3), as the acquired value is the duplicate of the previous one, and the sequence of duplicate numbers may not be terminated yet.
IV. The value 3 after the fourth input (4), as the two latest adjacent values (3 and 4) are not duplicated anymore; thus, the sequence of duplicate adjacent numbers is terminated, and the program shall output the duplicate number.
According to this logic, the sequence 1 3 3 4 5 5 6 6 6 3 produces, in the end, the following values: 3 5 6
"""

# Tam sayı dizisini al ve sırala
numbers = []
while True:
  line = input("Bir tam sayı girin veya boş bir satır bırakın: ")
  if line:
    try:
      numbers.append(int(line))
    except ValueError:
      print("Lütfen geçerli bir tam sayı girin.")
  else:
    break
numbers.sort()

# Bitişik yinelenen sayıları bul ve göster
for i in range(1, len(numbers)):
  if numbers[i] == numbers[i-1]:
    print(numbers[i])


