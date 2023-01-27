"""
05.2.2 Sarhoş Yürüyüşü. Bir sokak ızgarasındaki bir ayyaş
rastgele dört yönden birini seçer ve tökezleyerek bir sonraki
kavşağa gider, sonra yine rastgele dört yönden birini seçer ve bu
böyle devam eder. Seçimler birbirini götürdüğü için ayyaşın ortalama
olarak uzağa gitmediğini düşünebilirsiniz, ama aslında durum bu değil.
Konumları tamsayı çiftleri (x, y) olarak temsil edin. Sarhoşun yürüyüşünü
(0,0)'dan başlayarak 100'den fazla kavşağa uygulayın ve bitiş konumunu
yazdırın.
[P4.24]
"""

def main():

    import random

    x, y = 0, 0

    for i in range(100):

        yön = random.randint(0, 3)

        if yön == 0:
            x += 1
        elif yön == 1:
            x -= 1
        elif yön == 2:
            y += 1
        else:
            y -= 1

    print("Son konumu: ( {}, {})".format(x, y))

if __name__ == "__main__":
    main()