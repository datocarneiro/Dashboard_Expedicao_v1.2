# Dashboard de expedição com webScraping - dato®


O código fornecido é um script Python que utiliza a biblioteca `Selenium` e o framework `Flask` para automatizar a extração de informações de uma página da web. O objetivo do código é contar a quantidade de ocorrências de determinadas palavras-chave em um website específico, e gerar um dashboard de expedidção para melhor gestão operacional.

### Tecnologia: 🎯 Python, Selenium, Pandas, Openpyxl, Flask, Html, CSS.

![image](https://github.com/datocarneiro/Dashboard_Expedicao_v1.2/assets/132966071/128c7c9c-541c-48fc-a20f-f3560c51bd99)


Aqui está uma documentação detalhada para o código: 

Importação de Bibliotecas:

from selenium import webdriver: Importa a classe webdriver da biblioteca Selenium, que permite a interação com o navegador.
from selenium.webdriver.chrome.options import Options: Importa a classe Options do módulo chrome.options da biblioteca Selenium, que permite configurar as opções do navegador Chrome.
from flask import Flask, render_template: Importa as classes Flask e render_template do módulo flask, que são usadas para criar um aplicativo Flask e renderizar templates HTML.
from selenium.webdriver.chrome.service import Service: Importa a classe Service do módulo chrome.service da biblioteca Selenium, que é usada para gerenciar o serviço do navegador Chrome.
from webdriver_manager.chrome import ChromeDriverManager: Importa a classe ChromeDriverManager do módulo chrome da biblioteca webdriver_manager, que é usada para gerenciar o driver do navegador Chrome.
from selenium.webdriver.common.by import By: Importa a classe By do módulo common.by da biblioteca Selenium, que é usada para selecionar elementos na página com base em diferentes estratégias de localização.
import time: Importa o módulo time do Python, que é usado para adicionar pausas no código.

*** Lembre-e se instalar cada um no shell do replit ***
```python
pip install flask
pip install selenium
pip install webdriver_manager
```

Configuração do Aplicativo Flask:
```python
app = Flask(__name__):
```
###  Cria uma instância do aplicativo Flask.
Variáveis Globais:

resultados = {}: Cria um dicionário vazio chamado resultados para armazenar os resultados da contagem das palavras-chave.
palavras_chave: Uma lista de palavras-chave que serão contadas na página.
Função contar_palavras_chave():

Essa função é responsável por abrir o navegador Chrome, fazer login em uma página web, iterar através de uma lista de palavras-chave e contar o número de ocorrências dessas palavras-chave.
Ela utiliza a biblioteca Selenium para interagir com a página da web e realizar as ações necessárias.
No final, retorna um dicionário com os resultados da contagem e o número total de palavras encontradas.
Rota Principal do Flask:

@app.route('/'): Define a rota principal do aplicativo Flask.
A função exibir_resultados() é executada quando a rota principal é acessada.
Dentro dessa função, chama-se a função contar_palavras_chave() para obter os resultados atualizados da contagem das palavras-chave.
Em seguida, filtra as palavras-chave e resultados para exibir apenas aqueles com contagens maiores que zero.
Renderiza o template HTML index.html passando os resultados e o total de palavras como parâmetros.
Execução do Aplicativo Flask:

if __name__ == '__main__':: Verifica se o script está sendo executado diretamente.
app.run(host='0.0.0.0', port=8080): Inicia o aplicativo Flask, tornando-o disponível em http://localhost:8080.
Essa é uma visão geral da funcionalidade do código fornecido. Ele automatiza a contagem de palavras-chave em uma página da web específica e exibe os resultados em uma interface web usando o framework Flask.
