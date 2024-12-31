DELETE FROM users
WHERE username = 'jane_smith';

DELETE FROM customers
WHERE user_username = 'john_doe';

DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS users;

DROP DATABASE IF EXISTS real_estate_users_db;