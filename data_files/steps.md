## Django project this is still 'work-in-progress' project.
Having said that it's far from being completed. However, the 'core' functionality is there.

## About
Test yourself by translating words and phrases split between eight levels - from easiest 'A1' to hardest 'C2'.
If you feel adventurous try the 'wymieszanie' category which is a mixed bag - contains all level words that are NOT in any of the other categories. Additionally, you can also practise some popular English proverbs.
There are 30k+ words in the database to choose from to keep you occupied that are randomly selected from the database based on
chosen 'play' settings.

Both pronunciation audio, as well as an image for the word being guessed, are scraped live (at the time of displaying a word) from the internet (details in the Data Sources section). Having said that, especially when it comes to images, they might be off as they weren't 'approved' by myself - they are just what the website that is being scraped returns.

## Running
1. Install project requirements:
`pip install -r requirements.txt`

2. in the project's root folder (where the `manage.py` file is):
`python manage.py runserver`

3. click 'Start' on the navbar and choose your difficulty settings.

## Data Sources
1. The raw_data file that was parsed from: [Wiki-Matthias_Buchmeier](http://en.wiktionary.org/wiki/User:Matthias_Buchmeier)
2. English pronunciation being scraped from:
- [Oxford Learner's Dictionary](https://www.oxfordlearnersdictionaries.com/) proper RP pronunciation
- [diki.pl](https://www.diki.pl/) <- not as nice as Oxford but works much faster
3. Images being scraped from: [unsplash](https://unsplash.com)

## Prepare database input file - IGNORE this step
This step is **not** required as the properly populated database is included in the project. This is just to show how I prepared the original txt file that was used for populating the appropriate table.

To process raw_words.txt file so it is ready for the database run once:
- clean_data.lean_data_file()
- clean_data.add_word_level()

## To do next
- in hindsight - amend display flex to display grid for /play/:
    - row 1 English and translate cards
    - row 2: span 2 - image filling entire row
- add the ability to edit a record in the database if the translation/meaning/part of the word is incorrect
- add the ability to delete an entry from the database if something is wrog with it (vulgar?)
- add the About page with an explanation of how the site works and how to guess words, emphasize that users should pay attention to English meaning and what the words is (given by the site) as the one word can have multiple meanings depending on context and which part of the language it is!
- SERIOUS REFACTORING of the wordLearn/views.py required
- add static file for missing image and no pronunciation
- add user model
- add tracking user's progress
- in perspective further prettification - add CSS, bootstrap maybe, make it look at least semi-acceptable

## implemented
- create /play/ site - cards with an English word, translation and image scraped from the internet
- add image and pronunciation to guessing words /play/ site
- add stats to the /result/ site - replies success rate summary
- prettify /result/site - data is passed to the template correctly already; maybe in a table?
- implement results site /result/ skeleton done - display statistics of user's guesses
- add input fields for /play/ site and validate input, once validated implemented/result/ site
- use JSON file for words selected from the database for guessing (practising)
- add a site where you select a level of difficulty of the words you want to try to guess
- add one-word translation check site /guess/
- think of a website from where I can get example images for the words - mayhap one of the below - using website scraping
    - [pexels](https://www.pexels.com)
    - [unsplash](https://unsplash.com) <- currently using this
    - [pixabay](https://pixabay.com/)
- add oxford dictionary pronunciation to /random_word
- add pronunciation (scraping websites)
- add to random_word polish and English explanations in a list if more than one is possible; split into table rows
- move the translation code to the view, don't leave it in the HTML template, check if the pronunciation is available and if it isn’t, display an appropriate message.
- create a page for randomly selected word from the database - display details
- create a database - use the 'cleaned' text file
- clean raw_words file
