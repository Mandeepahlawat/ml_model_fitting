from sklearn.neural_network import MLPClassifier
from models.defaults import DEFAULTS

class MlpClassifier():
	
	def __init__(self, dataset):
		self.dataset = dataset
		self.nn = MLPClassifier(**DEFAULTS[dataset]['nn']['defaults'])
		print("""
			**********************
			Neural Network
			**********************
		""")
	
	def train_and_predict(self, X, y, X_test):
		'''
		fit training dataset and predict values for test dataset 
		'''
		self.nn.fit(X,y)
		self.nn.predict(X_test)

	def score(self, X, X_test, y, y_test):
		'''
		Returns the score of knn by fitting training data
		'''
		self.train_and_predict(X, y, X_test)
		return self.nn.score(X_test, y_test)

	def create_new_instance(self, values):
		return MLPClassifier(**{**values, 'random_state': 0})

	def param_grid(self, is_random=False):
		'''
		dictionary of hyper-parameters to get good values for each one of them
		'''
		return DEFAULTS[self.dataset]['nn']['param_grid']

	def __str__(self):
		return "Neural Network"