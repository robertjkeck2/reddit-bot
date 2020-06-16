import praw
import json
import os


class Autobot():

	def __init__(self):

		self.credential_filepath = os.path.realpath(os.path.dirname(__file__))
		self.credential_file = os.path.join(self.credential_filepath, 'redditCredentials.json')

	def initialize_instance(self):

		with open(self.credential_file) as cred_file:
			creds = json.load(cred_file)

		client_id = creds["app_data"]["client_id"]
		client_secret = creds["app_data"]["client_secret"]
		user_agent = creds["app_data"]["user_agent"]
		username = creds["login_data"]["username"]
		password = creds["login_data"]["password"]

		self.reddit = praw.Reddit(client_id = client_id,
							 client_secret = client_secret,
							 user_agent = user_agent,
							 username = username,
							 password = password)
		
		self.reddit.read_only = True

	def get_submission(self, sub):

		self.subreddit = self.reddit.subreddit(sub)
		for submission in self.subreddit.hot(limit=10):
		    print(submission.title) 

a = Autobot()
a.initialize_instance()
a.get_submission('learnpython')


	
