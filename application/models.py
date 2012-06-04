"""
models.py

App Engine datastore models

"""


from google.appengine.ext import db


class ExampleModel(db.Model):
    """Example Model"""
    example_name = db.StringProperty(required=True)
    example_description = db.TextProperty(required=True)
    added_by = db.UserProperty()
    timestamp = db.DateTimeProperty(auto_now_add=True)

class MonitoredCourse(db.Model):
    user = db.UserProperty(required=True)
    ccn = db.StringProperty(required=True)
    name = db.StringProperty()
    status = db.StringProperty()
    availability = db.BooleanProperty()
    date = db.DateTimeProperty(auto_now_add = True)
    monitor_type = db.StringProperty(required=True)
    # for type: "1" = monitor actual enrollment
    # "2" = monitor enroll, "other" monitors "other" reserved seating

class UserSetting(db.Model):
	user = db.UserProperty(required=True)
	cell_mail = db.StringProperty()
		
		
