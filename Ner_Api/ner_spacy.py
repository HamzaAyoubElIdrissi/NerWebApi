import spacy
import pandas as pd
from spacy import displacy


sm_nlp = spacy.load("en_core_web_sm")
lg_nlp = spacy.load("en_core_web_lg")

def ner_spacy(text):
    doc = lg_nlp(text)
    entities = []
    for ent in doc.ents:
        entities.append((ent.text, ent.label_))
    return entities

def extract_entities(text):
    data = {"TEXT": [], "PERSON": [], "PRODUCT": [], "MONEY": [], "LOC": [], "GPE": [], "ORG": []}
    df = pd.DataFrame(data)

    per_list = []
    pro_list = []
    mon_list = []
    loc_list = []
    gpe_list = []
    org_list = []

    doc = lg_nlp(text)

    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            per_list.append(ent.text)
            per_list = list(set(per_list))
        elif ent.label_ == 'PRODUCT':
            pro_list.append(ent.text)
            pro_list = list(set(pro_list))
        elif ent.label_ == 'MONEY':
            mon_list.append(ent.text)
            mon_list = list(set(mon_list))
        elif ent.label_ == 'LOC':
            loc_list.append(ent.text)
            loc_list = list(set(loc_list))
        elif ent.label_ == 'GPE':
            gpe_list.append(ent.text)
            gpe_list = list(set(gpe_list))
        elif ent.label_ == 'ORG':
            org_list.append(ent.text)
            org_list = list(set(org_list))

    df = pd.DataFrame({
        "TEXT": [text],
        "PERSON": [per_list],
        "PRODUCT": [pro_list],
        "MONEY": [mon_list],
        "LOC": [loc_list],
        "GPE": [gpe_list],
        "ORG": [org_list]
    })
    return df
