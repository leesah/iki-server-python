from __future__ import with_statement
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import users
from models import Knower
    
class MainPage(webapp.RequestHandler):
    
    
    def get(self):
        account = users.get_current_user()
        if account == None:
            self.redirect(users.create_login_url(dest_url='/main', federated_identity='gmail.com'))
        else:
            if Knower.all().filter('account = ', account).count(1) == 0:
                Knower(credits = 0, fines = 0, pains = 0).put()
                
            with open("main.html") as f:
                for line in f:
                    self.response.out.write(line)
        

application = webapp.WSGIApplication([('/main', MainPage)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
