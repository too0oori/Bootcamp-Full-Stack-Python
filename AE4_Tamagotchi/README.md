
Ejercicio individual

Objetivos

    Continuar practicando la OOP y asociación de clases

Clase Persona: Atributos

    Nombre
    Apellido
    Tamagotchi

Métodos

    jugar_con_tamagotchi()
    darle_comida()
    curarlo()

class Persona:

   #__init__(nombre, apellido, tamagotchi)

   #Métodos:

   #jugar_con_tamagotchi(): juega e invoca el método de tamagotchi jugar()

   #darle_comida(): le da de comer su tamagotchi invocando al método de tamagotchi comer()

   #curarlo(): sana las heridas de su tamagotchi invocando al método de tamagotchi curar()

Clase Tamagotchi: Atributos

    Nombre
    Color
    Salud
    Felicidad
    Energia

Métodos

    jugar()
    comer()
    curar()

class Tamagotchi:

   #__init__(nombre, color). Puedes colocar valores default para salud, felicidad y energía

   #Métodos:

   #jugar(): incrementa la felicidad el 10, disminuye la salud en 5

   #comer(): incrementa la felicidad en 5, aumenta la salud en 10

   #curar(): incrementa la saludo en 20, disminuye la felicidad en 5

    Crea la clase Persona con los atributos mencionados
    Crea la clase Tamagotchi con los atributos mencionados
    Desarrolla los métodos de jugar_con_tamagotchi(), darle_comida() y curarlo() para la clase Persona
    Desarrolla los métodos de jugar(), comer() y curar() para la clase Tamagotchi
    Crea una instancia de Persona y asígnale una instancia de Tamagotchi al atributo tamagotchi
    Haz que la persona le de comer, cure y juegue con su tamagotchi
    BONUS NINJA: Modulariza tus clases, colocándolas en distintos archivos
    BONUS SENSEI: Usa la herencia para crear subclases de Tamagotchi con sus personajes. Hecha un vistazo aquí. 

