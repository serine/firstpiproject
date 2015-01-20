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
        self.redirect('/gettingstarted')

class SettingUpHandler(Handler):
    def get(self):
        self.render('gettingstarted.html')
   
class Step1Handler(Handler):
    def get(self):
        self.render('stepone.html')

class Step2Handler(Handler):
    def get(self):
        self.render('steptwo.html')

class Step3Handler(Handler):
    def get(self):
        self.render('stepthree.html')

class Step4Handler(Handler):
    def get(self):
        self.render('stepfour.html')


application = webapp2.WSGIApplication([('/', MainPage),
                                       ('/gettingstarted', SettingUpHandler),
                                       ('/gettingstarted/stepone', Step1Handler),
                                       ('/gettingstarted/steptwo', Step2Handler),
                                       ('/gettingstarted/stepthree', Step3Handler),
                                       ('/gettingstarted/stepfour', Step4Handler),
                                       ('/raspberrypi', RaspberryPiHandler)],
                                       debug=True)
