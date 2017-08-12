import requests
import os

API_KEY = str('trnsl.1.1.20161025T233221Z.47834a66fd7895d0.'
              'a95fd4bfde5c1794fa433453956bd261eae80152')
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def directory_file(way=''):
    """Абсолютный путь к фаилу, аргумент - (путь от директории с __file__)"""
    file = os.path.join(os.path.dirname(os.path.abspath(__file__)), way)
    return file


def build_direcrory(directory):
    """
    Проверяет существование директории и если нет то создает ее,
    аргумент - (требуемая директория)
    """
    if directory not in os.listdir(directory_file()):
        os.mkdir(directory_file(directory))


def open_file_read(file_):
    """
    Считываем файл
    :param file_: считываемый файл
    :return: содержимое файла
    """
    with open(file_, 'r') as file:
        data = file.read()
    return data


def open_file_write(file_, data):
    """
    Запись результата в файл
    :param file_: Записываемый файл
    :param data: Записываемые данные
    """
    with open(file_, 'w') as file:
        file.write(data)


def translate_ru(text):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param to_lang:
    :return:
    """

    params = {
        'key': API_KEY,
        'text': text,
        'lang': 'ru',
        'options': 1
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    return ''.join(json_['text'])


def main():
    build_direcrory('Result')  # Создаем папку Result

    #  Список фаилов в папке Source
    file_source = os.listdir(directory_file('Source'))
    for list_file in file_source:
        #  Считываем фаил и переводим
        result = translate_ru(
            open_file_read(directory_file(os.path.join('Source', list_file))))

        #  Результат
        open_file_write(
            directory_file(os.path.join('Result', list_file)),
            result
        )


main()
