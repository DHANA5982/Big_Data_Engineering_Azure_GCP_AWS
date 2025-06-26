CREATE DATABASE CompanyDB;

USE CompanyDB;

CREATE TABLE Employees(
	EmpID INT, 
    EmpName VARCHAR(20),
    EmpDepartment VARCHAR(20),
    EmpSalary INT,
    EmpJoinDate DATE
);

CREATE TABLE Departments(
	DepID INT, 
    DepName VARCHAR(20),
    DepHeadName VARCHAR(20),
    DepStaffCount INT
);

INSERT INTO Employees VALUES
(01, 'Dhanasekar', 'Data Science', '5000000', '2025-07-01'),
(02, 'Balaji', 'Designing', '4000000', '2024-06-01'),
(03, 'Akil', 'Designing', '3000000', '2019-06-01');

INSERT INTO Departments VALUES
(01, 'Analysis', 'Dhanasekar', 10),
(02, 'SMD Design', 'Balaji', 15),
(03, 'Valve Design', 'Akil', 20);

SELECT * FROM Employees;
SELECT * FROM Departments;