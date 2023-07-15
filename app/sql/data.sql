-- Insert records into the Groups table
INSERT INTO groups (group_name)
VALUES ('Group A'),
       ('Group B'),
       ('Group C');
-- Insert records into the subjects table
INSERT INTO subjects (title)
VALUES ('Mathematics'),
       ('Science'),
       ('English'),
       ('Tamil'),
       ('Social Science'),
       ('Biology'),
       ('Accounts'),
       ('Commerce'),
       ('Economics'),
       ('History');
-- Insert records into the Students table
INSERT INTO students (first_name, last_name, group_id)
VALUES
  ('John', 'Doe', 1),
  ('Jane', 'Smith', 2),
  ('Alice', 'Johnson', 1),
  ('Robert', 'Williams', 3),
  ('Emily', 'Davis', 2),
  ('Davis', 'Emily', 1),
  ('William', 'Joy', 3),
  ('Sneha', 'Williams', 3),
  ('jonathan', 'David', 2),
  ('aaron', 'julian', 1),
  ('julian', 'aaron', 3),
  ('Andy', 'mishra', 2),
  ('sandip', 'kumar', 3),
  ('Mani', 'Mani', 1),
  ('kumar', 'Nanda', 3);
-- Insert records into the marks table
INSERT INTO marks (student_id, subject_id, date_time, mark)
VALUES (1, 1, '2023-07-13 10:00:00', 85),
       (2, 2, '2023-07-14 11:30:00', 90),
       (3, 3, '2023-07-13 09:00:00', 44),
       (1, 2, '2023-07-13 09:00:00', 76),
       (5, 3, '2023-07-13 09:00:00', 89),
       (3, 1, '2023-07-13 09:00:00', 43),
       (7, 3, '2023-07-13 09:00:00', 28),
       (5, 2, '2023-07-13 09:00:00', 37),
       (9, 1, '2023-07-13 09:00:00', 64),
       (7, 3, '2023-07-13 09:00:00', 45);
-- Insert records into the Teachers table
INSERT INTO teacher (subject_id, group_id)
VALUES (1, 1),
       (2, 2),
       (3, 3);
