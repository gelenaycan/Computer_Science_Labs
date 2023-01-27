"""
DNA sequences are like long strings consisting of only four letters:
'A', 'C', 'T' and 'G'. Write a program that takes as input a "long sequence"
of DNA of twenty characters and a "short sequence" of three characters and displays:
I. if the "long sequence" contains the "short sequence";
II. if yes:
a. from which position of the "long sequence" the "short sequence" starts;
b. how many times the "long sequence” contains the shorter substring.

"""
def main():

  uzun = input("Insert a long DNA code.")
  uzun = uzun.upper()

  kısa = input("Insert a short DNA, JUST 3: ")
  kısa = kısa.upper()

  if len(kısa) !=3:
    print("ERROR, WRITE JUST 3 LETTERS")
    exit()

  bul = uzun.find(kısa)

  if bul == -1:
    print("kısa sequence is not present in uzun sequence")
  else:
    print("uzun sequence is present starting from position", kısa)

    tekrar = uzun.count(kısa)
    print("sequence", kısa, "appears", tekrar, "times")

if __name__ == "__main__":
  main()










"""long_sequence = 'ACTGATCGATCGATCGATCGCGAATCGATCGA'
short_sequences = ['ATC', 'GAT', 'CGA']

#find() fonksiyonunu kullanarak kısa diziyi uzun dizide arayalım

index = long_sequence.find(short_sequences[0])
if index != -1:
  print('"uzun dizi", "kısa dizi"yi içerir')
  print('"uzun dizi"nin', index, 'konumundan "kısa dizi" başlar')
  count = long_sequence.count(short_sequences[0])
  print('"uzun dizi"nin', count, 'kez daha "kısa dizi"yi içerir')
else:
  print('"uzun dizi", "kısa dizi"yi içermiyor')"""
