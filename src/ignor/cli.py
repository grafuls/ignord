"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -mignor` python will execute
    ``__main__.py`` as a script. That means there will not be any
    ``ignor.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there"s no ``ignor.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import argparse
import os

import requests

parser = argparse.ArgumentParser(description="Generate a gitignore file for a specific language.")
parser.add_argument("language", help="The language of the project you want to generate the gitignore file for.", default="python")


def get_gitignore(language):
    url = "https://raw.githubusercontent.com/github/gitignore/master/%s.gitignore" % language.capitalize()
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception("Could not download gitignore file for language %s" % language)


def save_gitignore(language, content):
    path = os.path.join(os.getcwd(), ".gitignore")
    with open(path, "wb") as f:
        f.write(content)


def main(args=None):
    args = parser.parse_args(args=args)
    content = get_gitignore(args.language)
    save_gitignore(args.language, content)
    print("Gitignore file generated for language %s" % args.language)
