# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 10:26:06 2021

@author: Javier
"""

from pymongo import MongoClient  # IMPORTO LA LIBRERIA PYMONGO




def del_base_datos():
    pass



def ubicacion():

    lugar = int(input("Pulsa 1 para trabajar en Local y 2 para trabajar en remoto...: "))

    global client

    if lugar == 1:

        client = MongoClient("localhost") # LE INDICO QUE ES UNA BASE DE DATOS CREADA EN LOCAL
        print ("\nAhora estás conectado en Local")

    else:
        remoto = input("Introduce la instrucción para la conexión..:") # INTRODUZCO LA DIRECCIÓN PROPORCIONADA EN ATLAS

        client = MongoClient(remoto)
        print ("\nAhora estás conectado en Remoto")









def crear_base_datos():

    global a

    a = input("\nIntroduzca el nombre de la nueva base de datos...: ")

    global db


    db = client[(a)]   # CREO LA BASE DE DATOS EN LOCAL

    print ("\nNueva base de datos creada en local con nombre "+str(a)+"\nNo se mostrará hasta que no tenga una colección y un documento")







def crear_coleccion():

    col = input("\nIntroduzca el nombre de la nueva Colección...: ")

    global coleccion


    coleccion = db[(col)] # CREO LA COLECCIÓN EN LA BASE DE DATOS "PRUEBA"

    print ("\nNueva colección creada en la base de datos "+str(a) + "  con nombre " + str(col) + "\nNo se mostrará hasta que no tenga un documento")







def crear_documentos():



    coleccion.insert_one({   # INSERTO UN DOCUMENTO EN LA COLECCIÓN

                                "edad": 20,
                                "nombre": "Javier0",
                                "intereses": ["musica0", "deportes0"]

                                })





    coleccion.insert_many([      # INSERTO 2 DOCUMENTOS A LA VEZ CON MANY
                            {
                                "edad": 21,
                                "nombre": "Javier1",
                                "intereses": ["musica1", "deportes1"]
                                },
                            {
                                "edad": 22,
                                "nombre": "Javier2",
                                "intereses": ["musica2", "deportes2"]
                                }

        ])




# print (client.list_database_names()) # IMPRIMO LA BASES DE DATOS QUE TENGO EN LOCAL
# print("\n")


# print ("\nEn la colección hay, " + str(coleccion.count_documents({}))+" documentos ")  # CUENTO LOS DOCUMENTOS QUE HAY EN LA COLECCIÓN




def edicion():

    for i in coleccion.find({}):   # MUESTRA TODOS LOS DOCUMENTOS

        print("\n"+str(i))


    coleccion.delete_one({     # BORRA LAS COLECCIONES QUE CONTIENEN EN EL DOCUMENTO "EDAD" EL VALOR 20
                          "edad": 20
                          })


    coleccion.update_many({     # SUSTITULLE EL VALOR 22 EN EDAD POR 30

                           "edad": 22
                           }, {
                               "$set": {
                                   "edad": 19
                                   }

                               })






def del_coleccion():

    print ("\n Las colecciones existentes son: "+ (db.list_collection_names()))   # IMPRIMO LAS COLECCION DE LA BASE DE DATOS CREADA




#coleccion.delete_many({})  # BORRA TODAS LAS COLECCIONES

#db.drop_collection("personas") # ELIMINA LAS COLECCIONES

#client.drop_database("kk")  #ELIMINA LA BASE DE DATOS



menu = False

while not menu:

    print("\n")
    print ("1.- DONDE QUEREMOS TRABAJAR")
    print ("2.- CREAR BASE DE DATOS")
    print ("3.- CREAR COLECCION")
    print ("4.- CREAR DOCUMENTOS")
    print ("5.- EDICION DE DOCUMENTOS")
    print ("6.- ELIMINAR COLECCION")
    print ("7.- ELIMINAR BD")
    print ("8.- SALIR")


    op = int(input("\nEscoja una opción...: "))


    if op == 1:
        ubicacion()

    elif op ==2:
        crear_base_datos()

    elif op ==3:
        crear_coleccion()

    elif op ==4:
        crear_documentos()

    elif op ==5:
        edicion()

    elif op ==6:
        del_coleccion()

    elif op ==7:
        del_base_datos()

    elif op == 8:
        menu=True

    else:

        print("\nSolo puedes marcar un número del 1 al 8, zopenco")















