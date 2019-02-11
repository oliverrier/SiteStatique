# SiteStatique

## Présentation du projet

Ce projet à pour but de convertir un dossier de fichiers écrits en markdown en fichiers HTML.

## Fonctionnement du programme

Le programme utilise le package ![markdown2](https://github.com/trentm/python-markdown2) du Python Package Index.
Voici comment l'installer:

```bash
pip install -r requirement.txt
```

Il fonctionne en ligne de commande, voici un exemple:

```bash
program.py -i MarkdownFiles -o HtmlFiles
```

On appelle le programme avec `program.py`.
Voici les arguments que l'on peut passer dans notre commande:

Argument version courte | Argument version longue | Explications
------------ | ------------- |-----------
-h | --help | Affiche tous les arguments possibles et vous explique comment les utiliser
-i | --input-directory | Dossier contenant les fichiers Markdown
-o | --output-directory | Dossier destination pour les fichiers HTML

Vous aurez chaque fichier markdown converti en fichier HTML dans le dossier destination.