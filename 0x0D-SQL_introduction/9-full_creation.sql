-- Script to create second table without error and set id as an integer variable, name as character variable, and score as int
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);

-- Script to create 4 records
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (1, "John", 10);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (2, "Alex", 3);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (3, "Bob", 14);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (4, "George", 8);
