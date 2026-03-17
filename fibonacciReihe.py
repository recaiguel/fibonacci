# n definiert die häufigkeit der Folgen dieser Fibonacci-Reihe
n = 15

# 0 und 1 ist der Startpunkt. Ohne diese beiden Werte 
# funktioniert die Fibonacci Reihe nicht
a = 0
b = 1

for f in range(n):
    
    # berechnet f als eine Folge in der Fibonacci-Reihe,
    # der sich aus a + b ergibt
    f = a + b
    
    # Überschreibt die Variablen so dass Sie auch die
    # letzten beiden Werte in der Fib.-Reihe darstellen
    a = b
    b = f
    
    # gibt die aktuelle Folge in der Fib.-Reihe wieder
    print(f)
    