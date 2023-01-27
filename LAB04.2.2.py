"""

Write a code in python. The radioactive decay of radioactive
material can be modelled through the following
equation: 𝐴  =  𝐴0𝑒−𝜆𝑡, where 𝐴 is the quantity of
the material at time 𝑡, 𝐴0 is the
quantity of the material at time 0 , and 𝜆 is the
decay rate. More precisely 𝜆 = ln 2 , where 𝑇1⁄ is 𝑇1⁄2 2
the half-life of the substance (expressed in the same
unit of measure of 𝑡).
Technetium-99 is a radioisotope used for diagnostics of
brain images. It has a half-life of 6 hours. Write a program
showing the relative quantity 𝐴/𝐴0 in a patient body for
each hour during the 24 hours next to the administration of the dose

"""

import math

#yarı ömrü verilen radyıizotop için "L(LAMBDA)" değerini hesapla

half_life = 6 # yarı ömrü 6 saat verilmiştir
lam = math.log(2) / half_life  # L = ln2 / T1/2

"""
 #İlk miktarı verilen A0 değerini kullanarak, 24 saat sürecek bir döngü
oluştur ve her saat için A/A0 nispi miktarını hesapla
"""
A0 = 100 #ilk miktar verilmiştir
for t in range(24): # 24 saat sürecek bir döngü oluşturuyoruz
    # A = A0e-Lt denklemini kullanarak A/A0 nispi miktarını hesapla
    A = A0 * math.exp(-lam * t)
    # Her saat için nispi mikrarını yazdır
    print(f"{t+1}. saatte A/A0 nispi miktarı: {A/A0: .3f}")
