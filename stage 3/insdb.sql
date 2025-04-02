INSERT INTO Attends (
                        attendanceDate,
                        classId,
                        memberId
                    )
                    VALUES (
                        '2025-10-01',
                        1,
                        1
                    ),
                    (
                        '2025-10-02',
                        2,
                        2
                    ),
                    (
                        '2025-10-03',
                        3,
                        3
                    ),
                    (
                        '2025-10-04',
                        4,
                        4
                    ),
                    (
                        '2025-10-05',
                        5,
                        5
                    );
INSERT INTO Classes (
                        gymID,
                        instructorId,
                        classCapacity,
                        duration,
                        classType,
                        className,
                        classId
                    )
                    VALUES (
                        1,
                        1,
                        15,
                        45,
                        'Yoga',
                        'Yoga for Beginners',
                        1
                    ),
                    (
                        2,
                        2,
                        15,
                        45,
                        'Zumba',
                        'Afternoon Zumba',
                        2
                    ),
                    (
                        3,
                        3,
                        15,
                        45,
                        'HIIT',
                        'Advanced HIIT',
                        3
                    ),
                    (
                        4,
                        4,
                        15,
                        45,
                        'Weights',
                        'Weight Training I',
                        4
                    ),
                    (
                        5,
                        5,
                        15,
                        45,
                        'HIIT',
                        'Morning HIIT',
                        5
                    );
INSERT INTO Equipment (
                          gymId,
                          quantity,
                          type,
                          name,
                          equipmentId
                      )
                      VALUES (
                          1,
                          1,
                          'Cardio',
                          'Sprint Machine I',
                          1
                      ),
                      (
                          2,
                          2,
                          'Strength',
                          'The Muscle Builder',
                          2
                      ),
                      (
                          3,
                          1,
                          'Flexibility',
                          'The Flexinator',
                          3
                      ),
                      (
                          4,
                          3,
                          'Recovery',
                          'Rest n'' Recover',
                          4
                      ),
                      (
                          5,
                          4,
                          'Cardio',
                          'Sprint Machine II',
                          5
                      );
INSERT INTO GymFacility (
                            manager,
                            phone,
                            location,
                            gymId
                        )
                        VALUES (
                            'Jack Neil',
                            '111-9999',
                            'Central Area Gym',
                            1
                        ),
                        (
                            'Mary Berk',
                            '111-9998',
                            'Uptown Gym',
                            2
                        ),
                        (
                            'James Sunderland',
                            '111-9997',
                            'Main Street Gym',
                            3
                        ),
                        (
                            'Leon Kennedy',
                            '111-9996',
                            'Downtown Main Gym',
                            4
                        ),
                        (
                            'John Doe',
                            '111-9999',
                            'Downtain Studio Gym',
                            5
                        );
INSERT INTO Instructor (
                           email,
                           phone,
                           specialty,
                           name,
                           instructorId
                       )
                       VALUES (
                           'john@mail.com',
                           '111-9999',
                           'Yoga',
                           'John',
                           1
                       ),
                       (
                           'mary@mail.com',
                           '111-9998',
                           'Zumba',
                           'Mary',
                           2
                       ),
                       (
                           'lain@mail.com',
                           '111-9997',
                           'Weights',
                           'Lain',
                           3
                       ),
                       (
                           'lindsey@mail.com',
                           '111-9996',
                           'Cardio',
                           'Lindsey',
                           4
                       ),
                       (
                           'ella@mail.com',
                           '111-9995',
                           'Zumba',
                           'Ella',
                           5
                       );
INSERT INTO Member (
                       membershipEndDate,
                       membershipStartDate,
                       age,
                       address,
                       phone,
                       email,
                       name,
                       memberID
                   )
                   VALUES (
                       '2025-12-01',
                       '2025-10-01',
                       30,
                       '''775 James Street''',
                       '''111-9999''',
                       'Eldred_Padberg@gmail.com',
                       'Eldred',
                       1
                   ),
                   (
                       '2025-12-02',
                       '2025-10-02',
                       42,
                       '''1482 Poplar Chase Lane''',
                       '''111-9998''',
                       'Beryl.Keebler@gmail.com',
                       'Berl',
                       2
                   ),
                   (
                       '2025-12-03',
                       '2025-10-03',
                       29,
                       '4261 Bombardier Way''',
                       '''111-9997''',
                       'Ozella.Friesen@gmail.com',
                       'Ozella',
                       3
                   ),
                   (
                       '2025-12-04',
                       '2025-10-04',
                       18,
                       '''4592 Henery Street''',
                       '''111-9996''',
                       'Johnny_Haag51@gmail.com',
                       'Johny',
                       4
                   ),
                   (
                       '2025-12-05',
                       '2025-10-05',
                       22,
                       '''3671 Bungalow Road''',
                       '''111-9995''',
                       'Rosella68@gmail.com',
                       'Rosella',
                       5
                   );
INSERT INTO MembershipPlan (
                               cost,
                               planType,
                               planId
                           )
                           VALUES (
                               99,
                               'Annual',
                               1
                           ),
                           (
                               7,
                               'Monthly',
                               2
                           ),
                           (
                               99,
                               'Annual',
                               3
                           ),
                           (
                               7,
                               'Monthly',
                               4
                           ),
                           (
                               99,
                               'Annual',
                               5
                           );
INSERT INTO Payment (
                        paymentDate,
                        amountPaid,
                        planId,
                        memberId,
                        paymentId
                    )
                    VALUES (
                        '2025-10-01',
                        70,
                        1,
                        1,
                        1
                    ),
                    (
                        '2025-10-02',
                        25,
                        2,
                        2,
                        2
                    ),
                    (
                        '2025-10-03',
                        15,
                        3,
                        3,
                        3
                    ),
                    (
                        '2025-10-04',
                        25,
                        4,
                        4,
                        4
                    ),
                    (
                        '2025-10-05',
                        45,
                        5,
                        5,
                        5
                    );
