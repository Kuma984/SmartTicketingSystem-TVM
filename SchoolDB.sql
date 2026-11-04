-- =========================================================================
-- SE Lab 7: School Management Database (SchoolDB) - Database First Approach
-- Student: 524K0021 - Trinh Duc Long
-- Instructor: Ky-Trung Pham (FIT - TDTU)
-- =========================================================================

IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'SchoolDB')
BEGIN
    CREATE DATABASE SchoolDB;
END
GO

USE SchoolDB;
GO

-- 1. Table: Departments
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Departments')
BEGIN
    CREATE TABLE Departments (
        DepartmentID INT PRIMARY KEY IDENTITY(1,1),
        Name NVARCHAR(50) NOT NULL,
        Budget DECIMAL(18, 2) NOT NULL,
        StartDate DATE NOT NULL
    );
END
GO

-- 2. Table: Instructors
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Instructors')
BEGIN
    CREATE TABLE Instructors (
        InstructorID INT PRIMARY KEY IDENTITY(1,1),
        FirstName NVARCHAR(50) NOT NULL,
        LastName NVARCHAR(50) NOT NULL,
        HireDate DATE NOT NULL
    );
END
GO

-- 3. Table: Courses
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Courses')
BEGIN
    CREATE TABLE Courses (
        CourseID INT PRIMARY KEY IDENTITY(1,1),
        Title NVARCHAR(100) NOT NULL,
        Credits INT NOT NULL,
        DepartmentID INT FOREIGN KEY REFERENCES Departments(DepartmentID)
    );
END
GO

-- 4. Table: Students
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Students')
BEGIN
    CREATE TABLE Students (
        StudentID INT PRIMARY KEY IDENTITY(1,1),
        FirstName NVARCHAR(50) NOT NULL,
        LastName NVARCHAR(50) NOT NULL,
        EnrollmentDate DATE NOT NULL
    );
END
GO

-- 5. Table: Enrollments
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Enrollments')
BEGIN
    CREATE TABLE Enrollments (
        EnrollmentID INT PRIMARY KEY IDENTITY(1,1),
        CourseID INT FOREIGN KEY REFERENCES Courses(CourseID),
        StudentID INT FOREIGN KEY REFERENCES Students(StudentID),
        Grade DECIMAL(3, 2)
    );
END
GO

-- Seed Sample Data as required by Lab 7
IF NOT EXISTS (SELECT * FROM Departments)
BEGIN
    INSERT INTO Departments (Name, Budget, StartDate) VALUES 
    ('Computer Science', 120000.00, '2023-01-01'),
    ('Software Engineering', 150000.00, '2023-01-01'),
    ('Information Technology', 110000.00, '2023-01-01');
END
GO

IF NOT EXISTS (SELECT * FROM Instructors)
BEGIN
    INSERT INTO Instructors (FirstName, LastName, HireDate) VALUES 
    ('John', 'Doe', '2020-08-15'),
    ('Ky-Trung', 'Pham', '2018-09-01'),
    ('Sarah', 'Connor', '2021-03-10');
END
GO

IF NOT EXISTS (SELECT * FROM Courses)
BEGIN
    INSERT INTO Courses (Title, Credits, DepartmentID) VALUES 
    ('Introduction to Programming', 3, 1),
    ('Object Oriented Software Engineering', 4, 2),
    ('Database Management Systems', 3, 1),
    ('Web Application Development', 3, 3);
END
GO

IF NOT EXISTS (SELECT * FROM Students)
BEGIN
    INSERT INTO Students (FirstName, LastName, EnrollmentDate) VALUES 
    ('Jane', 'Smith', '2023-09-01'),
    ('Duc Long', 'Trinh', '2024-09-01'),
    ('My Duyen', 'Vo', '2023-09-01'),
    ('Hoang Anh', 'Tran', '2024-09-01');
END
GO

IF NOT EXISTS (SELECT * FROM Enrollments)
BEGIN
    INSERT INTO Enrollments (CourseID, StudentID, Grade) VALUES 
    (1, 1, 3.50),
    (2, 2, 3.90),
    (3, 3, 3.75),
    (4, 4, 3.80),
    (1, 2, 4.00);
END
GO

-- Verify tables and counts
SELECT 'Departments' AS [Table], COUNT(*) AS [Count] FROM Departments
UNION ALL
SELECT 'Instructors', COUNT(*) FROM Instructors
UNION ALL
SELECT 'Courses', COUNT(*) FROM Courses
UNION ALL
SELECT 'Students', COUNT(*) FROM Students
UNION ALL
SELECT 'Enrollments', COUNT(*) FROM Enrollments;
GO
