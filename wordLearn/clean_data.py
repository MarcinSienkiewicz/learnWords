# Both below methods to be run ONCE

# clean_data_file(); method cleans input data file, perares is for adding diff index
# add_word_level(); adds world difficulty level - file is ready for populating db

def clean_data_file():
    import re
    from pathlib import Path

    # Wczytanie pliku wejściowego i jego obróbka
    file_loc = Path(Path(__file__).parents[1] / 'data_files')
    file_path = Path(file_loc / 'raw_words.txt')

    with open(file_path, encoding='utf-8') as file:
        odczytane = [x.replace("\n","") for x in file.readlines()]
        
    # wyrażenia regularne - tokenizacja
    # dopuszczalne tlumaczenia uwaga będą rozdzielone ';' jeśli więcej niż jedno poprawne!!
    # trudno by było odgadnąć słowo jeśli tylko jedna możliwość tłumaczenia jest dobra

    result = []

    peng = re.compile(r'([^\{]*)')  # słówko angielskie
    ppart = re.compile(r'\{(.*?)\}')  # angielska część mowy
    pengdef = re.compile(r'\(.*\)')  # definicja angielska


    def tlumaczenie_polskie(wartosc):
        pplsplt = odczytane[idx].split(" :: ")
        if len(pplsplt) > 1:  # znaczy jest tłumaczenie
            ppltranslation = pplsplt[1].split(", ")
            if len(ppltranslation) == 1:
                if '{' not in ppltranslation[0]:
                    ppltranslation = ppltranslation[0].replace(",",";")
                else:                
                    ppltranslation = ppltranslation[0][:ppltranslation[0].find("{")-1].replace(",",";")
            else:
                # fix kombinacje gdy oddzielne słowa maja i nie maja { }            
                for x in range(len(ppltranslation)):
                    if "{" not in ppltranslation[x]:
                        continue
                    else:
                        ppltranslation[x] = ppltranslation[x][:ppltranslation[x].find('{')-1].replace(',',';')
                ppltranslation = ";".join(ppltranslation)
        else: return 0
        return ppltranslation


    for idx in range(len(odczytane)):
        # cześć polska (tłumaczenie) wymaga nieco wiecej pracy
        # gdyż dopuszczalne jest kilka tłumaczeń i wtedy akceptowalne tłumaczenia rozdzielone ';'     
        cztery = tlumaczenie_polskie(odczytane[idx])
        if cztery == 0:
            continue  # jeśli nie ma tłumaczenia polskiego - nie chcemy
        
        # jeśli nie ma angielskiej definicji - nie chcemy
        if "(" not in odczytane[idx]:
            continue
        
        raz = peng.match(odczytane[idx]).group(0)[:-1].replace(',','')   
        dwa = ppart.findall(odczytane[idx])[0]
        if dwa in ['suffix', 'prefix', 'prop', 'interj']:
            continue  # nie chcemy prefixów, suffixów, nazw własnych, wykrzyknienia
        trzy = pengdef.findall(odczytane[idx])[0][1:-1].replace(',','')
        
        result.append([raz,dwa,trzy,cztery])
        
        
    # cleanup polskiego tłumaczenia - usunięcie fraz [miedzy nawiasami kwadratowymi]
    ptlclean = re.compile(r'\[(.*?)\]')
    ctr = 0
    for idx in range(len(result)):
        while '[' in result[idx][3]:
            ctr += 1
            result[idx][3] = re.sub(ptlclean, '', result[idx][3], count=5)
            
            
    # cleanup angielskieg - zamiana ', ' na ';' aby się ładnie jako *.csv zapisało
    for x in range(len(result)):
        result[x][2] = result[x][2].replace(", ", ";")


    # zamiana akronimów i skrótów części mowy na właściwe nazwy
    mapowanie = {'n':'rzeczownik', 'adj':'przymiotnik', 'v':'czasownik', 'adv': 'przysłówek', 'prep':'przyimek',
                'phrase':'wyrażenie', 'proverb':'przysłowie', 'num':'numer/numeryczne', 'pron':'zaimek',
                'conj':'spójnik', 'determiner':'określnik', 'particle':'partykuła', 'contraction':'forma skrócona',
                'article':'rodzajnik'}
    for x in range(len(result)):
        result[x][1] = mapowanie.get(result[x][1])


    # dodanie znaku nowej lini przed zapisaniem do pliku
    cleaned_list = [','.join(x)+"\n" for x in result]

    
    # zapisanie do pliku przetworzonego pliku wejściowego
    with open(Path(file_loc / 'parsed_data.txt'), 'w', encoding='utf-8') as file:
        file.writelines(cleaned_list)


# working on parsed_data input file - adding word diffuculty index
def add_word_level():    
    from pathlib import Path

    # getting cleaned data for db
    src = (Path(__file__).parents[1] / 'data_files/parsed_data.txt')
    with open(src, encoding='utf-8') as file:
        db_data = [x.replace('\n', '').split(",") for x in file.readlines()]  

    # add level info from another file    
    with open(Path(__file__).parents[1] / 
        'data_files/level_data.txt', encoding='utf-16') as file:
        odczytane = [x.replace("\n",'').split(",") for x in file]
    
    lvl_dict = {x[0]:x[-1] for x in odczytane}

    for ind in range(len(db_data)):
        if db_data[ind][1] == 'przysłowie':
            db_data[ind].append('przysłowie')
        elif (db_data[ind][0].lower() in lvl_dict.keys()) or (db_data[ind][0] in lvl_dict.keys()):            
            db_data[ind].append(lvl_dict.get(db_data[ind][0]))
        else:
            db_data[ind].append('wymieszane')
    
    
    # write final version that will be pushed to database
    db_data = [",".join(x) for x in db_data]

    with open(Path(__file__).parents[1] / 'data_files/complete.txt', 'w' ,encoding='utf-8') as file:
        file.writelines([x+"\n" for x in db_data])    