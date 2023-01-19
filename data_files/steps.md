## Data Source
1. Raw datafile for parsing from: http://en.wiktionary.org/wiki/User:Matthias_Buchmeier
2. Englis RP pronounciatinon scraped from https://www.oxfordlearnersdictionaries.com/
3. Cleaned data imported using sqlite_tools (30k+ records in db)

## Prepare database input file
To process raw_words.txt file so it is ready for the database run once:
- clean_data.lean_data_file()
- clean_data.add_word_level()

## To do next
1. populate db with the file from clean_data.add_world_level() output
