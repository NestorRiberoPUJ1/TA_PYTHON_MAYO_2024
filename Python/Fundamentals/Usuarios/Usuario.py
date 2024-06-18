




from TarjetaDeCredito.Tarjeta import TarjetaCredito


class Usuario:
    def __init__(self, nombre, apellido, email, tarjeta=TarjetaCredito()):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.tarjeta = tarjeta

    def hacer_compra(self,monto):
        self.tarjeta.compra(monto)
        return self

    def pagar_tarjeta(self,monto):
        self.tarjeta.pago(monto)
        return self

    def mostrar_saldo_usuario(self):
        self.tarjeta.mostrar_info_tarjeta() 
        return self
