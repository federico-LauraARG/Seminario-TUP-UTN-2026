#ejercicio integrador 1
nombre_person_1 = input("ingrese su nombre: ")
edad_person_1 = int(input("ingrese su edad: "))
peso_person_1 = int(input("inrgese su peso: "))

nombre_person_2 = input("ingrese su nombre: ")
edad_person_2 = int(input("ingrese su edad: "))
peso_person_2 = int(input("inrgese su peso: "))

precio_por_kilo = 1000
suma_de_pesos = peso_person_1 + peso_person_2
promedio_edad = (edad_person_1 + edad_person_2) / 2
costo_de_viaje = suma_de_pesos * precio_por_kilo

print(f"hola {nombre_person_1} y {nombre_person_2}, sus pesos son {peso_person_1} y {peso_person_2} kilos, sumados los dos da {suma_de_pesos} kilos y el promedio de edad es de {promedio_edad} años y su viaje tiene un valor de {costo_de_viaje} pesos.")

#ejercicio integrador 2
cant_toneladas = int(input("ingrese la cantidad de toneladas: "))
kilos = cant_toneladas * 1000
capacidad_del_camion = 3500
cant_camiones = (kilos + capacidad_del_camion - 1) // capacidad_del_camion

print(f"Se van a necesitar {cant_camiones} camiones para transportar los materiales")

kilometros = int(input("ingrese la cantidad de Kms por recorrer: "))
velocidad_max = 90
tiempo = kilometros / velocidad_max

print(f"El tiempo que tardara cada uno de los camiones en llegar a destino es {tiempo} horas")
