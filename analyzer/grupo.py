class Grupo:

	def __init__(self, id1, mensajes1):

		self.id=id1
		self.mensajes= mensajes1

	def setId(self,id1):
		self.id=id1

	def getId(self):
		return self.id

	def setMensajes(self,mensajes1):
		self.mensajes=mensajes1

	def getMensajes(self):
		return self.mensajes