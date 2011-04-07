from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import users
    
class MainPage(webapp.RequestHandler):
    
    
    def get(self):
        p = self.request.params
        self.response.out.write(p)
        #self.redirect(users.create_login_url(dest_url='/welcome', federated_identity='gmail.com'))


application = webapp.WSGIApplication([('/_ah/login_required', MainPage)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
