import os

API_ID = 6492815
API_HASH = '7de31d943cad5bdcf5b5fa7526f8aa7e'

# пользователь, с которого будут приниматься юзернеймы получателей
ADMIN = 'dalerzafarovich'

# папка, где храняться все шаблоны
TEMPLATES_FOLDER = 'templates'

# список названий шаблонов
TEMPLATES_LIST = [
    '1.txt',
    '2.txt',
]

# задержка между сообщениями в секундах
DELAY = 2

# не трогать
TEXT_LIST = []

for template in TEMPLATES_LIST:
    with open(f'{TEMPLATES_FOLDER}/{template}', 'r', encoding='utf-8') as f:
        TEXT_LIST.append(f.read())
