CREATE DATABASE StudentDB;
USE StudentDB;

CREATE TABLE Students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    hobby VARCHAR(100),
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    birth_year INT,
    homework_score INT
);
INSERT INTO Students (hobby, first_name, last_name, birth_year, homework_score) VALUES
('reading', 'Ivan', 'Petrov', 2000, 15),
('sports', 'Anna', 'Sidorova', 1999, 8),
('music', 'Dmitry', 'Ivanov', 2001, 12),
('traveling', 'Olga', 'Kuznetsova', 1998, 20),
('painting', 'Alex', 'Smirnov', 1997, 5),
('cooking', 'Maria', 'Volkova', 2002, 14),
('dancing', 'Nikita', 'Petrova', 2000, 9),
('gaming', 'Elena', 'Andreeva', 1996, 22),
('hiking', 'Sergey', 'Mikhailov', 2001, 11),
('fishing', 'Victoria', 'Lobanova', 1995, 7);
SELECT * FROM Students WHERE LENGTH(last_name) > 10;
UPDATE Students SET first_name = 'genius' WHERE homework_score > 10;
SELECT * FROM Students WHERE first_name = 'genius';
DELETE FROM Students WHERE id % 2 = 0;
