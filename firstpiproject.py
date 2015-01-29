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
        elif item == "quizraspberry":
            self.redirect('/raspberrypi/quiz')

class QuizPiHandler(Handler):
    def get(self):
        self.render("quizraspberrypi.html")

    def post(self): 
        answer = self.request.get("answer")
        if answer != "three":
            self.render("quizraspberrypi.html", error='Try again :(')
        else :
            self.redirect("/raspberrypi/successone")

class SuccessOneHandler(Handler):
    def get(self):
        self.render("successone.html")
           
    def post(self):
        item = self.request.get("item")
        if item == "back2raspberry":
            self.redirect('/raspberrypi')
        elif item == 'gettingstarted':
            self.redirect('/gettingstarted')

class GettingStartedHandler(Handler):
    def get(self):
        self.render('gettingstarted.html')
  
    def post(self):
        item = self.request.get("item")
        if item == "back2raspberry":
            self.redirect('/raspberrypi')
        elif item == "checkparts":
            self.redirect('/gettingstarted/parts')

class PartsHandler(Handler):
    def get(self):
        self.render('parts.html')
  
    def post(self):
        
        item  = self.request.get("item")
        if item == "back2gettingstarted":
            self.redirect("/gettingstarted")
        elif item == "assemblingpi":
            self.redirect("/gettingstarted/parts/assemblingpi")

class AssemblingPiHandler(Handler):
    def get(self):
        self.render('assemblingpi.html')

    def post(self):
        item = self.request.get("item")
        if item == "back2parts":
            self.redirect("/gettingstarted/parts")
        elif item == "checkpirepheries":
            self.redirect("/gettingstarted/parts/pirepheries")

class PirepheriesHandler(Handler):
    def get(self):
        self.render('pirepheries.html')
   
    def post(self):
        item = self.request.get("item")
        if item == "back2parts":
            self.redirect("/gettingstarted/parts")
        elif item == "linuxandcli":
            self.redirect('/learninglinux')

class LearningLinuxHandler(Handler):
    def get(self):
        self.render('learninglinux.html')
    
    def post(self):
        item = self.request.get("item")
        if item == "back2gettingstarted":
            self.redirect("/gettingstarted")
        elif item == "quizlinux":
            self.redirect("/learninglinux/quiztwo")

class QuizLinuxHandler(Handler):
    def get(self):
        self.render("quizlinux.html")

    def post(self): 
        answer = self.request.get("answer")
        if answer != "two":
            self.render("quizlinux.html", error='Try again :(')
        else :
            self.redirect("/learninglinux/successtwo")

class CLIHandler(Handler):
    def get(self):
        self.render("cliintro.html")
 
    def post(self):
        item = self.request.get("item")
        if item == "back2learninglinux":
            self.redirect("/learninglinux")
        elif item == "quizcli":
            self.redirect("/learninglinux/cliintro/quizcli")


class SuccessTwoHandler(Handler):
    def get(self):
        self.render("successtwo.html")
           
    def post(self):
        item = self.request.get("item")
        if item == "back2linux":
            self.redirect('/learninglinux')
        elif item == 'learningcli':
            self.redirect('/learninglinux/cliintro')
   
class SuccessThreeHandler(Handler):
    def get(self):
        self.render("successthree.html")
           
    def post(self):
        item = self.request.get("item")
        if item == "back2linux":
            self.redirect('/learninglinux')
        elif item == 'learningcli':
            self.redirect('/commandsbasics')
 
class QuizCLIHandler(Handler):
    def get(self):
        self.render("quizcli.html")

    def post(self): 
        answer = self.request.get("answer")
        if answer != "three":
            self.render("quizcli.html", error='This is correct, but there is a better answer :)')
        else :
            self.redirect("/learninglinux/cliintro/successthree")

class CommandsBasicsHandler(Handler):
    def get(self):
        self.render("commandsbasics.html")

    def post(self): 
        item = self.request.get("item")
        if item == "back2learnlinux":
            self.redirect("/learninglinux")
        elif item == "bootingup":
            self.redirect("/bootingup")

class BootingUpHandler(Handler):
    def get(self):
        self.render('bootingup.html')
 
    def post(self):
        item = self.request.get("item")
        if item == "back2commandsbasics":
            self.redirect('/commandsbasics')
        elif item == 'games':
            self.redirect('/games')
 
class GamesHandler(Handler):
    def get(self):
        self.render("/games.html")

application = webapp2.WSGIApplication([('/', MainPage),
                                       ('/gettingstarted', GettingStartedHandler),
                                       ('/gettingstarted/parts', PartsHandler),
                                       ('/learninglinux', LearningLinuxHandler),
                                       ('/learninglinux/quiztwo', QuizLinuxHandler),
                                       ('/learninglinux/cliintro', CLIHandler),
                                       ('/learninglinux/cliintro/quizcli', QuizCLIHandler),
                                       ('/gettingstarted/parts/assemblingpi', AssemblingPiHandler),
                                       ('/gettingstarted/parts/pirepheries', PirepheriesHandler),
                                       ('/raspberrypi', RaspberryPiHandler),
                                       ('/raspberrypi/quiz', QuizPiHandler),
                                       ('/raspberrypi/successone', SuccessOneHandler),
                                       ('/learninglinux/successtwo', SuccessTwoHandler),
                                       ('/learninglinux/cliintro/successthree', SuccessThreeHandler),
                                       ('/commandsbasics', CommandsBasicsHandler),
                                       ('/bootingup', BootingUpHandler),
                                       ('/games', GamesHandler)],
                                       debug=True)
