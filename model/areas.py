from pydoc import describe


class Areas:
    def __init__(self,descri,estado):
        self.descri = descri
        self.estado = estado

    def getDescri(self):
        return self.descri
    def setDescri(self,descri):
        self.descri=descri
        
    def getEstado(self):
        return self.estado
    def setEstado(self,estado):
        self.estado = estado