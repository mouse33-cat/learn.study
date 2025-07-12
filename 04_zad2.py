import import_zad2
import math


a = float(input("Podaj liczbę A : "))
b = float(input("Podaj liczbę B :"))

c = import_zad2.przeciwprostokątna(a, b)
c = math.sqrt((pow(a, 2) + (pow(b, 2))))
print("To jest przeciwprostokątna : ", c )