from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import users
from models import Knowledge, User
    
class MainPage(webapp.RequestHandler):
    
    
    def get(self):
        p = self.request.params.mixed()
        p['u'] = users.get_current_user().email()
        Knowledge(info=p['i'], location='%(a)s,%(o)s' % p).put()
        
        user = User.all().filter('user = ', p['u']).fetch(1)[0]
        user.location = '%(a)s,%(o)s' % p
        user.credits += 1
        if p['i'] == 'p':
            user.pains += 1
        else:
            user.fines += 1
        user.put()
        
        self.response.out.write('%(u)s reports %(i)s from %(a)s,%(o)s.' % p)


application = webapp.WSGIApplication([('/know', MainPage)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
