## DATA MUNIPULATION

USE CompanyDB;

CREATE TABLE CustomerInfo(
	CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(25),
    LastName VARCHAR(25),
    Salary INT
);

INSERT INTO CustomerInfo(FirstName, LastName, Salary) VALUES 
('Alex', 'Sins', 100000), 
('Bob', 'Merley', 150000),
('Evans', 'George', 120000),
('Bright', 'Will', 90000),
('Luke', 'Sinclaire', 123000),
('Chris', 'Tele', NULL);

SELECT * FROM CustomerInfo;

SELECT FirstName, LastName 
FROM CustomerInfo
WHERE Salary IS NULL;

UPDATE CustomerInfo
SET Salary = 80000
WHERE Salary IS NULL;

DELETE FROM CustomerInfo
WHERE CustomerID = 1;

ALTER TABLE CustomerInfo
ADD COLUMN Education VARCHAR(25),
ADD COLUMN Married VARCHAR(25),
ADD COLUMN Children INT;


## SCHEMA OF THE TABLE

DESC CustomerInfo;

ALTER TABLE CustomerInfo
DROP COLUMN Children;