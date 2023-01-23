from .clean_data import add_word_level, clean_data_file  # prepare input for db
from .db_queries import query_me, populate_db
from .utilities import oxford_pron, diki_pron, get_image_url, one_record_context
from django.shortcuts import render


# database records summary
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

# display one randomally selected word
def rnd_view(request):    
    context_record = one_record_context()
    return render(request, 'rnd_word.html', context=context_record)

# record saved in ctx dictionary
ctx = dict()
def guess_view(request):
    global ctx
    if request.method == "GET":                
        ctx = one_record_context()        
        print("English:", ctx.get('eng'))
        print("Polish:", ctx.get('plFirst'))
        print("Other translations:", ctx.get('plRest'))
        #
        return render(request, 'guess_word.html', ctx)
    if request.method == "POST":
        akceptowalne = ''
        odpowiedz = request.POST.get('tlumaczenie').lower().strip()  
        tlumaczenia = []
        tlumaczenia.append(ctx.get('plFirst'))
        if len(ctx.get('plRest')) > 0:
            tlumaczenia += ctx.get('plRest')       

        result = "Nie odgadłeś :/"
        for t in tlumaczenia:            
            if t.lower().strip() == odpowiedz:
                result = "Brawo, zgadłeś!"
                break
        # akceptowalne odpowiedzi jeśli nie odgadnięto
        if result == 'Nie odgadłeś :/':
            
            # v1 - answers in one line            
            # akceptowalne = f"""<br><br><u>Acceptable answers were:</u> <br>
            # <font size="+2">
            # {"; ".join(tlumaczenia)}</font>"""

            # v2 - modify so they are on below another
            akceptowalne = '<br><br>Acceptable answers were:<br><font size="+1"><ul>'            
            for x in tlumaczenia:
                akceptowalne += f"<li>{x}</li>"            
            akceptowalne += "</ul></font>"
        #
        context = {
            'odpowiedz': odpowiedz,
            'rezultat': result,
            'akceptowalne': akceptowalne,
        }
        return render(request, 'guess_result.html', context)