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
- make 3 cards horizontally for /play/ - word with what it is, image in second, user's reply in third
- add ability to edit record in database if translation/meaning/part of word is incorrect
- add ability to delete entry from database if something wrog with it (vulgar?)
- add about page with explanation how the site works and how to guess words, emphasize that use should pay attention to english meaning and what the words is (given by the site) as the one word can have multiple meanings depending on context and which part of language it is!
- REFACTORING of the views.py methods
- Add static file for missing image and no pronunciation
- add user model
- add tracking user's progres 
- In perspective pretiffy - add CSS, bootstrap maybe, make it look at least semi-acceptable

## Done - moved from 'To do'
- add image and pronouciation to guessing words /play/ site
- add stats to the /result/ site - replies succes rate summary
- pretiffy /result/site - data is returned to it correct already; maybe in a table?
- Implement results site /result/ skeleton done - display statistics of user's guesses
- add input fields for /play/ site and validate input, once validated implement /result/ site
- Use json file for words selected from the database for guessing (practicing)
- Add site where you select level of difficulty of the words you want to try to guess
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
