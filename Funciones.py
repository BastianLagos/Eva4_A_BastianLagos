from beautifultable import BeautifulTable
from Alumnos import Alumnos
from DAO import DAO
from os import system
import json
import os
import requests

class Funciones():

    d = DAO()

# ---------------------------------------------------------------------

    def __init__(self):
        pass

# ---------------------------------------------------------------------

    def menu(self):
        while True:
            try:
                system("cls")
                print("-----------------------")
                print("--- MENÚ DE ALUMNOS ---")
                print("-----------------------")
                print("1.Registrar Alumnos")
                print("2.Listar Alumnos")
                print("3.Buscar Alumnos")
                print("4.Modificar Datos De Alumnos")
                print("5.Eliminar Alumnos")
                print("6.Estadistica")
                print("7.Salir")
                op = int(input("Digite Una Opcion : "))
                if op!=1 and op!=2 and op!=3 and op!=4 and op!=5 and op!=6 and op!=7:
                    print("\n--- Error De Opcion De Menu!! ---")
                    system("pause")
                else:
                    if op==1:
                        self.__registrarAlumnos()
                    elif op==2:
                        self.__listarAlumnos()
                    elif op==3:
                        self.__buscarAlumnos()
                    elif op==4:
                        self.__modificarDatosDeAlumnos()
                    elif op==5:
                        self.__eliminarAlumnos()
                    elif op==6:
                        self.__estadistica()
                    elif op==7:
                        self.__salir()
                        os._exit(1)
            except:
                print("\n--- Error De Opcion Try!! ---")
                system("pause")

