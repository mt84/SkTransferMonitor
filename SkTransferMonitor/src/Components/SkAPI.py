'''
Created on May 2, 2013

@author: MT
'''
import cookielib
import urllib
import urllib2

class SkAPI(object):
    """Represent ABSTRACT SK API object."""
    def __init__(self, login, password):
        """ Initialize HTTP connection."""
        self.login = login
        self.password = password

        self.cj = cookielib.CookieJar()
        self.opener = urllib2.build_opener(
            urllib2.HTTPRedirectHandler(),
            urllib2.HTTPHandler(debuglevel=0),
            urllib2.HTTPSHandler(debuglevel=0),
            urllib2.HTTPCookieProcessor(self.cj)
        )
        self.opener.addheaders = [
            ('User-agent', ('Mozilla/4.0 (compatible; MSIE 6.0; '
                           'Windows NT 5.2; .NET CLR 1.1.4322)')),
            ('Accept-Charset', 'UTF-8')
        ]
        
    def skLogin(self, skURL):
        """Login to SK page."""
        login_data = urllib.urlencode({
            'ilogin' : self.login,
            'ipassword' : self.password,
        })
        self.opener.open(skURL, login_data)