# Author: Oshan Mendis
# Date: 2025-12-12
# Description: College Database CRUD program

import sqlite3
from typing import Dict, List, Tuple, Any, Optional


class CollegeDatabase:
    def __init__(self, db_name):
        self.db_name = db_name  # Setting the db name
        self.conn = sqlite3.connect(self.db_name)  # Connecting to database
        self.cursor = self.conn.cursor()  # Setting the cursor to run SQL queries

    def create_table(self, table_name, columns: dict) -> None:
        """
        table_name: Name of the table
        columns example:
        {
            "id": "INTEGER",
            "name": "TEXT",
            "age": "INTEGER"
        }
        """

        # Build SQL dynamically
        column_defs = ", ".join([f"{col} {dtype}" for col, dtype in columns.items()])

        sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_defs})"

        self.cursor.execute(sql)
        self.conn.commit()
        print(f"Table '{table_name}' created successfully.")

    def insert_record(self, table_name: str, data: Dict[str, Any]) -> None:
        """
        Insert a record into the specified table.
        data: dict of column: value
        """
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["?" for _ in data])
        values = tuple(data.values())

        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        try:
            self.cursor.execute(sql, values)
            self.conn.commit()
            print(f"Record inserted into '{table_name}'.")
        except sqlite3.Error as e:
            print(f"Error inserting record into '{table_name}': {e}")

    def fetch_all(self, table_name: str) -> List[Tuple]:
        """
        Fetch all records from a table.
        Returns a list of tuples.
        """
        sql = f"SELECT * FROM {table_name}"
        try:
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            print(f"Error fetching data from '{table_name}': {e}")
            return []

    def fetch_by_condition(self, table_name: str, condition: str, params: Tuple = ()) -> List[Tuple]:
        """
        Fetch records matching the condition.
        condition: SQL condition string e.g. "id = ?"
        params: tuple of values for placeholders
        """
        sql = f"SELECT * FROM {table_name} WHERE {condition}"
        try:
            self.cursor.execute(sql, params)
            rows = self.cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            print(f"Error fetching data with condition from '{table_name}': {e}")
            return []

    def update_record(self, table_name: str, update_data: Dict[str, Any], condition: str, params: Tuple) -> None:
        """
        Update records in a table matching the condition.
        update_data: dict of columns and new values
        condition: SQL condition string e.g. "id = ?"
        params: tuple of values for condition placeholders
        """
        set_clause = ", ".join([f"{col} = ?" for col in update_data.keys()])
        values = tuple(update_data.values()) + params

        sql = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
        try:
            self.cursor.execute(sql, values)
            self.conn.commit()
            print(f"Record(s) updated in '{table_name}'.")
        except sqlite3.Error as e:
            print(f"Error updating records in '{table_name}': {e}")

    def delete_record_by_condition(self, table_name: str, condition: str, params: Tuple) -> None:
        """
        Delete records from a table matching the condition.
        condition: SQL condition string e.g. "id = ?"
        params: tuple of values for placeholders
        """
        sql = f"DELETE FROM {table_name} WHERE {condition}"
        try:
            self.cursor.execute(sql, params)
            self.conn.commit()
            print(f"Record(s) deleted from '{table_name}'.")
        except sqlite3.Error as e:
            print(f"Error deleting records from '{table_name}': {e}")

    def close(self) -> None:
        self.conn.close()


if __name__ == "__main__":

    database = CollegeDatabase("yoobee_college.db")

    database.create_table(
        "student",
        {
            "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
            "first_name": "TEXT",
            "last_name": "TEXT",
            "dob": "TEXT",
            "email": "TEXT UNIQUE"
        }
    )

    database.create_table(
        "course",
        {
            "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
            "course_name": "TEXT",
            "course_code": "TEXT UNIQUE",
            "description": "TEXT",
            "category": "TEXT"
        }
    )

    database.create_table(
        "teacher",
        {
            "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
            "first_name": "TEXT",
            "last_name": "TEXT",
            "email": "TEXT UNIQUE",
            "phone": "TEXT"
        }
    )

    # Insert a student
    database.insert_record("student", {
        "first_name": "Oshan",
        "last_name": "Mendis",
        "dob": "1995-10-23",
        "email": "oshan.mendis@yoobee.com"
    })

    database.insert_record("student", {
        "first_name": "Kavindu",
        "last_name": "Perera",
        "dob": "2000-11-11",
        "email": "kavindu.perera@yoobee.com"
    })

    database.insert_record("student", {
        "first_name": "Nirmal",
        "last_name": "Perera",
        "dob": "2001-11-12",
        "email": "nirmal.perera@yoobee.com"
    })

    database.insert_record("student", {
        "first_name": "Rukshan",
        "last_name": "Perera",
        "dob": "2002-08-13",
        "email": "rukshan.perera@yoobee.com"
    })

    database.insert_record("student", {
        "first_name": "Vinuka",
        "last_name": "Perera",
        "dob": "2003-09-14",
        "email": "vinuka.perera@yoobee.com"
    })

    database.insert_record("student", {
        "first_name": "Ganuke",
        "last_name": "Perera",
        "dob": "1985-08-13",
        "email": "ganuke.perera@yoobee.com"
    })

    database.insert_record("student", {
        "first_name": "John",
        "last_name": "Doe",
        "dob": "2000-01-01",
        "email": "john.doe@example.com"
    })

    # Fetch all students
    students = database.fetch_all("student")
    print("All students:", students)

    # Fetch student with id=3
    student = database.fetch_by_condition("student", "id = ?", (3,))
    print("Student with ID 3:", student)

    # Update student's last name where id=2
    database.update_record("student", {"last_name": "Fernando"}, "id = ?", (2,))

    # Delete student where id=1
    database.delete_record_by_condition("student", "id = ?", (7,))

    # Fetch all students after update & deletion
    students = database.fetch_all("student")
    print("All students:", students)
    
    database.close()
