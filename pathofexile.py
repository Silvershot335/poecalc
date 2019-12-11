import math

#

calc = input("What calculation would you like to make:\nArmor\nEvasion\nImplicit\nBrick\nHit ENTER to exit")

if "armor" in calc.casefold():
            armor = input("What is your armor value?")
            dr = (int(armor) / (int(armor) + (10 * 1000)))
            print("You will reduce " + "{:.0%}".format(dr) + (" of a 1,000 damage hit."))

if "evasion" in calc.casefold():
            er = input("Enter your Evasion Rating:")
            dc = input("Enter your Dodge Chance:")
            dc1 = "." + dc
            ec = (584 * 1.15) / (584 + ((float(er) * .25) ** .8))
            cp1 = (1 - ec)
            cp2 = 1 - float(dc1)
            cpa = 1 - (cp1 * cp2)
            print("Your chance to prevent attacks is " "{:.2%}".format(cpa) + ".")

if "implicit" in calc.casefold():
            attempts = input("How many attempts?")
            implicit = input("How many implicits?")
            d = (.25 ** int(implicit))
            c = (int(attempts) - int(implicit))
            e = (.75 ** int(c))
            a = (d * e)
            fx = math.factorial(int(attempts))
            fj = math.factorial(int(implicit))
            fxj = math.factorial(int(attempts) - int(implicit))
            b = (fx) / (fj * fxj)
            f = (a * b)
            print("There's is a " "{:.2%}".format(f) + " of having " + implicit + " implicits in " + attempts + " attempts.")

if "brick" in calc.casefold():
            x = input("How Many Attempts?")
            y = (-.75 ** int(x))
            z = (1 + y)
            print("There is a " "{:.2%}".format(z) + " chance of bricking.")

