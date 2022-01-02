help = """

Le projet a bien été créé !

Pour initaliser l'environnement et installer les outils :

   $ cd {{cookiecutter.repo_name}}
   $ poetry install
   $ pip install -e

Pour créer faire du versionning :
   
   $ git init -b master
   $ git add . 
   $ git commit -m 'initial commit'
"""
print(help)