# ---------------------------------------------------------------------

    def __registrarAlumnos(self):
        while True:
            try:
                system("cls")
                rut = input("Digite El Rut De El/La Alumno/Alumna : ")
                if len(rut.strip())<9 or len(rut.strip())>12:
                    print("\n--- Debe Tener Entre 9 y 12 Caracteres!! ---")
                    system("pause")
                else:
                    r = self.d.comprobarRut(rut)
                    if r is None:
                        break
                    else:
                        print("\n--- El Rut (",rut,") Ya Existe!! ---")
                        system("pause")
            except:
                print("\n--- Error Al Intentar Almacenar El Rut!! ---")
                system("pause")

        while True:
            try:
                system("cls")
                nom = input("Digite El Nombre De El/La Alumno/Alumna : ")
                if len(nom.strip())<1 or len(nom.strip())>40:
                    print("\n--- Debe Tener Entre 1 y 40 Caracteres!! ---")
                    system("pause")
                else:
                    break
            except:
                print("\n--- Error Al Intentar Almacenar El Nombre!! ---")
                system("pause")

        while True:
            try:
                system("cls")
                pat = input("Digite El Apellido Paterno De El/La Alumno/Alumna : ")
                if len(pat.strip())<1 or len(pat.strip())>40:
                    print("\n--- Debe Tener Entre 1 y 40 Caracteres!! ---")
                    system("pause")
                else:
                    break
            except:
                print("\n--- Error Al Intentar Almacenar El Apellido Paterno!! ---")
                system("pause")

        while True:
            try:
                system("cls")
                mat = input("Digite El Apellido Materno De El/La Alumno/Alumna : ")
                if len(mat.strip())<1 or len(mat.strip())>40:
                    print("\n--- Debe Tener Entre 1 y 40 Caracteres!! ---")
                    system("pause")
                else:
                    break
            except:
                print("\n--- Error Al Intentar Almacenar El Apellido Materno!! ---")
                system("pause")

        while True:
            try:
                system("cls")
                eda = int(input("Digite La Edad De El/La Alumno/Alumna : "))
                if eda<1 or eda>125:
                    print("\n--- Debe Estar Entre 1 y 125!! ---")
                    system("pause")
                else:
                    break
            except:
                print("\n--- Error Al Intentar Almacenar La Edad!! ---")
                system("pause")

        while True:
            try:
                system("cls")
                respuesta = requests.get("https://movilappml2021.000webhostapp.com/EVA4_POO/FORMA_A/datos_cursos.json")
                dd = respuesta.json()
                tabla = BeautifulTable()
                for x in dd["cursos"]:
                    tabla.rows.append([x["idCur"],x["nomCur"]])
                tabla.columns.header = ["ID CURSO","NOMBRE CURSO"]
                print(tabla)
                opc = int(input("Digite El ID Del Curso De El/La Alumno/Alumna : "))
                if opc!=1 and opc!=2 and opc!=3 and opc!=4 and opc!=5 and opc!=6 and opc!=7 and opc!=8:
                    print("\n--- El ID del Curso Debe Estar Entre 1 y 8!! ---")
                    system("pause")
                else:
                    if opc==1:
                        cur = "1 A"
                    elif opc==2:
                        cur = "1 B"
                    elif opc==3:
                        cur = "2 A"
                    elif opc==4:
                        cur = "2 B"
                    elif opc==5:
                        cur = "3 A"
                    elif opc==6:
                        cur = "3 B"
                    elif opc==7:
                        cur = "4 A"
                    else:
                        cur = "4 B"
                    break
            except:
                print("\n--- Error Al Intentar Almacenar El Curso!! ---")
                system("pause")

        while True:
            try:
                system("cls")
                respuesta = requests.get(" https://movilappml2021.000webhostapp.com/EVA4_POO/FORMA_A/datos_ensenanzas.json")
                dd = respuesta.json()
                tabla = BeautifulTable()
                for x in dd["ensenanzas"]:
                    tabla.rows.append([x["idEns"],x["nomEns"]])
                tabla.columns.header = ["ID ENSEÑANZA","NOMBRE ENSEÑANZA"]
                print(tabla)
                opci = int(input("Digite El ID De la Enseñanza De El/La Alumno/Alumna : "))
                if opci!=1 and opci!=2:
                    print("\n--- El ID de la Enseñanza Debe Estar Entre 1 y 2!! ---")
                    system("pause")
                else:
                    if opci==1:
                        ens = "BASICA"
                    else:
                        ens = "MEDIA"
                    break
                        
            except:
                print("\n--- Error Al Intentar Almacenar La Enseñanza!! ---")
                system("pause")

        a = Alumnos()
        a.setRut(rut.upper())
        a.setNombre(nom.upper())
        a.setPaterno(pat.upper())
        a.setMaterno(mat.upper())
        a.setEdad(eda)
        a.setCurso(cur)
        a.setEnsenanza(ens)
        a.setEstado(1)

        self.d.agregarAlumnos(a)

        system("cls")
        print("------------------------")
        print("--- REGISTRO EXITOSO ---")
        print("------------------------")
        print("RUT         : ",a.getRut())
        print("NOMBRE      : ",a.getNombre())
        print("APE PATERNO : ",a.getPaterno())
        print("APE MATERNO : ",a.getMaterno())
        print("EDAD        : ",a.getEdad())
        print("CURSO       : ",a.getCurso())
        print("ENSEÑANZA   : ",a.getEnsenanza(), end="\n\n")
        system("pause")
        self.menu()

#-----------------------------------------------------------------------------------------------------------

    def __listarAlumnos(self):
        r = self.d.obtenerAlumnos()
        if len(r)==0:
            system("cls")
            print("--------------------------------------")
            print("--- No Hay Registros Para Listar!! ---")
            print("--------------------------------------")
            system("pause")
            self.menu()
        else:
            tabla = BeautifulTable()
            for x in r:
                dd = json.loads(x[1])
                tabla.rows.append( [  x[0], dd["nom"], dd["pat"], dd["mat"], dd["eda"],dd["cur"],dd["ens"] ])
            tabla.columns.header = ["RUT","NOMBRE","A PATERNO","A MATERNO","EDAD","CURSO","ENSEÑANZA"]
            system("cls")
            print("--- LISTADO ALUMNOS ---")
            print(tabla, end="\n\n")
            system("pause")
            self.menu()

