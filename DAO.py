from Alumnos import Alumnos
import json
from os import system
import pymysql

class DAO:

    def __init__(self):
        pass

# ---------------------------------------------------------------------

    def conectar(self):
        self.con = pymysql.connect(
            host = "localhost", 
            user = "root",
            password = "",
            db = "eva_4_a"
        )
        self.cursor = self.con.cursor()

# ---------------------------------------------------------------------

    def desconectar(self):
        self.con.close()

# ---------------------------------------------------------------------
    
    def comprobarRut(self, rut):
        try:
            self.conectar()
            sql = "select rut_alu from alumnos where rut_alu=%s and est_alu=1"
            self.cursor.execute(sql, rut)
            rs = self.cursor.fetchone()
            self.desconectar()
            return rs
        except:
            print("\n--- Error Al Comprobar Rut (DAO)!! ---")
            system("pause")

# ---------------------------------------------------------------------

    def agregarAlumnos(self, a):
        try:
            rut = a.getRut()
            nom = a.getNombre()
            pat = a.getPaterno()
            mat = a.getMaterno()
            eda = a.getEdad()
            cur = a.getCurso()
            ens = a.getEnsenanza()
            est = a.getEstado()
            self.conectar()
            sql = "insert into alumnos (rut_alu, det_alu, est_alu) values (%s, %s,%s)"
            dd = {"nom":nom, "pat":pat, "mat":mat, "eda":eda, "cur":cur, "ens":ens}
            cad = json.dumps(dd)
            val = (rut, cad, est)
            self.cursor.execute(sql, val)
            self.con.commit()
            self.desconectar()
        except:
            print("\n--- Error Al Agregar Alumnos (DAO)!! ---")
            system("pause")

# ---------------------------------------------------------------------

    def obtenerAlumnos(self):
        try:
            self.conectar()
            sql = "select rut_alu, det_alu from alumnos where est_alu=1"
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
            self.desconectar()
            return rs
        except:
            print("\n--- Error Al Obtener Alumnos(DAO)!! ---")
            system("pause")

#-----------------------------------------------------------------------------------

    def buscarAlumnos(self, rut):
        try:
            self.conectar()
            sql = "select rut_alu as RUT, json_unquote(json_extract(det_alu, '$.nom')) as NOMBRE, json_unquote(json_extract(det_alu, '$.pat')) as PATERNO, json_unquote(json_extract(det_alu, '$.mat')) as MATERNO, json_unquote(json_extract(det_alu, '$.eda')) as EDAD, json_unquote(json_extract(det_alu, '$.cur')) as CURSO, json_unquote(json_extract(det_alu, '$.ens')) as ENSEÑANZA from alumnos where rut_alu=%s and est_alu=1"
            self.cursor.execute(sql, rut)
            rs = self.cursor.fetchone()
            if rs is None:
                self.desconectar()
                return None
            else:
                a = Alumnos()
                a.setRut(rs[0])
                a.setNombre(rs[1])
                a.setPaterno(rs[2])
                a.setMaterno(rs[3])
                a.setEdad(rs[4])
                a.setCurso(rs[5])
                a.setEnsenanza(rs[6])
                self.desconectar()
                return a
        except:
            print("\n--- Error Al Buscar Alumno (DAO)!! ---")
            system("pause")

#-----------------------------------------------------------------------------------------------

    def modificarDatos(self, rut, dato, nuevo):
        try:
            self.conectar()
            val = (nuevo, rut)
            if dato==1:
                sql = "update alumnos set rut_alu=%s where rut_alu=%s"
            elif dato==2:
                sql = "update alumnos set det_alu=json_replace(det_alu, '$.nom', %s) where rut_alu=%s"
            elif dato==3:
                sql = "update alumnos set det_alu=json_replace(det_alu, '$.pat', %s) where rut_alu=%s"
            elif dato==4:
                sql = "update alumnos set det_alu=json_replace(det_alu, '$.mat', %s) where rut_alu=%s"
            elif dato==5:
                sql = "update alumnos set det_alu=json_replace(det_alu, '$.eda', %s) where rut_alu=%s"
            elif dato==6:
                sql = "update alumnos set det_alu=json_replace(det_alu, '$.cur', %s) where rut_alu=%s"
            elif dato==7:
                sql = "update alumnos set det_alu=json_replace(det_alu, '$.ens', %s) where rut_alu=%s"

            self.cursor.execute(sql, val)
            self.con.commit()
            self.desconectar()
        except:
            print("\n--- Error Al Modificar Datos (DAO)!! ---")
            system("pause")

#-----------------------------------------------------------------------------------

    def buscarAlumnosId(self, id):
        try:
            self.conectar()
            sql = "select*from alumnos where id_alu=%s and est_alu=1"
            self.cursor.execute(sql, id)
            rs = self.cursor.fetchone()
            if rs is None:
                self.desconectar()
                return None
            else:
                return rs
        except:
            print("\n--- Error Al Buscar Alumno (DAO)!! ---")
            system("pause")

#-----------------------------------------------------------------------------------------

    def eliminarAlumnos(self, id):
        try:
            self.conectar()
            sql = "update alumnos set est_alu=2 where id_alu=%s"
            self.cursor.execute(sql, id)
            self.con.commit()
            self.desconectar()
        except:
            print("\n--- Error Al Eliminar Alumno (DAO)!! ---")
            system("pause")

#-------------------------------------------------------------------------------------------------

    def cantidadAlumnos(self):
        try:
            self.conectar()
            sql = "select count(*) from alumnos where est_alu=1"
            self.cursor.execute(sql)
            rs = self.cursor.fetchone()
            self.desconectar()
            return rs
        except:
            print("--- ERROR AL CONTAR REGISTROS ---")
            system("pause")

#-------------------------------------------------------------------------------------------------

    def sumaEdades(self):
        try:
            self.conectar()
            sql = "select SUM(json_extract(det_alu, '$.eda')) from alumnos where est_alu=1"
            self.cursor.execute(sql)
            rs = self.cursor.fetchone()
            self.desconectar()
            return rs
        except:
            print("--- ERROR AL SUMAR EDADES ---")
            system("pause")

#-------------------------------------------------------------------------------------------------

    def promedioEdades(self):
        try:
            self.conectar()
            sql = "select AVG(json_extract(det_alu, '$.eda')) from alumnos where est_alu=1"
            self.cursor.execute(sql)
            rs = self.cursor.fetchone()
            self.desconectar()
            return rs
        except:
            print("--- ERROR AL PROMEDIAR EDADES ---")
            system("pause")