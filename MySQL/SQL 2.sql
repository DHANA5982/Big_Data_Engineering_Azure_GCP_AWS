## CREATE DATABASE, TABLE

CREATE DATABASE SchoolDB;

USE SchoolDB;

CREATE TABLE Students(
	StudentID INT, 
    FirstName VARCHAR(20),
    LastName VARCHAR(20),
    EmailID VARCHAR(30),
    EnrollmentDate DATE
);

CREATE TABLE Course(
	CourseID INT, 
    CourseName VARCHAR(20),
    Department VARCHAR(20), 
    Credits INT
);


## INSERT DATA INTO TABLES

INSERT INTO Students VALUES
(01, 'Dhanasekar', 'Govindaraj', 'd.g@srcas.ac.in', '2016-05-28'),
(02, 'Balaji', 'Mohan', 'b.m@srcas.ac.in', '2016-05-05'),
(03, 'Akil', 'Kumar', 'a.k@srcas.ac.in', '2016-05-06');

INSERT INTO Course VALUES
(01, 'Statistics', 'Mathematics', 60),
(02, 'Python', 'Computer-Science', 60),
(03, 'Power Electronics', 'Electronics', 60);

SELECT * FROM Students;
SELECT * FROM Course;
SHOW TABLES;

DROP TABLE Students;
DROP TABLE Course;
DROP DATABASE SchoolDB;
