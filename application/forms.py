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
	cell_mail_map = """[(u'{number}@txt.voice.google.com', u'google_voice'), (u'{number}@mymetropcs.com', u'metro_pcs'), (u'{number}@messaging.nextel.com', u'nextel'), (u'{number}@page.att.net', u'at_and_t_paging'), (u'{number}@utext.com', u'unicel'), (u'{number}@sms.bluecell.com', u'bluegrass'), (u'{number}@blueskyfrog.com', u'blueskyfrog'), (u'{number}@cingular.com', u'cingular'), (u'{number}@messaging.sprintpcs.com', u'sprint'), (u'{number}@sms.smartmessagingsuite.com', u'at_and_t_global_sms'), (u'{number}@cellcom.quiktxt.com', u'cellcom'), (u'{number}@sms.cvalley.net', u'chariton_valley'), (u'{number}@myhelio.com', u'helio'), (u'{number}@bellsouth.cl', u'bellsouth'), (u'{number}@myboostmobile.com', u'boostmobile'), (u'{number}@smtext.com', u'simple_mobile'), (u'{number}@psms.bluesky.as', u'bluesky'), (u'{number}@echoemail.net', u'esendex'), (u'{number}@gocbw.com', u'cincinnati_bell'), (u'{number}@vmobl.com', u'virgin_mobile'), (u'{number}@zsend.com', u'pioneer'), (u'{number}@email.uscc.net', u'us_cellular'), (u'{number}@usamobility.net', u'usa_mobility'), (u'{number}@vtext.com', u'verizon_wireless'), (u'{number}@vtext.com', u'pageplus'), (u'{number}@page.southernlinc.com', u'southernlink'), (u'{number}@iwirelesshometext.com', u'iwireless_sprint'), (u'{number}@sms.xit.net', u'xit_comm'), (u'{number}@gscsms.com', u'golden_state'), (u'{number}@sms.mycricket.com', u'cricket'), (u'{number}@mmst5.tracfone.com', u'tracfone'), (u'{number}@rinasms.com', u'syringa'), (u'{number}@qwestmp.com', u'qwest'), (u'{number}@mobile.kajeet.net', u'kajeet'), (u'{number}@cwemail.com', u'centennial_wireless'), (u'{number}@txt.att.net', u'at_and_t'), (u'{number}@sms.pscel.com', u'psc_wireless'), (u'{number}@tmomail.net', u't_mobile'), (u'{number}@rinasms.com', u'south_central'), (u'{number}@comcastpcs.textmsg.com', u'comcast_pcs'), (u'{number}@txt.att.net', u'at_and_t_mobility'), (u'{number}@csouth1.com', u'cellularsouth'), (u'{number}@message.alltel.com', u'alltel'), (u'{number}.iws@iwspcs.net', u'iwireless_tmobile'), (u'{number}@pcs.rogers.com', u'rogers_wireless'), (u'{number}@vtext.com', u'straight_talk'), (u'{number}@sms.elementmobile.net', u'element'), (u'{number}@teleflip.com', u'teleflip'), (u'{number}@sms.cleartalk.us', u'cleartalk'), (u'{number}@msg.acsalaska.com', u'alaska_communications'), (u'{number}@sms.alltelwireless.com', u'alltel_allied'), (u'{number}@msg.telus.com', u'telus_mobility'), (u'{number}@paging.acswireless.com', u'ameritech'), (u'{number}@viaerosms.com', u'viaero'), (u'{number}@mobile.gci.net', u'general_comm')]"""
	cell = wtf.TextField('Cell Phone Number', validators=[validators.Length(10,10)])
	provider = wtf.SelectField('Provider', choices = cell_mail_map)
		