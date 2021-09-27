from django.shortcuts import render
import requests


def home(request):

    result = {}

    headers = {'Authorization': 'Token 1ee251b0d02cc0c9cbb4f96d4243a8fc207ea162'}
    url = 'http://127.0.0.1:8000/api/v2/cursos/'

    requisicao = requests.get(url=url, headers=headers)
    # print(requisicao.content)
    # print(requisicao.json())
    # print(requisicao.text)

    result = {
        'api': requisicao.json()['results']
    }

    # print(requisicao.json()['results'])
    # for l in requisicao.json()['results']:
    #     print(l)

    return render(request, 'cursos/home.html', result)
