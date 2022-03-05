from selenium import webdriver
from bs4 import BeautifulSoup as soup
from time import sleep, time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

class DataColector():
    def __init__(self):
        self.driver_path = 'chromedriver'
        self.options = webdriver.ChromeOptions()
        #        self.options.add_argument('user-data-dir=Perfil')
        self.options.headless = True
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def acessa(self, url):
        self.chrome.get(url)

    def faz_login(self, login, senha):
        user = self.chrome.find_element_by_id('login')
        pwd = self.chrome.find_element_by_id('senha')
        user.send_keys(login)
        pwd.send_keys(senha)
        btn_efetuar_login = self.chrome.find_element_by_css_selector(
            '#ng-view > div > div:nth-child(2) > div:nth-child(2) > div.col-lg-4.painel-login > form > button')
        btn_efetuar_login.click()

    def clica_veiculos(self):
        try:
            self.aguardar_por('//*[@id="topo-menu-aux"]/ul/li[4]/a')
            link_veiculos = self.chrome.find_element_by_css_selector('#topo-menu-aux > ul > li:nth-child(4) > a')
            link_veiculos.click()
        except Exception as e:
            print('Erro ao clicar em veiculos:', e)

    @staticmethod
    def verifica_se_existe_dado(dicionario, chave_dicionario, palavra, elemento_dos_dados):
        for n in range(len(elemento_dos_dados)):
            dicionario[chave_dicionario] = elemento_dos_dados[n].text if palavra in elemento_dos_dados[
                n].text else 'Null'
            if not dicionario[chave_dicionario] == 'Null':
                break
        return dicionario[chave_dicionario]

    def coletar_dados(self, lista):
        quadro_informacoes = self.coleta_html()
        quadro_informacoes = quadro_informacoes.find('div', {'class': 'quadro_esquerdo'})
        container = {}

        # Dados do header - Nome e tipo
        container['nome'] = str(quadro_informacoes.find('div', {'class': 'nome-motorista'}).text)
        container['tipo'] = str(quadro_informacoes.find('div', {'class': 'tipo-motorista'}).text)

        # Dados da localização, se não existir incluir 'Null' no dicionario
        localizacao = quadro_informacoes.find('div', {'class': 'informacoes barra-vert'}).find('div',
                                                                                               {'class': 'veiculoInfo'})
        if not localizacao:
            container['localizacao'] = 'Null'
        else:
            container['localizacao'] = localizacao.u.text

        # Dados de contato e origem
        container['cidade_origem'] = quadro_informacoes.findAll('div', {'class': 'item', 'style': ' '})[0].text
        container['celular'] = quadro_informacoes.findAll('div', {'class': 'item', 'style': ' '})[1].text

        # Detalhes do veiculo
        detalhes_veiculo = quadro_informacoes.find('div', {'class': 'detalhe-veiculo'}).findAll('div', {
            'style': 'width:579px; height:27px; overflow:hidden; '})

        # Inicio da coleta dos dados
        DataColector.verifica_se_existe_dado(container, 'placa', 'PLACA', detalhes_veiculo)
        DataColector.verifica_se_existe_dado(container, 'marca', 'MARCA', detalhes_veiculo)
        DataColector.verifica_se_existe_dado(container, 'ano', 'ANO', detalhes_veiculo)
        DataColector.verifica_se_existe_dado(container, 'modelo', 'MODELO', detalhes_veiculo)
        DataColector.verifica_se_existe_dado(container, 'rntrc', 'RNTRC', detalhes_veiculo)
        DataColector.verifica_se_existe_dado(container, 'veiculo', 'VEÍCULO', detalhes_veiculo)
        DataColector.verifica_se_existe_dado(container, 'carroceria', 'CARROCERIA', detalhes_veiculo)
        DataColector.verifica_se_existe_dado(container, 'capacidade', 'CAPACIDADE', detalhes_veiculo)
        DataColector.verifica_se_existe_dado(container, 'rastreador', 'RASTREADOR', detalhes_veiculo)

        return lista.append(container)

    def navega_em_motoristas(self):
        try:
            dados_coletados = []
            for n in range(1, 20):
                self.aguardar_por(f'//*[@id="glb-interna_div_corpo_lista"]/div[{n}]/div[1]/div[2]/div[1]/strong/a')
                link_motorista = self.chrome.find_element_by_xpath(
                    f'//*[@id="glb-interna_div_corpo_lista"]/div[{n}]/div[1]/div[2]/div[1]/strong/a').get_attribute(
                    'href')
                if not link_motorista:
                    continue
                self.chrome.execute_script(f"window.open('{link_motorista}', '_blank')")
                self.chrome.switch_to.window(self.chrome.window_handles[-1])
                self.coletar_dados(dados_coletados)
                self.chrome.close()
                self.chrome.switch_to.window(self.chrome.window_handles[0])
            return dados_coletados
        except Exception as e:
            print(f'Erro ao coletar dados: Tentativa {n} -', e)

    def navega_entre_paginas(self, numero_de_paginas):
        try:
            lista_geral_de_dados = []
            for n in range(1, numero_de_paginas):
                conteudo_da_pagina = self.navega_em_motoristas()
                lista_geral_de_dados.extend(conteudo_da_pagina)
                sleep(5)
                self.chrome.get(f'https://www.site.com.br/pages/{n + 1}')
            return lista_geral_de_dados
        except Exception as e:
            print('Erro ao navegar em paginas:', e)


    def aguardar_por(self, xpath):
        WebDriverWait(self.chrome, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, xpath)))

    def fecha_aba(self):
        self.chrome.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')

    def coleta_html(self):
        html = soup(self.chrome.page_source, 'html.parser')
        return html

    def sair(self):
        self.chrome.quit()


if __name__ == '__main__':
    inicio = time()
    browser = DataColector()
    browser.acessa('https://site.com.br/')
    browser.faz_login('login', 'senha')
    browser.clica_veiculos()
    data = browser.navega_entre_paginas(10)
    browser.sair()
    data_json = json.dumps(data, indent=True)
    with open('data.json', 'w+') as file:
        file.write(data_json)
    fim = time()
    tempo_total = fim - inicio
    print(f'{tempo_total} Seg')

'''
    for lista in data:
        for valor in lista:
            for chave, conteudo in valor.items():
                print(f'{chave}: {conteudo}')
            print('-=' * 40)
'''


