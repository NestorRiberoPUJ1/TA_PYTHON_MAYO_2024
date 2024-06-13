class TarjetaCredito:

    tarjetas = []
    # Incluye en este método valores por default

    def __init__(self, saldo_pagar=0, limite_credito=3000, intereses=0.01):

        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses

        TarjetaCredito.tarjetas.append(self)

    def compra(self, monto):
        if (self.saldo_pagar + monto > self.limite_credito):
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito")
            return self
        self.saldo_pagar += monto
        return self

    def pago(self, monto):
        self.saldo_pagar -= monto
        return self

    def mostrar_info_tarjeta(self):
        print(f"Saldo a pagar: ${self.saldo_pagar}")
        return self

    def cobrar_interes(self):
        self.saldo_pagar += self.saldo_pagar * self.intereses
        # 1000 += 1000 * 0.01 = 1000 + 10 = 1010
        return self

    @classmethod
    def mostrar_todas_tarjetas(cls):
        for tarjeta in cls.tarjetas:
            tarjeta.mostrar_info_tarjeta()