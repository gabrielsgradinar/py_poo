def decorator(funcao):
    def wrapper(*arg, **kwargs):
        print('Ola Mundo')
        print(f'Arg: {arg}')
        print(f'Kwargs: {kwargs}')
        funcao(*arg)
    return wrapper


class MinhaClasse:

    @decorator
    def metodo(self, num):
        print(f'Estou na minha classe {num}')

    
cl = MinhaClasse()
cl.metodo(1)