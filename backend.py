import urllib2
import re
from google.appengine.api import mail
from google.appengine.api import urlfetch

from monitor import MonitoredCourses


def app(*args, **kwargs):
	regex_enrolled = re.compile("<blockquote>(\d+)\&nbsp\;student\(s\) \D+(\d+)")
	regex_wl = re.compile("(\d+)\D*?waiting list\D+(\d+)")
	for course in MonitoredCourses.all():
		url = "http://infobears.berkeley.edu:3400/osc/?_InField1=RESTRIC&_InField2=%s&_InField3=12D2" % course.ccn
		result = urlfetch.fetch(url).content

		try:
			enroll = re.findall(regex_enrolled, result)[0]
			wl = re.findall(regex_wl, result)[0]

			# tentative strategy
			if enroll[0] is not enroll[1]:
				# inform certain user
				mail.send_mail(sender="adslcx@gmail.com",
								to=course.user.email(),
								subject="Course availbility",
								body=result)
		except:
			pass

	return ['Done']