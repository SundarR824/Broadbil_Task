
-- Create the groups table
CREATE TABLE IF NOT EXISTS groups (
                         group_id INT AUTO_INCREMENT PRIMARY KEY,
                         group_name VARCHAR(50)
                     );
-- Create the subjects table
CREATE TABLE IF NOT EXISTS subjects (
                           subject_id INT AUTO_INCREMENT PRIMARY KEY,
                           title VARCHAR(50)
                      );
-- Create the students table
CREATE TABLE IF NOT EXISTS students (
                           student_id INT AUTO_INCREMENT PRIMARY KEY,
                           first_name VARCHAR(30),
                           last_name VARCHAR(30),
                           group_id INT,
                           CONSTRAINT FK_Students_Groups FOREIGN KEY (group_id) REFERENCES groups(group_id)
                           ON DELETE CASCADE
                           ON UPDATE CASCADE
                       );
-- Create the marks table
CREATE TABLE IF NOT EXISTS marks (
                        mark_id INT AUTO_INCREMENT PRIMARY KEY,
                        student_id INT,
                        subject_id INT,
                        date_time DATETIME,
                        mark INT,
                        CONSTRAINT FK_Marks_Students FOREIGN KEY (student_id) REFERENCES students(student_id),
                        CONSTRAINT FK_Marks_Subjects FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
                        ON DELETE CASCADE
                        ON UPDATE CASCADE
                    );
-- Create the teacher table
CREATE TABLE IF NOT EXISTS teacher (
                         teacher_id INT AUTO_INCREMENT PRIMARY KEY,
                         subject_id INT,
                         group_id INT,
                         CONSTRAINT FK_Teacher_Subjects FOREIGN KEY (subject_id) REFERENCES subjects(subject_id),
                         CONSTRAINT FK_Teacher_Groups FOREIGN KEY (group_id) REFERENCES groups(group_id)
                         ON DELETE CASCADE
                         ON UPDATE CASCADE
                     );