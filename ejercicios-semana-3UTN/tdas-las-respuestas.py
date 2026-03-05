print("Bienvenidos a la UTN")

nombre = input("ingresa tu nombre de usuario: ")
print(f"su nombre de usuario es: {nombre}")

nombre = input("ingrese su nombre: ")
edad = int(input("ingrese su edad: "))
print(f"Usted se llama {nombre} y su edad es {edad}")

operador_a = input("ingrese el primer numero: ")
operador_b = input("ingrese el segundo numero: ")
operador_a = int(operador_a)
operador_b = int(operador_b)
resultado = operador_a + operador_b
print(f"El resultado de la suma es: {resultado}")

input("seleccione la operación:(suma/resta/multiplicacion/division) ")
operador_a = input("ingrese el primer numero: ")
operador_b = input("ingrese el segundo numero: ")
operador_a = int(operador_a)
operador_b = int(operador_b)
suma = operador_a + operador_b
resta = operador_a - operador_b
multiplicacion = operador_a * operador_b
division = operador_a / operador_b
print(f"el resultado de la suma es: {suma}")
print(f"el resultado de la resta es: {resta}")
print(f"el resultado de la multiplicacion es: {multiplicacion}")
print(f"el resultado de la division es: {division}")

operador_a = input("ingrese el primer numero: ")
operador_b = input("ingrese el segundo numero: ")
operador_a = int(operador_a)
operador_b = int(operador_b)
resto = operador_a % operador_b
print(f"el resto de dividir {operador_a} y {operador_b} es {resto}")

sueldo = input("ingrese el sueldo: ")
sueldo = int(sueldo)
sueldo_actualizado = sueldo * 1.15
print(f"Su sueldo actualizado es de: {sueldo_actualizado}")

sueldo = input("ingrese su sueldo: ")
incremento = input("ingrese el porcentaje de incremento: ")
sueldo = int(sueldo)
incremento = int(incremento)
sueldo_actualizado = sueldo + (sueldo * incremento / 100)
print(f"el sueldo actualizado es de: {sueldo_actualizado}")

importe = input("ingrese el importe: ")
importe = int(importe)
importe_actualizado = importe - (importe * 0.20)
print(f"el importe actualizado es de: {importe_actualizado}")

importe_usuario = input("ingrese el importe: ")
descuento_usuario = input("ingrese su descuento: ")
importe_usuario = int(importe_usuario)
descuento_usuario = float(descuento_usuario)
descuento = importe_usuario * (descuento_usuario / 100)
importe_actualizado = importe_usuario - descuento
print(f"el importer con el descuento actualizado es: {importe_actualizado}")

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