#-------------------------------------------------------------------------------------------------------

    def __buscarAlumnos(self):
        try:
            system("cls")
            rut = input("Digite El Rut De El Alumno o La Alumna a Buscar : ")
            if len(rut.strip())<9 or len(rut.strip())>12:
                print("\n--- Debe Tener Entre 9 y 12 Caracteres!! ---")
                system("pause")
                self.menu()
            else:
                a = self.d.buscarAlumnos(rut)
                if a is None:
                    print("\n--- Rut Buscado (",rut,") No Encontrado!! ---")
                    system("pause")
                    self.menu()
                else:
                    system("cls")
                    print("-------------------------")
                    print("--- ALUMN@ ENCONTRAD@ ---")
                    print("-------------------------")
                    print("RUT       :",a.getRut())
                    print("NOMBRE    :",a.getNombre())
                    print("PATERNO   :",a.getPaterno())
                    print("MATERNO   :",a.getMaterno())
                    print("EDAD      :",a.getEdad())
                    print("CURSO     :",a.getCurso())
                    print("ENSEÑANZA :",a.getEnsenanza(), end="\n\n")
                    system("pause")
                    self.menu()
        except:
            print("\n--- Error Al Intentar Buscar Alumno!! ---")
            system("pause")
            self.menu()

#-----------------------------------------------------------------------------------------------------

    def __modificarDatosDeAlumnos(self):
        try:
            system("cls")
            rut = input("Digite El Rut De El/La Alumno/Alumna Que Desea Modificar Los Datos : ")
            if len(rut.strip())<9 or len(rut.strip())>12:
                print("\n--- Debe Tener Entre 9 y 12 Caracteres!! ---")
                system("pause")
                self.menu()
            else:
                a = self.d.buscarAlumnos(rut)
                if a is None:
                    print("\n--- Rut Buscado (",rut,") No Encontrado. Imposible Modificar Datos!! ---")
                    system("pause")
                    self.menu()
                else:
                    system("cls")
                    print("--------------------------")
                    print("--- PERSONA ENCONTRADA ---")
                    print("--------------------------")
                    print("RUT       :",a.getRut())
                    print("NOMBRE    :",a.getNombre())
                    print("PATERNO   :",a.getPaterno())
                    print("MATERNO   :",a.getMaterno())
                    print("EDAD      :",a.getEdad())
                    print("CURSO     :",a.getCurso())
                    print("ENSEÑANZA :",a.getEnsenanza(), end="\n\n")
                    
                    print("1.RUT // 2.NOMBRE // 3.PATERNO // 4.MATERNO // 5.EDAD // 6.CURSO // 7.ENSEÑANZA // 8.CANCELAR")
                    dato = int(input("Digite El Dato Que Desea Modificar : "))
                    if dato!=1 and dato!=2 and dato!=3 and dato!=4 and dato!=5 and dato!=6 and dato!=7 and dato!=8:
                        print("\n--- Error De Opcion De Modificar Datos!! ---")
                        system("pause")
                        self.menu()
                    else:  
                        nuevo = input("Digite El Nuevo Valor Para Modificarlo : ") 
                        if dato==1:
                            if len(nuevo.strip())<9 or len(nuevo.strip())>12:
                                print("\n--- Debe Tener Entre 1 y 12 Caracteres!! ---")
                                system("pause")
                                self.menu()
                            else:
                                r = self.d.comprobarRut(nuevo)
                                if r is None:
                                    self.d.modificarDatos(rut, dato, nuevo.upper())
                                else:
                                    print("\n--- El Rut (",nuevo,") Ya Existe. Ingrese Uno Diferente!! ---")
                                    system("pause")
                                    self.menu()
                        
                        elif dato==2:
                            if len(nuevo.strip())<1 or len(nuevo.strip())>40:
                                print("\n--- Debe Tener Entre 1 y 40 Caracteres!! ---")
                                system("pause")
                                self.menu()
                            else:
                                self.d.modificarDatos(rut, dato, nuevo.upper())

                        elif dato==3:
                            if len(nuevo.strip())<1 or len(nuevo.strip())>40:
                                print("\n--- Debe Tener Entre 1 y 40 Caracteres!! ---")
                                system("pause")
                                self.menu()
                            else:
                                self.d.modificarDatos(rut, dato, nuevo.upper())

                        elif dato==4:
                            if len(nuevo.strip())<1 or len(nuevo.strip())>40:
                                print("\n--- Debe Tener Entre 1 y 40 Caracteres!! ---")
                                system("pause")
                                self.menu()
                            else:
                                self.d.modificarDatos(rut, dato, nuevo.upper())
                        
                        elif dato==5:
                            if int(nuevo)<1 or int(nuevo)>125:
                                print("\n--- Debe Estar Entre 1 y 125!! ---")
                                system("pause")
                                self.menu()
                            else:
                                self.d.modificarDatos(rut, dato, int(nuevo))

                        elif dato==6:
                            respuesta = requests.get("https://movilappml2021.000webhostapp.com/EVA4_POO/FORMA_A/datos_cursos.json")
                            dd = respuesta.json()
                            tabla = BeautifulTable()
                            for x in dd["cursos"]:
                                tabla.rows.append([x["idCur"],x["nomCur"]])
                            tabla.columns.header = ["ID CURSO","NOMBRE CURSO"]
                            print(tabla)
                            op = input("Digite El Nuevo Valor Para Modificarlo : ")
                            if op==1:
                                nuevo = "1 A"
                            elif op==2:
                                nuevo = "1 B"
                            elif op==3:
                                nuevo = "2 A"
                            elif op==4:
                                nuevo = "2 B"
                            elif op==5:
                                nuevo = "3 A"
                            elif op==6:
                                nuevo = "3 B"
                            elif op==7:
                                nuevo = "4 A"
                            else:
                                nuevo = "4 B"
                            self.d.modificarDatos(rut, dato, nuevo)
                        elif dato==7:
                            respuesta = requests.get(" https://movilappml2021.000webhostapp.com/EVA4_POO/FORMA_A/datos_ensenanzas.json")
                            dd = respuesta.json()
                            tabla = BeautifulTable()
                            for x in dd["ensenanzas"]:
                                tabla.rows.append([x["idEns"],x["nomEns"]])
                            tabla.columns.header = ["ID ENSEÑANZA","NOMBRE ENSEÑANZA"]
                            print(tabla)
                            op = input("Digite El Nuevo Valor Para Modificarlo : ")
                            if op==1:
                                nuevo = "BASICA"
                            else:
                                nuevo = "MEDIA"
                            self.d.modificarDatos(rut, dato, nuevo)

                        else:
                            self.menu()

                        system("cls")
                        print("-------------------------------")
                        print("--- MODIFICACIÓN EXITOSA!! ---")
                        print("-------------------------------")
                        system("pause")
                        self.menu()                
        except:
            print("\n--- Error Al Intentar Modificar Datos!! ---")
            system("pause")
            self.menu()
