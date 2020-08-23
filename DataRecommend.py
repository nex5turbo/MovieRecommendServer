import pandas as pd
import ast
import sys
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#
inputData = str(sys.argv[1])
# print(inputData)

data = pd.read_csv(f'./movies_metadata.csv')
data = data[['id', 'genres', 'vote_average', 'vote_count',
             'popularity', 'title', 'tagline', 'overview']]

m = data['vote_count'].quantile(0.9)
data = data.loc[data['vote_count'] >= m]

C = data['vote_average'].mean()


def weighted_rating(x, m=m, C=C):
    v = x['vote_count']
    R = x['vote_average']

    return (v / (v+m) * R) + (m / (m + v) * C)


data['score'] = data.apply(weighted_rating, axis=1)

data['genres'] = data['genres'].apply(ast.literal_eval)
data['genres'] = data['genres'].apply(
    lambda x: [d['name'] for d in x]).apply(lambda x: " ".join(x))

count_vector = CountVectorizer(ngram_range=(1, 3))
c_vector_genres = count_vector.fit_transform(data['genres'])

genres_cosine_similarity = cosine_similarity(
    c_vector_genres, c_vector_genres).argsort()[:, ::-1]


def get_recommend_movie_list(df, movie_title, top=30):
    target_movie_index = df[df['title'] == movie_title].index.values

    similarity_index = genres_cosine_similarity[target_movie_index, :top].reshape(
        -1)
    sim_index = similarity_index[similarity_index != target_movie_index]

    result = df.iloc[sim_index].sort_values('score', ascending=False)[:10]
    return result


print(get_recommend_movie_list(data, movie_title=inputData).title)
