from sklearn.tree import DecisionTreeClassifier
from models.defaults import DEFAULTS
import numpy as np

class DTClassifier():

    def __init__(self,dataset):
        self.dataset = dataset
        self.decisiontree = DecisionTreeClassifier(**DEFAULTS[dataset]['dt']['defaults'])
        print("""
    		**********************
    		Decision Tree Classifier
    		**********************
    	""")

    def train(self, X, y, X_test):
        '''
        fit training dataset and predict values for test dataset
        '''
        self.decisiontree.fit(X, y)
        self.decisiontree.predict(X_test)

    def score(self, X, X_test, y, y_test):
        '''
        Returns the score of Decision Tree by fitting training data
        '''
        self.train_and_predict(X, y, X_test)
        return self.decisiontree.score(X_test, y_test)

    def create_new_instance(self, values):
        return DTClassifier(**{**values})

    def param_grid(self, is_random=False):
        '''
        dictionary of hyper-parameters to get good values for each one of them
        '''
        # random search only accepts a dict for params whereas gridsearch can take either a dic or list of dict
        return DEFAULTS[self.dataset]['dt']['param_grid']

    def __str__(self):
        return "DecisionTree"