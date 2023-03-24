import concurrent.futures                                          #library for concurrent tasks
import urllib.request                                              #library that handles url requests
import threading                                                   #for threading
import newspaper                                                   #library newspaper for web scrapping newspapers
from newspaper import Article                                      #article is an object of newspaper
import timeit                                                      #function to count time taken
           
                          
URLs = ['http://www.foxnews.com/',                                 #list of URLs to be accessed
        'http://www.cnn.com/',
        'http://www.derspiegel.de/',
        'http://www.bbc.co.uk/',
        'https://theguardian.com',]
                          
def load_url(url, timeout):                                        #load_url function takes two arguments url and timeout to limit
    with urllib.request.urlopen(url, timeout=timeout) as conn:     #time wasted and automate timeout
        return conn.read().                                        #use urlib.request to open and read urls
                          
def get_headlines():

    for url in URLs:
        result = newspaper.build(url, memoize_articles=False)
        print('\n''The headlines from %s are' % url, '\n')
        for i in range(1,6):
            art = result.articles[i]
            art.download()
            art.parse()
            print(art.title)
def parse():
    result = newspaper.build(url, memoize_articles=False)
    art = result.articles[i]
    art.download()
    art.parse()
    return art.title


def  concurrent_headlines():
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:          #we start using threadpool and set workers to5
        future_to_url = {executor.submit(load_url , url, 10): url for url in URLs}  #built in function submit takes a function,url
        for headlines in concurrent.futures.as_completed(future_to_url):            #and timeout and gets the data.all as executor
            url = future_to_url[headlines]                                          #for all the completed url submit requests
            try:                                                                    #url is the resulted array element with index
                data = headlines.result()                                           #headlines
            except Exception as exc:                                                #try setting data to index of future_to_url’s
                print('%r generated an exception: %s' % (url, exc))                 #result as data
            else:                                                                   #raise an exception and print it out
                result = newspaper.build(url, memoize_articles=False)              #store in a variable result the outcome of
                print('\n''The headlines from %s are' % url, '\n')                #built in method build() in newspaper lib
                for i in [1,2,3,4,5]:                                             #which builds articles out of urls
                    art = result.articles[i]                                     #loop 5 times through url data
                    art.download()                                               #for every loop get the [i] element (headline)
                    art.parse()                                                  #downlaod and parse to access titles
                    print(art.title)                                             #print titles
                
                        
if __name__ == '__main__':
    import timeit                                                                   #import timeit to calculate time taken
    elapsed_time = timeit.timeit("concurrent_headlines()", setup="from __main__ import concurrent_headlines", number=2)/2  #use time it on function concurrent_headlines()           
    print(elapsed_time)                                            #print time taken
