import spacy
from spacy import displacy


sm_nlp = spacy.load("en_core_web_sm")
lg_nlp = spacy.load("en_core_web_lg")

def ner_spacy(text):
    doc = lg_nlp(text)
    entities = []
    for ent in doc.ents:
        entities.append((ent.text, ent.label_))
    return entities
