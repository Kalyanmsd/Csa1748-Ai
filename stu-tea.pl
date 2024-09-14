% Facts representing which teachers teach which students
% Format: teaches(Teacher, Student)

teaches('Mr. Smith', 'John Doe').
teaches('Ms. Johnson', 'Alice White').
teaches('Mr. Smith', 'David Black').
teaches('Ms. Johnson', 'Clara Green').
teaches('Dr. Brown', 'Bob Johnson').

% Rule to find all students taught by a specific teacher
find_students(Teacher, Student) :-
    teaches(Teacher, Student).

% Rule to find all teachers of a specific student
find_teachers(Student, Teacher) :-
    teaches(Teacher, Student).

% Rule to check if two students share the same teacher
same_teacher(Student1, Student2) :-
    teaches(Teacher, Student1),
    teaches(Teacher, Student2),
    Student1 \= Student2.

% Rule to find if a student has multiple teachers
multiple_teachers(Student) :-
    teaches(Teacher1, Student),
    teaches(Teacher2, Student),
    Teacher1 \= Teacher2.
