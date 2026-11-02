# MCA101P-AS11: Database Management with Python

This folder has 30 separate Python 3 programs based on Lab Sheet-08. They use SQLite (`sqlite3`), which is included with Python, so no MySQL service or external package is needed. Every script uses the same `student_db.sqlite3` database file beside the script and closes its connection.

## Run

Extract the folder, open a terminal in it, and run a file such as `python 03_create_students_table.py`. Run program 03 before student CRUD/query tasks. Programs 08 and 09 add sample records; rerunning them inserts more records. Program 21 creates `courses` and `enrollments`; to view JOIN results, insert enrollment rows linking existing student IDs and course IDs.

Program 20 uses `DELETE FROM` because SQLite does not support `TRUNCATE TABLE`; this clears rows while retaining the table structure. Program 27 expects `students_import.csv` with headers `name,age,marks`. Program 26 writes `students_export.csv`. Program 30 is the interactive Add, View, Update marks, Delete menu.

The scripts are provided as source code and were not executed as part of this delivery. Run each program after preparing the table or CSV inputs described above.
