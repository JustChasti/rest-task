"""     Настройки
headers - заголовки
url - сервер flask
base name pass user - настройки подключения к postgres
type_server - тип сервера 'http://' или 'https://' с которого идут запросы и на который api отправляет потом ответы
"""


headers = {'Content-type': 'application/json', 'Accept': 'text/plain', 'Content-Encoding': 'utf-8'}
type_server = 'http://'
url = 'http://127.0.0.1:5000/'
base_name = "test1"
base_pass = "qm7hFSIW"
base_user = "postgres"