#--------------------------------------------------------------------------------

    def __eliminarAlumnos(self):
        try:
            system("cls")
            id = int(input("Digite El ID De El/La Alumno/Alumna a Eliminar : "))
            if id<1 or id>999:
                print("\n--- El ID Debe Estar Entre 1 y 999!! ---")
                system("pause")
                self.menu()
            else:
                a = self.d.buscarAlumnosId(id)
                if a is None:
                    print("\n--- ID Buscado (",id,") No Encontrado. Imposible Eliminar!! ---")
                    system("pause")
                    self.menu()
                else:
                    self.d.eliminarAlumnos(id)
                    print("-------------------------------------")
                    print("--- ALUMNO ELIMINADO CORRECTAMENTE ---")
                    print("--------------------------------------")
                    system("pause")
                    self.menu()
        except:
            print("\n--- Error Al Intentar Eliminar Alumno!! ---")
            system("pause")
            self.menu()

# ---------------------------------------------------------------------

    def __estadistica(self):
        system("cls")
        print("-------------------")
        print("--- ESTADISTICA ---")
        print("-------------------")
        r = self.d.cantidadAlumnos()
        x = self.d.sumaEdades()
        y = self.d.promedioEdades()
        print("CANTIDAD DE ALUMNOS REGISTRADOS : ", r[0])
        print("SUMA DE EDADES DE ALUMNOS       : ",x[0])
        print("PROMEDIO DE EDADES DE ALUMNOS   : ", y[0])
        print("------------------------------")
        system("pause")
# ---------------------------------------------------------------------

    def __salir(self):
        system("cls")
        print("\n-------------------")
        print("--- Ok. Adios!! ---")
        print("-------------------")
        system("pause")
