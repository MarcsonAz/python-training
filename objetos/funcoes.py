from random import randint

def soma(x,y,z=2):
    print(x+y+z)
    return x+y+z

def funcao_dinamica(*args,**kwargs):
    print(args)
    print(kwargs)

def gerar_numero():
    x = randint(0,9)
    y = randint(0,2)
    try:
        print(x/y)
    except ZeroDivisionError:
        print("Não pode dividir por Zero")
    except:
        print("Ocorreu um erro!")

