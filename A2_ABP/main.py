from tarjeta import TarjetaCredito

def main():
    # Crear 3 tarjetas
    tarjeta1 = TarjetaCredito(limite_credito=1000, intereses=0.02)
    tarjeta2 = TarjetaCredito(limite_credito=1500, intereses=0.03, saldo_pagar=100)
    tarjeta3 = TarjetaCredito(limite_credito=500, intereses=0.025)

    # Para la primera tarjeta: 2 compras, 1 pago, cobrar intereses, mostrar info (encadenado)
    tarjeta1.compra(200).compra(300).pago(100).cobrar_interes().mostrar_info_tarjeta()

    # Para la segunda tarjeta: 3 compras, 2 pagos, cobrar intereses, mostrar info (encadenado)
    tarjeta2.compra(250).compra(400).compra(300).pago(150).pago(200).cobrar_interes().mostrar_info_tarjeta()

    # Para la tercera tarjeta: 5 compras excediendo límite, mostrar info (encadenado)
    tarjeta3.compra(150).compra(200).compra(100).compra(150).compra(200).mostrar_info_tarjeta()

    # BONUS: Mostrar información de todas las tarjetas
    TarjetaCredito.mostrar_todas_las_tarjetas()

if __name__ == "__main__":
    main()