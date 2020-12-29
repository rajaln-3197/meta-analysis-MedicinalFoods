import spacy
import glob
from spacy.gold import GoldCorpus
from spacy.scorer import Scorer
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt

MODEL_PATH = './models/md/model-best'
nlp = spacy.load(MODEL_PATH)
def eval_test():
    for filename in glob.glob('./Unseen/*.txt'):
        f = open(filename,'r',encoding="utf8")
        sample = f.readline()
        doc = nlp(sample)
        out = open('eval_out.txt','a',encoding="utf8")
        out.write('\n')
        for ent in doc.ents:
            entity = ent.label_ + ':' + ent.text + '\n'
            print(str(entity))
            out.write(str(entity))
        out.close
        print('\n')
#eval_test()

def generate_scatter():
    VAL_FILENAME = './val/val.json'

    val_corpus = GoldCorpus(VAL_FILENAME, VAL_FILENAME)
    docs_golds = list(val_corpus.train_docs(nlp))
    docs, golds = zip(*docs_golds)
    ner = nlp.pipeline[0][1]
    predictions = list(ner.pipe(docs))

    tag_counts = Counter()
    scorer = Scorer()
    for y_p, y_t in zip(predictions, golds):
        scorer.score(y_p, y_t)
        for tag in y_t.ner:
            tag_counts[tag.split('-')[-1]] += 1
    print(scorer.ents_p, scorer.ents_r, scorer.ents_f)
    scores = (pd.DataFrame.from_dict(scorer.ents_per_type, orient='index')
                        .join(pd.Series(tag_counts, name='support'))
                        .sort_values(by='support', ascending=False))
    print(scores)

    fig = scores.plot.scatter(x='support', y='f', c='DarkBlue').get_figure().savefig('output.png')
#generate_scatter()

def visualize():
    from spacy import displacy
    f = open('./Unseen/ashwagandha_212.txt','r',encoding="utf8" )
    sample = f.readline()
    doc = nlp(sample)
    sentence_spans = list(doc.sents)
    svg = displacy.serve(sentence_spans, style="dep")
    output_path = Path("sentence.svg")
    output_path.open("w", encoding="utf-8").write(svg)
visualize()