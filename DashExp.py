import os
from flask import Flask, render_template, request, redirect, url_for
from markupsafe import Markup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import concurrent.futures
import time
from dotenv import load_dotenv

app = Flask(__name__)



palavras_chave = []
first_run = True  # Variável global para rastrear a primeira execução

@app.route('/')
def login():
    return render_template('login.html', mensagem_erro="")

@app.route('/verificar_senha', methods=['POST'])
def verificar_senha():
    login = os.getenv('LOGIN')
    senha = os.getenv('SENHA')
    nome_inserido = request.form['nome']
    senha_inserida = request.form['senha']
    
    if nome_inserido == login and senha_inserida == senha:
        return redirect(url_for('login_passou'))
    else:
        mensagem_erro = "Nome ou senha incorretos. Tente novamente."
        return render_template('login.html', mensagem_erro=mensagem_erro)

@app.route('/login_passou')
def login_passou(): 
    estilos = '<style>.conteudo-gerado { font-size: 50px; color: blue; }</style>'
    rendered_template = render_template('gerando_dados.html')
    rendered_template = Markup(estilos + rendered_template)
    script = Markup('<script>setTimeout(function() { window.location.href = "/executar_contar_palavras_chave"; }, 1000);</script>')
    rendered_template += script
    
    return rendered_template

def contar_palavras_chave_async():
    print('... Iniciando código ...')
    global resultados, palavras_chave, first_run
    resultados = {}

    print(" ...............ENTREOU DEF CONTAR PALAVRACHAVE...............")

    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless')  # Adiciona a opção para o modo headless
    options.add_argument('--disable-gpu')  # Desativa a GPU, recomendável no modo headless
    options.add_argument('window-size=1366x768')  # Define o tamanho da janela

    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico, options=options)

    navegador.execute_script("document.body.style.zoom='75%'")

    print(" ...............PASSOU OPTION...............")

    apikey = os.getenv('APIKEY')
    usuario = os.getenv('USUARIO')
    senha_usuario  = os.getenv('SENHA_USUARIO')

    print('... Logando ...')
    navegador.get("https://amplo.eship.com.br/")
    # WebDriverWait(navegador, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login"]'))).send_keys(usuario)
    # WebDriverWait(navegador, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="senha"]'))).send_keys(senha_usuario)
    WebDriverWait(navegador, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="apikey"]'))).send_keys(apikey)
    WebDriverWait(navegador, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Entrar"]/span'))).click()

    WebDriverWait(navegador, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="FormListarOrdem"]/ul/li[2]/div/a[3]/div'))).click()
    print('... Abriu lista para 100... e iniciando FOR ...')

    time.sleep(10)

    for palavra in palavras_chave:
        resultados[palavra] = 0
    print("... passou for ...")

    while True:
        print('... Iniciando FOR ...')
        try:
            WebDriverWait(navegador, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="FormListarOrdem"]')))
            elementos = navegador.find_elements(By.XPATH, '//*[@id="FormListarOrdem"]')
            
            for elemento in elementos:
                conteudo_elemento = elemento.text
                for palavra in palavras_chave:
                    resultados[palavra] += conteudo_elemento.count(palavra)
                    # print(f'... Palavra {palavra} encontrada ...')

            # Verifica se há próxima página
            proxima_pagina_elemento = navegador.find_element(By.XPATH, '//*[@id="FormListarOrdem"]/ul/li[6]')
            if "disabled" in proxima_pagina_elemento.get_attribute("class"):
                print("Não há mais páginas para avançar.")
                break
        except NoSuchElementException:
            print("... Elemento não encontrado ...")
            break
        except TimeoutException:
            print("... TimeoutException: Elemento não encontrado no tempo limite ...")
            break
            
        print('... Proxima página ...')
        try:
            proxima_pagina_elemento.click()
            time.sleep(10)
        except TimeoutException:
            print("... TimeoutException: Próxima página não encontrada no tempo limite ...")
            break

    print('... Atualizando Resultados ...')
    resultados = {palavra: int(quantidade) for palavra, quantidade in resultados.items()}
    total_palavras = sum(resultados.values())
    print('... Return Resultados ...')

    # Espera de 5 minutos antes de reiniciar o loop, exceto na primeira execução
    if not first_run:
        print('... Aguardando 4 minutos antes de reiniciar ...')
        time.sleep(240)  # 240 segundos = 4 minutos
    first_run = False  # Atualiza a variável para indicar que a primeira execução já ocorreu

    return resultados, total_palavras


@app.route('/executar_contar_palavras_chave')
def executar_contar_palavras_chave():
    global palavras_chave, resultados
    with concurrent.futures.ThreadPoolExecutor() as executor:
        palavras_chave = [
                        "TOTAL EXP",
                        "PAPAPA - TOTAL",
                        "FM",
                        "DATO TESTE",
                        "AG AMINTAS",
                        "AG LAMENHA",
                        "OLIST RETIRA",
                        "AG ANGELO",
                        "ENTREGA OSVALDO",
                        " JAD ",
                        # "ESM",
                        # "LATAM",
                        # "AZUL",
                        # "GOL",
                        # "ANDREIA SSA",
                        "POSTA JA",
                        "RETIRA NA AMPLO",
                        "BLING",
                        "SUBWAY - AMPLO",
                        "MULHERES",
                        "TRANSPORTADORA",
                        "BRASPRESS",
                        # "RODONAVES",
                        # "PAULISTANA",
                        # "ADW",
                        # "TECMAR",
                        # "MAEX",
                        # "BEMOL",
                        # "DESTAK",
                        # "AVANCE",
                        # "DOMINIO",
                        # "EBTRANS",
                        # "RAFAEL BERNAL",
                        # "RODOVIASUL",
                        # "URANOLOG",
                        # "MMCOSTA",
                        # "RODOVITOR",''
                        "TRANSPO-ALMENARA",
                        "LOGGI",
                        "AGF XAXIM",
                        "J&T",
                        # "CDM - AZUL",
                        # "CDM - CORREIOS CENTENARIO",
                        # "CDM - DBA",
                        # "CDM - DIALOGO",
                        # "CDM - FEDEX",
                        # "CDM - FOX",
                        # "CDM - JADLOG",
                        # "CDM - MAGALU",
                        # "CDM - NOVA ELOHIM",
                        # "CDM - POT SPEED",
                        # "CDM - RETIRA",
                        # "CDM - REVISAR TRANSPORTES",
                        'IMBERA - ESM',
                        'IMBERA - MOTOBOY',
                        'IMBERA - PEGA ENTREGA',
                        'IMBERA - RETIRA',
                        'IMBERA - RODONAVES',
                        'IMBERA - AGF AMINTAS',
                        "AMAZON",
                        "PEGA ENT"
                        ]
        
        resultados, total_palavras = contar_palavras_chave_async()
    
    palavras_chave = [palavra for palavra in palavras_chave if resultados.get(palavra, 0) != 0]
    resultados = {palavra: quantidade for palavra, quantidade in resultados.items() if quantidade != 0}
    
    return render_template('index.html', resultados=resultados, total_palavras=total_palavras)

if __name__ == '__main__':
    app.run() #host="0.0.0.0", port=8080)