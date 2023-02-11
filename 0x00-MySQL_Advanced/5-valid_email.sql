-- SQL script that creates a trigger.
DELIMITER //
CREATE TRIGGER email_validate_trigger BEFORE UPDATE on users
FOR EACH ROW
BEGIN
IF NEW.email <> OLD.email
THEN
SET NEW.valid_email = 0;
END IF;
END;
//