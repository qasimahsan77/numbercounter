"""
Definition of urls for NumberCountAPI.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

urlpatterns = [
    # Examples:url(r'^$', app.views.home, name='home'),
    #url('^$',app.views.home),
    url(r'^countnumber$', app.views.countnumber),
]
