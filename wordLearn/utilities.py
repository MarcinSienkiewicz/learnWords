from bs4 import BeautifulSoup
import requests

def diki_pron(word):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.'}    
    url = f"https://www.diki.pl/slownik-angielskiego?q={word}"
    r = requests.get(url, headers=header)
    soup = BeautifulSoup(r.text, 'lxml')
    
    try:
        mp3 = 'https://diki.pl/'
        mp3 += soup.find('span', class_='audioIcon').get('data-audio-url')
        # return html code for audio
        # if you only need url for audio file return mp3 NOT the below 'audio' variable
        
        # if pronunciation found on Oxford Dictionary
        r.close()
        return f"""<audio controls>
            <source src="{mp3}"
            type="audio/mpeg">
            Your browser does not support the audio element.
            </audio>"""

    except AttributeError:
        # if no pronunciation found on Oxford Dictionary site        
        r.close()
        return "<h2>Sadly, no pronunciation availble for this.</h2>"
        

def oxford_pron(word):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.'}    
   
    # oxford url
    url = f'https://www.oxfordlearnersdictionaries.com/definition/english/{word}?q={word}'
    
    # alternative oxford url below - tends to work worse
    # url = f'https://www.oxfordlearnersdictionaries.com/definition/english/{word}'
        
    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, 'lxml')
    try:
        mp3 = soup.find('div', class_='sound audio_play_button pron-uk icon-audio').get('data-src-mp3')        
        # return html code for audio
        # if you only need url for audio file return mp3 NOT the below 'audio' variable
        
        # if pronunciation found on Oxford Dictionary
        r.close()
        return f"""<audio controls>
            <source src="{mp3}"
            type="audio/mpeg">
            Your browser does not support the audio element.
            </audio>"""

    except AttributeError:
        # if no pronunciation found on Oxford Dictionary site        
        r.close()
        return "<h2>Sadly, no pronunciation availble for this.</h2>"
    