#crear una lista vacia 
letras_verificadas = []
cantidad_letras = 5 
palabra_ingresada = "oxbar"
#definir la cantidad de letras de la palabra 
def verificador_palabra(palara_ingresada, palabra_secreta):
    for i in range(cantidad_letras):
        las_palabras_son_iguales = palabra_ingresada[i] == palabra_secreta[i] #true o falsa
        la_letra_existe_en_la_palabra = palabra_ingresada[i] in palabra_secreta
