import random


# Funcion auxiliar que se usa para "recortar" un conjunto de número
def TRIM(L, epsilon):
    m = len(L)  # Incializamos m como la longitud de l lista L
    L0 = [L[0]]  # Inicializamod L0 con el primer elemento de L (En el libro es L')
    last = L[0]  # Inicializa last con el primer elemento de L

    for i in range(1, m):
        yi = L[i]
        # Si el elemento actual es mayor que el último hacemos: last * (1 + epsilon),
        if yi > (last * (1 + epsilon)):
            L0.append(yi)
            last = yi
           
            print(f" L = {L0} ")
       
    return L0

# Funcion auxiliar que mezcla y ordena dos listas (se omite en el libro)
def MERGE_LISTS(L, L0):
    # Combina y ordena las listas L y L0
    merged = sorted(L + L0)
    return merged

# Función que modela el algortimo APRROX-SUBET-SUM del libro
def APPROX_SUBSET_SUM(S, t, epsilon):
    n = len(S) # Inicializamos n = |S|
    L0 = [0]  # Inicializamos L0 con el elemento 0
    print(f"Incializando L0 = {L0}")

    for i in range(1, n+1):
        Li = MERGE_LISTS(L0, [x + S[i - 1] for x in L0])

        Li = TRIM(Li, epsilon / (2 * n))

        # Filtramos los elementos mayores que t en Li
        Li = [x for x in Li if x <= t]

        if not Li:
            # Si Li está vacía, salimos
            break

        L0 = Li  # Actualiza L0 con Li
        print(f"L{i + 1} = {L0} ")

    return max(L0)  # Devuelve el valor máximo de L0


    # Imprimir el resultado final
    print(f"Resultado final: {max(L0)}")
    return max(L0)


# Función que genera 50 números pseudoaleatorios diferentes
def genera_random_numbers():
    return random.sample(range(1, 1000), 50)


# Función para ejecutar el ejemplar 1
def run_example1():
    print(f"------------------------------------------------------")
    print(f"Ejemplar 1 (Proporcionado en el libro):")
    
    S1 = [104, 102, 201, 101]
    t1 = 308
    epsilon1 = 0.40
    
    print(f"S: {S1}")
    print(f"t: {t1}")
    print(f"Epsilon: {epsilon1}")
    print(f"------------------------------------------------------")
    print(f"------------------------------------------------------")

    result1 = APPROX_SUBSET_SUM(S1, t1, epsilon1)
    print(f"El resultado es: {result1}")

# Función para ejecutar el ejemplar 2, en el que haremos 50 números pseudoaleatorios
def run_example2():
    print(f"------------------------------------------------------")
    print(f"Ejemplar 2 (Números Pseudoaleatorios):")
    S2 = genera_random_numbers()
    t2 = 666
    epsilon2 = 0.331
    print(f"S: {S2}")
    print(f"t: {t2}")
    print(f"Epsilon: {epsilon2}")
    print(f"------------------------------------------------------")
    print(f"------------------------------------------------------")
    print(f"Proceso...")
    result2 = APPROX_SUBSET_SUM(S2, t2, epsilon2)
    print(f"El resultado es: {result2}")
    
 
# Menu sencillo que saldrá al ejecutar   
while True:
    print("\nSelecciona una opciAón:")
    print("1. Ejemplar 1 - (Libro)")
    print("2. Ejemplar 2")
    print("3. Salir")

    choice = input("Ingrese el número de la opción: ")

    if choice == "1":
        run_example1()
    elif choice == "2":
        run_example2()
    elif choice == "3":
        print("La ejecución ha finalizado")
        break
    else:
        print("Opción no válida!!!")
