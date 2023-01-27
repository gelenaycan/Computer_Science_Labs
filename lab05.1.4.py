"""
05.1.4 At cinema. Write an application to pre-sell a limited number of cinema tickets.
Each buyer can buy as many as 4 tickets. No more than 100 tickets can be sold. Implement a
program that prompts the user for the desired number of tickets and then displays the number of
remaining tickets. Repeat until all tickets have been sold, and then display the total number of buyers.
"""


def main():

    biletler = 0
    alıcılar = 0

    max_bilet = 100

    while biletler < max_bilet:

        num_tickets = int(input("Kaç bilet satın almak istersiniz? (En fazla 4)"))


        if num_tickets > 4:
            print("Maksimum 4 alabilirsin")

        elif num_tickets <= 0:
            print("Geçersiz girdi lütfen pozitif bir sayı girin: ")

        elif biletler + num_tickets > max_bilet:
            print("Üzgünüz, sadece {} kalan bilet var.".format(max_bilet - biletler))
        else:
            biletler += num_tickets
            alıcılar += 1

            print("Satın alımınız için teşekkürler! {} kalan bilet".format(max_bilet-biletler))


    print("Tüm biletler satıldı. Toplam alıcı sayısı: {}".format(alıcılar))


if __name__ == "__main__":
    main()