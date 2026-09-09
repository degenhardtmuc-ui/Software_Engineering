INSERT INTO grades
(student_id, course_id, score, date, notes)
VALUES ('S001', 'CS102', 92.0, '2026-07-10', 'Sehr gute Leistung');

INSERT INTO grades
(student_id, course_id, score, date, notes)
VALUES ('S001', 'DB101', 88.0, '2026-07-12', 'Gute Datenbankkenntnisse');

INSERT INTO grades
(student_id, course_id, score, date, notes)
VALUES ('S002', 'CS102', 76.0, '2026-07-10', 'Bestanden');

INSERT INTO grades
(student_id, course_id, score, date, notes)
VALUES ('S002', 'DB101', 45.0, '2026-07-12', 'Noch nicht bestanden');

INSERT INTO grades
(student_id, course_id, score, date, notes)
VALUES ('S003', 'CS101', 95.0, '2026-07-14', 'Ausgezeichnet');

INSERT INTO grades
(student_id, course_id, score, date, notes)
VALUES ('S003', 'CS102', 91.0, '2026-07-15', 'Sehr gute Programmierleistung');

INSERT INTO grades
(student_id, course_id, score, date, notes)
VALUES ('S003', 'DB101', 42.0, '2026-07-16', 'Noch nicht bestanden');

#Kontrolle:

SELECT COUNT(*) FROM courses;
SELECT COUNT(*) FROM grades;