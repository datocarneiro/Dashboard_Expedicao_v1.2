# Dashboard de expedição com webScraping - dato®


## Introdução
O projeto de Contagem de Palavras-Chave é uma aplicação web desenvolvida com o framework Flask, que utiliza Selenium para automatizar a navegação em uma página web e contar a ocorrência de palavras-chave específicas. O objetivo é permitir a automação da coleta de dados gerando um dashboard para gerenciamento operacional.

### Funcionalidades
* Autenticação de Usuário:
Permite que o usuário se autentique no sistema com um nome de usuário e senha.

* Contagem de Palavras-Chave:
Navega automaticamente em uma página web especificada e conta a ocorrência de uma lista predefinida de palavras-chave.

* Visualização de Resultados:
Exibe os resultados da contagem de palavras-chave em uma interface web amigável.

### Tecnologia: 🎯 Python, Selenium, Pandas, Openpyxl, Flask, Html, CSS.

![image](https://github.com/datocarneiro/Dashboard_Expedicao_v1.2/assets/132966071/128c7c9c-541c-48fc-a20f-f3560c51bd99)

Instale as Dependências:
```python
pip install -r requirements.txt
```

## Estrutura do projeto
```markdown
projeto-contagem-palavras-chave/
├── app.py
├── templates/
│   ├── login.html
│   ├── gerando_dados.html
│   └── index.html
├── .env
├── requirements.txt
└── README.md
```

## Documentação da API

### Endpoints

1. **Login**
   - **URL**: `/`
   - **Métodos**: `GET`
   - **Descrição**: Exibe a página de login para autenticação do usuário.

2. **Verificar Senha**
   - **URL**: `/verificar_senha`
   - **Métodos**: `POST`
   - **Parâmetros**:
     - `nome`: Nome do usuário.
     - `senha`: Senha do usuário.
   - **Descrição**: Verifica as credenciais do usuário. Se corretas, redireciona para a página de processamento. Caso contrário, exibe uma mensagem de erro.

3. **Login Passou**
   - **URL**: `/login_passou`
   - **Métodos**: `GET`
   - **Descrição**: Exibe a página de carregamento e redireciona automaticamente para iniciar a contagem de palavras-chave.

4. **Executar Contagem de Palavras-Chave**
   - **URL**: `/executar_contar_palavras_chave`
   - **Métodos**: `GET`
   - **Descrição**: Inicia a contagem de palavras-chave na página web especificada e exibe os resultados.

