import random

def generar_contrasena():
    mayusculas = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    minusculas = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o","p", "q", "r", "s", "t", "u","v", "w", "x", "y", "z" ]
    numeros = ["1","2","3","4","5","6","7","8","9","0"]
    simbolos = ["!", "#", "$", "&", "/", "*", "(", ")", "?", "¿"]

    caracteres = mayusculas + minusculas + numeros + simbolos

    contrasena = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)
    
    contrasena = "".join(contrasena)
    return contrasena

        
def run():
    contrasena =  generar_contrasena()
    print("Tu nueva contraseña es: " + contrasena)

if __name__ == "__main__":
    run()