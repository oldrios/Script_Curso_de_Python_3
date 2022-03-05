from classes import Carrinho, Produto

p1 = Produto('Tenis', 150)
p2 = Produto('Camiseta', 30)
p3 = Produto('Caneca', 15)
p4 = Produto('Boné', 70)
carrinho = Carrinho()


carrinho.inserir_produtos(p1)
carrinho.inserir_produtos(p2)
carrinho.inserir_produtos(p3)
carrinho.inserir_produtos(p4)
carrinho.lista_produtos()
carrinho.soma_total()






