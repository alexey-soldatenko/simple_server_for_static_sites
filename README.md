# simple_server_for_static_sites
Проект представляет собой простейший сервер для статических сайтов. Выполнен при использовании python3 и сопутствующих библиотек(socket, os, sys и др.)
Работает по протоколу HTTP.

Сервер обрабатывает входящий запрос, проверяет соответствует ли путь в запросе существующим url (см. settings/urls), а также если запрашивается файл, существует ли он в static.
Далее заполняются заголовки и читается запрошенный файл, который является телом сообщения сервера. После чего выполняется отправка ответа.

Запуск сервера осуществляется запуском файла start_server.py (как из терминала python3 start_server.py, так и из вашего ide).
