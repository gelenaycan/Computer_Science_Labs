"""

bi seyler var


Write a program for the conversion of units of measurement.
It asks the user for: the starting unit of measurement
(choosing from: ml, l, g, kg, mm, cm, m, km); the unit of
measurement to which it wants to convert
(choosing from: fl, oz, gal, oz, lb, in, ft, mi),
rejecting incompatible conversions (such as, for example, km to gal);
the value to be converted. The program is supposed to display the
data entered and the value resulting from the conversion.
"""


# Ölçü birimlerinin birbirine dönüştürülme oranları
conversion_rates = {
    "ml": {
        "fl": 0.033814,
        "oz": 0.033814,
        "gal": 0.000264172,
        "lb": 0.00000220462,
        "in": 0.0610237,
        "ft": 0.00104438,
        "mi": 6.2137e-8,
    },
    "l": {
        "fl": 33.814,
        "oz": 33.814,
        "gal": 0.264172,
        "lb": 0.0220462,
        "in": 61.0237,
        "ft": 1.04438,
        "mi": 6.2137e-7,
    },
    "g": {
        "oz": 0.035274,
        "lb": 0.00220462,
    },
    "kg": {
        "oz": 35.274,
        "lb": 2.20462,
    },
    "mm": {
        "in": 0.0393701,
        "ft": 0.00328084,
        "mi": 6.2137e-9,
    },
    "cm": {
        "in": 0.393701,
        "ft": 0.0328084,
        "mi": 6.2137e-8,
    },
    "m": {
        "in": 39.3701,
        "ft": 3.28084,
        "mi": 6.2137e-7,
    },
    "km": {
        "in": 39370.1,
        "ft": 3280.84,
        "mi": 0.00621371,
    },
}

# Kullanıcıdan giriş verilerini al
start_unit = input("Başlangıç ölçü birimi: ")
end_unit = input("Dönüştürülecek ölçü birimi: ")
value = float(input("Dönüştürülecek değer: "))

#ölçü birimlerinin uyumlu olup olmadığını kontrol et

if end_unit not in conversion_rates[start_unit]:
    print("bu ölçü birimleri arasında dönüş mümkün değildir.")
    exit()

#dönüştürme oranını hesaplayın ve değerini dönüştürün

conversion_rate = conversion_rates[start_unit][end_unit]
converted_value = value*conversion_rate

#girdi verilerini ve dönüştürme sonucunu göster

print("başlangıç ölçü birimi: ", start_unit)
print("dönüştürülecek ölçü birimi: ", end_unit)
print("dönüştürülecek değer: ", value)
print("Dönüştürme sonucu: ", converted_value)



# ya da


def main():
    # Read the unit to convert from and to.

    from_unit = input("Convert from? (ml, l, g, kg, mm, cm, m, km): ")
    to_unit = input("Convert to? (fl. oz, gal, oz, lb, in, ft, mi): ")

    # Volume units.
    if from_unit == "ml" and to_unit == "fl. oz":
        factor = 0.03381406
    elif from_unit == "l" and to_unit == "fl. oz":
        factor = 33.81405650
    elif from_unit == "ml" and to_unit == "gal":
        factor = 0.00026417
    elif from_unit == "l" and to_unit == "gal":
        factor = 0.26417218

    # Weight / mass units.
    elif from_unit == "g" and to_unit == "oz":
        factor = 0.03527399
    elif from_unit == "kg" and to_unit == "oz":
        factor = 35.27399072
    elif from_unit == "g" and to_unit == "lb":
        factor = 0.00220462
    elif from_unit == "kg" and to_unit == "lb":
        factor = 2.20462442

    # Distance units.
    elif from_unit == "mm" and to_unit == "in":
        factor = 0.03937008
    elif from_unit == "cm" and to_unit == "in":
        factor = 0.39370079
    elif from_unit == "m" and to_unit == "in":
        factor = 39.37007874
    elif from_unit == "km" and to_unit == "in":
        factor = 39370.07874016
    elif from_unit == "mm" and to_unit == "ft":
        factor = 0.00328084
    elif from_unit == "cm" and to_unit == "ft":
        factor = 0.03280840
    elif from_unit == "m" and to_unit == "ft":
        factor = 3.28083990
    elif from_unit == "km" and to_unit == "ft":
        factor = 3280.83989501
    elif from_unit == "mm" and to_unit == "mi":
        factor = 0.00000062
    elif from_unit == "cm" and to_unit == "mi":
        factor = 0.00000621
    elif from_unit == "m" and to_unit == "mi":
        factor = 0.00062137
    elif from_unit == "km" and to_unit == "mi":
        factor = 0.62137119
    # Incompatible units.
    else:
        exit("Those units are not compatible.")

    # Read the value to convert from the user.
    value = float(input("Value? "))

    # Compute the result.
    result = value * factor

    # Display the result.
    print(value, from_unit, "=", result, to_unit)


if __name__ == "__main__":
    main()