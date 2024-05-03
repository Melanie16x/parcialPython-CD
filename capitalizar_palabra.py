# Pido al usuario que ingrese una palabra o frase para capitalizar
palabra_frase = str(input('Ingrese una palabra o frase para capitalizar: '))

# Defino una funcion llamada "capitalizar_palabra" para que realice dicha tarea 
# (capitalizar el string que ingrese el usuario)
def capitalizar_palabra(palabra_frase):

    # Utilizo el metodo "capitalize" para capitalizar el string que ingrese el usuario y
    # lo muestro por la terminal
    print(palabra_frase.capitalize())

    # Retorno la palabra capitalizada
    return palabra_frase

# LLamo a la funcion para que realice el proceso de capitalizar
# Le paso a la funcion un parametro, el cual es la palabra o frase que ingrese el usuario
capitalizar_palabra(palabra_frase)