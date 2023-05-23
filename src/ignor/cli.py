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
parser.add_argument("language", nargs='?', help="The language of the project you want to generate the gitignore file for.")
parser.add_argument("-l", "--list", help="List the languages that are supported.", action="store_true", required=False)


class Ignor:
    def __init__(self):
        try:
            self.languages = self.list_languages()
        except Exception as ex:
            print(ex)
            return 1

    @staticmethod
    def get_gitignore(language, url):
        headers = {"Accept": "application/vnd.github.raw"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.content
        else:
            raise Exception("Could not download gitignore file for language %s" % language)

    def list_languages(self):
        url = "https://api.github.com/repos/github/gitignore/branches/main"
        response = requests.get(url)
        languages = []
        if response.status_code == 200:
            response_json = response.json()
            sha = response_json.get("commit").get("commit").get("tree").get("sha")
            url_tree = f"https://api.github.com/repos/github/gitignore/git/trees/{sha}"
            response_tree = requests.get(url_tree)
            response_tree_json = response_tree.json()
            tree = response_tree_json.get("tree")
            for language in tree:
                path = language.get("path")
                url = language.get("url")
                if ".gitignore" in path:
                    languages.append({"name": path.split(".")[0], "url": url})

        else:
            raise Exception("Could not get a list of supported languages.")

        return languages

    @staticmethod
    def save_gitignore(content):
        path = os.path.join(os.getcwd(), ".gitignore")
        with open(path, "wb") as f:
            f.write(content)


def main(args=None):
    args = parser.parse_args(args=args)
    ignor = Ignor()
    if args.list:
        for lang in ignor.languages:
            try:
                print(lang["name"])
            except AttributeError:
                pass
        return 0
    elif args.language:
        for lang in ignor.languages:
            if args.language.lower() in lang["name"].lower():
                try:
                    content = ignor.get_gitignore(lang["name"], lang["url"])
                except Exception as ex:
                    print(ex)
                    return 1
                ignor.save_gitignore(content)
                print("Gitignore file generated for language %s" % lang["name"])
                return 0
        print(f"Language {args.language} not supported.")
        return 1
    else:
        parser.print_help()
        return 0
