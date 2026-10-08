#1. El programa: Dada una nota de examen y un porcentaje de asistencia, devuelve aprobado True o False.
#2. Condiciones: Nota examen algo >= 70 y asistencia algo>= 80. 

#3. Recoger nota y asistencia.
#    - Concepto: usamos input para recoger los datos (score y assistance)
#    - Convertimos la nota y asistencia a int.  
# Explicación: Input recoge una entrada de trexto del usuario en el terminar, el texto se ve en la terminal y tú meter el valor, solo recoge strings. 
# Explicación: ponemos el int delante porque es más limpio, en vez de hacer en una linea debajo score = int(score). 
score = int(input("Introduce la nota del examen ( de 0 a 100): "))

assistance = int(input("Introduce la asistencia ( 0 a 100 sin %):"))


#4. Asigno True o False a aprobado en base a las condiciones. 
aproved = False 
# Hemos escrito aproved = false como si fuera por defecto, para que la siguiente línea sea la que establece que SI CUMPLES LAS CONDICIONES, entonces aproved cambia a true. 
if score >= 70 and assistance >= 80:
    aproved = True

#5. Devolver aprobado True o False
if aproved:
    print("Has aprovado fokin máquina")
else:
    print("Hay que renacer de las cenizas")
    
#Otra manera de hacerlo sería: 
#   if score >= 70 and assistance >=80:
#      print("has aprobado bro ")
#   else: 
#      print("Julio es un buen mes para intentarlo")