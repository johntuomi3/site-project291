"""
Routes and views for the bottle application.
"""
import os
from bottle import route, view
import markdown
from datetime import datetime


@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(
        title='Contact',
        message='Your contact page.',
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='About',
        message='Your application description page.',
        year=datetime.now().year
    )

@route('/blog')
@view('blog')
def blog():
    md = markdown.Markdown(output_format='html5')
    """Renders the blog page."""
    for root, dirs, files in os.walk('static/blog'):
        for file in files:
            if file.endswith(".md"):
                f = open(os.path.join(root, file).replace('//','\\'),'r')
                content = f.read()
                content = md.convert(content)

                
                
        
    
    return dict(
        title='About',
        message='Your application description page.',
        year=datetime.now().year,
        blog_content= content
    )
    