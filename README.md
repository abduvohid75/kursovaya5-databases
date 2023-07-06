# Курсовая 5. Работа с базами данных

## Как запустить
1. В первую очередь необходимо ввести данные своей базы данных в **keys.py**. 

2. После, в своей СУБД выполнить запрос из **queries.sql**.

3. После всех выполненных манипуляций можно смело запускать **main.py**.

## Примечание
В файле **add_companies_to_db.py** выполняются все операции для добавления вакансий и компаний в БД.

Файл **get_info_from_db.py** предназначен для получения данных из БД.

В файле **keys.py** хранится ключ, необходимый для соединения с БД.

В **utils.py** содержится класс DBManager, в котором хранятся все функции для взаимодействия С БД.

И наконец, **main.py** запускает сам проект и служит подобием интерфейса для пользователя.



В условиях курсовой работы указано, что таблица также должна включать в себя столбец зарплаты. При этом не уточнялось какую - начальную, среднюю или максимальную, или же всё сразу.

Поэтому было принято решение брать **только начальную зп**.