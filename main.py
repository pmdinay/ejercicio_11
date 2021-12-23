""" Programa para ordenar numeros de menor a mayor"""
import bubble_sort as bs
while True:
    fin = False
    list = []
    while True:
        while True:
            elemento = input("Elemento de la lista: ")
            if elemento == "fin":
                fin = True
                break

            try:
                elemento = int(elemento)
                break
            except:
                print("El elemnto tiene que ser int")
        if fin:
            break
        if elemento == -9999:
            break
        list.append(elemento)
    if fin:
        break
    l_o = bs.BubbleSort(list)
    print("Lista ordenada: \n", l_o.sorted_list)
