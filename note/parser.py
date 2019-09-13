import os
import shutil
import requests
import time

from bs4 import BeautifulSoup as bs


from main.models import Note

requests.packages.urllib3.disable_warnings()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/75.0.3770.142 Safari/537.36"
           }


def url_pars(request):
    """ Функция собирает в список, все не обработанные записи """
    urls = [Note.objects.filter(is_active=False)]
    return urls


def work_pars(request):
    """" Парсер для заметок пользователей. """
    urls = url_pars  # передаем список необработанных заметок
    b_urls = urls  # url-заметок
    # Проходимся по списку и обрабатываем заметки
    for b_url in b_urls:
        session = requests.Session()  # открываем сессию
        request = session.get(b_url, headers=headers)  # отправляем запрос по указанному адрессу
        if request.status_code == 200:
            # Если ответ последовал, то выполняем код дальше
            soup = bs(request.content, 'html.parser')
            title = soup.find('title').text  # Возвращает title html-страницы
            # Возвращает meta тэг description, если его нет то возвращает пустой список
            description = soup.find_all('meta', {'name': 'description'})
            if description:
                descr = description[0]['content']
            else:
                descr = None

            image = soup.find('link', {'rel': 'shortcut icon', 'rel': 'icon'})['href']  # Возвращает link с адресом: favicon.ico
            if image[:4] == 'http' or image[:5] == 'https':
                media_root = '../media'
                if not image.startswith(('data:image', 'javascript')):
                    filename = image.split('/')[-1].split("?")[0]  # поучаем иконку
                    r = session.get(image, stream=True, verify=False)
                    # сохраняем(записываем) её в двоичном коде, размер не должен превышать 1024
                    with open(filename, 'wb') as f:
                        for chunk in r.iter_content(chunk_size=1024):
                            f.write(chunk)

                    current_image_absolute_path = os.path.abspath(filename)  # получаем абсолютный путь до папки
                    shutil.move(current_image_absolute_path, media_root)  # перемещает иконку на директорию выше, в папку медиа

                    update_note = Note()
                    update_note.url = b_url
                    update_note.title = title
                    update_note.description = descr
                    update_note.image = filename
                    update_note.is_parse = True
                    update_note.save()



work_pars()

