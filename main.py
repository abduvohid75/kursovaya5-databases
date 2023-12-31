import add_companies_to_db
import get_info_from_db

while True:
    message = input(
        '\n1. Добавить вакансии компании в БД\n2. Взаимодействие с БД\n\nДля продолжения введите 1 или 2, либо stop для остановки\n\n')
    if message == '1':
        add_companies_to_db.add_companies()
    elif message == '2':
        request = input(
            '\n1. Получить список всех компаний и количество вакансий у каждой компании.\n2. Получить список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.\n3.Получить среднюю зарплату по вакансиям.\n4.Получить список всех вакансий, у которых зарплата выше средней по всем вакансиям.\n5.Получить список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”.\n\n')
        get_info_from_db.get_info(request)
    elif message.lower() == 'stop':
        break
