import argparse
import os
import requests
import json

parser = argparse.ArgumentParser(description="Generate a gitignore file for a specific language.")
parser.add_argument("language", nargs='?', help="The language of the project you want to generate the gitignore file for.")
parser.add_argument("-l", "--list", help="List the languages that are supported.", action="store_true", required=False)


class Ignord:
    def __init__(self):
        self.root = self.get_root()
        self.languages = self.get_languages()
          
    def get_root(self):
        url = "https://api.github.com/repos/github/gitignore/branches/main"
        response = requests.get(url)
        if response.status_code == 200:
            response_json = response.json()
            sha = response_json.get("commit").get("commit").get("tree").get("sha")
            root = self.get_tree(sha)
        else:
            raise Exception("Could not get file structure.")
        return root
      
    def get_languages(self):
        root = os.path.dirname(__file__)
        path = os.path.join(root, ".ignors")
        if os.path.exists(path) and os.stat(path).st_size > 0:
            with open(path, "r") as _file:
                langs = json.load(_file)
                return langs
        else:
            languages = self.traverse_tree_append(self.root)
            with open(path, "w") as _file:
                json.dump(languages, _file)
            return languages
          
    
    def get_tree(self, sha):
        url_tree = f"https://api.github.com/repos/github/gitignore/git/trees/{sha}"
        response_tree = requests.get(url_tree)
        if response_tree.status_code == 200:
            response_tree_json = response_tree.json()
            tree = response_tree_json.get("tree")
        else:
            raise Exception("Could not get tree.")
        return tree

    def get_gitignore(self, language, url):
        headers = {"Accept": "application/vnd.github.raw"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.content
        else:
            raise Exception("Could not download gitignore file for language %s." % language)
        
    def traverse_tree_append(self, tree, languages=None):
        languages = languages if languages else []
        for language in tree:
            path = language.get("path")
            url = language.get("url")
            if language.get("type") == "tree":
                child_tree = self.get_tree(language.get("sha"))
                languages = self.traverse_tree_append(child_tree, languages)
                continue
            if ".gitignore" in path:
                languages.append({"name": path.split(".")[0], "url": url})
        return languages

    @staticmethod
    def save_gitignore(content):
        path = os.path.join(os.getcwd(), ".gitignore")
        with open(path, "wb") as f:
            f.write(content)


def main(args=None):
    args = parser.parse_args(args=args)
    try:
        ignord = Ignord()
    except Exception as ex:
        print(ex)
        return 1
    if args.list:
        for lang in ignord.languages:
            try:
                print(lang["name"])
            except AttributeError:
                pass
        return 0
    elif args.language:
        for lang in ignord.languages:
            if args.language.lower() in lang["name"].lower():
                try:
                    content = ignord.get_gitignore(lang["name"], lang["url"])
                except Exception as ex:
                    print(ex)
                    return 1
                ignord.save_gitignore(content)
                print("Gitignore file generated for language %s" % lang["name"])
                return 0
        print(f"Language {args.language} not supported.")
        return 1
    else:
        parser.print_help()
        return 0
