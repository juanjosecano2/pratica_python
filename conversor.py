pesos = input("cuantos pesos colombianos tienes?")
pesos = float(pesos)
valordolar = 3.875
dolares = pesos / valordolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes: $" + dolares + " dolares")