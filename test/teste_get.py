import requests


headers = {'Authorization': 'Token 7c228e179f9cf734334c4b864accccaa6b6a3db5'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.get(url_base_cursos, headers=headers)
print(resultado.json())

# Testando conexão status_code 200
assert resultado.status_code == 200

# Testando se a API que não deveria existir, realmente retorna 404
# assert resultado.status_code == 404

# Testando a quantidade de registros
assert resultado.json()['count'] == 4
