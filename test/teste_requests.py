import requests


# GET para avaliações
# avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# Acessando o código de status HTTP
# print(avaliacoes.status_code)

# Acessando os dados da resposta
# print(avaliacoes.json())
# print(type(avaliacoes.json()))

# Acessando quantidade de registros
# print(avaliacoes.json()['count'])

# Acessando resultados
# print(avaliacoes.json()['results'])

# Acessando primeiro elemento da lista de resultados
# print(avaliacoes.json()['results'][0])

# Acessando somente nome de quem fez última avaliação
# print(avaliacoes.json()['results'][-1]['nome'])


# GET avaliação específica
# avaliacao = requests.get('http://localhost:8000/api/v2/avaliacoes/1/')
# print(avaliacao.json())


# GET cursos

# headers = {'Authorization': 'Token 7c228e179f9cf734334c4b864accccaa6b6a3db5'}
#
# cursos = requests.get(url='http://localhost:8000/api/v2/cursos/', headers=headers)
#
# print(cursos.status_code)
# print(cursos.json())
