



from Usuarios.Usuario import Usuario


Nestor = Usuario("Nestor","Ribero","nribero@codingdojo.la")

Nestor.mostrar_saldo_usuario()
Nestor.hacer_compra(100).hacer_compra(200).hacer_compra(300)
Nestor.mostrar_saldo_usuario()
Nestor.hacer_compra(2500)
Nestor.pagar_tarjeta(500).mostrar_saldo_usuario()