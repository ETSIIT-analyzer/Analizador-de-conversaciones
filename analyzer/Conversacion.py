class Analyzer:
    def cuentaMensaje(self,mensajes):
        return len(mensajes)
    def mensajeMasLargo(self,mensajes):
        m = []
        for mensaje in mensajes:
            if(len(mensaje)>len(m)):
                    m = mensaje
        return m, len(m)
