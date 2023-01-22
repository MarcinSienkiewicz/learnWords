from .clean_data import add_word_level, clean_data_file  # prepare input for db
from .db_queries import query_me, populate_db
from .utilities import oxford_pron, diki_pron
from django.shortcuts import render


def home_view(request):    
    # clean_data_file()  # run once to clean input data file    
    # add_word_level() # run once to get final version - ready to populate database    
    # populate_db()  # push all data from cleand input file to SQLite database

    qResult = query_me('home')
    totalRecords = 0
    for x in qResult:
        totalRecords += x[1]
    totalRecords = format(totalRecords, ',d')  # with thousands separator    
    # totalRecords = "{0:,}".format(1236577)  # alternative way to add comma separator    

    qResult = [(x[0], format(x[1], ',d')) for x in qResult]    
    context = {
        'totalRecords': totalRecords,
        'levels': qResult
    }
    return render(request, 'home.html', context)

def rnd_view(request):
    rolled = query_me('rnd')  # get one random word from db
    
    # comment out if you don't want to get pronoun - faster!
    # get rolled's pronounciation from oxf dict lower() as sometimes doesn't find if starts with UCase
    
    # oxford pronoun slow - usein diki istead - fully funtional though, just slow
    # speak = oxford_pron(rolled[1].lower())
    
    speak = diki_pron(rolled[1].lower())

    plTranslation = rolled[4].split(";")
    context ={
        'eng': rolled[1],
        'part': rolled[2],
        'meaning': rolled[3].split(";"),
        'plFirst': plTranslation[0],
        'plRest': plTranslation[1:],        
        'speak': speak
    }   
    return render(request, 'rnd_word.html', context)