entrada = input()
x, y = entrada.split(" ")

x = float(x)
y = float(y)

if( x > 0 and y > 0):
    print("Q1")
elif( x < 0 and y > 0 ):
    print("Q2")

elif( x < 0 and y < 0 ):
    print("Q3")

elif( x > 0 and y < 0 ):
    print("Q4")

elif( x != 0 and y == 0 ):
    print("Eixo X")

elif( x == 0 and y != 0 ):
    print("Eixo Y")
else:
    print("Origem")
