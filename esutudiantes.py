alumn={}

while True:
    opc=0
    print("Menu")
    print("1. Registrar Alumno y sus notas")
    print("2. Mostrar Alumno y sus notas ")
    print("3. modificar notas")
    print("4. Calcular promedio ")
    print("5. Salir ")

    
    opc=int(input("ingrese una opcion: "))
    if opc==1: 
        alumnos=int(input("diguite la cantidad de estudiantes por favor:"))
        for x in range(alumnos):
            estuden=input(f"resgistra el nombre del estudiante { x + 1}: ")
            
            seguirn=False
            while(seguirn==False):
                no1=float(input("introduce la nota 1:"))
                if (no1>=0 and no1<=5):
                    seguirn=True  

                else:
                    print("la nota que ingreso no es valida, por favor ingresa una que si sea valida (0-5.0)")
                    no1=float(input("introduce la nota 1:"))
            
                nota2=float(input("introduce la nota 2:"))
                if (nota2>=0 and nota2<=5):
                    seguirn=True

                else:
                    print("la nota que ingreso no es valida, por favor ingresa una que si sea valida (0-5.0)")
                    nota2=float(input("introduce la nota 2:"))
            
        
                no3=float(input("introduce la nota 3:"))
                if (no3>=0 and no3<=5):
                    seguirn=True
                    
                else:
                    print("la nota que ingreso no es valida, por favor ingresa una que si sea valida (0-5.0)")
                    no3=float(input("introduce la nota 3:")) 
                     
                notas=no1,nota2,no3
                alumn[estuden]=notas
                
    elif opc==2:
            print(alumn )
            
            
    elif opc==3:
        estuden=input("ingrese el nombre del estudainte:")
        
        notaNU=int(input("¿que nota deseas modificar? 1,2,3 "))
        if notaNU==1:
           if estuden in alumn:
                    no1=float(input("ingrese la nueva nota por favor:"))
                    alumn[estuden]=no1,nota2,no3
                    print("nota actualizada ")
                    
    
        
        elif notaNU==2:
            if estuden in alumn:
                nota2=float(input("ingrese la nueva nota por favor:"))
                alumn[estuden]=no1,nota2,no3
                print("nota actualizada ")
        
        elif notaNU==3:
             if estuden in alumn:
                    no3=float(input("ingrese la nueva nota por favor:"))
                    alumn[estuden]=no1,nota2,no3
                    print("nota actualizada ")
                    
        
        else:
            print("opcion no valida")
        
    elif opc==4:
        estuden=input("por favor ingrese el nombre del estudiante a calcular el promedio: ")
        no1,nota2,no3 = alumn[estuden]
        promedio=(no1 + nota2 + no3)/3
        print(f"el promedio del estudiante {estuden} es:",(promedio))
         


    elif opc==5:
        break            