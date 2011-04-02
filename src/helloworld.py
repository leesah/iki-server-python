from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from urllib import urlopen
from json import loads

class MainPage(webapp.RequestHandler):
    
    
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, webapp World!')
        result = urlopen('http://maps.googleapis.com/maps/api/geocode/json?latlng=40.714224,-73.961452&sensor=true').read()
        self.response.out.write(result)


application = webapp.WSGIApplication([('/', MainPage)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
