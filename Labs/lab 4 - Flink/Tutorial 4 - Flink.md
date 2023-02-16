# Lab 4 - Stream Processing avec Flink 🐿

## 📦Mise en place

Récupérez le code du TP sur git/moodle. Aller dans le dossier `lab 4 - Flink/docker` et lancez un cluster Flink avec la commande `docker compose up`. Votre cluster sera composé d'un `JobManager` et de 2 `TaskManager`. Rendez-vous sur url `localhost:8081` pour accédez à l'interface de Flink. Ici vous pourrez voir les jobs exécutés

Pour lancer un script lors du TP:

1. Mettez vos fichiers dans le dossier `codes` qui s'est crée lors de la création de votre cluster. Ce dossier est un volume docker et pointe vers le dossier `/opt/flink/code` dans le `JobManager`
2. Connectez vous au `JobManager` via une commande `docker exec -it container_id bash` et exécutez la commande `./bin/flink run --python codes/code_a_tester.py`
3. Regarder vos résultats dans le terminal où vous avez lancer votre `docker compose`. Comme Flink écrit beaucoup de log, il vous faudra remonter un peu dans les logs

Comme nous utilisons pyFlink il n'est pas possible de soumettre simplement un script à l'interface graphique.

### 🛴Manipulation de bases

Le but de cet exercice est d'extraire d'un stream les évènement que l'on recherche, et de modifier leur contenu.

Ouvrez le fichier `json_processing` . Voici les données que vous allez traiter : 

```json
(1, '{"name": "Flink", "tel": 123, "addr": {"country": "Germany", "city": "Berlin"}}'),
(2, '{"name": "hello", "tel": 135, "addr": {"country": "China", "city": "Shanghai"}}'),
(3, '{"name": "world", "tel": 124, "addr": {"country": "USA", "city": "NewYork"}}'),
(4, '{"name": "PyFlink", "tel": 32, "addr": {"country": "China", "city": "Hangzhou"}}')
```

Il vous faut filtrer les données pour garder uniquement les évènements qui proviennent de la chine, et ajouter le bon préfix téléphonique.

### 📚Wordcount

Le but de cet exercice est de transformer un stream et compter le nombre de mot total qu'il contient. Le code se trouve dans le fichier `wordcount.py`

### ➕Utilisation des états 1 : sommer des éléments

Le but de cet exercice es de créer une fonction qui va conserver la valeur d'un état pour faire une somme par utilisateur. Le code se trouve dans le fichier `state.py`

### 🕵️‍♀️Utilisation des états 2 : détecter des patterns

Dans cet exercices vous allez implémenter un system de détection de fraude bancaire via la recherche de pattern dans les transactions des utilisateurs. La règle de décision est la suivante, si un utilisateur réalise une transaction inférieur à 1€ puis une transaction supérieure à 500€ une alerte doit être émise. Le code à modifier est le fichier `frand_detection_job.py`. Il contient :

- La classe `FraudDetector` qui doit détecter la fraude et renvoyer une alerte. Actuellement elle renvoie une alerte pour toutes les transactions. Le state à utiliser est déjà défini.
- La classe `FraudDetectionJob` qui implémente le data stream. Pour cet exercice il est déjà implémenté, vous avez seulement à modifier la classe `FraudDetectior`
- La fonction `data_generation` qui va générer les données. La seul compte suspect sera le compte 9. 