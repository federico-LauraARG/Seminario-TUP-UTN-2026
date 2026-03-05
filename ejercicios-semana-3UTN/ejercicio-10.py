importe_usuario = input("ingrese el importe: ")
descuento_usuario = input("ingrese su descuento: ")

importe_usuario = int(importe_usuario)
descuento_usuario = float(descuento_usuario)

descuento = importe_usuario * (descuento_usuario / 100)
importe_actualizado = importe_usuario - descuento

print(f"el importer con el descuento actualizado es: {importe_actualizado}")

