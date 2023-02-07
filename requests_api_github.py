import requests

while True:
    usuario = str(input('Digite um usuário: '))
    link = requests.get('https://api.github.com/users/'+usuario)
    print(link.json()['avatar_url'])
