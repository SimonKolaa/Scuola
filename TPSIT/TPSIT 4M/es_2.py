def fibonacci(n):
   
    a, b = 0, 1
    
    fib_sequenza = []
    for _ in range(n):
        fib_sequenza.append(a)
        a, b = b, a + b
    
    return fib_sequenza

n_termini = 15
risultato = fibonacci(n_termini)
print(f"Fibonacci sequenza con {n_termini} termini:")
print(risultato)
