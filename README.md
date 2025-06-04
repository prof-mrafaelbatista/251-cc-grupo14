# 251-cc-grupo14

# fundamentos_python_site

##  Projeto Final Flask: Fundamentos de Programação em Python

# Estrutura do Site

•⁠  ⁠O site está dividido nas seguintes seções principais:

# Inicio: 
-Apresenta o propósito do site e direciona para os principais recursos.
# Equipe:
-Fomarda por Everton Fernandes, Sarah barreto, Alex Brito, Jasmin Cleide
# Fundamentos: 
-Contém fundamentos da Programação em Python e exemplos sobre cada fundamento, estruturas de repetição e de seleção, funções/procedimentos, vetores/matrizez e tratamentos de exceções.
# Dicionário de Termos: 
-Um glossário de conceitos importantes da programação, armazenado em um arquivo de texto.
# Assistente IA (Gemini): 
-Permite ao usuário fazer perguntas e obter respostas geradas pela API do Gemini, facilitando o seu aprendizado e tirando suas dúvidas. 


# Tecnologias Utilizadas

# Linguagem principal: 
-Python 3.11
# Framework web: 
-Flask
# Frontend: 
-HTML, CSS (Bootstrap), Jinja2 (para templates dinâmicos)
# API de IA: 
-Google Gemini (via Gemini API)
# Armazenamento de dados: 
-Arquivo ⁠ .txt ⁠ para o dicionário de termos


# Integração com a API do Gemini

Foi implementado o

####import google.generativeai as genai

Para acessar os modelos da linha Gemini. 
Esse SDK facilita o envio de perguntas e 
o recebimento de respostas.

Logo depois foi configurado a chave:

####genai.configure(api_key="AIzaSyA8h_ugTP7OMGz8sMUeq1gvrDIDh0H-lG0")

esse exemplo acima configura a chave de API, que é usada para autenticar seu aplicativo com a API do Gemini. Essa chave é sensível e não deve ser exposta em código público, pois pode ser usada por terceiros para consumir sua cota.

próximo passo foi implementado o modelo:

####model = genai.GenerativeModel("gemini-2.0-flash")

gemini-2.0-flash é uma versão otimizada para respostas rápidas e baixo custo.

acrescentamos também essa função abaixo:

####def perguntar_gemini(pergunta): try: response = model.generate_content(pergunta) return response.text except Exception as e: return f"Erro: {str(e)}"

Essa função: 
-Recebe uma pergunta como string (pergunta); 
-Usa o modelo para gerar uma resposta com .generate_content(pergunta); 
-Retorna o texto da resposta (response.text); 
-Se houver erro (Ex:falta de internet, chave inválida, problema com a API), 
-retorna a mensagem de erro.

##Resumo da integração: 
1-Instala-se o SDK com: pip install google-generativeai 
2-Usa-se a API Key do Google AI Studio. 
3-Um modelo (GenerativeModel) é implementado. 
4-O método .generate_content() é usado para gerar respostas com base na entrada do usuário.


# Como foi Executado o Flask Localmente

Pré-requisitos
•⁠  ⁠Python 3.11
•⁠  ⁠Git (opcional)
•⁠  ⁠Instalar dependências:

pip install flask

# Passo à Passo:

1.⁠ ⁠Clone o repositório:
git clone https://github.com/prof-mrafaelbatista/251-cc-grupo14
cd 251-cc-grupo14

2.⁠ ⁠Crie um arquivo ⁠ .env ⁠ com a chave da API:

GEMINI_API_KEY=sua_chave_aqui

3.⁠ ⁠Execute a aplicação:

python app.py

4.⁠ ⁠Acesse no navegador:

http://127.0.0.1:5000/


# Principais Partes do Código

# app.py: 
•⁠  ⁠Arquivo principal da aplicação Flask. Define as rotas, renderiza as páginas HTML e lida com requisições.
# templates: 
•⁠  ⁠Pasta contendo os arquivos HTML com o motor de templates Jinja2.
# static: 
•⁠  ⁠CSS, imagens ou JS utilizados no site.
# dictionary.txt: 
•⁠  ⁠Arquivo com os termos do dicionário técnico.
# gemini_api.py: 
•⁠  ⁠Arquivo separado com a função de integração com a API.
