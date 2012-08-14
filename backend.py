
from application.models import MonitoredCourse
from application.helper import content_fetch, aval_fetch, inform_user
import logging


def monitor(*args, **kwargs):
	for course in MonitoredCourse.all().fetch(None):
		try:
			content = content_fetch(course.ccn)
			status, availability = aval_fetch(course.monitor_type, content)
			logging.info(status)
			if availability != course.availability:
				course.availability = availability
				course.status = status
				course.put()
				inform_user(course.user, course)
			elif status != course.status:
				course.status = status
				course.put()
		except Exception, e:
			return str(e)




	return 'done'