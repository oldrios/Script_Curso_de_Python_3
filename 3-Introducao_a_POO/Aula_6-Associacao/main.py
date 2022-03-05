from classes import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor(12324)
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever(escritor.nome)
