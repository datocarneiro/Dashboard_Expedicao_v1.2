import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time


import dotenv
palavra = dotenv.dotenv_values('TESTE')

# palavra_os = os.getenv('TESTE')

def teste():
    print(" ...............ENTREOU DEF CONTAR PALAVRACHAVE...............")
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    # options.add_argument('--headless')  # Adiciona a opção para o modo headless
    # options.add_argument('--disable-gpu')  # Desativa a GPU, recomendável no modo headless
    options.add_argument('window-size=1920x1080')  # Define o tamanho da janela

    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico, options=options)

    print(" ...............PASSOU OPTION...............")

    navegador.get('https://google.com.br')

    WebDriverWait(navegador, 15).until(EC.presence_of_element_located((By.ID, 'APjFqb'))).send_keys(palavra)
    print( 'ja informamos a chave ')
    time.sleep(50)
teste()

