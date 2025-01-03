CREATE DATABASE real_estate_users_db;
USE real_estate_users_db;

CREATE TABLE users (
    username VARCHAR(150) PRIMARY KEY,
    password_hash VARCHAR(255) NOT NULL,
    creation_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_update_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE customers (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    user_username VARCHAR(150) NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    gender ENUM('Male', 'Female', 'Other') DEFAULT 'Other',
    email VARCHAR(254) NOT NULL UNIQUE,
    phone_number CHAR(9) NOT NULL UNIQUE,
    address TEXT,
    preferences JSON,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT fk_customers_user_username FOREIGN KEY (user_username) REFERENCES users (username) ON DELETE CASCADE
);