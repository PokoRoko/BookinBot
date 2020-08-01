import cv2


def search_face(url_photo):
    """
    Функция ищет лица на фото
    :param url_photo: ссылка на фото
    :return: True или False
    """
    # Читаем фото по ссылке
    cap = cv2.VideoCapture(url_photo)
    ret, img = cap.read()
    # Подключаем каскадный фильтр
    face_cascade = cv2.CascadeClassifier(r'C:\Users\BookinOff\Desktop\BookinBot\haarcascade_frontalface_default.xml')
    # Делаем фото серым
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Счетчик лиц)
    count = 0
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        count += 1

    # Если счетчик больше одного, возвращает True
    if count > 0:
        return True
    else:
        return False
    # При необходимости сохраняем фото с выделением
    #cv2.imwrite('obrabotochka.png', img)
