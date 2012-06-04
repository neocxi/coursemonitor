import urllib2
import re
from google.appengine.api import mail
from google.appengine.api import urlfetch

from application.models import MonitoredCourse
from application.helper import content_fetch, aval_fetch, inform_user


def monitor(*args, **kwargs):
	for course in MonitoredCourse.all().fetch(None):
		try:
			content = content_fetch(course.ccn)
			status, availability = aval_fetch(course.monitor_type, content)
			if availability is not course.availability:
				course.availability = availability
				course.status = status
				course.put()
				inform_user(course.user, course)
			elif status is not course.status:
				course.status = status
				course.put()
		except:
			pass




	return ['Done']