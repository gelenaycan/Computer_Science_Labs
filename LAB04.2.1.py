"""

tekrar bak saçmaladı

 The game of Nim. In this game, two players alternate extracting marbles from a pile. At each round, the number of marbles taken is up to the player, providing it is at least one, and at most half of the number of marbles currently available. The player that takes the last marble loses.
Write a program allowing a user to play against the computer. The program shall:
I. Generate a random number between 10 and 100 to use as the quantity of marbles in the pile in the beginning of the game.
II. Generate a random number, either 0 or 1, to decide whether the first move is on the player or on the computer.
III. Generate a random number, either 0 or 1, to decide if the computer must play in a smart or dumb way:
a. By playing dumb, on every move the computer takes a random number of marbles from the sack (between 1 and n/2, given n as the current number of marbles left in the pile).
b. By playing smart, it takes a number of marbles so that the number of the remaining ones is a power of 2 diminished by 1 unit, meaning: 3, 7, 15, 31 o 63. This move is always valid, except when the number of marbles is equal to a power of 2 diminished by 1. If such is the case, it randomly plays a valid move.
You can experimentally verify that the computer cannot be beat in smart mode, unless the initial pile contains 15, 31 or 63 marbles. The same goes for human players: if the player draws first and knows this strategy, the computer cannot win.

Nim'in oyunu. Bu oyunda, iki oyuncu dönüşümlü olarak bir desteden misketleri çıkarıyor. Her turda, alınan bilyelerin sayısı oyuncuya bağlıdır ve şu anda mevcut olan bilye sayısının en az bir ve en fazla yarısı kadardır. Son bilyeyi alan oyuncu kaybeder.
Bir kullanıcının bilgisayara karşı oynamasına izin veren bir program yazın. Program:
I. Oyunun başında yığındaki misket miktarı olarak kullanmak için 10 ile 100 arasında rastgele bir sayı oluşturun.
II. İlk hamlenin oyuncuda mı yoksa bilgisayarda mı olduğuna karar vermek için 0 veya 1 olarak rastgele bir sayı oluşturun.
III. Bilgisayarın akıllı mı yoksa aptalca mı oynaması gerektiğine karar vermek için 0 veya 1 olarak rastgele bir sayı oluşturun:
a. Aptalı oynayarak, bilgisayar her harekette çuvaldan rastgele sayıda misket alır (destede kalan bilye sayısı n olarak verildiğinde 1 ile n/2 arasında).
b. Akıllı oynayarak, bir dizi misket alır, böylece kalanların sayısı 2'nin kuvveti 1 birim azalır, yani: 3, 7, 15, 31 veya 63. misket sayısı, 2'nin kuvvetinin 1 eksiltilmesine eşittir. Böyle bir durumda, rastgele geçerli bir hamle oynar.
İlk deste 15, 31 veya 63 bilye içermediği sürece, bilgisayarın akıllı modda yenemeyeceğini deneysel olarak doğrulayabilirsiniz. Aynı şey insan oyuncular için de geçerli: eğer oyuncu önce çizerse ve bu stratejiyi bilirse bilgisayar kazanamaz.
"""

import random

# deste için rastgele bir sayı üretin
pile = random.randint(10, 100)

# oyun sırasında, destedeki misket sayısını güncelleyin ve oyunun sonuna gelinip gelinmediğini kontrol edin
while pile > 0:
    # kullanıcıdan misket sayısını girdiği deste ile oynayan bir bilgisayar
    print("Destede şu anda", pile, "misket var. Kaç tane almak istersiniz?")
    num_taken = int(input())

    # oyuncunun alabileceği misket sayısını sınırlandırın
    if num_taken < 1 or num_taken > (pile // 2):
        print("Geçersiz seçim. Lütfen 1 ile", (pile // 2), "arasında bir sayı seçin.")
        continue

    # misketleri çıkarın ve bilgisayarın hamlesine geçirin
    pile -= num_taken

    # bilgisayar aptal modda oynayarak, çuvaldan rastgele sayıda misket alın
    num_taken = random.randint(1, (pile // 2))
    pile -= num_taken

# oyun sona erdi, son hamleyi yapan oyuncu kaybetti
print("Bilgisayar kazandı!")
