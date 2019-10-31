# -*- coding: utf-8 -*-
import sys
import os

# Obtain project root path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# For finding modules to test
sys.path.insert(0, project_root)

import src.Conversacion.analyzer
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
