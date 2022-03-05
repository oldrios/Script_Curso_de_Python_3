class Car:
    marca = 'Ford'

#    def __init__(self):         # Dessa forma o atributo da instância terá
#        self.marca = 'Ferrari'  # um valor diferente do atributo da classe


carro1 = Car()
carro2 = Car()

# carro1.marca = 'Audi'   #  Ao "alterarmos" o atributo da classe através da instância
# print(carro1.__dict__)  #  o Python na verdade entenderá que estamos está criando um
# print(carro2.__dict__)  #  atributo novo para a instância e assim como mostra nesse
# print(Car.__dict__)     #  print usando o dunder dict, a instância carro1 agora tem
# print()                 #  um atributo que tem o mesmo nome que o atributo da classe

# Car.marca = 'VW'  # Alterando todos os dados do atributo da classe (Método correto.)

print(carro1.marca)
print(carro2.marca)
print(Car.marca)
