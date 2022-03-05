from vendas.formata.precos import formata_precos


def percent(n):
    n = n / 100
    return n


def desconto(valor, reducao):
    '''
    Considerar valor o preco que quer aplicar o desconto.
    Reducao é o valor em percentual para efetuar o desconto.
    '''
    try:
        valor = float(valor)
        reducao = float(reducao)
        return formata_precos(valor - valor * percent(reducao))
    except IndentationError:
        pass


def aumento(valor, acrescimo):
    '''
    Considerar valor o preco que quer aplicar o desconto.
    Acrescimo é o valor em percentual para efetuar o aumento.
    '''
    try:
        valor = float(valor)
        acrescimo = float(acrescimo)
        return formata_precos(valor + valor * percent(acrescimo))
    except IndentationError:
        pass


