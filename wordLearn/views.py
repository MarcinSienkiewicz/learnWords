from .clean_data import add_word_level, clean_data_file  # prepare input for db
from .db_queries import query_me, populate_db
from django.shortcuts import render


def home_view(request):    
    # clean_data_file()  # run once to clean input data file    
    # add_word_level() # run once to get final version - ready to populate database
    
    populate_db()
    return render(request, 'home.html')