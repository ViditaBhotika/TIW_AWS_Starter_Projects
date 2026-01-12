import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'packages'))

import botocore.session
from aws_secretsmanager_caching import SecretCache, SecretCacheConfig
import json

'''
This is code to get the Secrets of TIW, you SHOULD NOT need to modify this file at all if everything is setup correctly!

What are TIW Secrets?
    - We pay for services like Fabman and AWS, and we also have our own private Canvas page we need to manage.
    - We definitely DO NOT want any random person messing with our Fabman, Canvas or AWS.
    - AWS Secrets manager is a seamless way we can store and share secrets with the people we trust, which includes you!

This code will pull the secret API keys for Fabman and Canvas to your code. You may look at and print them, but understand that it is VERY sensitive 
information that ABSOLUTELY SHOULD NOT be shared with anyone that is not TIW affiliated. Treat it like the password to your personal computer. 

Additionally, if you decide to push your code to GitHub, double check and make sure that none of these keys are in any files you push. You wouldn't 
post your computer password to Instagram right? So please don't do that here.
'''

# the client talks to AWS using the secret key logins during 'aws configure'
client = botocore.session.get_session().create_client('secretsmanager')
cache_config = SecretCacheConfig()

# the cache stores the passwords locally
cache = SecretCache( config = cache_config, client = client)

# these are the secrets in JSON format
secret = json.loads(cache.get_secret_string('prod/portal/canvasApiKey'))


# gets the fabman API key
def get_fabman_secret():
    return secret["FABMAN_KEY"]

# gets the live canvas API key
def get_official_canvas_secret():
    return secret["CANVAS_TEACHER_KEY"]

# gets the dev canvas API key
def get_dev_canvas_secret():
    return secret["DEV_TEACHER_KEY"]
