#1. Mostrar por pantalla: “Hola Mundo, esto es Python!”.
print("Hola Mundo, esto es Python!")

#2. Escriba un programa que solicite el nombre del usuario y luego muestre el
#mensaje de salida “Hola nombre”, donde nombre es el nombre que ingresó el
#usuario.
print("Escriba su nombre")
nombre = input()
print("Hola "+ nombre)

#3. Solicite al usuario su nombre y luego solicite su apellido y por último
#muestre el mensaje de salida “Hola nombre apellido”.
print("Escriba su primer Nombre")
nombre = input()
print("Escriba su apellido")
apellido = input()
print("Hola "+ nombre, apellido)

#4. Pida al usuario que ingrese 2 números para luego sumarlos y mostrar en
#pantalla: “La respuesta es XX”.
print("Escriba un número")
num1 = int(input())
print("Escriba otro número")
num2 = int(input())
suma = num1 + num2
print("La respuesta es", suma)

#5. Escriba un programa que pida al usuario que ingrese 3 números. Sume los
#dos primeros y luego multiplique este total por el tercero. Mostrar la respuesta
#en pantalla de la siguiente forma: “La respuesta es XX”.
print("Escriba un número")
num1 = int(input())
print("Escriba otro número")
num2 = int(input())
print("Escriba el último número")
num3 = int(input())
resultado = (num1 + num2) * num3
print("La respuesta es " + str(resultado))

#6. Programe una aplicación de consola que pregunte el precio total de la
#cuenta, luego pregunte cuántos comensales hay. A continuación deberá
#dividir la cuenta total por el número de comensales y mostrar cuánto debe
#pagar cada persona.
print("Escriba el precio total de la cuenta")
cuen= int(input())
print("Escriba por el numero de personas que deseadividir la cuenta")
comens= int(input())
total= cuen / comens
print("Cada persona debe pagar " + str(total))


#7. Pida al usuario un número x de días y luego mostrar por pantalla cuántas
#horas, minutos y segundos son esos números de días.
print("Escriba una cantidad de dias")
dias=int(input())
hora = dias * 24
minutos= dias * 60
segundos= dias * 60
print(dias, "dias son:", hora, "horas", minutos,
"minutos",segundos, "segundos" )

#8. Escriba un programa que permita al usuario ingresar la base y altura de un
#triángulo para luego imprimir por pantalla la superficie total.
print("Ingrese la base de su triangulo")
base= int(input())
print("Ingrese la altura de su triangulo")
altura= int(input())
sup = base * altura
print("La superficie de su triangulo es", sup)

#9. Pida al usuario que ingrese un texto para luego imprimirlo al revés. Ej: HOLA -> ALOH
print("Ingrese un texto")
text=input()
print("Texto invertido:", text[::-1])

#10. Escriba un programa que indique si un texto es palíndromo, es decir, se
#escribe igual al derecho que al revés. Por ejemplo: rayar, kayak, somos.
print("Escribe un texto para verificar si es palíndromo:")
text=input().replace(" "," ").lower()
if text == text[::-1]:
 print("El texto es palindromo")
else:
 print("El texto no es palindromo")

#11. Programe una aplicación de consola que muestre los primeros 5 caracteres
#de una cadena de texto ingresada por el usuario.
print("Ingrese un texto")
text=input().replace(" "," ")
print("primeros 5 caracteres:", text[:6:])

#12. Pedir al usuario que ingrese una fecha en formato dd/mm/aaaa e imprimir
#en pantalla el día, mes y año. Ej: Usuario ingresa: 17/05/1985 Programa
#imprime: Día: 17, Mes: 05 y Año: 1985
print("Ingrese el día")
dia=int(input())
print("Ingrese el mes")
mes=int(input())
print("Ingrese el año")
anio=int(input())
print("Día: "+ str(dia)+", "+"Mes: "+ str(mes)+" y "+
"Año: "+str(anio))

#13. Programe una aplicación de consola que solicite al usuario su nombre,
#después su apellido y a continuación su año de nacimiento. Con esos datos
#deberá generar una sugerencia de usuario y contraseña. Por ejemplo: nombre:
#Martín, apellido: Francisconi, Año nacimiento: 1985 -> Usuario: mfrancisconi,
#Contraseña: mf.1985.
print("Escriba su Nombre")
nombre=input()
print("Escriba su Apellido")
apellido=input()
print("Escriba su Año de Nacimiento")
nacimiento=input()
usuario= nombre[:1:] + apellido + nacimiento
contra= nombre[:1:] + apellido[:2:] + "." + nacimiento
print("Sugerencia de Usuario: " + str(usuario).lower())
print("Sugerencia de Contraseña: " +
str(contra).lower())

