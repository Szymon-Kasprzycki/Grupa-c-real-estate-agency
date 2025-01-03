UPDATE users
SET password_hash = 'new_secure_password_hash'
WHERE username = 'john_doe';

UPDATE customers
SET 
    first_name = 'Jonathan',
    last_name = 'Doe',
    email = 'updated_john@example.com',
    phone_number = '111222333',
    address = 'Updated Address St, Apt 42',
    preferences = '{"prefers_email": false, "prefers_sms": true}',
    updated_at = NOW()
WHERE id = 1;
