import telebot
from load_save import save_file
from face import search_face
from api_key import API_TOKEN


bot = telebot.TeleBot(API_TOKEN)
start_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
start_keyboard.row('Привет', 'Пока')


@bot.message_handler(commands=['start'])
def start_message(message):
    """
    При начале работы с новым пользователем оповещает в личный чат
    """
    bot.send_message(message.chat.id, 'Привет /start', reply_markup=start_keyboard)
    bot.send_message('338912956', f'Тут {message.from_user.username} бегает где-то...', reply_markup=start_keyboard)


@bot.message_handler(content_types=['text'])
def get_text(message):
    """
    Простые "Привет", "Пока", "Непонимаю"...
    """
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, f'Прощай, {message.from_user.first_name}.')
    elif message.text.lower() == 'гори':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMRXyLY7ixFFl6nCfH-wV4fiNyBBJQAAgUBAAJWnb0Kt-T9tg5FX3caBA')
    else:
        bot.send_message(message.chat.id, 'Я не понимаю что тут нааписано 🧐')
        print(f'{message.from_user.first_name} написал: {message.html_text}')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    """
    Если в сообщении содержится фото, ищем на фото лицо, если лицо найдено, фото сохраняется в папку с фото
    по id пользователя
    """
    id_user = message.chat.id
    id_file = message.photo[len(message.photo)-1].file_id  # Возвращает id самого качественное фото
    url_file = get_url(id_file)
    if search_face(url_file):
        save_file(url_file, id_user, 'photo')
        bot.send_message(message.chat.id, 'Опаньки! Схороню.')
    else:
        bot.send_message(message.chat.id, 'Пейзажи, картинки... Хоть кто-нибудь лицо прислал(.')


@bot.message_handler(content_types=['voice'])
def get_audio(message):
    """
    Если в сообщении содержится фото, ищем на фото лицо, если лицо найдено, фото сохраняется в папку с аудио
    по id пользователя
    """
    id_user = message.chat.id
    id_file = message.voice.file_id
    url_file = get_url(id_file)
    save_file(url_file, id_user, 'voice')


def get_url(file_id):
    """
    Функция для получения ссылки на файл
    :param file_id: id файла который хотим получить
    :return: полная ссылка для загрузки файла
    """
    file_info = bot.get_file(file_id)
    url_file = 'https://api.telegram.org/file/bot{0}/{1}'.format(API_TOKEN, file_info.file_path)
    return url_file

bot.polling()