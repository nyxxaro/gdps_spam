# GDPS Spammer

> Инструмент для спама аккаунтами на приватных серверах Geometry Dash (GDPS).

## Дисклеймер

Проект предназначен **исключительно для образовательных целей** - демонстрация уязвимости открытого API регистрации на GDPS-хостингах (изначально на FruitSpace).

Автор **не призывает** использовать этот инструмент для атак на реальные серверы. Все действия вы совершаете на свой страх и риск.

---

## Структура

```
[ROOT]
└── main.py               
```

## Требования

- Python 3.8+
- `aiohttp`
- `requests`

## Установка

```bash
git clone https://github.com/nyxxaro/gdps_spam.git
cd gdps_spam
pip install aiohttp requests
```

## Запуск

```bash
python main.py
```

## Как это работает

Для каждой регистрации скрипт отправляет `POST` на `accounts/registerGJAccount.php` целевого сервера со следующими данными:

| Поле | Значение |
|------|----------|
| `userName` | случайное число `1` — `9 999 999` |
| `password` | `123456` |
| `email` | `<случайное_число>m@gmail.com` |
| `secret` | `Wmfv3899gc9` |


## 📄 Лицензия

![License](https://www.gnu.org/graphics/gplv3-with-text-136x68.png)
