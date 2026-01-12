<h1 align="center">Texas Inventionworks and AWS Lambda</h1>
<p align="center">
  <img src="https://github.com/user-attachments/assets/7bf3c49f-d705-495c-81aa-7a67a30cf121" />
  <img src="https://github.com/user-attachments/assets/082ff99f-0ba5-4b3f-9448-bf375477f505" />
</p>

## Intro to AWS Lambda

AWS Lambda is like an always-on mini computer that can execute a programming function anytime you want! You can run it when a defined event happens, or even on a timer.

TIW uses **AWS Lambda** to automatically sync the trainings between **Canvas**, the AWS Database (**AWS DynamoDB**), and **Fabman**. Another use case for an **AWS Lambda** to periodically poll who has activated a Fabman MAC, and see, in real time, who is checked into a machine.

# The Exercise

In this exercise, you will face a very realistic scenario that will help you...

1. Setup developing with AWS tools locally
2. Learn how to get data from Fabman
3. Learn how to deploy your source code to a new Lambda
4. Learn how to run and see the results of your Lambda

Before moving on to **The Scenario**, take some time to look through the code in this folder and try to understand what is going on.

# The Scenario

Steve and Steven want to find all of the people named "Steve" and "Steven" to email every "Steve" and "Steven" an invitation for a "Steve'n Steve" party. They don't really know how to go about this, so they come to you for help.
You know about this very handy Fabman API call that can get all of the information about every student in Fabman, and you can use this to find all of the people named "Steve" and "Steven". You plan to write and deploy a Lambda for them so that they can run it when they want to without bothering you anymore.

# Your Task

Write code under the _TODO_ sections of the **lambda_function.py** code to print all the members in Fabman named "Steve" and "Steven", as well as their emails.

# Rundown of the Files in AWS_Lambda

1. **packages/** : this is a folder of python code that we did not write! Python packages, or dependencies, helps us write code a lot easier without having to code absolutely EVERYTHING from scratch. You should not need to install any other packages to make this work, and if you want to learn more about Python packages and how to install them DM me!
2. **lambda_function.py** : this is where you will write your python code for this task. The lambda_handler() in lambda_function.py is the entry point for where your lambda will begin execution. Inside the handler there are three TODO statements which you will need to complete in order to complete the task!
3. **README.md** : this file stores the text that you are reading right now! It's basically just a description/helpful guide to the code
4. **requirements.txt** : this text file contains the names of the packages that help our code run. Take a look at the packages we need and try to piece together what they do in the context of our code.
5. **secrets.py** : this code lets us retrieve key information stored in AWS Secrets Manager. Don't worry too much about this file, but if you are curious totally take a look inside!

# Setup

1. Make sure you have the AWS Command Line Interface (CLI) installed and set up with your TIW AWS Credentials
2. Clone the repo (if you haven't already)

# Deployment Steps

Once you have written all of your code in the **lambda_function.py** file, and it works locally, you are ready to deploy your Lambda to AWS!

1. Navigate to the root directory of your project
2. Zip or compress only the "lambda_function.py" and the "secrets.py", and name it **"[YOUR_NAME]\_lambda.zip"**
3. Go to AWS Lambda in the AWS Console in your internet browser
4. Click **Create Function** in the top right corner of the screen
5. Name your function **"[YOUR_NAME]\_lambda"**
6. Change the runtime to **Python 3.13**
7. Click **Create Function** to create your Lambda!
8. **Message me** that you got to this step. I will need to add the necessary permissions for your Lambda to work properly and I'll let you know when you can continue.
9. Once I add the right permissions to your lambda, click into the lambda you just created
10. Under the **"Code"** tab, click **"Upload From"** and select **".zip file"**
11. Click Upload and find the zip file you just created named **"[YOUR_NAME]\_lambda.zip"** and hit Save
12. Scroll down to the bottom of the Lambda screen to the "Layers" section.
13. Click "Add layer" > "Custom layers" > choose "all-purpose-layer" > choose the latest version > click "Add" in the bottom right
14. Once its done updating, navigate to the Test tab and the the orange Test button to run your lambda.
15. If all goes well, you should see a green pop up saying the Lambda executed properly. Open the window to see your results!

# Hints / Troubleshooting

1. What do you think the line `members = fabman.get_members(q='matt')` will do? How could you change the parameters to _query_ something else?
2. To get the last name of a member, the line `member.__getattribute__("lastName")` might be helpful. Same goes for the first name and the email _attributes_.
3. While it is ok to call the Fabman API as many times as you wish, the more times you call the API, the longer and more expensive your code is. Can you solve the problem by using only one API call?
4. If the previous hints did not help at all, take a look at the **/utils/** folder in **fabmansync** and see if you can pull some good information from those files.
5. If you get a TIMEOUT error saying the function execution took too long in AWS Lambda, under the Configuration tab, increase the timeout time from 3 seconds to 5.
6. Message me with other issues you run into!
