-- resets the attribute valid_email only when the email has been changed.

DROP TRIGGER IF EXISTS reset_valid_email;
CREATE TRIGGER reset_valid_email
BEFORE INSERT ON users
FOR EACH ROW
UPDATE users SET email = users.valid_email
WHERE email NOT LIKE valid_email;
