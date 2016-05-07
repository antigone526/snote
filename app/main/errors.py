# -*- coding: utf-8 -*-
from flask import render_template
from . import main as MAIN

@MAIN.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html', title='page not found');

@MAIN.app_errorhandler(500)
def page_not_found(error):
    return render_template('500.html', title='internal Server Error');
