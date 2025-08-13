class Tamagotchi:

    def __init__(self, nombre, color, salud=50, felicidad=60, energia=30):
       self.nombre = nombre
       self.color = color
       self.salud = salud
       self.felicidad = felicidad
       self.energia = energia

    def jugar(self):
       print(f"{self.nombre} está jugando :D.\n")
       self.felicidad += 10
       self.salud -= 5
       print(f"Felicidad: {self.felicidad}, Salud: {self.salud}\n")
       print("Tu Tamagotchi se siente cada vez más feliz!!\n")

    def comer(self):
       print(f"{self.nombre} está comiendo :3.\n")
       self.felicidad += 5
       self.salud += 10
       print(f"Felicidad: {self.felicidad}, Salud: {self.salud}\n")
       print("Tu tamagotchi adora comer!")

    def curar(self):
       print(f"{self.nombre} está siendo curado.\n")
       self.salud += 20
       self.felicidad -= 5
       print(f"Felicidad: {self.felicidad}, Salud: {self.salud}\n")
       print("Tu Tamagotchi se siente mucho mejor!\n")
