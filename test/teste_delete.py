import requests


headers = {'Authorization': 'Token 1ee251b0d02cc0c9cbb4f96d4243a8fc207ea162'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.delete(url=f'{url_base_cursos}7/', headers=headers)

# Testando código de status http se é igual 204
print(resultado.status_code)
assert resultado.status_code == 204

# Testando se o tamanho do conteúdo retornado é 0
assert len(resultado.text) == 0
