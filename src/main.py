from flask import Flask, render_template, render_template_string
import markdown
from flask_flatpages import FlatPages
from os import listdir
from datetime import datetime
import time


def render_links(text):
    prerendered_body = render_template_string(text)
    return markdown.markdown(prerendered_body, extensions=["pymdownx.tasklist"])


app = Flask(__name__)
app.config["FLATPAGES_AUTO_RELOAD"] = True
app.config["FLATPAGES_EXTENSION"] = ".md"
app.config["FLATPAGES_ROOT"] = "articles"
app.config["FLATPAGES_HTML_RENDERER"] = render_links
flat_pages = FlatPages(app)


@app.route("/")
def welcome_page():
    return render_template("welcome_page.html", year=datetime.now().year)


@app.route("/blog", defaults={"name": None})
@app.route("/blog/<name>")
def blog(name: str):
    year = datetime.now().year
    if name:
        article = flat_pages.get_or_404(f"blog/{name}")
        return render_template("article.html", article=article, year=year)
    articles = []
    for article in listdir("articles/blog/"):
        articles.append(flat_pages.get_or_404("blog/" + article.removesuffix(".md")))
    articles.sort(
        key=lambda c: time.mktime(time.strptime(c["date"], "%d.%m.%Y")),
        reverse=True,
    )
    return render_template("articles.html", articles=articles, year=year, is_blog=True)


@app.route("/portfolio", defaults={"name": None})
@app.route("/portfolio/<name>")
def portfolio(name: str):
    year = datetime.now().year
    if name:
        article = flat_pages.get_or_404(f"portfolio/{name}")
        return render_template("article.html", article=article, year=year)
    articles = []
    for article in listdir("articles/portfolio/"):
        articles.append(
            flat_pages.get_or_404("portfolio/" + article.removesuffix(".md"))
        )
    articles.sort(
        key=lambda c: time.mktime(time.strptime(c["date"], "%d.%m.%Y")),
        reverse=True,
    )
    return render_template("articles.html", articles=articles, year=year, is_blog=False)


if __name__ == "__main__":
    app.run()
