# -*- coding: utf-8 -*-
import unittest
from Conversacion import Analyzer
from grupo import Grupo

class Test(unittest.TestCase):

    def test_conversacion(self):
        analyzer = Analyzer()
        mensajesPrueba=['Prueba contador','lksadhflkdsaf','kjsagfhjadsgfkdsjhbczxvds']
        self.assertEqual(analyzer.cuentaMensaje(mensajesPrueba),3,"Deberían ser 3 mensajes")


    def test_longitud(self):
        analyzer = Analyzer()
        mensajesPrueba=['Prueba contador','lksadhflkdsaf','kjsagfhjadsgfkdsjhbczxvds']
        mensajePrueba= "kjsagfhjadsgfkdsjhbczxvds"
        tam = len(mensajePrueba)
        self.assertEqual(analyzer.mensajeMasLargo(mensajesPrueba),
                                        (mensajePrueba,tam),"Deberia ser " + mensajePrueba + " " + str(tam))

    def test_integracion(self):
        analyzer = Analyzer()
        mensajes = ['hola','que tal?','bine', 'y tu?']
        grupo1=Grupo(1,mensajes)
        mensajes = ['mañana','es la excursion','vienes?']
        grupo2=Grupo(2,mensajes)

        grupos=[]
        grupos.append(grupo1)
        grupos.append(grupo2)

        analyzer.setGrupos(grupos)

        self.assertEqual(analyzer.grupoMasActivo(), grupo1, "el grupo mas activo es el 1")

    def test_palabraMasRepetida(self):
        analyzer = Analyzer()
        mensajes = ['hola','adios','hola', 'hola','si']
        self.assertEqual(analyzer.palabraMasRepetida(mensajes), 'hola', "La palabra más repetida es hola")



if __name__ == '__main__':
    unittest.main()
