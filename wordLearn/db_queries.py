# database queries go here
import random
from django.db import connection

def populate_db():
    from pathlib import Path
    import time
    time_st = time.perf_counter()

    file_exists = Path(Path(__file__).parents[1] / 'data_files/complete.txt').exists()
    db_entries = query_me()[0]

    if db_entries == 0 and file_exists:
        print("STATUS OK: All ready for the dabatase data import.")
        # actual import data here
        src = Path(__file__).parents[1] / 'data_files/complete.txt'
        with open(src, encoding='utf-8') as file:
            db_input = [x.replace('\n','').split(",") for x in file.readlines()]
                
        c = connection.cursor()
        for x in range(len(db_input)):
            c.execute("""
            INSERT INTO wordLearn_word(english, part, eng_meaning, polish, level)
            VALUES(:english, :part, :eng_meaning, :polish, :level);
            """, {'english':db_input[x][0], 'part':db_input[x][1], 
            'eng_meaning':db_input[x][2], 'polish':db_input[x][3],
            'level':db_input[x][4]})        
        c.close()
        print('It took:', time.perf_counter() - time_st)

    elif not file_exists:
        raise FileNotFoundError("No input file in the 'data_files' directory! Aborting.")
    else:
        raise ValueError('The table is NOT empty! Delete all data before import.')        

def query_me(attr):    
    c = connection.cursor()
    if attr == 'home':
        c.execute("""
        SELECT level, COUNT(id) FROM wordLearn_word
        GROUP BY level
        ORDER BY level;
        """)
        return c.fetchall()
    
    # Word Of The Day query - bez przysłów
    if attr=='rnd':
        c.execute('SELECT COUNT(*) FROM wordLearn_word')
        noRecords = c.fetchone()[0]        
        import random        
        getThisId = random.randint(1,noRecords)
        
        while True:
            c.execute("""SELECT * FROM wordLearn_word
            WHERE id=:rolled""", {'rolled':getThisId})
            rolled = c.fetchone()
            if rolled[2] != 'przysłowie':
                return rolled


def guessing_game_records(level, how_many):    
    c = connection.cursor()
    c.execute("SELECT * FROM wordLearn_word WHERE level LIKE :level",{'level':level})
    return random.sample(c.fetchall(), int(how_many))   
