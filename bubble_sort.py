"""Creación clase bubble sort"""

class BubbleSort:
    def __init__(self, lista):
        n = len(lista)
        for i in range(n - 1): #El rango se emplea para definir donde empieza y acaba esa variable
                              #la i controla las veces que tengo que hacer el bucle y hasta que posición llego comparando.
            for j in range(n - 1 - i): #n - 1 - i se utiliza para que no vuelva a hacer operaciones innecesarias
                                    #en este caso - i le dice que no vuelva a la posición que ha llegado en el anterior bucle
                                    # podria ser prescindible
                if lista[j] > lista[j + 1]: #Compara un numero en la posición j con el siguiente.
                    aux = lista[j + 1] #Guarda la posición que borra en una variable.
                    lista[j + 1] = lista[j] #Intercambia las posiciones.
                    lista[j] = aux #llama a la posición vacía como la variable que ha borrado
        self.sorted_list = lista #Almacenar lista en sorted_list, que es una variable del objeto.

