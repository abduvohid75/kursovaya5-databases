CREATE TABLE vacancies
(
    id int PRIMARY KEY,
    vacancy text NOT NULL,
    url text NOT NULL,
    company_name varchar(100) NOT NULL,
    salary_start int
);