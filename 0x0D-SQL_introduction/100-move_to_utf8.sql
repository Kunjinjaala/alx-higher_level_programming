-- A a script that converts hbtn_0c_0 database to UTF8

-- Convert database to utf8
ALTER DATABASE hbtn_0c_0 utf8mb4 CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

--
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table MODIFY name VARCHAR CHARACTER SET
utf8mb4 COLLATE utf8mb4_unicode_ci;
