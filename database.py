import pathlib
import sqlite3
from dataclasses import dataclass


@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''


def fix_db_path(db_name):

    if pathlib.Path(db_name).suffix == '':
        db_name += '.db'
    return db_name


class Database():
    def __init__(self, DB_NAME):

        self.db_name = fix_db_path(DB_NAME)
        self.conn = sqlite3.connect(self.db_name)
        self.conn.execute('''CREATE TABLE IF NOT EXISTS note
                    (id INTEGER primary key, title STRING, content STRING not null)''')
        self.conn.commit()

    def add(self, note):
        self.notation = f"INSERT INTO note (title, content) VALUES ('{note.title}','{note.content}');"
        self.conn.execute(self.notation)
        self.conn.commit()

    def get_all(self,):
        self.cursor = self.conn.execute("SELECT id, title, content FROM note")
        self.note_list = []
        for linha in self.cursor:
            note_obj = Note(linha[0], linha[1], linha[2])
            self.note_list.append(note_obj)
        return self.note_list

    def get_specific(self, id):
        self.string_edit = f"SELECT id, title, content FROM note WHERE id = {id}"
        self.cursor = self.conn.execute(self.string_edit)
        self.note_list = []
        for linha in self.cursor:
            note_obj = Note(linha[0], linha[1], linha[2])
            self.note_list.append(note_obj)
        print(f'{self.note_list} \n\n')
        return self.note_list[0]

    def update(self, entry):
        string_edition = f"UPDATE note SET title = '{entry.title}', content = '{entry.content}' WHERE id = {entry.id};"
        self.cursor = self.conn.execute(string_edition)
        self.conn.commit()

    def delete(self, note_id):
        delete_command = f"DELETE FROM note WHERE id = {note_id};"
        self.cursor = self.conn.execute(delete_command)
        self.conn.commit()
