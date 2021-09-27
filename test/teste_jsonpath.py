from jsonpath import jsonpath
import requests


avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')
# resultados = jsonpath(avaliacoes.json(), 'results')
# print(resultados)

# primeiro = jsonpath(avaliacoes.json(), 'results[0]')
# print(primeiro)

# nome = jsonpath(avaliacoes.json(), 'results[0].nome')
# print(nome)

# Todos os nomes que avaliaram o curso
nomes = jsonpath(avaliacoes.json(), 'results[*].nome')
print(nomes)
