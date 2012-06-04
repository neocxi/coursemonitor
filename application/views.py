"""
views.py

URL route handlers

Note that any handler params must match the URL route params.
For example the *say_hello* handler, handling the URL route '/hello/<username>',
  must be passed *username* as the argument.

"""


from google.appengine.api import users
from google.appengine.runtime.apiproxy_errors import CapabilityDisabledError

from flask import render_template, flash, url_for, redirect

from models import *
from decorators import login_required, admin_required
from forms import CourseForm, SettingForm

from helper import *

def home():
    return redirect(url_for('list_courses'))


def say_hello(username):
    """Contrived example to demonstrate Flask's url routing capabilities"""
    return 'Hello %s' % username


@login_required
def list_courses():
    """List all courses"""
    # authorized_users = UserSetting.all()
    # if users.get_current_user not in authorized_users:
    #     flash(u'unauthorized user: %s' % users.get_current_user().email())
    #     return render_template('base.html', logout_url=users.create_logout_url("/"))


    monitored_courses = MonitoredCourse.all().filter('user =', users.get_current_user() ).fetch(10)
    form = CourseForm()

    if form.validate_on_submit():
        
        course = MonitoredCourse(
            ccn = form.ccn.data,
            user = users.get_current_user(),
            monitor_type = form.monitor_type.data
            
        )
        try:
            content = content_fetch(form.ccn.data)
            course.name = name_fetch(content)
            course.status, course.availability = aval_fetch(course.monitor_type, content)
            course.put()
            flash(u'Course %s successfully saved.' % course.name, 'success')
            return redirect('/')
        except:
            flash(u'Something wrong, check CCN.', 'info')
            return redirect('/')

    return render_template('list_courses.html', courses=monitored_courses, form=form, logged_in = True, logout_url = users.create_logout_url('/'))


@login_required
def delete_course(ccn):
    course = MonitoredCourse.all().filter('user =', users.get_current_user()).filter('ccn =', str(ccn)).fetch(1)[0]
    try:
        course.delete()
        flash(u'Course %s successfully deleted.' % ccn, 'success')
        return redirect(url_for('list_courses'))
    except CapabilityDisabledError:
        flash(u'App Engine Datastore is currently in read-only mode.', 'info')
        return redirect(url_for('list_courses'))

@login_required
def account_setting():
    return 'not functional yet'
    # return render_template('setting.html', form = SettingForm(), logged_in = True, logout_url = users.create_logout_url('/'))

@admin_required
def admin_only():
    """This view requires an admin account"""
    return 'Super-seekrit admin page.'


def warmup():
    """App Engine warmup handler
    See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests

    """
    return ''

