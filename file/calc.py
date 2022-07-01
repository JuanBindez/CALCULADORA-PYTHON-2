

class Logica():
    '''Aqui fica a lógica da calculadora'''
    def __init__(self, x, y):
        self.x = x
        self.y = y
    

    def logica_adicao(self):
        return 'Resultado =' + str(self.x+self.y)

    def logica_subtracao(self):
        return 'Resultado =' + str(self.x-self.y)

    def logica_divisao(self):
        return 'Resultado =' + str(self.x/self.y)

    def logica_multiplicacao(self):
        return 'Resultado =' + str(self.x*self.y)