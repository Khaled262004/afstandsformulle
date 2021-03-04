from math import*
text = "Hallo, wat leuk dat je vandaag gebruik maakt van de afstandscalculator.\nMet deze tool kan je de afstand berekenen tussen een lijn en een punt met behulp van de afstandsformule.\nOok is het mogelijk om punten te vergelijken en te kijken welke dichterbij de lijn is. \nOm het programma te herstarten, klik op run. \nNatuurlijk hebben we een paar gegevens van je nodig: \n"
xp, yp = float(input(text +
                     "\nWat is het x coördinaat van het punt: ")), float(input("Wat is het y coördinaat van het punt: "))

a = float(input("Als ax + by = c, geef de waarde van a: "))
b = float(input("Geef de waarde van b: "))
c = float(input("Geef de waarde van c: "))

t = a * xp + b * yp - c
n = pow(a, 2) + pow(b, 2)

afstand = str(abs(t)/sqrt(n))
print("\nVoor het 1e punt gelden de coördinaten:  (" + str(xp) + "," + str(yp) + ")\n\nVoor de lijn geldt: " + str(a) + "x + " + str(b) + "y = " + str(c))
print("\nDe afstand tussen het 1e punt en de lijn = " + afstand)

pt2= input("\nWil je dit punt vergelijken met een ander punt(beantwoord met ja of nee)?: ").lower()

if pt2 == "ja":
    xp2, yp2 = float(input("\nWat is het x coördinaat van het 2e punt: ")), float(
        input("Wat is het y coördinaat van het 2e punt: "))
    t2 = a * xp2 + b * yp2 - c
    afstand2 = str(abs(t2) / sqrt(n))
    print("\nVoor het 2e punt gelden de coordinaten: (" + str(xp2) + "," + str(yp2) + ")")
    print("\nDe afstand tussen het 2e punt en de lijn = " + afstand2)

    if afstand > afstand2:
        print("\nHet 2e punt is dichterbij bij de lijn dan het 1e punt")
    elif afstand < afstand2:
        print("\nHet 1e punt is dichterbij de lijn dan het 2e punt")
    elif afstand == afstand2:
        print("\nAllebei de punten zijn even ver van de lijn")
else:
    print("\nokay!")

how = input("\nWil je de uitwerkingen zien (beantwoord met ja of nee)?: ").lower()

if how == "ja":
    print("\nax + by - c\n"
          "-----------\n"
          "sqrt(a^2 + b^2)\n"
          "\na = " + str(a) + "\nb = " + str(b) + "\nc = " + str(c) + "\nxP = " + str(xp) + "\nyp = " + str(yp))
    print("\n dus, \n")
    print("|" + str(a) + "*" + str(xp) + "+" + str(b) + "*" + str(yp) + "-" + str(c) + "|")
    print("--------------------")
    print("sqrt(" + str(pow(a, 2)) + "+" + str(pow(b, 2)) + ")\n")

    print(abs(t))
    print("---")
    print(sqrt(n))



    print("\n= " + afstand)
    print("\n|" + str(a) + "*" + str(xp2) + "+" + str(b) + "*" + str(yp2) + "-" + str(c) + "|")
    print("--------------------")
    print("sqrt(" + str(pow(a, 2)) + "+" + str(pow(b, 2)) + ")\n")

    print(abs(t2))
    print("---")
    print(sqrt(n))

    print("\n= " + afstand2)

    if afstand > afstand2:
        print("\n" + afstand + ">" + afstand2)
        print("\ndus het 2e punt is dichterbij de lijn dan het 1e punt")
    elif afstand < afstand2:
        print("\n" + afstand + "<" + afstand2)
        print("\ndus het 1e punt is dichterbij de lijn dan het 2e punt")
    elif afstand == afstand2:
        print("\n" + afstand + "=" + afstand2)
        print("\ndus allebei de punten zijn even ver van de lijn")
else:
    print("\nokay!")

k = input("\npress enter to exit")