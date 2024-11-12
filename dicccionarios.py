frutas_colores = {"manzana":"rojo","pera":"verde","uva":"morada"}
print(frutas_colores)

#diccionario datos personales
datos_personales = {"nombre":"juana","apellido":"manotoa","edad":46,"estado":True}
print(datos_personales["nombre"])

#añadir una nueva fruta
frutas_colores["naranja"]="anaranjado" 
frutas_colores["papaya"]="amarilla"
print("el diccionario actual es :",frutas_colores)

#eliminar frutas 
frutas_colores.pop("papaya")
