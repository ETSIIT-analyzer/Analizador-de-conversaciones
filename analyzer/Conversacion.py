from grupo import Grupo


class Analyzer:
        

	def __init__(self,grupos1=[]):

		self.grupos = grupos1


	def setGrupos(self,grupos1):
		self.grupos=grupos1

	def getGrupos(self):
		return self.grupos

        def cuentaMensaje(self,mensajes):
                return len(mensajes)
        
        def mensajeMasLargo(self,mensajes):
                m = []
                for mensaje in mensajes:
                        if(len(mensaje)>len(m)):
                                m = mensaje
                return m, len(m)
                        
	def grupoMasActivo(self):
                longitud = 0
     	        for grupo in self.grupos:
     		        n=self.cuentaMensaje(grupo.getMensajes())
     		        if n > longitud:
     			        longitud=n
     			        grupoDef = grupo
     	        return grupoDef




