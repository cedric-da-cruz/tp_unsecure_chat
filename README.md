# tp_unsecure_chat

Prise en main

    Q1 : Que pensez-vous de la confidentialité des données vis à vis du serveur ?
    A1 :Les données ne sont pas chiffrés sur le serveur, on peut les voir passer de manière transparente ce qui n'est pas très sécurisé
    
    Q2 : Pouvez vous expliquer en quoi la sérialisation pickle est certainement le plus mauvais choix ?
    A2 :La sérialisation pickle est un mauvais choix car les données ne sont pas chiffrées et on pourra pas vérifier si les données ont été altérées entre l'envoie et la reception. En plus le pickle peut venir lancer du code python a notre insu

    Q3 : Quels types de sérialisation pourrait-on utiliser pour éviter cela ? (hors CVE)
    A3 : On pourrait utiliser JSON ou msgpack(utilisé plus loin dans le TP)
