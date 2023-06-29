import FuncionesColegio as fc

while True:
    try:
        fc.limpiarpantalla()

        fc.titulo("Colegio San Charlis")
        print("""
        1) Registrar alumno
        2) Buscar alumno
        3) Imprimir certificados
        0) Salir""")
        opcion=int(input("Seleccione :"))

        if opcion==0:
            print("Adios :D")
            break

        elif opcion==1:
            fc.titulo("Registrar Alumno")
            rut=int(input("Ingrese rut :"))
            nom=input("Ingrese nombre :")
            edad=int(input("Ingrese edad :"))
            gen=input("Ingrese genero :")
            prom=str(input("Ingrese promedio :"))
            fechm=input("Ingrese fecha de matricula :")
            nomap=input("Ingrese nombre de apoderado :")
            fc.guardar(rut,nom,edad,gen,prom,fechm,nomap)

        elif opcion==2:
            fc.titulo("Buscar Alumno")
            rut=int(input("Ingrese rut alumno :"))
            fc.buscaralumno(rut)

        elif opcion==3:
            fc.titulo("Imprimir Certificados")
            cert=int(input("Ingrese 1 para Anotaciones||Ingrese 2 para Notas|| Ingrese 3 para Certificado Alumno Regular :"))
            if cert==1:
                rut=int(input("Ingrese rut :"))
                fc.anotaciones(rut)
            
            elif cert==2:
                rut=int(input("Ingrese rut :"))
                fc.notas(rut)

            elif cert==3:
                rut=int(input("Ingrese rut :"))
                fc.alumnoregular(rut)

            else:
                print("Opcion no valida")

            
        else:
            print("Opcion no valida")
    except:
        print("Error en el sistema")
    