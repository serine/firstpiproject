import os, webapp2, jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainPage(Handler):
    def get(self):
        #items = self.request.get_all("food")
        self.render('home.html')
   
    def post(self):
        self.redirect('/raspberrypi')

class RaspberryPiHandler(Handler):
    def get(self):
        self.render('raspberrypi.html')

    def post(self):
        item = self.request.get("item")
        if item == "back2home":
            self.redirect("/")
        elif item == "gettingstarted":
            self.redirect('/gettingstarted')

class GettingStartedHandler(Handler):
    def get(self):
        self.render('gettingstarted.html')
  
    def post(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        item = self.request.get("item")
        if item == "one":
            self.redirect('/gettingstarted/parts')
        elif item == "two":
            self.redirect('/learninglinux')

class PartsHandler(Handler):
    def get(self):
        self.render('parts.html')
  
    def post(self):
        
        item  = self.request.get("item")
        if item == "back2gettingstarted":
            self.redirect("/gettingstarted")

class LearningLinuxHandler(Handler):
    def get(self):
        self.render('learninglinux.html')

class AssemblingPiHandler(Handler):
    def get(self):
        self.render('assemblingpi.html')

    def post(self):
        item = self.request.get("item")
        if item == "back2parts":
            self.redirect("/gettingstarted/parts")
        elif item == "checkpirepheries":
            self.redirect("/gettingstarted/pirepheries")

class PirepheriesHandler(Handler):
    def get(self):
        self.render('pirepheries.html')
   
    def post(self):
        item = self.request.get("item")
        if item == "back2parts":
            self.redirect("/gettingstarted/parts")
          
class Step4Handler(Handler):
    def get(self):
        self.render('stepfour.html')


application = webapp2.WSGIApplication([('/', MainPage),
                                       ('/gettingstarted', GettingStartedHandler),
                                       ('/gettingstarted/parts', PartsHandler),
                                       ('/learninglinux', LearningLinuxHandler),
                                       ('/gettingstarted/assemblingpi', AssemblingPiHandler),
                                       ('/gettingstarted/pirepheries', PirepheriesHandler),
                                       ('/raspberrypi', RaspberryPiHandler)],
                                       debug=True)
