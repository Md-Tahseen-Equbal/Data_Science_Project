CREATE DATABASE IF NOT EXISTS Grocery_store;
USE Grocery_store;

CREATE TABLE IF NOT EXISTS supplier (
    sup_id TINYINT PRIMARY KEY,
    sup_name VARCHAR(255),
    address TEXT
);

CREATE TABLE IF NOT EXISTS categories (
    cat_id TINYINT PRIMARY KEY,
    cat_name VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS employees (
    emp_id TINYINT PRIMARY KEY,
    emp_name VARCHAR(255),
    hire_date VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS customers (
    cust_id SMALLINT PRIMARY KEY,
    cust_name VARCHAR(255),
    address TEXT
);


CREATE TABLE IF NOT EXISTS products (
    prod_id TINYINT PRIMARY KEY,
    prod_name VARCHAR(255),
    sup_id TINYINT,
    cat_id TINYINT,
    price DECIMAL(10,2),
    FOREIGN KEY (sup_id) REFERENCES supplier(sup_id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (cat_id) REFERENCES categories(cat_id) ON UPDATE CASCADE ON DELETE CASCADE
);



CREATE TABLE IF NOT EXISTS orders (
    ord_id SMALLINT PRIMARY KEY,
    cust_id SMALLINT,
    emp_id TINYINT,
    order_date VARCHAR(255),
    FOREIGN KEY (cust_id) REFERENCES customers(cust_id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS order_details (
    ord_detID SMALLINT AUTO_INCREMENT PRIMARY KEY,
    ord_id SMALLINT,
    prod_id TINYINT,
    quantity TINYINT,
    each_price DECIMAL(10,2),
    total_price DECIMAL(10,2),
    FOREIGN KEY (ord_id) REFERENCES orders(ord_id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (prod_id) REFERENCES products(prod_id) ON UPDATE CASCADE ON DELETE CASCADE
);
