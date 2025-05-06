import multiprocessing

def quadrato(n):
    return n ** 2

if __name__ == "__main__":
    numeri = [1, 2, 3, 4, 5]
    with multiprocessing.Pool() as pool:
        # Esegue il quadrato su ogni numero con processi diversi
        risultati = pool.map(quadrato, numeri)
        for risultato in risultati:
            print(risultato)
