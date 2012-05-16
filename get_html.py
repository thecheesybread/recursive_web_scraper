import urllib2
from pymongo import Connection

connection = Connection('localhost', 27017)




first_url = sys.argv[1]
save_file = open('1save_file', r)
counter = 0


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
