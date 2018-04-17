import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random, math
import re
from scipy import stats
from collections import Counter

def read_data(file):
	data = pd.read_csv(file, delimiter=',')
	# return data.values.tolist()
	return data

def get_string_data(data):
	return str(pd.to_datetime(data)).split()[0]

if __name__ == '__main__':
	""" PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked """
	train_data = read_data('train.csv')
	gender = read_data('gender_submission.csv') 
	test = read_data('test.csv')

	print(train_data[train_data['PassengerId'] == 10])