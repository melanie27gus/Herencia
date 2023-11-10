from cuenta import Cuenta


class CuentaAhorros(Cuenta):
    def __init__(self, numero, nombre_propietario, saldo, interes: float = None):
        super().__init__(numero, nombre_propietario, saldo)
        self._interes = interes

    @property
    def interes(self):
        return self._interes

    @interes.setter
    def interes(self, nuevo_interes):
        self._interes = nuevo_interes

    def credito(self, cantidad):
        self.saldo += cantidad

    def debito(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Fondos insuficientes")

    def mostrar_saldo(self):
        print(f"Saldo de la cuenta de ahorros {self.numero}: ${self.saldo}")

    def pagar_interes(self):
        interes_ganado = self.saldo * (self.interes / 100)
        self.saldo += interes_ganado


# Ejemplo
#cuenta_pr = CuentaAhorros(numero='373828', nombre_propietario='Camila', saldo=5346.00, interes=2.5)
#cuenta_pr.credito(275.00)
#cuenta_pr.debito(140.00)
#cuenta_pr.mostrar_saldo()
#cuenta_pr.pagar_interes()
#cuenta_pr_saldo()


#MELANIE GUSQUI PALLO