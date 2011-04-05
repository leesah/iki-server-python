from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from models import Knowledge, User

SELF_CONFIDENCE = 0.6
DECREMENT_OF_UNKNOWN = 0.5

class MainPage(webapp.RequestHandler):
    
    
    def get(self):
        self.response.out.write('All users\n')
        users = User.all().fetch(1024)
        for u in users:
            self.response.out.write('%(u)s, %(c)s\n' % {'u':u.user, 'c':u.credits})
    
        self.response.out.write('All knowledges\n')
        knowledges = Knowledge.all().fetch(1024)
        for k in knowledges:
            self.response.out.write(k.user)
        
        
        
application = webapp.WSGIApplication([('/test', MainPage)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
