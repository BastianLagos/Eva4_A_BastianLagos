class Alumnos:
    __id = 0
    __rut = ""
    __nombre = ""
    __paterno = ""
    __materno = ""
    __edad = 0
    __curso = ""
    __ensenanza = ""
    __estado = 0

    def __init__(self):
        pass

    def getId(self):
        return self.__id
    
    def setId(self, id):
        self.__id = id

    def getRut(self):
        return self.__rut

    def setRut(self, rut):
        self.__rut = rut
    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def getPaterno(self):
        return self.__paterno

    def setPaterno(self, paterno):
        self.__paterno = paterno

    def getMaterno(self):
        return self.__materno

    def setMaterno(self, materno):
        self.__materno = materno

    def getEdad(self):
        return self.__edad

    def setEdad(self, edad):
        self.__edad = edad

    def getCurso(self):
        return self.__curso

    def setCurso(self, curso):
        self.__curso = curso

    def getEnsenanza(self):
        return self.__ensenanza

    def setEnsenanza(self, ensenanza):
        self.__ensenanza = ensenanza

    def getEstado(self):
        return self.__estado

    def setEstado(self, estado):
        self.__estado = estado
