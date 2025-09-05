
# EJERCICIO 2 

from cancion import Cancion

print("ejercicio 2")

c1=Cancion("Me vas a extrañar", 129, "Cumbia Villera")
        


c2=Cancion("Felices los 4 ",  229, "Reggaeton") 
        


c3= Cancion("Goteo",   185, "Trap"  )
        



print (c1 .obtenerNombre())

print (c2 .obtenerNombre())

print (c3 .obtenerNombre())




print(" Ejercicio 3")

print (c1.obtenerGenero())

print (c2.obtenerGenero())

print (c3.obtenerGenero())



print("ejercicio4")

c3.establecerGenero("Rock")



print ("Nuevo genero  de Goteo es" ,c3.obtenerGenero())

