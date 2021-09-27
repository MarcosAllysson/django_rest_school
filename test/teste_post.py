import requests


headers = {'Authorization': 'Token 7c228e179f9cf734334c4b864accccaa6b6a3db5'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

novo_curso = {
    "titulo": "Gerência agil de projetos com scrum",
    "url": "https://gk.com.br"
}

resultado = requests.post(url_base_cursos, headers=headers, data=novo_curso)

# Testando código de status http
assert resultado.status_code == 201

# Testando se o título do curso retornado é o mesmo do informado
assert resultado.json()['titulo'] == novo_curso['titulo']
