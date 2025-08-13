class Persona:

   def __init__(self, nombre, apellido, tamagotchi):
       self.nombre = nombre
       self.apellido = apellido
       self.tamagotchi = tamagotchi

   def jugar_con_tamagotchi(self):
       print(f"{self.nombre} está jugando con {self.tamagotchi.nombre}.\n")
       self.tamagotchi.jugar()
   
   def darle_comida(self):
       print(f"{self.nombre} le está dando de comer a {self.tamagotchi.nombre}.\n")
       self.tamagotchi.comer()
   
   def curarlo(self):
       print(f"{self.nombre} está curando a {self.tamagotchi.nombre}.\n")
       self.tamagotchi.curar()