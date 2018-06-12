#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 01:19:47 2018

@author: user
"""

import pandas as pd

unames =  ['user','gender','age','occupation','zip']
users = pd.read_table('users.dat', sep = '::', engine = 'python', names = unames)

rnames = ['user', 'movie', 'rating', 'timestamp']
ratings = pd.read_table('ratings.dat', sep = '::', engine = 'python', names = rnames)

mnames = ['movie','title','genres']
movies = pd.read_table('movies.dat', sep = '::', engine = 'python', names = mnames)

data = pd.merge(pd.merge(users, ratings), movies)

# we convert the movie genres to a set of dummy variables 
movies = pd.concat([movies, movies.genres.str.get_dummies(sep='|')], axis=1)  
movies.head()
