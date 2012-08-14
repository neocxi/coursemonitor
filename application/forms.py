"""
forms.py

Web forms based on Flask-WTForms

See: http://flask.pocoo.org/docs/patterns/wtforms/
     http://wtforms.simplecodes.com/

"""

from flaskext import wtf
from flaskext.wtf import validators


class ExampleForm(wtf.Form):
    example_name = wtf.TextField('Name', validators=[validators.Required()])
    example_description = wtf.TextAreaField('Description', validators=[validators.Required()])

class CourseForm(wtf.Form):
	"""docstring for CourseForm"""
	ccn = wtf.TextField('Course Control Number', validators=[validators.Length(5,5)])
	monitor_type = wtf.SelectField(u'What to monitor', choices=[('1', 'Enrolled Slot'), 
																('2', 'Waitlist Slot')])
	# custom monitor type according to seat division
		
class SettingForm(wtf.Form):
	"""docstring for SettingFOrm"""
	cell_mail_map = [(u'@txt.voice.google.com', u'google_voice'), (u'@mymetropcs.com', u'metro_pcs'), (u'@messaging.nextel.com', u'nextel'), (u'@page.att.net', u'at_and_t_paging'), (u'@utext.com', u'unicel'), (u'@sms.bluecell.com', u'bluegrass'), (u'@blueskyfrog.com', u'blueskyfrog'), (u'@cingular.com', u'cingular'), (u'@messaging.sprintpcs.com', u'sprint'), (u'@sms.smartmessagingsuite.com', u'at_and_t_global_sms'), (u'@cellcom.quiktxt.com', u'cellcom'), (u'@sms.cvalley.net', u'chariton_valley'), (u'@myhelio.com', u'helio'), (u'@bellsouth.cl', u'bellsouth'), (u'@myboostmobile.com', u'boostmobile'), (u'@smtext.com', u'simple_mobile'), (u'@psms.bluesky.as', u'bluesky'), (u'@echoemail.net', u'esendex'), (u'@gocbw.com', u'cincinnati_bell'), (u'@vmobl.com', u'virgin_mobile'), (u'@zsend.com', u'pioneer'), (u'@email.uscc.net', u'us_cellular'), (u'@usamobility.net', u'usa_mobility'), (u'@vtext.com', u'verizon_wireless'), (u'@vtext.com', u'pageplus'), (u'@page.southernlinc.com', u'southernlink'), (u'@iwirelesshometext.com', u'iwireless_sprint'), (u'@sms.xit.net', u'xit_comm'), (u'@gscsms.com', u'golden_state'), (u'@sms.mycricket.com', u'cricket'), (u'@mmst5.tracfone.com', u'tracfone'), (u'@rinasms.com', u'syringa'), (u'@qwestmp.com', u'qwest'), (u'@mobile.kajeet.net', u'kajeet'), (u'@cwemail.com', u'centennial_wireless'), (u'@txt.att.net', u'at_and_t'), (u'@sms.pscel.com', u'psc_wireless'), (u'@tmomail.net', u't_mobile'), (u'@rinasms.com', u'south_central'), (u'@comcastpcs.textmsg.com', u'comcast_pcs'), (u'@txt.att.net', u'at_and_t_mobility'), (u'@csouth1.com', u'cellularsouth'), (u'@message.alltel.com', u'alltel'), (u'.iws@iwspcs.net', u'iwireless_tmobile'), (u'@pcs.rogers.com', u'rogers_wireless'), (u'@vtext.com', u'straight_talk'), (u'@sms.elementmobile.net', u'element'), (u'@teleflip.com', u'teleflip'), (u'@sms.cleartalk.us', u'cleartalk'), (u'@msg.acsalaska.com', u'alaska_communications'), (u'@sms.alltelwireless.com', u'alltel_allied'), (u'@msg.telus.com', u'telus_mobility'), (u'@paging.acswireless.com', u'ameritech'), (u'@viaerosms.com', u'viaero'), (u'@mobile.gci.net', u'general_comm')]
	cell = wtf.TextField('Cell Phone Number', validators=[validators.Length(10,10)])
	provider = wtf.SelectField('Provider', choices = cell_mail_map)
		