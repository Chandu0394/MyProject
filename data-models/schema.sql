CREATE TABLE Customer (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(255),
    country VARCHAR(100),
    city VARCHAR(100)
);

CREATE TABLE Product (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(255),
    product_category VARCHAR(100),
    price DECIMAL(10, 2),
    ecommerce_website_name VARCHAR(255)
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    qty INT,
    datetime DATETIME,
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
    FOREIGN KEY (product_id) REFERENCES Product(product_id)
);

CREATE TABLE Payment (
    payment_txn_id VARCHAR(255) PRIMARY KEY,
    order_id INT,
    payment_type VARCHAR(50),
    payment_txn_success CHAR(1),
    failure_reason VARCHAR(255),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
);
