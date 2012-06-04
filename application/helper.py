import re
from google.appengine.api import urlfetch, mail, users
from models import UserSetting


name_regex = re.compile('<FONT FACE="Helvetica, Arial, sans-serif" SIZE=1><b>(\w+)<BR>(.*?)<\/a>')
enrolled_regex = re.compile('<blockquote>(\d+)\&nbsp\;student\(s\) \D+(\d+)')
wl_regex = re.compile('(\d+)\D*?waiting list\D+(\d+)')

def content_fetch(ccn = None):
	if ccn:
		url = "http://infobears.berkeley.edu:3400/osc/?_InField1=RESTRIC&_InField2=%s&_InField3=12D2" % ccn
		return urlfetch.fetch(url).content

def name_fetch(content = None):
	if content:
		return reduce(lambda x,y:x+y, 
					re.findall(name_regex, content)[0], '')

def aval_fetch(monitor_type = None, content = None):
	if monitor_type and content:
		if monitor_type == '1':
			enroll = re.findall(enrolled_regex, content)[0]
			aval = enroll[0] != enroll[1]
			status = "Available!" if aval else "Currently full."
			status+= "Enrolled %s out of a limit of %s" % enroll
		elif monitor_type == '2':
			enroll = re.findall(wl_regex, content)[0]
			aval = enroll[0] != enroll[1]
			status = "Available!" if aval else "Currently full."
			status+= "Waitlisted %s out of a limit of %s" % enroll
		else:
			aval = False
			status = 'stub'
		return status, aval

def inform_user(user, course):
	cell_mail = UserSetting.all().filter('user =', users.get_current_user()).fetch(1)[0]
	for email in (user.email(), cell_mail):
		if email:
			mail.send_email(sender="adslcx@gmail.com",
						to = email,
						subject = "%s now available!" % course.name,
						body = course.status)
