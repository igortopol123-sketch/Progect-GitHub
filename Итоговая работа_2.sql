--
-- Файл сгенерирован с помощью SQLiteStudio v3.4.17 в Вс ноя 23 11:05:14 2025
--
-- Использованная кодировка текста: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Таблица: authors
CREATE TABLE IF NOT EXISTS authors (
  author_id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  birth_year INTEGER
);
INSERT INTO authors (author_id, name, birth_year) VALUES (NULL, 'Ãàëèíà Ðîìàíîâà', 1985);
INSERT INTO authors (author_id, name, birth_year) VALUES (NULL, 'Àíòîí Ëàçàðåâ', 1979);
INSERT INTO authors (author_id, name, birth_year) VALUES (NULL, 'Ìàðèÿ Êóçíåöîâà', 1990);
INSERT INTO authors (author_id, name, birth_year) VALUES (NULL, 'Èãîðü Ñîêîëîâ', 1988);
INSERT INTO authors (author_id, name, birth_year) VALUES (NULL, 'Åêàòåðèíà Íîâèêîâà', 1983);
INSERT INTO authors (author_id, name, birth_year) VALUES (NULL, 'Äàíèèë Âîëêîâ', 1992);
INSERT INTO authors (author_id, name, birth_year) VALUES (NULL, 'Îëüãà Ìîðîçîâà', 1987);
INSERT INTO authors (author_id, name, birth_year) VALUES (NULL, 'Ñåðãåé Ïåòðîâ', 1984);
INSERT INTO authors (author_id, name, birth_year) VALUES (NULL, 'Àëåêñàíäð Áåëîâ', 1991);
INSERT INTO authors (author_id, name, birth_year) VALUES (NULL, 'Åëåíà Êèñåëåâà', 1986);

-- Таблица: books
CREATE TABLE IF NOT EXISTS books (
  book_id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  genre TEXT,
  published_year INTEGER,
  author_id INTEGER NOT NULL,
  FOREIGN KEY (author_id) REFERENCES authors(author_id)
);
INSERT INTO books (book_id, title, genre, published_year, author_id) VALUES (1, 'Òåíè ãîðîäà', 'Ñîâðåìåííàÿ ïðîçà', 2018, 1);
INSERT INTO books (book_id, title, genre, published_year, author_id) VALUES (2, 'Ïèñüìà áåç îòâåòà', 'Äðàìà', 2020, 2);
INSERT INTO books (book_id, title, genre, published_year, author_id) VALUES (3, 'Ãðàíèöà âåòðà', 'Ôýíòåçè', 2019, 3);
INSERT INTO books (book_id, title, genre, published_year, author_id) VALUES (4, 'Ìãíîâåíèå â ìåòðî', 'Ëèò. òðèëëåð', 2021, 4);
INSERT INTO books (book_id, title, genre, published_year, author_id) VALUES (5, 'Çèìíèé çâîíîê', 'Êðèìè/ìèñòèêà', 2022, 5);
INSERT INTO books (book_id, title, genre, published_year, author_id) VALUES (6, 'Ñâåò çà ãðàíüþ', 'Íàó÷íàÿ ôàíòàñòèêà', 2017, 6);
INSERT INTO books (book_id, title, genre, published_year, author_id) VALUES (7, 'Ãîðîä áåç ñíîâ', 'Ñîâðåìåííàÿ ïðîçà', 2020, 7);
INSERT INTO books (book_id, title, genre, published_year, author_id) VALUES (8, 'Ïàâëèíüè ãëàçà', 'Ñáîðíèê ðàññêàçîâ', 2023, 8);
INSERT INTO books (book_id, title, genre, published_year, author_id) VALUES (9, 'Ñåðûé ãîðîä, ñèíèé äîæäü', 'Ïñèõîëîãè÷åñêèé ðîìàí', 2021, 9);
INSERT INTO books (book_id, title, genre, published_year, author_id) VALUES (10, 'Êîä òèøèíû', 'Äåòåêòèâ', 2024, 10);

-- Запрос: поиск всех книг автора Галина Романова
SELECT b.book_id, b.title, b.published_year, b.genre
FROM books b
JOIN authors a ON b.author_id = a.author_id
WHERE a.name = 'Галина Романова';

-- Запрос: Подсчёт количества книг на каждого автора
SELECT a.name AS author, COUNT(*) AS book_count
FROM authors a
LEFT JOIN books b ON b.author_id = a.author_id
GROUP BY a.author_id, a.name
ORDER BY book_count DESC;

-- Запрос: Поиск книг, название которых начинается с определенной буквы
SELECT title, published_year
FROM books
WHERE title LIKE 'Ï%'
ORDER BY title;

-- Запрос: Сортировка книг по году издания от новых к старым
SELECT *
FROM books
ORDER BY published_year DESC;




sf tableName => SELECT columns FROM tableName

sc tableName => SELECT count(*) FROM tableName

sl tableName => SELECT * FROM tableName ORDER BY key DESC LIMIT 100;

ct => CREATE TABLE

ii tableName => INSERT INTO

us tableName => UPDATE SET

uw tableName => UPDATE SET WHERE

df tableName => DELETE FROM

dw tableName => DELETE FROM WHERE');
INSERT INTO demo (ID, Name, Hint) VALUES (11, 'SQLite 3.50.4', 'SQL OnLine on JavaScript');
INSERT INTO demo (ID, Name, Hint) VALUES (12, '[RightClick] mouse', 'Opens many additional features');
INSERT INTO demo (ID, Name, Hint) VALUES (13, 'Left-Panel, Table', '[RightClick] mouse "Context menu"');
INSERT INTO demo (ID, Name, Hint) VALUES (14, 'Tabs', 'mouse: [RightClick] , [MiddleClick] , [Wheel] , [LeftClick]');
INSERT INTO demo (ID, Name, Hint) VALUES (15, 'SQL Editor', 'autocomplete: [Ctrl-Space] or [Alt-Space]; run: [Shift-Enter]');
INSERT INTO demo (ID, Name, Hint) VALUES (16, 'Size table', 'Fast scroll million rows');
INSERT INTO demo (ID, Name, Hint) VALUES (17, 'Share', 'Create public link DB');
INSERT INTO demo (ID, Name, Hint) VALUES (18, '21', 'Number of color themes');
INSERT INTO demo (ID, Name, Hint) VALUES (19, 'ai.Url', 'https://sqliteonline.com/LICENSE');
INSERT INTO demo (ID, Name, Hint) VALUES (20, 'ai.Color', '#9393ad');
INSERT INTO demo (ID, Name, Hint) VALUES (21, 'ai.Image', 'Blob - png, jpg, gif or String(base64) [DbClick] row');
INSERT INTO demo (ID, Name, Hint) VALUES (22, 'SQL', 'Syntax example library');
INSERT INTO demo (ID, Name, Hint) VALUES (23, 'CREATE', 'CREATE TABLE table_name (col1, col2)');
INSERT INTO demo (ID, Name, Hint) VALUES (24, 'SELECT', 'SELECT * FROM table_name');
INSERT INTO demo (ID, Name, Hint) VALUES (25, 'INSERT', 'INSERT INTO table_name (col1, col2) VALUES ("example","test")');
INSERT INTO demo (ID, Name, Hint) VALUES (26, 'UPDATE', 'UPDATE table_name SET col1="work" WHERE col2="test"');
INSERT INTO demo (ID, Name, Hint) VALUES (27, 'DELETE', 'DELETE FROM table_name');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;

