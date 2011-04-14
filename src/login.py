from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import users
from urllib import quote
    
class MainPage(webapp.RequestHandler):
    
    
    def get(self):
        urlToContinue = quote('&'.join(['='.join([k, v]) for (k, v) in self.request.params.iteritems()]).lstrip('continue='))
        self.response.out.write(urlToContinue)
        self.redirect(users.create_login_url(dest_url=urlToContinue, federated_identity='gmail.com'))


application = webapp.WSGIApplication([('/_ah/login_required', MainPage)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
