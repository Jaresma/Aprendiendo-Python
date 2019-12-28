""" listas inmutables es decir
no se pueden modificar 
permite extraer porcione s, pero el resultado
es una nueva tupla

no permiten busqueda
si permiten comprobar si un elemtno se encuentra
en la tupla
ventajas:
mas rapida
menos espacio
formatean strings
pueden utilizarse como claves en un 
diccionario 
sintaxis de las tuplas
nombreTupla=(elem1,elem2,elem3)
"""

mitupla=("juan",13,1,1995,13)

print(mitupla[2])
""" convertir tupla en lista  (list)"""
""" de lista a tupla (tuple) """
milista=list(mitupla)
print(milista)
print(mitupla)
""" podemos verificar s existen en la tupla """
print("juan" in mitupla)
print("juangrwg" in mitupla)
"""  cuantos elementos se encuentran dentro de una tupla (count) """
print(mitupla.count(13))
""" ver de que tama;o es una tupla (len)"""
print(len(mitupla))
""" tupla unitaria """
tuplaunitaria=("juan",)
print(len(tuplaunitaria))
""" empaquetado de tupla """
tuplaem="juan",1,13,19
print(tuplaem)
""" desempaquetado de tupla """
nombre,dia,mes,ago=tuplaem
print(nombre)
print(ago)
print(mes)
print(dia)
""" HINT:NO PODEMOS MODIFICAR LAS TUPLAS  """

