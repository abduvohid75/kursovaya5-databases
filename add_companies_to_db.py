def add_companies():
    try:
        import requests
        import utils
        from keys import DB_CONFIGS

        class HHAPI:  # класс для api
            BASE_URL = 'https://api.hh.ru/'

            def __init__(self):
                self.session = requests.Session()

            def search_employers(self, text):  # функция берет информацию о работодателе
                url = self.BASE_URL + 'employers'
                params = {'text': text}
                response = self.session.get(url, params=params)
                response.raise_for_status()

                # отфильтровать результаты, проверяя название каждого работодателя
                items = [item for item in response.json()['items'] if item['name'].lower() == text.lower()]
                return items

            def search_vacancies_by_employer(self, employer_id):  # поиск ваканский от работодателя
                url = self.BASE_URL + 'vacancies'
                params = {'employer_id': employer_id}
                response = self.session.get(url, params=params)
                response.raise_for_status()
                return response.json()['items']

        api = HHAPI()
        db = utils.DBManager(*DB_CONFIGS)  # параметры для подключения к БД
        db.connect()  # подключение к БД

        employers = api.search_employers(input('\nВведите имя компании: '))

        print(f'Инфорамция о компании: {employers}' if employers else 'Нет компаний с таким названием')

        for employer in employers:
            employer_name = employer['name']
            print(f"Вакансии от {employer_name}:")
            employer_vacancies = api.search_vacancies_by_employer(employer['id'])
            for vacancy in employer_vacancies:  # проходимся по вакансиям компании
                vacancy_name = vacancy['name']  # имя вакансии
                vacancy_id = vacancy['id']  # уникальный id
                vacancy_url = vacancy['apply_alternate_url']  # ссылка на вакансию
                vacancy_salary = vacancy['salary']  # зп

                if vacancy_salary:
                    vacancy_salary = vacancy['salary'][
                        'from']  # некоторые работодатели не указывают начальную зп, пришлось придумывать костыли

                db.add_to_db(vacancy_id, vacancy_name, vacancy_url, employer_name, vacancy_salary)

                print(f'Вакансия {vacancy_name} успешно добавлена в БД')

        db.disconnect()  # отключение соединений
    except Exception as e:
        print('Ошибка: ', e)  # обработка ошибок

    # 10 выбранных компаний: Сбер банк, Yandex, Лента, Just Clothes, Лукойл, Мегафон, Газпром нефть, Концерн ВКО Алмаз - Антей, Госкорпорация Росатом, Почта России
