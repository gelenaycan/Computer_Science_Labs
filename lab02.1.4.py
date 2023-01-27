"""
#Writing the pseudocode and Python program that helps a person decide whether or not to buy a hybrid car. The program's entries should be:
I. the cost of a new car;
II. estimation of kilometers traveled in one year;
III. Estimation of fuel cost;
IV. Efficiency in kilometers per liter;
V. Estimated resale value of the used car after 5 years.
Calculate the 5-year total cost of ownership of the vehicle (ignore the cost of financing for simplicity).
To provide input to the program, search the Web for realistic prices and consumption for two alternatives to
buying a new car in the same price range: a hybrid model or and a petrol. Run the program twice to compare the two
alternatives, taking into account the current fuel price and an estimated 30,000 kilometers per year.
"""

#değişkenleri girelim

yeni_hybrid = int(input("Hybrid araba değerini giriniz: "))
yeni_petrol = int(input("Petrollü araba değerini giriniz: "))
yıllık_km = int(input("Yılda ortalama kaç km gidileceğini yazınız: "))
verimlilik = int(input("Litre başına kaç km verimlilik: "))
petrol_fiyatı = int(input("Petrol fiyatını yazın: "))
satılabilecek_araba = int(input("tahmini 2.el satış değeri: "))


#hybrid için hesaplama

hesaplanan_hybrid = yeni_hybrid + ((yıllık_km / verimlilik) * petrol_fiyatı) - satılabilecek_araba
print("Bir hybrid araba sahip olmak beş yılda ortalama", hesaplanan_hybrid, "tl kazandırır")

hesaplanan_petrol = yeni_petrol + ((yıllık_km / verimlilik)* petrol_fiyatı) - satılabilecek_araba
print("Bir petrollü araba sahibi olmak beş yılda ortalama", hesaplanan_petrol, "tl kazandırır.")

# underscore is used to separate the thousands for readability purposes
KILOMETERS_PER_YEAR = 30_000  # 2.


# the above statement is exactly equal to KILOMETERS_PER_YEAR = 30000

def main():
    initial_cost = int(input("Car's initial cost (in €): "))  # 1.
    cost_of_fuel = int(input("Cost of fuel (in €): "))  # 3.
    km_per_liter = int(input("Kilometers per liter: "))  # 4.
    resale_value = int(input("Car's resale value in 5 years (in €): "))  # 5.

    fuel_needed = 5 * (KILOMETERS_PER_YEAR / km_per_liter)  # 6.
    total_fuel_cost = fuel_needed * cost_of_fuel  # 7.

    car_total_cost = initial_cost + total_fuel_cost - resale_value  # 8.

    print(f"The total cost of the car for 5 years is {car_total_cost}€.")  # 9.


if __name__ == "__main__":
    main()



#define the variables

cost_new_hybrid = int(input("Cost of new hybrid:"))
cost_new_gas = int(input("cost of new gas:"))
distance_per_year = int(input("distance of per year:"))
fuel_cost = int(input("fuel cost is:"))
fuel_efficiency = int(input("fuel efficiency is:"))
resale_value_used = int(input("resale value used:"))

#calculate the total cost of owning a hybrid for 5 years

total_cost_hybrid = cost_new_hybrid + (distance_per_year / fuel_efficiency) * fuel_cost - resale_value_used
print("The total cost of owning a hybrid for 5 years is:", total_cost_hybrid)

#calculate the total cost of owning a gas for 5 years

total_cost_gas = cost_new_gas + (distance_per_year / fuel_efficiency) * fuel_cost - resale_value_used
print("the total cost of owning a gas for 5 years is:", total_cost_gas)



