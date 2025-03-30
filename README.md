# tp_unsecure_chat

Prise en main

    Q1 : Que pensez-vous de la confidentialité des données vis à vis du serveur ?
    A1 :Les données ne sont pas chiffrés sur le serveur, on peut les voir passer de manière transparente ce qui n'est pas très sécurisé
    
    Q2 : Pouvez vous expliquer en quoi la sérialisation pickle est certainement le plus mauvais choix ?
    A2 :La sérialisation pickle est un mauvais choix car les données ne sont pas chiffrées et on pourra pas vérifier si les données ont été altérées entre l'envoie et la reception. En plus le pickle peut venir lancer du code python a notre insu

    Q3 : Quels types de sérialisation pourrait-on utiliser pour éviter cela ? (hors CVE)
    A3 : On pourrait utiliser JSON ou msgpack(utilisé plus loin dans le TP)

Authenticated Encryption

    Q4 : Pourquoi le chiffrement seul est-il insuffisant ?
    A4 : en chiffrant le message on peut s'assurer de sa confidentialité mais on peut pas empecher un attaquant de venir modifier notre message

    Q5 : Quelle fonction(s?) en python permet de générer un salt avec une qualité cryptographique ?
    A5 : la fct os.urandom() permet la creation d'un salt de qualité cryptographique

    Q6 : Faudra t-il transmettre le salt comme champ en clair supplémentaire du paquet message ?
    A6 : Afin de confirmer la key a la reception il faudra utiliser le salt donc oui il est necessaire de transmettre le salt en clair

    Q7 : Que constatez-vous côté serveur ?
    A7 : On ne peut plus comprendre les messages car ils sont chiffré , on voit aussi le salt en lair que l'on fait passer avec le message

    Q8 : Que peux faire le serveur si il est malveillant sur les messages ?
    A8 : S'il est malveillant le serveur peut modifier le contenue de nos messages afin de les rendre illisibles après le déchiffrement à la reception

Authenticated Encryption with Associated Data

    Q9 : Que faudrait-il faire en théorie pour éviter l’action du rogue server ? Pourquoi Fernet n’est pas adapté dans ce cadre ?
    A9 : Il faudrait mettre en place une signature numérique. Fernet n'est pas adapté car il ne permet pas de vérifier que le message n'a pas été altéré durant le transit

    Q10 : Dans la pratique, quelle solution simple et sous optimal peut-on mettre en place afin de conserver Fernet ?
    A10 : On peut utiliser un nickname associer au message, alors si le message est altéré puis renvoyé par le rogue serveur le message n'aura plus le meme nickname associé. Donc si le nickname est modifé alors le message a été altéré