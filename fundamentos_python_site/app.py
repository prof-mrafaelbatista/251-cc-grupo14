from flask import Flask, render_template, request, redirect, url_for, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)
DICTIONARY_FILE = 'dictionary.txt'

genai.configure(api_key="AIzaSyA8h_ugTP7OMGz8sMUeq1gvrDIDh0H-lG0")
model = genai.GenerativeModel("gemini-2.0-flash")


def ler_termos():
    if not os.path.exists(DICTIONARY_FILE):
        return {}
    with open(DICTIONARY_FILE, 'r', encoding='utf-8') as f:
        linhas = f.readlines()
    termos = {}
    for linha in linhas:
        if ':' in linha:
            termo, definicao = linha.strip().split(':', 1)
            termos[termo] = definicao
    return termos

def salvar_termos(termos):
    with open(DICTIONARY_FILE, 'w', encoding='utf-8') as f:
        for termo, definicao in termos.items():
            f.write(f"{termo}:{definicao}\n")

# --- Rotas ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/equipe')
def equipe():
    return render_template('equipe.html')

@app.route('/fundamentos_1selecao')
def fundamentos_selecao():
    return render_template('fundamentos_1selecao.html')

@app.route('/fundamentos_2repeticao')

def fundamentos_repeticao():
    return render_template('fundamentos_2repeticao.html')

@app.route('/fundamentos_3vetores')
def fundamentos_vetores():
    return render_template('fundamentos_3vetores.html')

@app.route('/fundamentos_4funcoes')
def fundamentos_funcoes():
    return render_template('fundamentos_4funcoes.html')

@app.route('/fundamentos_5tratamentos')
def fundamentos_tratamentos():
    return render_template('fundamentos_5tratamentos.html')

@app.route('/perguntas', methods=['GET', 'POST'])
def perguntas():
    resposta = None
    if request.method == 'POST':
        pergunta = request.form['pergunta']
        resposta = perguntar_gemini(pergunta)
    return render_template('perguntas.html', resposta=resposta)
def perguntar_gemini(pergunta):
    try:
        response = model.generate_content(pergunta)
        return response.text
    except Exception as e:
        return f"Erro: {str(e)}"

@app.route('/dicionario')
def dicionario():
    termos = ler_termos()
    return render_template('dicionario.html', termos=termos)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    termo = request.form['termo']
    definicao = request.form['definicao']
    termos = ler_termos()
    termos[termo] = definicao
    salvar_termos(termos)
    return redirect(url_for('dicionario'))

@app.route('/editar/<termo>', methods=['GET', 'POST'])
def editar(termo):
    termos = ler_termos()
    if request.method == 'POST':
        nova_definicao = request.form['definicao']
        termos[termo] = nova_definicao
        salvar_termos(termos)
        return redirect(url_for('dicionario'))
    return render_template('editar_termo.html', termo=termo, definicao=termos[termo])

@app.route('/deletar/<termo>')
def deletar(termo):
    termos = ler_termos()
    if termo in termos:
        del termos[termo]
        salvar_termos(termos)
    return redirect(url_for('dicionario'))

if __name__ == '__main__':
    app.run(debug=True)
