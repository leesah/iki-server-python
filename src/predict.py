from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from models import Knowledge, Knower

SELF_CONFIDENCE = 0.9
DECREMENT_OF_UNKNOWN = 0.5

class MainPage(webapp.RequestHandler):
    
    
    def get(self):
        latitude = float(self.request.get('a'))
        longitude = float(self.request.get('o'))
        bottomLeft = '%(a)f,%(o)f' % {'a':latitude - 1, 'o':longitude - 1}
        topRight = '%(a)f,%(o)f' % {'a':latitude + 1, 'o':longitude + 1}

        # All knowers in this region
        knowers = Knower.all().filter('location > ', bottomLeft).filter('location > ', topRight).fetch(1024)
    
        # All knowledges in this region
        knowledges = Knowledge.all().filter('location > ', bottomLeft).filter('location > ', topRight)
        
        # All pains
        pains = knowledges.filter('info = ', 'p').fetch(1024)
        painCredits = dict()
        for k in pains: painCredits[k.account] = Knower.all().filter('account = ', k.account).fetch(1)[0].credits
        wet = 0
        for c in painCredits.values(): wet += c
        
        # All fines
        fines = knowledges.filter('info = ', 'f').fetch(1024)
        fineCredits = dict()
        for k in fines: fineCredits[k.account] = Knower.all().filter('account = ', k.account).fetch(1)[0].credits
        dry = 0
        for c in fineCredits.values(): dry += c
        
        # All unknowns
        unknownCredits = dict()
        for k in knowers:
            if not painCredits.has_key(k) and not fineCredits.has_key(k): unknownCredits[k.account] = k.credits
        unknown = 0
        for c in unknownCredits.values(): unknown += c * DECREMENT_OF_UNKNOWN
        
        self.response.out.write(wet / (wet + dry + unknown) * SELF_CONFIDENCE)
            
        
application = webapp.WSGIApplication([('/predict', MainPage)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
