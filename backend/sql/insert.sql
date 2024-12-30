INSERT INTO users (username, password_hash, creation_date, last_update_date)
VALUES ('john_doe', 'hashed_password_1', NOW(), NOW()),
       ('jane_smith', 'hashed_password_2', NOW(), NOW());

INSERT INTO customers (user_username, first_name, last_name, gender, email, phone_number, address, preferences, created_at, updated_at)
VALUES ('john_doe', 'John', 'Doe', 'Male', 'john@example.com', '123456789', '123 Elm St', '{"prefers_email": true}', NOW(), NOW()),
       ('jane_smith', 'Jane', 'Smith', 'Female', 'jane@example.com', '987654321', '456 Oak St', '{"prefers_sms": true}', NOW(), NOW());

