---
layout: page
title: Big data : TP hadoop
---


- [Création un cluster EMR (HDFS/Hadoop MapReduce/Spark) sur AWS](#création-un-cluster-emr-hdfshadoop-mapreducespark-sur-aws)
- [Manipulation de Hadoop Distributed File System (HDFS)](#manipulation-de-hadoop-distributed-file-system-hdfs)
- [Lancer un tâche MapReduce de base](#lancer-un-tâche-mapreduce-de-base)
  - [Wordcount :](#wordcount-)
  - [Grep](#grep)
  - [Estimation de Pi](#estimation-de-pi)
  - [Exercice](#exercice)
- [Créer ses propres tâches en MapReduce](#créer-ses-propres-tâches-en-mapreduce)
  - [Exercice : calculer la température max annuelle aux Etats-Unis](#exercice--calculer-la-température-max-annuelle-aux-etats-unis)


MapReduce est l'un des modèles de programmation les plus utilisé pour traiter de gros volumes de données. Initialement développé par Google pour pouvoir passer facilement à l'échelle son moteur d'indexation web, il existe aujourd'hui des implémentations open source comme Hadoop MapReduce.

Hadoop est un véritable écosystème big data avec plusieurs projets pour proposer des solutions pour mettre en place un système distribué performant, résiliant et extensible. Les deux projets fondamentaux de la pile Hadoop sont HDFS (Hadoop FileSystem) pour le stockage distribué et Hadoop MapReduce pour le calcul distribué.

Dans ce TP vous allez :

1. Créer un cluster Hadoop sur AWS avec le service EMR (Elastic Map Reduce)
2. Utiliser votre cluster pour stocker des fichiers (partie HDFS)
3. Lancer des traitements en python sur votre fichier (Hadoop MapReduce)

> Remarque : pour de meilleurs performances les traitements devraient être fait en java. Mais pour gagner du temps nous allons rester en python.

## Création un cluster EMR (HDFS/Hadoop MapReduce/Spark) sur AWS

Dans cette partie vous allez créer un cluster Hadoop sur AWS. Le procédure ce trouve dans la fiche "Hadoop cluster creation in AWS"

Une fois votre cluster mise en place vous allez devoir vous y connecter en SSH en utilisant un client SHH. Egalement pour accéder aux IHM du cluster vous allez devoir suivre la procédure présente sur la page de votre cluster.

Une fois connecté à votre cluster définissez la variable environnement suivante `HADOOP_PREFIX=/lib/hadoop-mapreduce`. Cela vous permettra de gagner un peu de temps pour écrire les commandes hadoop.

## Manipulation de Hadoop Distributed File System (HDFS)

Le but de cette exercice est que vous réalisiez des opération simple sur HDFS. Le shell du système de fichier distribué (DFS) s'appelle avec `hadoop dfs`. Ce shell dispose de nombreuses commandes qui ressemble au celle d'un shell classique pour interagir avec HDFS, où d'autres système de fichiers que supporté par Hadoop comme le FS local, HFTP, S3, S3 FS etc. Le shell DFS est appelé par  

```
hdfs dfs <args>
```

Toutes les commandes du shell DFS prennent des URIs en argument. Leur format est  `scheme://authority/path`. Pour HDFS `scheme` vaut `hdfs`, et pour le FS local `file`. `scheme` et `authority` sont optionnels et s'ils ne sont pas spécifiés, le schéma par défaut de la configuration est appliqué (pour le TP pas besoin de les remplir). Un fichier ou dossier HDFS comme `/parent/child` peut être spécifié comme `hdfs://namenodehost/parent/child` ou `/parent/child` (si la configuration par défaut pointe vers `hdfs://namenodehost` )

Voici les commandes les plus courantes :

```shell
hdfs dfs -cat URI [URI ...]#Copies source paths to stdout.
hdfs dfs -copyFromLocal <localsrc> URI
hdfs dfs -copyToLocal [-ignorecrc] [-crc] URI <localdst>
hdfs dfs -get [-ignorecrc] [-crc] <src> <localdst>
hdfs dfs -ls <args>
hdfs dfs -mkdir <paths>
hdfs dfs -put <localsrc> ... <dst>
hdfs dfs -rmr URI [URI ...]
```

Vous allez maintenant générer des fichiers via le script `generator.sh` téléchargeable avec un `curl https://raw.githubusercontent.com/HealerMikado/big_data_course_insset/main/Labs/lab%201-%20HDFS%20-%20MapReduce/TP1-Resources/generator.sh >> generator.sh`. Générez les fichiers loremIpsum-500, loremIpsum-250 and loremIpsum-25 qui font 500Mo 250Mo et 25Mo en utilisant les fichiers loremIpsum and generator.sh (`./generator.sh loremIpsum X`). Copiez le fichier vers HDFS (put), affichez les (cat) aller voir les interface graphique puis supprimez les (rmr).

## Lancer un tâche MapReduce de base

Dans cette partie vous allez exécuter trois tâches Mapreduce de base. Elles sont généralement utilisées pour du bencharmking car sont simples et viennent avec les distributions Hadoop. Nous allons simplement les exécuter en appelant le code déjà compilé.

### Wordcount :

C'est l'exemple le plus simple pour faire du MapReduce. Il permet de compter le nombre occurrence de chaque mot dans un texte

```
hadoop jar $HADOOP_PREFIX/hadoop-mapreduce-examples.jar wordcount input output
```

Avec `input` le dossier contenant les fichiers en entrée (vous allez devoir uploader de nouveau les fichiers générés précédemment), `output` est le dossier qui contiendra les résultats. Regardez les fichiers de sortie, de log et les GUI d'Hadoop.

> Tips : Hadoop MapReduce va mettre les sorties dans HDFS. Pour les récupérer sur le namenode vous pouvez faire `hdfs dfs -get output output` et ensuite les lires avec un `cat output/*`

### Grep

Grep permet de trouver le nombre occurrence d'une expression régulières donnée. Essayer avec différents mots comme fermentum, ligula ou hadoop.

```
hadoop jar $HADOOP_PREFIX/hadoop-mapreduce-examples.jar grep input output 'regex'
```

### Estimation de Pi

Permet d'estimer pi avec la méthode quasi-Monte Carlo. Un point est généré dans [0,1]x[0,1] et on regarde s'il est dans le quart de cercle de centre (0,0) et de rayon 1. 

>  C'est une extrêmement mauvaise méthode pour approximer Pi mais là n'es pas le propos.

```
hadoop jar $HADOOP_PREFIX/hadoop-mapreduce-examples.jar pi maps samples_per_map
```

avec maps le nombre de map tasks utilisés et sample_per_map le nombre de reducer. Lancez l'esitmation avec 20 map tasks et 1000 reducers. Regarder les logs et faites varier ses nombres.

### Exercice

Utilisez les 3 fonctions exemples suivantes

- teragen: pour générer des données
- terasort: pour lancer le terasort
- teravalidate: pour vérifier que tout est bon

pour faire un terrasort

Pour obtenir la doc des fonctions vous pouvez faire `hadoop jar $HADOOP_PREFIX/hadoop-mapreduce-examples.jar teragen/terasort/teravalidate`

## Créer ses propres tâches en MapReduce

Pour cette exercice vous allez créer une tâche MapReduce. cela va passer par l'écriture d'un code pour la partie Map et un autre pour la partie Reduce. Hadoop MapReduce est écrit en java et attend qu'on lui envoie du code java pour ses traitements. Mais il est possible de passer outre cette limitation en utilisant le capacité d'Hadoop à streamer les données dans la STDOUT et de lire depuis STDIN. Ainsi Hadoop, déployer notre script sur tous les nœud et exécuter, streamer les données du fichier qui vont être lu par python puis python va traiter les données et les mettre dans la STDOUT pour qu'elles soient lu par Hadoop. Cela ajoute beaucoup d'overhead aux traitements. Et n'est pas recommandé si le temps perdu avec ses échanges est comparable au temps de traitement.

Voici un example pour faire un wordcount basique :

- fonction pour la tâche map

  ```python
  import sys
  
  # input comes from STDIN (standard input)
  for line in sys.stdin:
      # remove leading and trailing whitespace
      line = line.strip()
      # split the line into words
      words = line.split()
      # increase counters
      for word in words:
          # write the results to STDOUT (standard output);
          # what we output here will be the input for the
          # Reduce step, i.e. the input for reducer.py
          #
          # tab-delimited; the trivial word count is 1
          print(f'{word}\t 1' )
  ```

- fonction pour la tâche reduce 

  ```python
  from operator import itemgetter
  import sys
  
  current_word = None
  current_count = 0
  word = None
  # input comes from STDIN
  for line in sys.stdin:
      # remove leading and trailing whitespace
      line = line.strip()
      # parse the input we got from mapper.py
      word, count = line.split('\t', 1)
      # convert count (currently a string) to int
      try:
          count = int(count)
      except ValueError:
          # count was not a number, so silently
          # ignore/discard this line
          continue
  
      # this IF-switch only works because Hadoop sorts map output
      # by key (here: word) before it is passed to the reducer
      if current_word == word:
          current_count += count
      else:
          if current_word:
              # write result to STDOUT
              print(f'{current_word}, {current_count}')
          current_count = count
          current_word = word
  
  # do not forget to output the last word if needed!
  if current_word == word:
      print(f'{current_word}, {current_count}')
  ```

  Lancer ce scripte est un peu plus complexe que les précédents. Voici la commande  utiliser :

  ```shell
  hadoop jar /home/veda/Documents/hadoop/hadoop-2.10.1/share/hadoop/tools/lib/hadoop-streaming-2.10.1.jar \
  -input all/ \
  -output out_py \
  -mapper "python3 python/mapper.py" \
  -reducer "python3 python/reducer.py"
  ```

  

### Exercice : calculer la température max annuelle aux Etats-Unis

Pour cette exercice vous allez calculer la température annuel aux Etats-Unis et utilisant un extrait des données météorologique fournis pas la NOAA ([National Oceanic and Atmospheric Administration](https://www.noaa.gov/)). Le dataset complet est disponible ici : https://noaa-isd-pds.s3.amazonaws.com/index.html

Le format utilisé est un format positionnel. Les données qui nous intéresse pour cet exercice sont :

- l'année disponible à partir du caractère 15 et qui est codé sur 4 caractères
- La température qui est en centième de degré Celsius, disponible à partir du caractère d'index 87 et codé sur 5 caractères avec le signe +/- en premier caractère (exemple +1232 pour 12,32°C)
- La qualité de la mesure qui se trouve au caractère d'index 92, on ne gardera uniquement les qualités suivante `0,1,4,5,9` 

1. Téléchargez le dataset du TP disponible ici :

   `curl https://raw.githubusercontent.com/HealerMikado/big_data_course_insset/main/Labs/lab%201-%20HDFS%20-%20MapReduce/TP1-Resources/meto_data.txt >> meteo_data.txt`

2. Uploadez les données dans votre cluster HDFS

3. Réalisez deux scripts :
   - Méthode map qui va extraire les données souhaités (année, température, qualité) et les transmettre dans la STDOUT
   - Méthode reduce qui va lire les couples année:temperature et extraire le max pour chaque année. Hadoop MapReduce nous facilie la vie en ordonnant les clefs pour la partie reduce (ici les année). Donc des que vous changez de clef, vous avez terminé l'année courante.