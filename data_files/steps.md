## Data Sources
1. Raw datafile for parsing from: http://en.wiktionary.org/wiki/User:Matthias_Buchmeier
2. Englis RP pronounciatinon scraped from https://www.oxfordlearnersdictionaries.com/

## Prepare database input file
To process raw_words.txt file so it is ready for the database run once:
- clean_data.lean_data_file()
- clean_data.add_word_level()

## To do next
1. COMIT CHANGES BEFORE DOING THIS: add table column with mp3_url, whenever word is generated, check if the database if this has already pronounciation url, if so, load from the database, if not, scrape Oxf dictionary and save url into database so if searched for next time, it is loaded from the database NOT scraped - will be much faster. Eventually all pronouncioation link will be saved in the db so it will work much faster

### Done - moved from 'To do'
- add oxford dictionary pronouciation to /random_word
- diki.pl pron. added and used, faster than oxford dict.
- add to random_word polish and english explanations in a list if more than one  split into table rows
- Move translation code to the view, don't leave in HTML template. Add check if pronounciation not available and if so, display message about that.
