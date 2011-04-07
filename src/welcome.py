from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import users
from models import Knower
    
class MainPage(webapp.RequestHandler):
    
    
    def get(self):
        account = users.get_current_user()
        if Knower.all().filter('account = ', account).count(1) == 0:
            Knower(credits = 0, fines = 0, pains = 0).put()
        self.response.out.write('Welcome %(a)s. <a href="/">Back</a>' % {'a':account})


application = webapp.WSGIApplication([('/welcome', MainPage)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
