# Declaramos una variable
calificacion = input("Introduce tu calificación: ")
calificacion = int(calificacion)

# Preguntamos si la calificación es menor a 700 
if calificacion < 700: 
    print("Reprobado")
elif calificacion > 1000 : 
    print("No se puede mas de 1000 puntos")
else: 
    print("Felicidades")



# Verificación de mayoria de edad
edad = input("Introduce tu edad")
edad = int(edad)

if edad >=18 and edad <=110 :
    print("Eres bienvenido")
elif edad > 100 :
    print("Te podemos fiar si vienes acompañado de tus abuelitos")
elif edad < 0 :
    print("Imposible")
else :
    print("Eres menor de edad")