"""
A person on average can jump off the ground with a speed of
11 kilometers per hour without having to fear leaving the
Earth's surface. Conversely, if a person jumped with the
same speed while on Halley's Comet, would he or she be able
to return to the surface? Create a program that allows the
user to input a launch speed (in kilometers per hour) from
the surface of Halley's Comet, and determine whether the
person jumping will be able to return to the surface. If
not, the program will need to calculate how much more mass
the comet would have to have for that to happen.
Hint: the escape velocity is equal to 𝜐𝑒𝑠𝑐𝑎𝑝𝑒   =  √2 𝐺 𝑀,
𝑅
where 𝐺  =  6.67  ×  10 −11 𝑁 𝑚2 / 𝑘𝑔2 is the gravitational constant, 𝑀 is the mass of the celestial body, and 𝑅 is the radius. Halley’s Comet has a mass of 2.2  × 1014 𝑘𝑔 and a diameter of 9.4 𝑘𝑚 . [P3.52]
"""
""""
import math

def yuzeye_donus_mumkunmu(firlatma_hizi):
    #halley kuyruklu yıldızı parametreleri
    m = 2.2 * 10 ** 14
    R = 9.4
    r = R /2

    #kaçış hızını hesapla

    G = 6.67 * 10 ** -11
    kacis_hizi = math.sqrt((2*G*m)/r)

    #Fırlatma hızıyla kaçış hızını karşılaştır
    if firlatma_hizi >= kacis_hizi:
        print("kisi yüzeye dönebilir.")
    else:
    #gerekli kütleyi hesapla
        gerekli_kutle = (firlatma_hizi ** 2) * r / (2*G)

        print(f"Bu fırlatma hızında kişinin yüzeye dönebilmesi için kuyruklu yıldızın {gerekli_kutle / 10**14} 10^^4kg kütleye sahip olması gerekir. ")

yuzeye_donus_mumkunmu(11)
yuzeye_donus_mumkunmu(20)
"""

import math

hız = int(input("Hızınızı girin: "))

kutle = 2.2 * 10**14
cap = 9.4
yaricap = cap / 2
g = 6.67 * 10 ** -11

kacis_hizi = math.sqrt((2*g*kutle)/yaricap)
gerekli_kütle = (kutle - ((kacis_hizi**2 * yaricap)/2*g))

if hız >= kacis_hizi:
    print("kişi yüzeye dönebilir.")
else:
    print((f"bu fırlatma hızındaki kişinin yüzeye dönebilmesi için", gerekli_kütle, "gerekir."))