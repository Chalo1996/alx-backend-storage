-- Creates a table users if it does not already exist

CREATE TABLE IF NOT EXISTS users (
 id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
 email VARCHAR(255) NOT NULL UNIQUE,
 name VARCHAR(255),
 country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
