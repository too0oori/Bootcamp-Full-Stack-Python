class TarjetaCredito:
    todas_las_tarjetas = []
    def __init__(self, limite_credito, intereses, saldo_pagar=0):
         self.saldo_pagar = saldo_pagar
         self.limite_credito = limite_credito
         self.intereses = intereses
         self.todas_las_tarjetas.append(self)

    def compra(self, monto):
        if self.saldo_pagar + monto > self.limite_credito:
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito")
        else:
            self.saldo_pagar += monto
        return self

    def pago(self, monto):
       self.saldo_pagar -= monto
       if self.saldo_pagar < 0:
              self.saldo_pagar = 0
       return self

    def mostrar_info_tarjeta(self):
        print(f"Saldo a pagar: {self.saldo_pagar}")
        return self

    def cobrar_interes(self):
        self.saldo_pagar += self.saldo_pagar * self.intereses
        return self

    @classmethod
    def mostrar_todas_las_tarjetas(cls):
            print("\n=== INFORMACIÓN DE TODAS LAS TARJETAS ===")
            for i, tarjeta in enumerate(cls.todas_las_tarjetas, 1):
                print(f"Tarjeta {i}: Saldo a Pagar: ${tarjeta.saldo_pagar}, Límite: ${tarjeta.limite_credito}, Interés: {tarjeta.intereses*100}%")