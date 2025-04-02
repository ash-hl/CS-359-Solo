CREATE TABLE Attends (
    memberId       INTEGER PRIMARY KEY
                           REFERENCES Member (memberID),
    classId        INTEGER REFERENCES Classes (classId),
    attendanceDate TEXT    NOT NULL
);

CREATE TABLE Classes (
    classId       INTEGER      PRIMARY KEY AUTOINCREMENT,
    className     VARCHAR (50),
    classType     VARCHAR (20) CHECK (classType IN ('Yoga', 'Zumba', 'HIIT', 'Weights') ),
    duration      INTEGER      NOT NULL,
    classCapacity INTEGER      NOT NULL,
    instructorId  INTEGER      REFERENCES Instructor (instructorId),
    gymID         INTEGER      REFERENCES GymFacility (gymId) 
);

CREATE TABLE Equipment (
    equipmentId INTEGER      PRIMARY KEY AUTOINCREMENT,
    name        VARCHAR (50) NOT NULL,
    type        VARCHAR (30) CHECK (type IN ('Cardio', 'Strength', 'Flexibility', 'Recovery') ),
    quantity    INTEGER (30),
    gymId       INTEGER      REFERENCES GymFacility (gymId) 
);

CREATE TABLE GymFacility (
    gymId    INTEGER       PRIMARY KEY AUTOINCREMENT,
    location VARCHAR (100),
    phone    VARCHAR (50),
    manager  VARCHAR (50) 
);

CREATE TABLE Instructor (
    instructorId INTEGER       PRIMARY KEY AUTOINCREMENT,
    name         VARCHAR (50),
    specialty    VARCHAR (50),
    phone        VARCHAR (15)  NOT NULL,
    email        VARCHAR (100) NOT NULL
);

CREATE TABLE Member (
    memberID            INTEGER       PRIMARY KEY AUTOINCREMENT,
    name                VARCHAR (50),
    email               VARCHAR (50)  NOT NULL,
    phone               VARCHAR (15),
    address             VARCHAR (100),
    age                 INTEGER       CHECK (age >= 15),
    membershipStartDate TEXT          NOT NULL,
    membershipEndDate   TEXT          NOT NULL
                                      CHECK (julianday(membershipEndDate) > julianday(membershipStartDate) ) 
);

CREATE TABLE MembershipPlan (
    planId   INTEGER      PRIMARY KEY AUTOINCREMENT,
    planType VARCHAR (20) CHECK (planType IN ('Monthly', 'Annual') ),
    cost     NUMERIC      NOT NULL
);

CREATE TABLE Payment (
    paymentId   INTEGER PRIMARY KEY AUTOINCREMENT
                        NOT NULL,
    memberId    INTEGER REFERENCES Member (memberID),
    planId      INTEGER REFERENCES MembershipPlan (planId),
    amountPaid  REAL,
    paymentDate TEXT    NOT NULL
);

CREATE TABLE sqlite_sequence(name, seq);
