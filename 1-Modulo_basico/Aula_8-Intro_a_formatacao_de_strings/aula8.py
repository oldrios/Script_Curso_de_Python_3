'''
Introdução a formatação de strings
'''

nome = 'Oldaque'
idade = 24
altura = 1.70
e_maior = idade >= 18
peso = 62
imc = peso / altura ** 2

print(nome, 'tem', idade,'anos de idade e seu IMC é:',imc)

'''
Podemos reescrever a função acima utilizando fStrings que isentam a necessidade de escrever o código
com a formatação utilizando aspas e virgula e assim trazendo as variáveis para dentro do contexto da string
utilizando a letra 'f' antes das aspas que iniciam a string e colocando as variáveis dentro de chaves {variavel}
'''
# Forma 1 de escrever com fstring
print(f'{nome} tem {idade} anos de idade e seu IMC é: {imc:.2f}')

# Forma 2 de escrever com fstring + .format
print('{} tem {} anos de idade e seu IMC é: {:.2f}'.format(nome, idade, imc))

# Forma 3 de escrever com fstring + .format
print('{0} tem {1} anos e seu IMC é: {2:.2f}'.format(nome, idade, imc))

'''
Estrutura da fstring utilizando '.format()'
print('{0} tem {1} anos e seu IMC é: {2:.2f}'.format(nome = 0, idade = 1, imc = 2)) e assim por diante
quanto mais variáveis eu adicionar ela será adicionada na sequência que é alimentada de 1 e 1
lembrando que o começo é sempre em 0

Pode-se usar a fstring com as variáveis em qualquer ordem sendo que depois da função '.format()' nós indicamos
qual serão as variáveis por ordem seguindo a estrutura indicada acima (começando em 0)
'''

# Exemplo de aplicação
print('{0} {1} tem {1} anos {2:.2f} e {1} seu IMC é: {2:.2f}'.format(nome, idade, imc))

'''
Também é possível dar 'apelidos' as variáveis e dessa forma não precisamos utilizar a ordem numerica.
Esse apelido deve ser atribuido na função '.format()'
'''

# Exemplo de aplicação
print('{n} tem {i} anos e seu IMC é: {im:.2f}'.format(n=nome, i=idade, im=imc))

