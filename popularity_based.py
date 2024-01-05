# -*- coding: utf-8 -*-
"""Popularity-based.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1781l2knuLz44hiIxouyoLhAqerQmanvd

# Introduction

This notebook contains `Popularity` based recommendation system.
Details of how it works is available on my Hashnode Blog site.

Link is [here](http://)

# Import files
"""

# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All"
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

"""# Read Dataset"""

credits = pd.read_csv("../input/tmdb-movie-metadata/tmdb_5000_credits.csv")
movies = pd.read_csv("../input/tmdb-movie-metadata/tmdb_5000_movies.csv")

"""# Basic Data Exploration"""

credits.columns

movies.columns

credits.shape, movies.shape

credits.head(2)

movies.head(2)

"""## Combine both datasets"""

df = pd.merge(movies, credits, left_on="id", right_on="movie_id")

credits.shape, movies.shape, df.shape

"""## Check datatypes"""

df.info()

"""# Poplularity Based RS"""

df.head(3)

df.columns

"""## Calculate Weighted Average"""

v = df['vote_count']
m = df['vote_count'].quantile(0.7)
R = df['vote_average']
c = df['vote_average'].mean()

df['weighted_avg'] = ((R * v)+(c * m))/(v+m)

top_20 = df.sort_values('weighted_avg', ascending=False)

top_20[['original_title', 'vote_count' ,'vote_average', 'weighted_avg']].head(20)

top_20[['original_title', 'vote_count' ,'vote_average', 'weighted_avg', 'popularity']].head(20)

"""## Scaling using MinMax"""

from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler()
scaled = sc.fit_transform(top_20[['weighted_avg','popularity']])
scaled = pd.DataFrame(scaled, columns=['scaled_wt_avg', 'scaled_popularity'])
top_20[['scaled_wt_avg', 'scaled_popularity']] = scaled
top_20[['original_title', 'vote_count' ,'vote_average', 'weighted_avg', 'popularity', 'scaled_wt_avg','scaled_popularity']].head(20)