from django.shortcuts import render
from django.db import connection


def hdd_data():
    from pathlib import Path

    src = (Path(__file__).parents[1] / 'data_files/parsed_data.txt')
    with open(src, encoding='utf-8') as file:
        for_db = [x.replace('\n', '') for x in file.readlines()]    
    return for_db


def populate_db():
    for_db = hdd_data()
    print(*for_db[5550:5560], sep='\n')
    
    c = connection.cursor()

    # populate db here (using SQL command or cmd and sqlite3.exe)
    c.execute('SELECT * FROM wordLearn_Word LIMIT 5')
    

    

    

def home_view(request):
    populate_db()
    return render(request, 'home.html')