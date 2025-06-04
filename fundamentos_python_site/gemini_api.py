import google.generativeai as genai

genai.configure(api_key="AIzaSyA8h_ugTP7OMGz8sMUeq1gvrDIDh0H-lG0")
model = genai.GenerativeModel('"gemini-2.0-flash"')


def perguntar_gemini(pergunta):
    try:
        response = model.generate_content(pergunta)
        return response.text
    except Exception as e:
        return f"Erro: {str(e)}"
