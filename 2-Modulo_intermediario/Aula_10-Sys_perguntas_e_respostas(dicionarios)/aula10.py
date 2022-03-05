'''
Nesta seção iremos montar um programa de perguntas e respostas
usando dicionários
'''

from time import sleep

perguntas = {
    'Pergunta 1': {
        'Pergunta': 'Em que ano e onde aconteceu o maior acidente aéreo da história do Brasil?',
        'Respostas': {
            'A': 'Ano 2007, em São Paulo',
            'B': 'Ano 2006, no Mato Grosso',
            'C': 'Ano 1982, no Ceará',
            'D': 'Ano 1996, em São Paulo',
            'E': 'Ano 1952, na Floresta Amazônica'
        },
        'resposta_certa' : 'a'
    },
    'Pergunta 2': {
        'Pergunta': 'Qual o motivo da condenação de Luís Inácio Lula da Silva em 2018?',
        'Respostas': {
            'A': 'Recebimento de apartamento de luxo no Guarujá (SP) como propina na Operação Lava Jato',
            'B': 'Corrupção e lavagem de dinheiro na Operação Lava Jato',
            'C': 'Tráfico de influência internacional na Operação Janus',
            'D': 'Obstrução da justiça na Operação Lava Jato',
            'E': 'Formação de quadrilha na Operação Lava Jato'
        },
        'resposta_certa' : 'a'
    },
    'Pergunta 3': {
        'Pergunta': 'Quais os quatros países que têm a maior população carcerária do mundo?',
        'Respostas': {
            'A': 'Brasil, Estados Unidos, México e Índia',
            'B': 'China, Estados Unidos, Índia e Indonésiao',
            'C': 'Rússia, Japão, Canadá e China',
            'D': 'Estados Unidos, China, Rússia e Brasil',
            'E': 'Brasil, Estados Unidos, China e Vaticano'
        },
        'resposta_certa' : 'd'
    },
    'Pergunta 4': {
        'Pergunta': 'Qual foi a revolução que alavancou a independência do Brasil e em 2017 completou o segundo centenário?',
        'Respostas': {
            'A': 'Revolução Farroupilha',
            'B': 'Revolução Federalista',
            'C': 'Revolução Praieira',
            'D': 'Revolução Pernambucana',
            'E': 'Revolução Acreana'
        },
        'resposta_certa' : 'd'
    },
    'Pergunta 5': {
        'Pergunta': 'O que é Brexit?',
        'Respostas': {
            'A': 'Saída do Reino Unido da Zona Euro',
            'B': 'Saída do Reino Unido da União Europeia',
            'C': 'Saída da Inglaterra do Reino Unido',
            'D': 'Fim da monarquia no Reino Unido',
            'E': 'Mudança do sistema de governo no Reino Unido'
        },
        'resposta_certa': 'b'
    },
}

resposta_c = 0

for pergunta_k, pergunta_v in perguntas.items():
    print(f'{pergunta_k} \n')
    print(f"{pergunta_v['Pergunta']} \n")

    for alternativa_k, resposta_v in pergunta_v['Respostas'].items():
        print(f'{alternativa_k}) {resposta_v}', flush=True)
        sleep(0.5)

    print()
    respota_user = input('Diga qual a alternativa correta: ')
    resposta_user = str(respota_user)

    if respota_user.lower() == pergunta_v['resposta_certa']:
        print('Muito bom!! você acertou')
        resposta_c += 1
    else:
        print('Resposta errada! Mais sorte da próxima vez!')
    print('_' * 40)
    print()

perfomance = resposta_c / len(perguntas) * 100
print(f'Você teve {perfomance}% de acerto no questionario')
print(f'{resposta_c} resposta(s) corretas de um total de {len(perguntas)} perguntas.')

