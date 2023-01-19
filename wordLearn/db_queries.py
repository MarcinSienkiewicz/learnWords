# database queries go here
from django.db import connection

def populate_db():
    from pathlib import Path
    file_exists = Path(Path(__file__).parents[1] / 'data_files/complete.txt').exists()
    db_entries = query_me()

    if db_entries == 0 and file_exists:
        print("STATUS OK: All ready for the dabatase data import.")
    elif not file_exists:
        raise FileNotFoundError("No input file in the 'data_files' directory! Aborting.")
    else:
        raise ValueError('The table is NOT empty! Delete all data before import.')        

def query_me():
    c = connection.cursor()
    c.execute("SELECT COUNT(*) FROM wordLearn_word")
    return c.fetchone()[0]