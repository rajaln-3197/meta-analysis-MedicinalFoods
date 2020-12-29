# meta-analysis-MedicinalFoods
Extracting relevant information from a large collection of research articles

# Data collection
Scrape Journal Articles related to Public Health for Stress, Anxiety, and Sleep Disorders from Pubmed. 

Run scrape_articles.py

# Annotation 
Set up Inception server on local machine: https://inception-project.github.io/

Annotate data according to the guidelines and tagsets available in 'inception' folder

# Preprocessing
unzip CoNLLL 2002'

Move and rename the files:(Powershell commands)

``Get-ChildItem annotation\ -Filter *.conll -Recurse | Rename-Item -NewName { $_.Directory.Name+'.conll'}``

``Get-ChildItem -Path .\code\annotation\ -Filter *.conll -Recurse -File | Move-Item -Destination .\code\annotation\CoNLL\``

``Get-ChildItem annotation\ -Filter *.conll -Recurse | Rename-Item -NewName { $_.Directory.Name}``

``Get-ChildItem -Path annotation\ -Filter *.txt -Recurse -File | Move-Item -Destination TXT\``

Run preprocess.py to get train and test files (Glove embeddings format also available)

# Running models


pip install spacy

python -m spacy download en_core_web_sm

run setup.py

python -m spacy convert --converter ner train.conll ./train

python -m spacy convert --converter ner val.conll ./val

python -m spacy debug-data en ./train ./val -p ner -b en_core_web_sm

python -m spacy train en ./models/md ./train ./val --base-model en_core_web_sm --pipeline ner -R -n 25

python -m spacy evaluate ./models/md/model-best ./val

python eval.py
