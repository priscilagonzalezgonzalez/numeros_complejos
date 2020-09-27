from complejo import Complejo


while True:
    print("MENU")
    print("1) Sumar dos numeros complejos")
    print("2) Restar dos numeros complejos")
    print("0) Salir")
    op = input()
    if(op == "0"):
        break
    
    real = int (input("Numero real: "))
    imaginario = int (input("Numero imaginario: "))
    c = Complejo(real, imaginario)
    real = int (input("Numero real: "))
    imaginario = int (input("Numero imaginario: "))
    c2 = Complejo(real, imaginario)
       

    if op == "1":
        Complejo.suma(c, c2)

    elif op == "2":
        Complejo.resta(c, c2)
    
