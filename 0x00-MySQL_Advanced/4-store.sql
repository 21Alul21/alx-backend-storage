--SQL script that shows and adds orders with trigger in action
SELECT * FROM items;
SELECT * FROM orders;

INSERT INTO orders (item_name, number) VALUES ('apple', 1);
INSERT INTO orders (item_name, number) VALUES ('apple', 3);
INSERT INTO orders (item_name, number) VALUES ('apple', 2);

SELECT "--"

SELECT * FROM items;
SELECT * FROM orders; 
