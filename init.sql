-- init.sql
USE e-commerce;

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    description TEXT,
    stock INT NOT NULL
);

INSERT INTO products (name, price, description, stock) VALUES
    ('Laptop', 1200.0, 'Powerful laptop with high-performance features', 50),
    ('Smartphone', 600.0, 'Latest smartphone with advanced technology', 100),
    ('Headphones', 100.0, 'High-quality over-ear headphones', 200),
    ('Camera', 800.0, 'Professional-grade digital camera', 30);
