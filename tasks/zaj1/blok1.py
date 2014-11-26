import math
lista = list(range(1,101))
#dzielenie wszystkich wartosci w liscie przez liczbe:
'''myList = [10,20,30,40,50,60,70,80,90]
myInt = 10
newList = [x / myInt for x in myList]'''
#print(sum(lista))
suma = 0
for i in lista:
	suma += i
print("Zad1: wyswietlanie sumy")
print(suma)
print
##########################################
xp=0
xk=2*math.pi
n=1000000
dx=(xk-xp)/n
calka=0

for i in range(1,n+1):
	calka += math.sin(xp + i*dx)
	#print(math.sin(xp + i*dx))
calka *= dx
print("Zad2: wartosc calki:")
print(calka)
print
###########################################
n=100000
dx=(xk-xp)/n
sin = {0:0}
for i in range(n+1):
	sin[round(i*dx,5)]=math.sin(i*dx)
print("Zad3, wyswietlam wartosc sinusa w 3.14159 dla stworzonego slownika:")
print(sin[3.14159])
print

kot = {
    "imie": "Paczus", 
    "rasa": "kot", 
    "masa": (10, "kg"),
    "wiek": (10, "lat")
}

pies = {
    "imie": "Reks", 
    "rasa": "dog", 
    "masa": (50, "kg"),
    "wiek": (8, "lat")
}
los = {
    "imie": "Edward", 
    "rasa": "bura", 
    "masa": (100, "kg"), 
    "wiek": (100, "lat")
}
homik = {
    "imie": "rysiek", 
    "rasa": "ruda", 
    "masa": (1, "kg"),
    "wiek": (1, "lat")
}
rybka = {
    "imie": "neo", 
    "rasa": "mala", 
    "masa": (0.1, "kg"),
    "wiek": (0.1, "lat")
}

lista = [kot, pies, los, homik, rybka]
print("Zad4, 1.cala struktura danych:")
print(lista)
print
print("Zad4, 2.Dane drugiego zwierza:")
print(lista[1])
print
print("Zad4, 2.Imie drugiego zwierza:")
print(lista[1]["imie"])
print
print("Zad4, 3.Wszystkie imiona:")
print
for i in lista:
	print(i["imie"])







