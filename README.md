# Скачивание изображений космоса и отправление в телеграм-канал

Модули, которые скачивают фотографии космоса, используя API веб-сервисов NASA и SpaceX, и отправляют в Telegram-канал

### Как установить

1. Создайте файл .env и добавьте токен, полученный из [Nasa](https://api.nasa.gov). Также добавьте токен Вашего бота и изначальное время между отправкой картинок. Вот пример:

```
    API_NASA_TOKEN=[Ваш Nasa токен]
    TG_TOKEN=[Токен бота]
    WAIT_TIME=[Время ожидания в секундах]
    TG_CHAT_ID=[Название телеграм-канала, в который отправляются картинки]
```

2. Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:

```
    pip install -r requirements.txt
```

### Как запустить

1. Скачайте картинки

    * Фотографии Земли из космоса:

    ```
        python get_epic_photos.py -c 20
    ```
    * Фотографии дня с изображениями космоса с сайта NASA:

    ```
        python get_nasa_day_images.py -c 15
    ```

    * Фотографии с запуска ракет SpaceX(параметром -id указываем ID запуска, а если он не указан, то скачиваются фотографии последнего запуска):

    ```
        python fetch_spacex_images.py -id 5eb87d47ffd86e000604b38a
    ```
    
2. Запустить бота

    * Чтобы отправить все фотографии из images с задержкой(можем указать в параметре -t задержку между фотографиями, то используется переменная окружения из .env):

    ```
        python telegram_bot.py -t [задержка в секундах]
    ```

    * Чтобы отправить один файл из images(Можно указать параметр -n: название фотографии, а если параметр не указан, то выберется случайная фотография и тоже отправится):

    ```
        python publish_photo.py -n [Название фотографии]
    ```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).