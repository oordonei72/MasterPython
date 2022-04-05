class Personal:
    def __init__(self,nombre,apellido,fecha_nac,sueldo):
        try:
            self.nombre = nombre
            self.apellido = apellido
            self.fecha_nac = fecha_nac
            self.sueldo = sueldo
        except:
            print('error creando el objeto')
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre = nombre

    def getApellido(self):
        return self.apellido
    def setApellido(self,apellido):
        self.apellido = apellido

    def getFechaNac(self):
        return self.getFechaNac
    def setFechaNac(self,fecha_nac):
        self.fecha_nac = fecha_nac

    def getEdad(self):
        return self.sueldo
    def setEdad(self,sueldo):
        self.edad = sueldo
        
