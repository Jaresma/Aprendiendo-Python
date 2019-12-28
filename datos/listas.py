""" una lista podemos guardar varios espacios en la memoria
    (son muy parecidos a arrays o vectores)
    nos permiten guardar cualquier tipo de valores
    se pueden expandir dinamicamente

    sintaxys
    nombreLista=[elem1,elem2,elem3]
    indice(posicion del elemento dentro de la lista)

"""

ListPersons=['maria','pepe','jair','jacobo']
""" agregar elemento al final de la lista """
ListPersons.append("abril")
""" agregar elemento en determinada posicion """
ListPersons.insert(2,"viviana")
""" agregar varios elementos """
ListPersons.extend(["holaa","mundo"])
"""  imprime toda la lista """
print(ListPersons[:]) 
""" por posicion(cuenta desde 0) """
print(ListPersons[2]) 
""" porsicion de lista """
print(ListPersons[0:3]) 
print(ListPersons[:3]) 
ListPersons.remove("jacobo")
print(ListPersons[2:]) 

print(ListPersons.index("jair"))
print ("jehfe" in ListPersons )
ListPersons.remove()


