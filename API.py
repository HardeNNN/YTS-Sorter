import requests
import json
from pygments import highlight, lexers, formatters
from termcolor import colored


# Replace with the correct URL
limit = input('Top N Movies?:')
url = 'https://yts.lt/api/v2/list_movies.json?sort_by=like_count&order_by=desc&limit=%s' %(limit,)
resp = requests.get(url)
myResponse = requests.get(url)
JSON_Output = input('Do you want to see JSON raw? Y/N: ')

# For successful API call, response code will be 200 (OK)
if(myResponse.ok):
    # Loading the response data into a dict variable
    # json.loads takes in only binary or string variables so using content to fetch binary content
    # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
    jData = json.loads(myResponse.content)
    print("The response contains {0} properties".format(len(jData)))
    print("\n")
    #print(jData)
    # Beautify JSON and output colored
    #print(json.dumps(jData, indent=2, sort_keys=True))
    formatted_json = json.dumps(jData, indent=2,sort_keys=True)
    colorful_json = highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
    if JSON_Output in ('Y', 'y'):
        print (colorful_json)
    else:
        pass
    
    # Extract Data From JSON
    dataLoop = jData['data']['movies']
    LoopCounter = 0
    ##print(colored('Movie title is: ', 'red'), colored(title, 'blue'))
    for x in dataLoop:
        
        # Data Variables
        CurrentMovieData = jData['data']['movies'][LoopCounter]
        title = CurrentMovieData['title']
        rating = CurrentMovieData['rating']
        summary = CurrentMovieData['summary']
        TorrentCounter = 0
        TorrentLoop = jData['data']['movies'][LoopCounter]['torrents']
        CurrentMovieTorrentData =TorrentLoop[TorrentCounter]
        seeds = TorrentLoop[TorrentCounter]['seeds']
        quality = CurrentMovieTorrentData['quality']
        

        
        # Printers
        print(colored('- Movie number', 'red'), colored(LoopCounter+1,'red'), colored('title is:','red'), colored(title, 'blue'), 'with a rating of', colored(rating, 'blue'), end= '\n\n')
        print(colored('Description: ','red'), summary, end= '\n\n')
        #TorrentInfo Loop
        for k in TorrentLoop:
            CurrentMovieTorrentData =TorrentLoop[TorrentCounter]
            seeds = TorrentLoop[TorrentCounter]['seeds']
            quality = CurrentMovieTorrentData['quality']
            size = CurrentMovieTorrentData['size']
            url = CurrentMovieTorrentData['url']
            #print('TorrentCounter: ',TorrentCounter)
            print(colored('Torrent Info: ','green'), seeds,'seeds, Quality:', quality,'size:',size,'Download URL:',url, end= '\n')
            TorrentCounter +=1
        LoopCounter +=1
        print(end='\n\n\n')
else:
    myResponse.status()