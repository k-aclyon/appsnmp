appsnmp
=======

Application web à l'aide de l'outil python-flask.


Cette application spécifique permet de récupérer certaines information snmp sur des routeurs distant à partir d'un adresse ip envoyée. Elle les compare avec les même données stockées dans une base de données MySQL.

appsnmp.py : programme principal

daemon.py : programme permettant de lancer l'application en tant que service avec gestion du pid

static : répertoire contenant les images, css

templates : contient les templates des pages web

utils.py : script de modules chargés par l'application principale. Notamment les fonctions permettant d'interroger la base de données ainsi que celle interrogeant les routeurs à l'aide de la commande snmpwalk. Je n'ai pas utilisé de module snmp faute d'en avoir trouver un qui fonctionne comme je le voulais.
