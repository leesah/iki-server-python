from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import users
from models import User
    
class MainPage(webapp.RequestHandler):
    
    
    def get(self):
        user = users.get_current_user()
        if User.all().filter('user = ', user).count(1) == 0:
            User(credits = 0, fines = 0, pains = 0).put()
        self.response.out.write('Welcome %(u)s. <a href="/">Back</a>' % {'u':user})


application = webapp.WSGIApplication([('/welcome', MainPage)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
