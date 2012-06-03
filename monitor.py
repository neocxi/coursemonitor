import webapp2

from google.appengine.ext import db
from google.appengine.api import users


authorized_users = ['adslcx@gmail.com']
class MonitoredCourses(db.Model):
    user = db.UserProperty(required=True)
    ccn = db.IntegerProperty(required=True)
    date = db.DateTimeProperty(auto_now_add = True)
# todo: refactor display and incoproate css and stuff 
class MainPage(webapp2.RequestHandler):
    def get(self):
        curr_user = users.get_current_user()
        if curr_user:
           if str(curr_user.email()) not in authorized_users: #insecure 
              self.response.out.write('Unauthorized user.%s <br />' % curr_user.email())
              self.response.out.write('<a href="%s">logout</a>' % users.create_logout_url(self.request.uri))

              return
        else:
           self.redirect(users.create_login_url(self.request.uri))

        courses_monitored = MonitoredCourses.all().filter('user =', curr_user)
        self.response.out.write("<html> <body> <ol>")
        for course in courses_monitored:
            self.response.out.write("<li> CCN: %s, Date added: %s </li>" % (course.ccn, course.date))
        self.response.out.write("</ol>")

        self.response.out.write("""
          <form action="/append" method="post">
            <div><textarea name="ccn" rows="1" cols="9"></textarea></div>
            <div><input type="submit" value="submit new course"></div>
          </form>
          <hr>
          <a href="%s"> logout </a>
        </body>
      </html>""" % users.create_logout_url(self.request.uri))

class AddCourse(webapp2.RequestHandler):
    """docstring for Add_course"""
    def post(self):

        new_course = MonitoredCourses(user = users.get_current_user(), 
                                ccn = int(self.request.get('ccn')))
        new_course.put()
        self.redirect('/')

app = webapp2.WSGIApplication([('/', MainPage),
                                ('/append', AddCourse)], debug = True)
        



        

            



