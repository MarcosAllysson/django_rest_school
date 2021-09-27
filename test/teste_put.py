import requests


headers = {'Authorization': 'Token 1ee251b0d02cc0c9cbb4f96d4243a8fc207ea162'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

curso_atualizado = {
    "titulo": "Gerência agil de projetos com scrum 2",
    "url": "https://gk.com.br/scrum1"
}

# Buscando curso com ID 7
# curso = requests.get(url=f'{url_base_cursos}7/', headers=headers)
# print(curso.json())

resultado = requests.put(url=f'{url_base_cursos}7/', headers=headers, data=curso_atualizado)

# Testando código de status http se é igual 200
print(resultado.status_code)
assert resultado.status_code == 200

# Testando se o título do curso retornado é o mesmo do informado
assert resultado.json()['titulo'] == curso_atualizado['titulo']

