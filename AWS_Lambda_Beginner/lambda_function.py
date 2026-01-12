from secrets import get_fabman_secret
from packages.fabman import Fabman
import json

def lambda_handler(event, context):
    """
    This is the Lambda handler -- this is the entry point where AWS Lambda looks for to run your code
    """

    print(get_fabman_secret())
    # this is how we initialize a fabman connection object using the API key we get in secrets.py
    fabman = Fabman(get_fabman_secret())


    # TODO: get members using fabman object, see hints in readme
    
    
    # TODO: initialize an array and loop through each steve/steven's first and last name, and email
    
    


    # TODO: print out all the steves and stevens and their emails
    
    

    # you can leave this as is, this will just signal to the Lambda environment that everything went well
    # status 200 = very good!
    return {
        'statusCode': 200,
        'body': json.dumps('Steve and Steven are very cool!')
    }


if __name__ == "__main__":
    lambda_handler(None, None)