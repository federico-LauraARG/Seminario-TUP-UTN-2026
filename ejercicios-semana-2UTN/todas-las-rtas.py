nombre_de_usuario = input("Escriba su nombre de usuario: ")
print(nombre_de_usuario)

num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))
resultado = num1 + num2
print("el resultado de la suma es ", resultado)

nombre_de_usuario = input("ingrese su nombre: ")
apellido_de_usuario = input("ingrese su apellido: ")
edad_de_usuario = int(input("ingrese su edad: "))
print(nombre_de_usuario)
print(apellido_de_usuario)
print(edad_de_usuario)

nombre = input("ingrese su nombre: ")
comision = int(input("Comision: "))
asignatura = input("Asignatura: ")
docente = input("Docente: ")
usuario_presente = bool(input("estuvo presente? si/no "))

print(nombre)
print(comision)
print(asignatura)
print(docente)
print(usuario_presente)

lado_cuadrado = int(input("ingrese el lado de un cuadrado: "))
superficie = lado_cuadrado ** 2
print(superficie)

ladoA_rectangulo = int(input("ingrese el lado A de un rectangulo: "))
ladoB_rectangulo = int(input("ingrese el lado B de un rectangulo: "))
superficie = ladoA_rectangulo * ladoB_rectangulo
print("La superficie del rectangulo es", superficie)

base_de_triangulo = int(input("ingrese la base de un triangulo: "))
altura_de_triangulo = int(input("ingrese la altura de un triangulo: "))
superficie = base_de_triangulo * altura_de_triangulo // 2
print(superficie)

nombre_de_producto = input("ingrese el nombre del producto: ")
precio_del_producto = float(input("ingrese el precio: "))
precio_final = precio_del_producto  * 1.21
print("El precio final con IVA es de:", precio_final)

nombre_de_alumno = input("ingrese su nombre: ")
apellido_de_alumno = input("ingrese su apellido: ")

nota1 = int(input("ingrese la primer nota: "))
nota2 = int(input("ingrese la segunda nota: "))
nota3 = int(input("ingrese la tercer nota: "))
promedio_final = (nota1 + nota2 + nota3) / 3
print("El promedio final es", promedio_final)

nombre_de_usuario = input("ingrese el nombre de usuario: ")
edad = int(input("ingrese su edad: "))
print("Dentro de 10 años tendrás:", edad + 10)