cant_toneladas = int(input("ingrese la cantidad de toneladas: "))
kilos = cant_toneladas * 1000
capacidad_del_camion = 3500
cant_camiones = (kilos + capacidad_del_camion - 1) // capacidad_del_camion

print(f"Se van a necesitar {cant_camiones} camiones para transportar los materiales")

kilometros = int(input("ingrese la cantidad de Kms por recorrer: "))
velocidad_max = 90
tiempo = kilometros / velocidad_max

print(f"El tiempo que tardara cada uno de los camiones en llegar a destino es {tiempo} horas")