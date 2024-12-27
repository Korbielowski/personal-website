from flask import Flask, render_template
from os import listdir
import markdown

app = Flask(__name__)


class Content:
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
            articles.append(read_content(file))
    articles.sort(key=lambda c: c.date, reverse=True)
    return render_template("blog.html", articles=articles)


@app.route("/articles/<article_name>")
def articles(article_name: str):
    with open("blog/" + article_name + ".md", "r") as file:
        return render_template("article.html", article=read_content(file))


@app.route("/portfolio")
def portfolio():
    projects = []
    for project in listdir("projects/"):
        with open("projects/" + project, "r") as file:
            projects.append(read_content(file))
    projects.sort(key=lambda c: c.date, reverse=True)
    return render_template("portfolio.html", projects=projects)


@app.route("/projects/<project_name>")
def projects(project_name: str):
    with open("projects/" + project_name + ".md", "r") as file:
        return render_template("project.html", project=read_content(file))


def read_content(file) -> Content:
    file_name = (
        file.name.removesuffix(".md").removeprefix("blog/").removeprefix("projects/")
    )
    lines: list[str] = file.readlines()
    title = lines[0].split('"')[1]
    date = lines[1].split('"')[1]
    body = markdown.markdown("".join(lines[2:]), extensions=["extra"])
    return Content(file_name, title, date, body)
