# -*- coding: utf-8 -*-
from Conversacion import Analyzer
import unittest

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
if __name__ == '__main__':
    unittest.main()
