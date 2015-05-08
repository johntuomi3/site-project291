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

last_10_blogs = []

@route('/blog')
@view('blog_index')
def blogIndex():
    content = ''

    """Renders the blog page."""
    for root, dirs, files in os.walk('static/blog'):
        for file in files:
            if file.endswith(".md"):
                blog_link = str("<a href='%s'>%s</a>" %('/static/blog/%s'%(file),str(file).replace(".md",'')))
                if blog_link not in last_10_blogs:
                    last_10_blogs.append(blog_link)
    return dict(
                title='Blog',
                message='Blog Index Page.',
                year=datetime.now().year,
                blog_content= content,
                last_10 = last_10_blogs
                )
    

@route('/static/blog/<filename>')
@view('blog_page')
def blogPage(filename):
    print(filename)
    md = markdown.Markdown(output_format='html5')
    for root, dirs, files in os.walk('static/blog'):
        for file in files:
            if file == filename:
                f = open('static/blog/%s' % (file),'r')
                content = f.read()
                content = md.convert(content)
                f.close()
    return dict(
                title=str(filename).replace('.md',''),
                message='Blog Page',
                year=datetime.now().year,
                blog_content= content,
                last_10 = last_10_blogs
                )
    
