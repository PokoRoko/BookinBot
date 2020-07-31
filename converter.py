from pydub import AudioSegment
import os


def convert_voice(dir_save, name_new_voice):
    """
    Функция конвертирует ogg в wav и удаляет старый файл
    :param dir_save: Адресс папки
    :param name_new_voice: Имя создаваемогофайла
    """
    voice_ogg = AudioSegment.from_ogg(f'{dir_save}/{name_new_voice}')
    # Задаем частоту дескретизации
    voice_ogg.set_frame_rate(16000)
    # Экспортируем в новый файл с новым расширением
    voice_ogg.export(f'./{dir_save}/{name_new_voice[:-4]}.wav', format='wav')
    # Признаюсь это не МНОГО костыль, но так проще обрабатывать файл
    os.remove(f'{dir_save}/{name_new_voice}')

