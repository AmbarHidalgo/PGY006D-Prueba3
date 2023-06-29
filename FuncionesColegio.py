import numpy
import random
import os
import msvcrt

colegio=numpy.empty([5,7],object)

def limpiarpantalla():
    print("<<PRESS ANY KEY TO CONTINUE>>")
    msvcrt.getch()
    os.system('cls')

def titulo(texto):
    print("-------------")
    print(f"  {texto}    ")
    print("--------------")



def validarrut(rut):
    for i in range(10):
        if rut[i,0]==rut:
            return 1
    return -1

def guardar(rut,nom,edad,gen,prom,fechm,nomap):
    if None in colegio:
        if validarrut(rut)<0:
            if len(nom)>=2:
                if edad>=4:
                    for i in range(8):
                        if colegio[i,0]==None:
                            colegio[i,0]=rut
                            colegio[i,1]=nom
                            colegio[i,2]=edad
                            colegio[i,3]=gen
                            colegio[i,4]=prom
                            colegio[i,5]=fechm
                            colegio[i,6]=nomap
                            break

                else:
                    print("La edad debe ser mayor o igual a 4 años")

            else:
                print("Los nombres deben tener minimo 2 caracteres")

        else:
            print("Rut ya existente")

    else:
        print("No hay espacio disponible")

def buscaralumno(rut):
    indice=validarrut(rut)
    print(f"""ALUMNO ENCONTRADO
        Rut             : {colegio[indice,0]}
        Nombre          : {colegio[indice,1]}
        Edad            : {colegio[indice,2]}
        Género          : {colegio[indice,3]}
        Promedio        : {colegio[indice,4]}
        Fecha Matricula : {colegio[indice,5]}
        Nombre Apoderado: {colegio[indice,6]}""")
      
    
#certificados de 1) anotaciones de un alumno, 2) certificado de notas y 3) certificado de alumno regular

#Anotaciones
listaanotaciones=[]
listaanotaciones.append("Buen alumno, responsable")
listaanotaciones.append("Llega siempre atrasado a clases")
listaanotaciones.append("Expulsado de la sala por referirse con insulto a sus pares")
listaanotaciones.append("Destaca por su buen desempeño y superamiento en la asignatura")
listaanotaciones.append("Problemas de conducta, se recomienda visitar un psicólogo")

#notas
listacertfnotas=[]
listacertfnotas.append("6,8")
listacertfnotas.append("2,3")
listacertfnotas.append("1,0")
listacertfnotas.append("5.7")
listacertfnotas.append("4.1")


def anotaciones(rut):
    indice=validarrut(rut)
    if indice>=0:
        print(f"""
        -----------------------
        CERTIFICADO ANOTACIONES
        ------------------------
        {colegio[indice,0]}
        {colegio[indice,1]}
        ------------------------
        ANOTACIONES
        - {listaanotaciones[random.randint(0,2)]}
        - {listaanotaciones[random.randint(0,3)]}
        - {listaanotaciones[random.randint(0,5)]}""")
    
    else:
        print("Rut no registrado")

def notas(rut):
    indice=validarrut(rut)
    if indice>=0:
        print(f"""
        -------------------
        CERTIFICADO NOTAS
        -------------------
        {colegio[indice,0]}
        {colegio[indice,1]}
        --------------------
        - NOTA1: {listacertfnotas[random.randint(0,2)]}
        - NOTA2: {listacertfnotas[random.randint(0,3)]} 
        - NOTA3: {listacertfnotas[random.randint(0,5)]}""")

    else:
        print("Rut no registrado")


def alumnoregular(rut):
    indice=validarrut(rut)
    if indice>=0:
        print(f"""
        ---------------------------
        CERTIFICADO ALUMNO REGULAR
        ---------------------------
        {colegio[indice,0]}
        {colegio[indice,1]}
        ---------------------------
        Actualmente el alumno {colegio[indice,1]} se encuentra registrado 
        como Alumno Regular en el colegio San Charlis 
        con ubicación en Puente Alto""")

    else:
        print("Rut no registrado")