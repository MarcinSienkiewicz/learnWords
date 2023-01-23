## Data Sources
1. Raw datafile for parsing from: http://en.wiktionary.org/wiki/User:Matthias_Buchmeier
2. Englis pronouciation scraped from:
- https://www.oxfordlearnersdictionaries.com/ proper RP pronouciation
- https://www.diki.pl/ <- not as nice as Oxford but works much faster
3. Images scraped from https://unsplash.com

## Prepare database input file
To process raw_words.txt file so it is ready for the database run once:
- clean_data.lean_data_file()
- clean_data.add_word_level()

## To do next
- add about page with explanation how the site works and how to guess words, emphasize that use should pay attention to english meaning and what the words is (given by the site) as the one word can have multiple meanings depending on context and which part of language it is!
- Add site where you select level of difficulty of the words you want to try to guess
- Implement guessing multiple words, count statistics
- Add static file for missing image and no pronunciation
- add user model
- add tracking user's progres 
- In perspective pretiffy - add CSS, bootstrap maybe?

## Done - moved from 'To do'
- add one word translation check site /guess/
- Think of a website from where I can get example image for the words - mayhap one of the below - using website scraping
    - https://www.pexels.com
    - https://unsplash.com  <- using this
    - https://pixabay.com/
- add oxford dictionary pronouciation to /random_word
- add pronouciation (scraping websites)    
- add to random_word polish and english explanations in a list if more than one split into table rows
- Move translation code to the view, don't leave in HTML template, check if pronounciation not available and if so, display message about that.
- create page for randomally selected word from the database - display details
- create database - use 'cleaned' txt file
- clean raw_words file
