contador = 1

def incrementar(n):
    global contador
    contador += n
    print(f"contador:_{contador}")