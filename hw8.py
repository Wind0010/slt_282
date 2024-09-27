
sqlite3 person.db


CREATE TABLE Departments (
    DepartmentID INTEGER PRIMARY KEY,
    DepartmentName TEXT NOT NULL
);


CREATE TABLE Employees (
    EmployeeID INTEGER PRIMARY KEY,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    DepartmentID INTEGER,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);
INSERT INTO Departments (DepartmentID, DepartmentName) VALUES
(101, 'HR'),
(102, 'IT'),
(103, 'Sales');
INSERT INTO Employees (EmployeeID, FirstName, LastName, DepartmentID) VALUES
(1, 'Beka', 'Bekovich', 101),
(2, 'Aimir', 'Baltabaev', 101),
(3, 'beka', 'bekabekov', 102),
(4, 'Sasha', 'Belii', 102),
(5, 'beka', 'krutoi', 103),
(6, 'Arsen', 'Doter', 103);




SELECT 
    Employees.EmployeeID, 
    Employees.FirstName, 
    Employees.LastName 
FROM 
    Employees 
JOIN 
    Departments ON Employees.DepartmentID = Departments.DepartmentID 
WHERE 
    Departments.DepartmentName = 'IT';



SELECT 
    Employees.EmployeeID, 
    Employees.FirstName, 
    Employees.LastName, 
    Departments.DepartmentName 
FROM 
    Employees 
JOIN 
    Departments ON Employees.DepartmentID = Departments.DepartmentID;
