
from flask import flash, render_template, redirect,url_for
from app.main import main
from app.models import Blog
from app.request import get_random_qoutes
from app.main.forms import BlogForm
from app import db
from flask_login import login_required



@main.route('/')
@main.route('/index')
def index():
    '''
    View function that sets index page
    '''
    title = 'Home'
    random_quote = get_random_qoutes()
    blogs = Blog.query.order_by(Blog.timestamp.desc()).all()
    return render_template('index.html', title=title, quotes=random_quote, blogs=blogs)



@main.route('/blog', methods=['GET','POST'])
@login_required
def createblog():
    '''
    View function that sets blog page
    '''
    title = 'Create blog'
    form = BlogForm()
    if form.validate_on_submit():
        blog = Blog(blog_title=form.blog_title.data, blog_post=form.blog_post.data,)
        db.session.add(blog)
        db.session.commit()
        flash('Blog has been created')
        return redirect(url_for('main.createblog'))
    blogs = Blog.query.order_by(Blog.timestamp.desc())
    return render_template('blog.html', title=title, form=form, blogs=blogs)


@main.route('/blog/delete/<int:id>')
def delete_blog_post(id):
    '''
    Function to delete blog post
    '''
    blog = Blog.query.filter_by(id=id).first()
    db.session.delete(blog)
    db.session.commit()
    flash(f'Blog {id} deleted')
    return redirect(url_for('main.createblog'))