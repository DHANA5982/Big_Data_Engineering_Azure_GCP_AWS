## TYPES OF CONSTRAINTS 

/*  PRIMARY KEY
	FOREIGN KEY
    UNIQUE
    NOT NULL
    CHECK
    DEFAULT
    INDEX
    CANDIDATE KEY
*/

USE LibraryDB;

CREATE TABLE Authors(
	AuthorID INT PRIMARY KEY,
	FirstName VARCHAR(25),
    LastName VARCHAR(25),
    Email VARCHAR(25)
);

INSERT INTO Authors VALUES
(1, 'JK', 'ROWLLING', 'jk.row@gmail.com'), 
(2, 'APJ', 'Abdul Kalam', 'apj.kalam@gmail.com');

SELECT * FROM Authors;

DESC Authors;

CREATE TABLE Books(
	BookID INT PRIMARY KEY,
    Title VARCHAR(25) NOT NULL,
    AuthorID INT,
    PublicationYear INT CHECK (PublicationYear > 0),
	FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID)
);

DESC Books;

INSERT INTO Books VALUES
(1, 'Harry Potter', 1, 1998),
(2, 'Wings of Fire', 2, 2000),
(3, 'Prince of Persia', NULL, 2001);

SELECT * FROM Books;

CREATE TABLE Student(
	StudentID INT NOT NULL,
    FirstName VARCHAR(25),
    LastName VARCHAR(25) NOT NULL,
    Age INT
);

ALTER TABLE Student
MODIFY Age INT NOT NULL;

ALTER TABLE Student
MODIFY StudentID INT NOT NULL PRIMARY KEY AUTO_INCREMENT;

SELECT * FROM Student;
DESC Student;

CREATE TABLE Singers(
	PersonID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(25) NOT NULL,
    LastName VARCHAR(25) UNIQUE,
    Age INT NOT NULL
);

INSERT INTO Singers(FirstName, LastName, Age) VALUES
('Ariana', 'Grande', 30),
('Du', 'Lipa', 32),
('Sabrina', 'Carpenter', 33),
('Taylor', 'Swift', 40),
('Dharia', Null, 28),
('Babe', 'Rexa', 41);

SELECT * FROM Singers;
DESC Singers;