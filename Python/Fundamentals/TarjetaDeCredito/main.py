

from Tarjeta import TarjetaCredito


chase= TarjetaCredito()
wellsFargo= TarjetaCredito(500, 1000, 0.02)
bofa= TarjetaCredito(100, 2000, 0.03)

chase.compra(100).compra(200).pago(150).cobrar_interes().mostrar_info_tarjeta()
#100 + 200 -150 = 150 
#150 + 150 * 0.01 = 150 + 1.5 = 151.5
wellsFargo.compra(100).compra(100).compra(50).pago(150).pago(75).cobrar_interes().mostrar_info_tarjeta()
bofa.compra(200).compra(800).compra(300).compra(500).compra(300).mostrar_info_tarjeta()

print("-------------------------------------------------")
TarjetaCredito.mostrar_todas_tarjetas()