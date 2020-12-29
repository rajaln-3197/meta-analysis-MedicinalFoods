import spacy
nlp = spacy.load('en_core_web_sm')
bytes_data = nlp.to_bytes()
lang = nlp.meta["lang"]  # "en"
pipeline = nlp.meta["pipeline"]  # ["tagger", "parser", "ner"]
if "ner" not in nlp.pipe_names:
        ner = nlp.create_pipe("ner")
        nlp.add_pipe(ner, last=True)
    # otherwise, get it so we can add labels
else:
        ner = nlp.get_pipe("ner")