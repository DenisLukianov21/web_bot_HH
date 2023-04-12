# Vacancies-bot
Этот бот поможет в мониторинге ваканский с сайта HH.ru, он создан с помощью библиотеки python-telegram-bot.


_*Проект выполнен для конференции "Научные перспективы 2023" в г. Дзержинск и находится в стадии MVP*_

Бота можной найти по ссылке:
```
https://t.me/webpy_bot
```

# Деплой и настройка бота
- Скопируйте репозиторий в нужную вам директорию
```bash
git clone git@github.com:DenisLukianov21/web_bot_HH.git
```
- Создайте и активируейте виртуальное окружение (для MacOS)
```bash
python3 -m venv env && source env/bin/activate
```
- Установите необходимые библиотеки
```bash
pip install -r requirements.txt
```
- В файле parser.py установите нужные вам значения
```python
params = {
    'text': 'NAME:Python', # Название вакансии
    'area': 66, # Область поиска вакансий
    'page': page, 
    'per_page': 1 # Вакансии на страницу
}
```
- Создайте файл .env и введите туда токен бота и chat_id, например:
```
TELEGRAM_TOKEN=MySuperSercetToken
chat_id=MyChatID
```
# Автор
Денис Лукьянов, 2023 г.

- Telegram  @NyamNyamIch12
- VK  https://vk.com/id129836106
- Email  denislukianov2001@yandex.ru
