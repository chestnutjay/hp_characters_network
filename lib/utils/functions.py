import pandas as pd
import numpy as np
import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span
from spacy import displacy
import networkx as nx

import matplotlib.pyplot as plt


def ner(file_name):
    ner = spacy.load("en_core_web_sm")
    matcher = PhraseMatcher(ner.vocab)
    pattern = ner('Hermione')
    matcher.add('HERMIONE', [pattern])