import urllib2
from pymongo import Connection, ASCENDING, DESCENDING
import re
from Queue import Queue

random_wait = True
wait_time = 3

"""Determines which urls to scrape through storing previous entries in database"""
url_to_scrape = sys.argv[1]
connection = Connection('localhost', 27017)
db = connection.get_html
url_collection = db[url_to_scrape]

cookie_handler = urllib2.HTTPCookieProcessor()
url_opener = urllib2.build_opener(MyHTTPRedirectHandler, cookie_handler)
url_opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5')]

def scrape_html():
    all_entries = url_collection.find({'counter' : {'$exists' : True}}).sort('counter', DESCENDING)
    
    if all_entries.count() == 0:
        print 'No previous recursive request found'
        explored_set = set()
        url_queue = Queue()
        url_queue.put(url_to_scrape)
        begin_get(url_queue, explored_set, 0)
        return

    current_entry = all_entries[0]
    current_counter = current_entry['counter']

    url_array = current_entry['url_array']
    url_queue = Queue()
    for x in url_array:
        url_queue.put(x)

    explored_array = current_entry['explored_array']
    explored_set = set()
    for x in explored_array:
        explored_set.add(x)
    
    begin_get(url_queue, explored_set, current_counter)

    
    
def begin_get(url_queue, explored_set, current_counter):
    save_counter = 0
    while not url_queue.empty():
        save_counter += 1
        if save_counter > 50:
            current_counter = save_entry(explored_set, url_queue, current_counter)
            save_counter = 0
        url = url_queue.get()
        page = url_opener.open(url)
        html = page.read()
        url_path = url.split('/')

        """Finds new urls"""
        links = [x.group(1) for x in re.finditer(r'href="([^"]*)"', html)
        

    print 'finish'
    

    

def save_entry(explored_set, url_queue, counter):
    print "CURRENTLY SAVING POSITION. DO NOT QUIT"
    counter += 1
    explored_array = []
    for x in explored_set:
        explored_array.append(x)

    url_array = []
    while not current_queue.empty():
        url_array.append(current_queue.get())
    for x in url_array:
        current_queue.put(x)
        
    new_entry = {'counter' : counter, 'url_array' : url_array, 'explored_array' : explored_array}
    url_collection.insert(new_entry)
    print "CAN QUIT NOW"
    return counter


def to_bytestring (s, enc='utf-8'):
    """Convert the given unicode string to a bytestring, using the standard encoding,                                                                                                                     
    unless it's already a bytestring"""
    if s:
        if isinstance(s, str):
            return s
        else:
            return s.encode(enc)

"""Handles opening sites that force you to redirect. """
class MyHTTPRedirectHandler(urllib2.HTTPRedirectHandler):
    def http_error_302(self, req, fp, code, msg, headers):
        return urllib2.HTTPRedirectHandler.http_error_302(self, req, fp, code, msg, headers)
    http_error_301 = http_error_303 = http_error_307 = http_error_302








def __name__ == '__main__':
    scrape_html()
