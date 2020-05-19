import datetime

from flask import render_template, redirect, url_for, request, abort, flash

from . import home
from .form import PostForm
from app.models import BlogModel
import markdown
import json


@home.route("/")
def index():
    return render_template("home/index.html")

@home.route("/blogs")
def blogs():
    today = datetime.date.today()
    alldata = BlogModel.get_all_public()
    return render_template("home/bloglist.html", alldata=alldata, today=today)
@home.route("/new", methods=["POST", "GET"])
def new():
    today = datetime.date.today()
    form = PostForm()
    if form.validate_on_submit():
        BlogModel.new_post(form.title.data, form.subtitle.data, form.content.data)
        return redirect(url_for("home.index"))
    return render_template("home/add.html", form=form, today=today)



@home.route("/manage")
def manage():
    today = datetime.date.today()
    alldata = BlogModel.get_manage_list()
    return render_template("home/manage.html", alldata=alldata, today=today)


@home.route("/get")
def get_article():
    today = datetime.date.today()
    id = request.args.get("id")
    if id is None:
        abort(404)
    article = BlogModel.get_article_by_id(id)
    #

    md = markdown.Markdown(
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ]
    )
    # article["content"] = markdown.markdown(article.get("content"),
    #     extensions=[
    #     # 包含 缩写、表格等常用扩展
    #     'markdown.extensions.extra',
    #     # 语法高亮扩展
    #     'markdown.extensions.codehilite',
    #     ])
    article["content"] = md.convert(article["content"])
    print(md.toc)
    return render_template("home/blogdetail.html", article=article, today=today, toc=md.toc)



@home.route("/edit", methods=["POST", "GET"])
def edit():

    today = datetime.date.today()
    id = request.args.get("id")
    if id is None:
        abort(404)
    article = BlogModel.get_article_by_id(id)
    form = PostForm()
    if form.validate_on_submit():
        BlogModel.new_post(form.title.data, form.subtitle.data, form.content.data)
        return redirect(url_for("home.index"))
    content = json.dumps(article["content"])
    return render_template("home/change.html", form=form, article=article, content=content, today=today)


@home.route("/delete")
def delete():
    id = request.args.get("id")
    if id is None:
        abort(404)
    status = BlogModel.delete_by_id(int(id))
    if status is False:
        flash("找不到该条数据，删除失败")
    else:
        flash("数据已经被删除")
    return redirect(url_for('home.manage'))

@home.route("/test")
def test():
    return render_template("home/bloglist.html")


@home.route("/about")
def about():
    return render_template("home/about.html")


@home.route("/contact")
def contact():
    return render_template("home/contact.html")


@home.route("/service")
def service():
    return render_template("home/service.html")