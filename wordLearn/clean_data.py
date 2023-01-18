# to be run ONCE to clean input data file so it is ready for populating database

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