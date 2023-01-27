"""

Write a program reading a word and showing all its substring, sorted by
increasing length. If the user inputs the string 'rum', the program shall output:
r
u
m
ru
um
rum

"""

#Kullanıcıdan bir kelime isteyin

kelime = input("Bir kelime girin: ")

#Tüm alt dizgileri alın ve uzunluğa göre sıralayın

alt_dizgiler =  sorted(set([kelime[i: j] for i in range(len(kelime)) for j in range(i + 1, len(kelime) + 1)]), key=len)

#alt dizgileri yazdırın

print("Alt dizgiler:")
for alt_dizgi in alt_dizgiler:
    print(alt_dizgi)