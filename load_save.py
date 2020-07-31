from converter import convert_voice
import requests
import os


def save_file(url_file, id_user, type_file):
    """
    Функция если необходимо создает  папку с "id_user" и подпапку "photo"
    и по порядку скачивает и сохраняет в ней файлы фото
    """

    file = requests.get(url_file)
    dir_save = f'collect/{id_user}/{type_file}'  # создает если необходимо папки
    try:
        os.makedirs(dir_save)
        if type_file == 'photo':
            with open(f'{dir_save}/photo_message_0.jpg', 'wb') as fd:
                for chunk in file:
                    fd.write(chunk)

        elif type_file == 'voice':
            with open(f'{dir_save}/audio_message_0.ogg', 'wb') as fd:
                for chunk in file:
                    fd.write(chunk)
            convert_voice(dir_save, 'audio_message_0.ogg')

    except:
        if type_file == 'photo':
            with open(f'{dir_save}/{name_new_photo(dir_save)}', 'wb') as fd:
                for chunk in file:
                    fd.write(chunk)

        elif type_file == 'voice':
            name_new_file = name_new_voice(dir_save)
            with open(f'{dir_save}/{name_new_file}', 'wb') as fd:
                for chunk in file:
                    fd.write(chunk)
            convert_voice(dir_save, name_new_file)


def name_new_photo(dir_save):
    """
    Функция принимает адресс с файлами, определяет максимальный порядковый номер,
    добавляет единицу
    :param dir_save: Папка с сохраненными файлами
    :return: возвращает полное имя нового файла
    """
    last_name = os.listdir(dir_save)
    new_name = f'photo_message_{len(last_name)}.jpg'
    return new_name


def name_new_voice(dir_save):
    """
    Функция принимает адресс с файлами, определяет максимальный порядковый номер,
    добавляет единицу
    :param dir_save: Папка с сохраненными файлами
    :return: возвращает полное имя нового файла
    """
    last_name = os.listdir(dir_save)
    new_name = f'audio_message_{len(last_name)}.ogg'
    return new_name
