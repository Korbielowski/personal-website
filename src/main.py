from flask import Flask, render_template
from os import listdir
import toml

app = Flask(__name__)


class Project:
    def __init__(self, file_name, title, h, body):
        self.file_name = file_name
        self.title = title
        self.h = h
        self.body = body


class Article:
    def __init__(self, file_name, title, date, body):
        self.file_name = file_name
        self.title = title
        self.date = date
        self.body = body


@app.route("/")
def welcome_page():
    return render_template("welcome_page.html")


@app.route("/blog")
def blog():
    articles = []
    for article in listdir("blog/"):
        with open("blog/" + article, "r") as file:
            articles.append(read_article(file))
    articles.sort(key=lambda a: a.date, reverse=True)
    return render_template("blog.html", articles=articles)


@app.route("/article/<article_name>")
def article(article_name: str):
    with open("blog/" + article_name + ".toml", "r") as file:
        return render_template("article.html", article=read_article(file))


@app.route("/portfolio")
def portfolio():
    projects = []
    for article in listdir("projects/"):
        with open("projects/" + article, "r") as file:
            projects.append(read_project(file))
    projects.sort(key=lambda p: p.date, reverse=True)
    return render_template("portfolio.html", projects=projects)


@app.route("/project/<project_name>")
def project(project_name: str):
    with open("projects/" + project_name + ".toml", "r") as file:
        return render_template("project.html", project_name=read_project(file))


def read_project(file) -> Project:
    article_file = toml.load(file)
    file_name = file.name.removesuffix(".toml").removeprefix("blog/")
    title = article_file["article-data"]["title"]
    date = article_file["article-data"]["date"]
    body = article_file["article"]["body"]
    return Project(file_name, title, date, body)


def read_article(file) -> Article:
    article_file = toml.load(file)
    file_name = file.name.removesuffix(".toml").removeprefix("blog/")
    title = article_file["article-data"]["title"]
    date = article_file["article-data"]["date"]
    body = article_file["article"]["body"]
    return Article(file_name, title, date, body)
