'''
add - Adiciona, update - Atualiza, clear - limpa, discard - descarta
union - (une)
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas no set da esquerda)
symmertric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)
more about set (Venn Diagram) https://brasilescola.uol.com.br/matematica/diagrama-de-venn.htm
'''
'''
s1 = {1, 2, 3, 4, 5, 6, 7, 8}

print(s1, type(s1))
'''

'''
Sets tem algumas funcionalidades muito interessante por exemplo:
- Ele ordena os dados na ordem crescente;
- Não aceita dados duplicados, então caso tenhamos uma lista ou tupla com valores duplicado;
- Se tentarmos inserir no set, algum valor duplicado, ele eliminará a cópia, mesmos que seja por comandos
de inserção, junção ou união;
'''

s1 = {1, 2, 2, 3, 3, 4, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 9, 8, 7}

# Usando função .add para adicionar valores repetidos

s1.add(1)  # Valor duplicado (Eliminará a cópia anterior e não se repetirá no set)
s1.add(2)  # Valor duplicado '' ''
s1.add(9)  # Valor duplicado '' ''
s1.add(15)  # Valor não duplicado, será adicionado ao set

# Atualizando dados de um set com a função .update() / mesmo principio de ordem e não duplicados

s1.update('opa')  # Strings são inseridas como objetos iteráveis no set
s1.update('opa')  # Inserindo item duplicado, seguirá o principio de não ter duplicados em sets
s1.update((3, 4, 800, 26, 7), [1, 8, 10, 20])  # Listas e tuplas também são iteráveis e o set exclui duplicados.
print(f's1 = {s1}')

'''
• União
A união entre dois conjuntos é formada pela junção dos elementos contidos em cada conjunto, em outras palavras: 
considera-se todos os elementos dos dois conjuntos. Veja:

Considere os conjuntos A = {1, 2, 3, 4} e B = {3, 4, 5, 6, 7}. A união entre eles é dada por:

A U B = {1, 2, 3, 4, 5, 6, 7}
'''

# Unindo dois sets para (union) -> |

s2 = {7, 6, 4, 3, 10, 12, 19}  # Há valores que também estão no set 1 (s1)
print(f's2 = {s2} \n')

s3 = s1 | s2  # Será apagado os valores -> {7, 6, 4, 3} pois eles se repetem nos dois sets

print(f'\t(União s1 + s2) s3 = {s3}')

'''
• Intersecção
A intersecção é um novo conjunto numérico formado por elementos que pertencem, de maneira simultânea, 
a outros conjuntos. De modo geral, a intersecção entre conjuntos no diagrama de Venn é 
dada pela parte comum aos gráficos envolvidos. Veja:

Considerando novamente os conjuntos A = {1, 2, 3, 4} e B = {3, 4, 5, 6, 7}, 
temos que os elementos que pertencem ao conjunto A e ao conjunto B, simultaneamente, são:

A ∩ B = {3, 4}
'''

# Fazendo interseção (intersection) &

s4 = s1 & s2  # Somente o que se repete nos dois set será intersectado

print(f'\t(Interseção s1 - x + x + s2 - x) s4 = {s4}')

'''
A diferença simétrica é uma operação que fazemos com conjuntos. Ela consiste em unir os dois conjuntos
e remover a parte em comum entre eles.
Exemplo de Diferença Simétrica:

Considerando
A={2,4,6,8,10,12,14} e B={1,2,3,4,5,6,7,8,9,10}.
A diferença simétrica então é:

A△B = (A∪B)−(A∩B)
A△B = {1,2,3,4,5,6,7,8,9,10,12,14} − {2,4,6,8,10}
A△B = {1,3,5,7,9,12,14}

Dica: Ele une e retira a inserção
'''

# Fazendo a diferença simétrica

s5 = s1 ^ s2

print(f'\t(Difereça simétrica união - interseção) s5 = {s5}\n')

'''
Exemplo de utilidade de um conjunto em python: Quando quero aplicar qualquer funcionalidade da 
teoria dos conjuntos em listas, tuplas ou dicionarios, exemplo:
'''

# Transformando uma lista e organizando o conjunto

l1 = [1, 5, 4, 3, 2, 5, 4, 6, 7, 100, 29, 100, 4, 3, 29, 5]
print(f'Lista l1: {l1}')

l1 = set(l1)
print(f'Transformando l1 em conjunto: {l1}')

l1 = list (l1)  # Transformando set em lista novamente


