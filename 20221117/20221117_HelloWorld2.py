"""
Ejercicio 20
Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos)
después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos,
20 céntimos o 10 céntimos).
"""


import datetime


def checkMoney():
    two_euro = int(input("Cuántas monedas de dos euros?")) * 2
    one_euro = int(input("Cuántas monedas de un euro?"))
    fifty_cent = float(input("Cuántas monedas de 50 céntimos?")) * 0.5
    twenty_cent = float(input("Cuántas monedas de 20 céntimos?")) * 0.2
    five_cent = float(input("Cuántas monedas de 10 céntimos?")) * 0.1

    total = float(two_euro + one_euro + fifty_cent + twenty_cent + five_cent)

    print("Tienes {:.2f} euros".format(total))


"""
Ejercicio 19
Escribir un algoritmo para calcular la nota final de un estudiante,
considerando que: por cada respuesta correcta 5 puntos, por una
incorrecta -1 y por respuestas en blanco 0. 
Imprime el resultado obtenido por el estudiante.
"""


def calcularNota(aciertos: int, fallos: int, en_blanco: int):
    try:
        return (int(aciertos) * 5) + (int(fallos) * -1) + (int(en_blanco) * 0)
    except ValueError:
        return "Los parámetros a recibir han de ser números."


"""
Ejercicio 18
Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.
"""


def muestraIniciales():
    name_surname = input("Dime to nombre y apellidos: ")
    name_surname.replace("[a-z ]", "")
    split = name_surname.split()  # Empty replaces all white space instances.
    iniciales = ""
    for word in split:
        iniciales += word[0]
    print(iniciales)


"""
Ejercicio 17
Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos.
El tiempo de viaje hasta llegar a otra ciudad B es de T segundos.
Escribir un algoritmo que determine la hora de llegada a la ciudad B.
"""


def calculaTiempo(horas: int, minutos: int, segundos: int, segundosExtra: int):
    try:
        segundosTotales = horas * 3600 + minutos * 60 + segundos
        resultado = datetime.timedelta(seconds=(segundosTotales + segundosExtra))
        print(f"Hora de salida {datetime.timedelta(seconds=segundosTotales)} y llegada: {resultado}")
    except TypeError:
        print("Sólo carácteres numéricos, por favor.")


def main():
    cond = 0
    while cond < 10:
        cond+= 1
        if cond == 5:
            print(cond)
            break
    else:
        print(cond)


main()
