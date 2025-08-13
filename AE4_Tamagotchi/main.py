from persona import Persona
from tamagotchi import Tamagotchi

el_tamagotchi = Tamagotchi("Haru", "Azul")
persona = Persona("Tori", "L", el_tamagotchi)

print("¡Bienvenido al mundo de Tamagotchi!\n")

print("Estado inicial de tu Tamagotchi:\n")
print(f"Nombre: {persona.tamagotchi.nombre}")
print(f"Salud: {persona.tamagotchi.salud}")
print(f"Felicidad: {persona.tamagotchi.felicidad}")
print(f"Energia: {persona.tamagotchi.energia}\n")

while True:
    print("¿Qué quieres hacer con tu tamagotchi?")
    print("1. Darle comida")
    print("2. Jugar con él")
    print("3. Curarlo")
    print("4. Salir \n")

    opcion = input("Elige una opción (1, 2, 3 o 4):")

    if opcion == "1":
        persona.darle_comida()
    elif opcion == "2":
        persona.jugar_con_tamagotchi()
    elif opcion == "3":
        persona.curarlo()
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida.")