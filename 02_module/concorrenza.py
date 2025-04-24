import concurrent.futures

def quadrato(n):
    return n ** 2

if __name__ == "__main__":
    numeri = [1, 2, 3, 4, 5]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Esegue il quadrato su ogni numero utilizzando thread diversi
        risultati = executor.map(quadrato, numeri)
        for risultato in risultati:
            print(risultato)