from .clean_data import add_word_level, clean_data_file  # prepare input for db
from .db_queries import query_me, populate_db, guessing_game_records
from .utilities import oxford_pron, diki_pron, get_image_url, one_record_context, calculate_result
from django.shortcuts import render, redirect
from .forms import SelectionForm

from pathlib import Path
import json

# database records summary
def home_view(request):    
    request.session['chosen'] = False  
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

# display one randomally selected word
def rnd_view(request):
    request.session['chosen'] = False 
    context_record = one_record_context()
    return render(request, 'rnd_word.html', context=context_record)

# choose word level and how many you want to practice
def choose_view(request):
    if request.method=='POST':
        request.session['chosen'] = request.POST  # session variable
        # used to pass data to the play_view method
        # word level and how many words user decided to go ahead with
        return redirect('/play/')

    working_file = Path(__file__).parents[1] / 'data_files/current_roll.json'
    if working_file.exists():
        working_file.unlink()
    form = SelectionForm()
    request.session['chosen'] = False
    request.session['user_answers'] = ""
    return render(request, 'choose_what.html', {'form':form})    


# actual functionality - checking if user knows words choses for him
# and selected randomally from the database based on the choose_view options
def play_view(request):    
    if request.session['chosen'] == False:
        return redirect('/choose/')

    working_file = Path(__file__).parents[1] / 'data_files/current_roll.json'    

    # if working file does not exist yet - first word to be presented to the user
    if working_file.exists() == False:
        lvl = request.session['chosen'].get('level_choices')
        how_many = request.session['chosen'].get('tries')      
        selected = guessing_game_records(lvl, how_many)                
    
        jFile = dict()
        for ind, val in enumerate(selected):
            jFile[ind] = val
        jFile['page'] = "-1"

        # write selected records to json file
        with open(working_file, 'w', encoding='utf-8') as file:
            json.dump(jFile, file, indent=2)
    
    # get correct entry for display    
    with open(working_file, encoding='utf-8') as file:
        selected = json.load(file)
    
    # print(*selected.items(), sep="\n")

    current_page = int(selected.get('page')) + 1
    selected['page'] = str(current_page)
    
    with open(working_file, 'w', encoding='utf-8') as file:
        json.dump(selected, file, indent=2)    
    
        
    # wpisywanie do zmiennej sesyjnej kolejnych odpowiedzi
    if len(request.POST) > 0:        
        request.session['user_answers'] += (request.POST.get('odgadywane')+";")
        # using string as session lists are awkward to use       
         
    
    # if last word got dispalyed - redirect to results (user score)
    # maybe pass results as session variable? or save to file
    # session variable easier
    if int(selected['page']) > len(selected)-2:
        return redirect('/result/')
    
    # getting image and pronunciation for word displayed for guessing
    pronURL = oxford_pron(selected[str(current_page)][1])
    imgURL = get_image_url(selected[str(current_page)][1])    
    meaning = selected[str(current_page)][3].split(";")

    print(meaning)

    context = {
        'word': selected[str(current_page)],        
        'meaning': selected[str(current_page)][3].split(";"),
        'wordPron': pronURL,
        'wordImage': imgURL,
    }
    return render(request, 'guessing_game.html', context)


def result_view(request):
    # calculate results here and pass them to be dispayed    
    # zrobić porównanie odpowiedzi i pytań, wyliczyć statystyki i przekazać
    # odpowiedć do template

    results = calculate_result(request.session['user_answers'])
    print(results[0])
    correct_ans = sum([1 if x[3]=='Correct!' else 0 for x in results])
    prc_correct = f"{correct_ans/len(results):.0%}"
    context = {
        'wyniki': results,
        'ile_pytan': len(results),
        'poprawnych': correct_ans,
        'procent_ok': prc_correct,
    }
    return render(request, 'results.html', context)