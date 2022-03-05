'''
Faça uma lista de tarefas com as seguintes opções:
    adicionar tarefa
    listar tarefas
    opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    opção de refazer (a cada vez que chamarmos, refaz a última ação)
'''

from time import sleep

tarefas = []
memory = []


def header(lista):
    print('*=' * 30, '\n')
    print('                 AGENDA DE TAREFAS 1.0.0')
    print('*=' * 30, '\n')
    print('\tTAREFAS A FAZER:\n')

    for i, item in enumerate(lista):
        print(f'\t{i+1} - {item}')
    print()


def opcoes():
    print('Seja bem vindo!\n'
          'O que deseja fazer?\n'
          '1 - Inserir tarefa\n'
          '2 - Desfazer última tarefa\n'
          '3 - Refazer última tarefa\n')

    try:
        opcao = int(input('Digite o número da operação desejada: '))
        return opcao
    except ValueError:
        return None


def insert_task(lista):
    insert = input('Insira a nova tarefa: ')
    lista.append(insert)


def undo(lista, memoria):
    print(f'Tarefa: "{tarefas[-1]}" foi removida da lista!')
    memoria.append(lista[-1])
    lista.pop()
    sleep(0.5)


def redo(lista, memoria):
    print(f'Tarefa: "{memoria[-1]}" foi inserida na lista!')
    lista.append(memoria[-1])
    memoria.pop()
    sleep(0.5)


if __name__ == '__main__':
    while True:
        header(tarefas)
        opcao = opcoes()
        try:
            if opcao == None:
                print('Não é uma opção valida, tente novamente!')
                sleep(3)
            elif opcao == 1:
                insert_task(tarefas)
            elif opcao == 2:
                undo(tarefas, memory)
            elif opcao == 3:
                redo(tarefas, memory)
        except IndexError:
            print('Não há valor para desfazer/refazer')
            sleep(1)

