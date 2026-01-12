#These lines import "packages" into our code so we can reuse lines from others' files
from secrets import get_fabman_secret
from packages.fabman import Fabman
import json

# This is the Lambda handler, which is the entry point AWS Lambda looks for to run your code
def lambda_handler(event, context):
    
    # "get_fabman_secret()" is a "method" that returns us a key we use to work with Fabman
    # Methods are actions that code can carry out
    print(get_fabman_secret())
    
    # "Fabman()" is an "object". It contains a list of properties we can access and has methods we can run
    # Here, we create a new Fabman object, and store it with the name "fabman"
    # Putting "get_fabman_secret()" within the parentheses "passes in" the necessary key, and allows us to successfully create a Fabman object
    fabman = Fabman(get_fabman_secret())

    # TODO: get all "Steve" and "Steven" members using our previously-created Fabman object
    # When we want to perform an action, we call methods associated with our object, which is done by writing "object.method" (in this case, fabman.methodName)
    # Look at the hints in readme to figure out which method to use here
    
    
    # TODO: loop through each Steve/Steven member, and print out their names and emails
    # The method from the previous step returns us an "array", which is a list of one type of object
    # We access each element in an array using a "for loop" (message me if you need help figuring out how to do this)
    # Look at the readme hints to figure out how to access the first name, last name, and email properties of each member
    # Hint: You may have to use an "if" statement to check whether the member's first name is Steve/Steven or not (I can help if needed)
    
    

    # You can leave this as is, this will just signal to the Lambda environment that everything went well
    # status 200 = very good!
    return {
        'statusCode': 200,
        'body': json.dumps('Steve and Steven are very cool!')
    }


if __name__ == "__main__":
    lambda_handler(None, None)
