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
        self.render('about.html')

class SettingUpHandler(Handler):
    def get(self):
        self.render('settingup.html')

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
                                       ('/settingup', SettingUpHandler),
                                       ('/settingup/stepone', Step1Handler),
                                       ('/settingup/steptwo', Step2Handler),
                                       ('/settingup/stepthree', Step3Handler),
                                       ('/settingup/stepfour', Step4Handler)],
                                       debug=True)
