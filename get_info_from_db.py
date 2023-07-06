def get_info(request):
    import utils
    from keys import DB_CONFIGS

    db = utils.DBManager(*DB_CONFIGS)  # параметры для подключения к БД
    db.connect()  # подключение к БД

    if (request == '1'):
        print(*db.get_companies_and_vacancies_count(), '\n')
    if (request == '2'):
        print(*db.get_all_vacancies(), '\n')
    if (request == '3'):
        print(*db.get_avg_salary(), '\n')
    if (request == '4'):
        print(*db.get_vacancies_with_higher_salary(), '\n')
    if (request == '5'):
        print(*db.get_vacancies_with_keyword(input('Введите ключевое слово для поиска: ')), '\n')

    db.disconnect()  # отключение соединений
