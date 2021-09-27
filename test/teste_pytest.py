import requests


class TesteCursos:
    headers = {'Authorization': 'Token 1ee251b0d02cc0c9cbb4f96d4243a8fc207ea162'}
    url_base_cursos = 'http://localhost:8000/api/v2/cursos/'

    def test_get_cursos(self):
        cursos = requests.get(url=self.url_base_cursos, headers=self.headers)

        assert cursos.status_code == 200

    def test_get_curso(self):
        curso = requests.get(url=f'{self.url_base_cursos}1/', headers=self.headers)

        assert curso.status_code == 200

    def test_post_curso(self):
        curso = {
            "titulo": "Programação em Ruby",
            "url": "https://gk3.com.br"
        }

        resposta = requests.post(url=self.url_base_cursos, headers=self.headers, data=curso)

        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == curso['titulo']

    def test_put_curso(self):
        atualizado = {
            "titulo": "Programação em C++",
            "url": "https://gk4.com.br"
        }

        resposta = requests.put(url=f'{self.url_base_cursos}2/', headers=self.headers, data=atualizado)

        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == atualizado['titulo']

    def test_put_titulo_curso(self):
        atualizado = {
            "titulo": "Programação em Python Advanced",
            "url": "https://gk5.com.br"
        }

        resposta = requests.put(url=f'{self.url_base_cursos}2/', headers=self.headers, data=atualizado)

        assert resposta.json()['titulo'] == atualizado['titulo']

    def test_delete_curso(self):

        curso = requests.put(url=f'{self.url_base_cursos}2/', headers=self.headers)

        assert curso.status_code == 204 and len(curso.text) == 0
