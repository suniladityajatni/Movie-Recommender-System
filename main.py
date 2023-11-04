import re
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd

def clean_title(title):
    title = re.sub("[^a-zA-Z0-9 ]", "", title)
    return title

class Main:
    def __init__(self):
        self.movies = pd.read_csv("movies.csv")
        self.movies["clean_title"] = self.movies["title"].apply(clean_title)
        with open('model.pickle', 'rb') as handle:
            self.vectorizer = pickle.load(handle)
        with open('vectors.pickle', 'rb') as handle:
            self.tfidf = pickle.load(handle)

    def search(self,title):
        title = clean_title(title)
        query_vec = self.vectorizer.transform([title])
        similarity = cosine_similarity(query_vec, self.tfidf).flatten()
        indices = np.argpartition(similarity, -5)[-5:]
        results = self.movies.iloc[indices].iloc[::-1]
        return results["title"].tolist()


if __name__ == "__main__":  
    obj=Main()
    print(obj.search("My name"))

