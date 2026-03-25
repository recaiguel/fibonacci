try:
    # n definiert die häufigkeit der Folgen dieser Fibonacci-Reihe
    n = int(input("Gib eine Zahl ein: "))

    # 0 und 1 ist der Startpunkt. Ohne diese beiden Werte 
    # funktioniert die Fibonacci Reihe nicht
    a = 0
    b = 1

    for f in range(n):

        # gibt die aktuelle Folge in der Fib.-Reihe wieder
        print(a)    

        # berechnet f als eine Folge in der Fibonacci-Reihe,
        # der sich aus a + b ergibt
        f = a + b
        
        # Überschreibt die Variablen so dass Sie auch die
        # letzten beiden Werte in der Fib.-Reihe darstellen
        a, b = b, f
    else:
        print("Die Fibonacci Folge beginnt immer mit '0, 1,'.")

except ValueError:
    print("bitte gib eine gültige Zahl ein.")
 
 
 
 
""" 
class FibonacciPython:

    @staticmethod
    def fibonacci(number: int) -> int:
    # implement me
    #folgen = 20

        a = 0
        b = 1
   
        for i in range(number - 2):
           
            a, b = b, a+b

            return b

    fibonacci(8) """

""" class FibonacciPython:

    @staticmethod
    def fibonacci(number: int) -> int:
        # implement me
        folgen = 20

        x=[0,1]
    
        for i in range(folgen):
            
            x.append(x[i]+x[i+1])
        print(x[number-1])

    fibonacci(6) """

""" 
class FibonacciPython:

    @staticmethod
    def fibonacci(number: int) -> int:
        # implement me
                           
        a = 0
        b = 1
   
        for i in range(number - 2):
           
            a, b = b, a+b

        return b
        
    print(fibonacci(9))    """ 