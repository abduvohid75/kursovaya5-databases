import psycopg2


class DBManager:  # класс для взаимодействия с БД
    def __init__(self, host, dbname, user, password):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password

        self.conn = None
        self.cur = None

    def connect(self):  # подключение к бд
        try:
            self.conn = psycopg2.connect(host=self.host, dbname=self.dbname, user=self.user, password=self.password)
            self.cur = self.conn.cursor()  # здесь создается курсор

        except psycopg2.Error as e:
            print("Ошибка при работе с БД", e)

    def disconnect(self):  # отключение соединений
        self.conn.close()

    def add_to_db(self, id, vacancy, url, company_name, salary):  # функция добавления вакансий в БД
        try:
            self.cur.execute('INSERT INTO vacancies VALUES(%s, %s, %s, %s, %s)',
                             (id, vacancy, url, company_name, salary))  # sql-запрос
            self.conn.commit()  # коммит изменений

        except psycopg2.Error as e:
            print("Ошибка при работе с БД", e)

    def get_companies_and_vacancies_count(self):  # функция возвращает список всех компаний и кол-во их ваканский
        try:
            self.cur.execute('SELECT company_name, COUNT(vacancy) FROM vacancies GROUP BY company_name')  # sql-запрос
            fetch = self.cur.fetchall()  # вывод

            return fetch

        except psycopg2.Error as e:
            print("Ошибка при работе с БД", e)

    def get_all_vacancies(
            self):  # функция возвращает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию
        try:
            self.cur.execute('SELECT company_name, vacancy, salary_start, url FROM vacancies')  # sql-запрос
            fetch = self.cur.fetchall()  # вывод

            return fetch

        except psycopg2.Error as e:
            print("Ошибка при работе с БД", e)

    def get_avg_salary(self):  # получение среднего значения начальной зп
        try:
            self.cur.execute('SELECT AVG(salary_start) FROM vacancies')  # sql-запрос
            fetch = self.cur.fetchall()  # вывод

            return fetch

        except psycopg2.Error as e:
            print("Ошибка при работе с БД", e)

    def get_vacancies_with_higher_salary(self):  # получение начальной зп выше среднего
        try:
            self.cur.execute(
                'SELECT vacancy, company_name, salary_start FROM vacancies WHERE salary_start > (SELECT AVG(salary_start) FROM vacancies)')  # sql-запрос
            fetch = self.cur.fetchall()  # вывод

            return fetch

        except psycopg2.Error as e:
            print("Ошибка при работе с БД", e)

    def get_vacancies_with_keyword(self, keyword):  # получение значений с ключевым словом
        try:
            self.cur.execute(f"SELECT * FROM vacancies WHERE vacancy LIKE '%{keyword}%'")  # sql-запрос
            fetch = self.cur.fetchall()  # вывод

            return fetch

        except psycopg2 as e:
            print("Ошибка при работе с БД", e)
