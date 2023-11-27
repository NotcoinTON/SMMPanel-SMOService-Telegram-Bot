<br/>
<p align="center">
  <a href="https://github.com/TegroTON/SMMPanel-SMOService-Telegram-Bot">
    <img src="static/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Smoservice Bot</h3>

  <p align="center">
    Система автоматизированной раскрутки и продвижения в социальных сетях❗️
    <br/>
    <br/>
    <a href="https://github.com/TegroTON/SMMPanel-SMOService-Telegram-Bot"><strong>Explore the docs »</strong></a>
    <br/>
    <br/>
    <a href="https://t.me/smoservicemedia_bot">View Demo</a>
    .
    <a href="https://github.com/TegroTON/SMMPanel-SMOService-Telegram-Bot/issues">Report Bug</a>
    .
    <a href="https://github.com/TegroTON/SMMPanel-SMOService-Telegram-Bot/issues">Request Feature</a>
  </p>
</p>

![Downloads](https://img.shields.io/github/downloads/TegroTON/SMMPanel-SMOService-Telegram-Bot/total) ![Contributors](https://img.shields.io/github/contributors/TegroTON/SMMPanel-SMOService-Telegram-Bot?color=dark-green) ![Issues](https://img.shields.io/github/issues/TegroTON/SMMPanel-SMOService-Telegram-Bot) ![License](https://img.shields.io/github/license/TegroTON/SMMPanel-SMOService-Telegram-Bot)

## Содержание

-   [О проекте](#о-проекте)
-   [Основные инструменты](#основные-инструменты)
-   [С чего начать](#с-чего-начать)
    -   [Пререквизиты](#пререквизиты)
    -   [Установка](#установка)
-   [Предложения и известные баги](#предложения-и-известные-баги)
-   [Авторы](#авторы)
-   [Благодарности](#благодарности)

## О проекте

![Screen Shot](static/main_menu.png)

🚀 SmoService Bot - Ваш идеальный инструмент для продвижения в социальных сетях! Получайте больше подписчиков, просмотров и многого другого с легкостью и эффективностью.

Основные функции:

-   Новый заказ: Быстро и удобно создайте заказ на накрутку нужного параметра.
-   История: Отслеживайте все свои заказы и их статус в одном месте.
-   Кошелек: Управляйте своими средствами, пополняйте баланс и оплачивайте услуги.
-   Рефералы: Приглашайте друзей и знакомых, получая вознаграждение за их активность.
-   Чеки: Поделитесь деньгами с кем-либо, используя простую ссылку для передачи.
-   Мои боты: Уникальный функционал! Создайте копию этого бота с новым ID.

Присоединяйтесь к нам и делайте ваш аккаунт популярным!

## Основные инструменты

Бот разработан с использованием современных технологических решений, обеспечивающих высокую производительность и стабильность работы. Использование асинхронных библиотек позволяет боту быстро и эффективно обрабатывать большое количество запросов, адаптируясь к высоким требованиям современных пользователей.

-   [python 3](https://www.python.org/downloads/)
-   [aiohttp](https://docs.aiohttp.org/en/v3.8.6/web_advanced.html)
-   [aiogram](https://aiogram.dev/)
-   [sqlite](https://www.sqlite.org/index.html)

## С чего начать

Для успешной настройки и стабильной работы бота необходимо следовать нижеуказанным техническим требованиям:

-   Сервер:
    Хостинг: Рекомендуется использовать VPS или выделенный сервер для оптимальной производительности и надежности. Сервер должен иметь стабильное интернет-соединение и соответствующие ресурсы (CPU, RAM) в зависимости от ожидаемой нагрузки.
    Операционная система:
    Рекомендуются современные дистрибутивы Linux, такие как Ubuntu, CentOS или Debian. Однако большинство UNIX-подобных систем также подойдут.
    Программное обеспечение:
    Python 3: Убедитесь, что на сервере установлена последняя стабильная версия Python 3. Это основной язык программирования, на котором написан ваш бот.

-   pip: Система управления пакетами для Python. Необходима для установки необходимых библиотек и зависимостей.

-   Примечание:
    Перед началом настройки рекомендуется проверить все установленное программное обеспечение на актуальность версий и наличие всех необходимых зависимостей.

### Пререквизиты

Для автоматической установки всех необходимых библиотек, вы можете использовать файл requirements.txt с приведенным выше содержимым, выполнив команду:

```sh
pip install -r requirements.txt
```

Это обеспечит установку всех нужных зависимостей для надежной работы вашего бота.

### Установка

**Шаг 1**

1.  Настройка файла .env для вашего бота
    Для корректной работы вашего бота необходимо правильно настроить файл конфигурации .env. Для этого выполните следующие действия:

    -   1 Создайте копию файла .env.dist и переименуйте её в .env:

        ```sh
            cd /path_to_bot_directory
            mv .env.dist .env
        ```

    -   2 Откройте файл .env и отредактируйте его переменные.

        ```env
            BOT_URL=  # Url ведущий на сервер вашего бота
            HOST=127.0.0.1
            PORT=  # Порт, который будет задействован

            # Bot settings
            BOT_TOKEN=  # Токен, полученный у @BotFather
            ADMIN_ID=  # Telegram ID администратора бота
            MAIN_BOT_PATH=  # Путь для Webhook главного бота
            OTHER_BOTS_PATH=  # Путь для Webhook пользовательских ботов

            # Tegro shop (Активно)
            TEGRO_API_URL=https://tegro.money/pay/
            TEGRO_SHOP_ID=  # ShopID вашего магазина Tegro.money
            TEGRO_API_KEY=  # API ключ вашего магазина
            TEGRO_SECRET_KEY=  # Секретный ключ вашего магазина

            # Cryptopay (Активно)
            CRYPTO_TOKEN=  # Токен вашего магазина CryptoPay
            CRYPTO_TOKEN_TEST=  # Токен вашего магазина CryptoPay в сети Testnet

            # Ton wallet (В разработке)
            WPAY_STORE_API_KEY=  # Ключ вашего магазина Ton Wallet

            # Unitpay (В разработке)
            UNITPAY_API_URL=https://unitpay.ru/api
            UNITPAY_PROJECT_ID=  # ID вашего проекта UnitPay
            UNITPAY_SECRET_KEY=  # Секретный ключ вашего магазина

            # Cloudpayments (В разработке)
            CLOUDPAYMENTS_API_URL=https://api.cloudpayments.ru
            CLOUDPAYMENTS_PUBLIC_ID=  # Cloudpayments public id
            CLOUDPAYMENTS_SECRET_KEY=  # Cloudpayments secret key

            # SmoService
            SMOSERVICE_KEY=  # API ключ вашего аккаунта SmoService
            SMOSERVICE_USER_ID=  # User ID вашего аккаунта SmoService

            #SmmPanel
            SMMPANEL_KEY=  # SmmPanel api key

            # Scheduled tasks intervals
            CHECK_ORDER_STATUS_INTERVAL=120  # Интервал проверки заказов
            AUTO_STARTING_ORDERS_INTERVAL=60  # Интервал активации новых заказов

            # WebApp links
            HELP_URL=https://ros.media/faq  # Url для кнопки "Помощь"
            FAQ_URL=https://smoservice.media/faq.php  # Url для кнопки "FAQ"

            # Broadcast messages
            BROADCAST_MESSAGES_PER_SECOND=10  # Количество сообщений в минуту при рассылке

            DEBUG=0  # Включение Debug-режима.
        ```

    -   3. Сохраните и закройте файл .env.

**Шаг 2**

2.  Получение HTTPS сертификата через Certbot
    Для обеспечения безопасности соединения с вашим сервером рекомендуется использовать HTTPS сертификат. Чтобы его получить, следуйте указаниям ниже:

    -   2.1. Перейдите на официальный сайт Certbot по следующей ссылке: https://certbot.eff.org/

    -   2.2. На сайте выберите программное обеспечение (web-сервер) и систему, которые используются на вашем сервере.

    -   2.3. Следуйте предложенной инструкции на сайте для установки и настройки Certbot. Это обычно включает в себя несколько команд, которые необходимо выполнить в вашем терминале или командной строке.

    -   2.4. После успешной настройки и получения сертификата, Certbot выведет в консоли информацию о местоположении ключей сертификата.

    -   2.5. Запишите или сохраните следующие пути:
        Путь к вашему приватному ключу (обычно privkey.pem)
        Путь к полному цепочному сертификату (обычно fullchain.pem)

    -   2.6. Укажите сохраненные пути в вашем конфигурационном файле или там, где это требуется для настройки вашего сервера.

    🚫 Никогда не делитесь приватными ключами и убедитесь, что у них соответствующие права доступа, чтобы они были недоступны для всех, кроме необходимых служб и администратора.

**Шаг 3**
Настройка Nginx для работы с вашим ботом
Для того чтобы ваш Telegram бот мог корректно обрабатывать запросы, необходимо настроить web-сервер Nginx. Следуйте инструкциям ниже:

-   3.1. Установка и исходная настройка Nginx

    -   3.1.1. Установите Nginx:

        ```sh
        sudo apt-get install -y nginx
        ```

    -   3.1.2. Перейдите в каталог, где хранятся доступные конфигурации сайтов:

        ```sh
        cd /etc/nginx/sites-available/
        ```

    -   3.1.3. Создайте и откройте новый конфигурационный файл:

        ```sh
        sudo nano telegram_bot.conf
        ```

-   3.2. Конфигурация файла
    В появившемся редакторе, впишите следующую конфигурацию, заменив пути к сертификату и ключу на ранее сохраненные и изменив имя вашего сервера:

    ```nginx
    server {
        listen 80;
        listen 443 ssl;
        server_name "доменное имя вашего сервера";
        ssl_certificate "путь к сертификату";
        ssl_certificate_key "путь к ключу сертификата";
        location / {
            proxy_set_header Host $http_host;
            proxy_redirect off;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Scheme $scheme;
            proxy_pass http://localhost:8001/;
        }
    }
    ```

Сохраните и закройте файл.

-   3.3. Активация и перезапуск Nginx

    -   3.3.1. Перейдите в каталог с активными конфигурациями:

        ```sh
        cd /etc/nginx/sites-enabled/
        ```

-   3.3.2. Создайте символическую ссылку на ваш конфигурационный файл:

    ```sh
    sudo ln -s ../sites-available/telegram_bot.conf telegram_bot.conf
    ```

-   3.3.3. Перезапустите Nginx для применения изменений:

    ```sh
    sudo service nginx restart
    ```

**Шаг 4**
Для того чтобы ваш бот всегда был в рабочем состоянии и автоматически запускался после перезагрузки сервера или внезапных отключений, создайте сервис, используя systemd.

-   4.1. Создание конфигурационного файла сервиса

    -   4.1.1. Перейдите в каталог systemd, где хранятся конфигурационные файлы сервисов:

        ```sh
        cd /etc/systemd/system/
        ```

-   4.1.2. Создайте и откройте новый файл для вашего сервиса:

    ```sh
    vim tgbot.service
    ```

-   4.2. Конфигурация файла сервиса
    В появившемся редакторе, вставьте следующую конфигурацию, изменив путь и имя пользователя на свои:

    ```sh
    [Unit]
    Description=Telegram Bot Service

    [Service]
    WorkingDirectory='путь до рабочей директории'
    User='имя пользователя'
    ExecStart=/usr/bin/python3 main.py

    [Install]
    WantedBy=multi-user.target
    ```

-   4.3. Активация и запуск сервиса

    -   4.3.1. Для того чтобы активировать и автоматически запускать сервис при загрузке системы, используйте следующую команду:

    ```sh
    sudo systemctl enable tgbot.service
    ```

-   4.3.2. Чтобы запустить вашего бота прямо сейчас с помощью созданного сервиса, используйте:

    ```sh
    sudo systemctl start tgbot.service
    ```

Проверьте статус вашего бота с помощью команды:

```sh
sudo systemctl status tgbot.service
```

Это позволит вам удостовериться, что ваш бот успешно запущен и работает корректно.

## Предложения и известные баги

Список предлагаемых функций (и известных проблем) см. в разделе ["Открытые вопросы"](https://github.com/TegroTON/SMMPanel-SMOService-Telegram-Bot/issues).

## Авторы

-   [**m1ja**](https://github.com/m1ja) - _python developer_ - _Разработка telegram_
-   [**Kopeikin Dmitrii**](https://github.com/Dmitrii-Kopeikin) - _Python, Js developer_

## Благодарности

-   [ShaanCoding](https://github.com/ShaanCoding/)
-   [Othneil Drew](https://github.com/othneildrew/Best-README-Template)
-   [ImgShields](https://shields.io/)
