""" estructura de datos
a la hora de almacenar los datos se
hace asociacion de tipo clave:valor 

puede almacenar cualquier valor diferente
podemos almacenar listas , tuplas y diccionarios
el orden con el que se almacenan los valores da igual

"""
""" clave:valor """
midiccionario={"Alemania":"Berlin","Francia":"Paris","Reino Unido":"Londres","Esp":"Madrid"}
print(midiccionario["Francia"])
print(midiccionario["Esp"])
print(midiccionario)
""" como agregar mas elementos """
midiccionario["Italia"]="Lisboa"
print(midiccionario)
""" modificar """
midiccionario["Italia"]="Roma"
print(midiccionario)
""" Eliminar """
del midiccionario["Reino Unido"]
print(midiccionario)

diccionario2={"Alemania":"Berlin",23:"Jordan","Mosquereros":3}
print(diccionario2)

mitupla=["Espania","Francia","Reino Unido","Alemania"]
tupla2dic={mitupla[0]:"Madrid",mitupla[1]:"Paris",mitupla[2]:"Londres",mitupla[3]:"Berlin"}
print(tupla2dic)
"""  como un diccionario almacene una tupla """
tuplaindic={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","Anillos":[1991,1992,1993,1996,1997,1998]}
print(tuplaindic)
print(tuplaindic["Anillos"])
""" accede a las llaves  """
print(tuplaindic.keys())
""" valores """
print(tuplaindic.values())
""" tama;o """
print(len(tuplaindic))
