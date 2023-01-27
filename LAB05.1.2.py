"""
05.1.2 Noms des pays. French country names are feminine when they end with the letter e, masculine
otherwise, except for the following which are masculine even though they end with e:
• le Belize
• le Cambodge
• le Mexique
• le Mozambique
• le Zaïre
• le Zimbabwe

Write a program that reads the French name of a country and adds the article: “le” for masculine or
“la” for feminine, such as “le Canada” or “la Belgique”.
However, if the country name starts with a vowel, use “l’”; for example, “l’Afghanistan”.
For the following plural country names, use “les”:
• les Etats-Unis
"""
def main():

    while True:

        exceptions = ["Belize, Cambodge, Mexique, Mozambique, Zaire, Zimbabwe"]
        exceptiions2 = ["Etats-Unis", "Pays-Bas"]
        country = input("What is country name?")

        if country in exceptions:
            print("le", country)
        elif country in exceptiions2:
            print("les", country)
        elif country[-1] == "e":
            print("la",country)
        elif country[0] in "aeiou":
            print("l'",country)
        else:
            print("le", country)

        country = input("Continue? [yes/no]: ")
        if country == "no":
            print("Thanks, goodbye.")
            exit()



if __name__ == "__main__":
    main()
