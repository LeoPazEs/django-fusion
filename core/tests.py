from django.test import TestCase

def add(num): 
    return num + 1 

class SimpleTestCase(TestCase): 
    
    # roda toda vez
    def setUp(self): 
        print('Iniciando o TestCase') 

    # Testa a unidade de código 
    def test_add_num(self):
        valor = add_num(41) 
        self.assertTrue(valor == 42)

