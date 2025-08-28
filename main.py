
# EJERCICIO 2 

from cancion import Cancion


c1=Cancion("Me vas a estrañar ",129 ,"Cumbia Villera")


c2=Cancion("Goteo " ,185, "Trap")


c3=Cancion("Felices los 4" ,229, "Reggeton")


 #  EJERCICIO 3 
                              

print (c1 .obtenerNombre () , "-", c1.obtenerGenero())


print (c2 .obtenerNombre () , "-", c2.obtenerGenero())




print (c3 .obtenerNombre () , "-", c3.obtenerGenero())



# EJERCICIO 4


c2.establecerGenero("Rock")



print ("Nuevo genero  de Goteo " ,c2.obtenerGenero())