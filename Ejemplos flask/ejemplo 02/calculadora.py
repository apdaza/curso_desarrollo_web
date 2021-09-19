class Calculadora:
    def __init__(self, valor1 = 0, valor2 = 0):
        self.valor1 = valor1
        self.valor2 = valor2
        self.resultado = 0
        self.operador = ""

    def sumar(self):
        self.operador = " + "
        self.resultado = self.valor1 + self.valor2

    def restar(self):
        self.operador = " - "
        self.resultado = self.valor1 - self.valor2

    def multiplicar(self):
        self.operador = " * "
        self.resultado = self.valor1 * self.valor2
    
    def dividir(self):
        self.operador = " / "
        self.resultado = self.valor1 // self.valor2

    def get_operacion(self):
        return str(self.valor1) + self.operador + str(self.valor2) + " = " + str(self.resultado)