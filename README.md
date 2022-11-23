# lambda-chatbot

This is a WebEx chatbot that leverages AWS Lambda functions to listen for messages and responds to them.

handler.py checks the google sheet for an existing row within the name column and responds with the corresponding value within the contactinfo column.

### Setup & Installation

Obtain the google sheet id and the sheet name. Make sure the sheet is publically available for this testing. The sheet should have two columns, one for the name and one for the contact info.

Install serverless package via npm. We'll use this to deploy our functions to AWS Lambda.

```
npm install dotenv
npm install -g serverless
```
Clone the repo

```
git clone https://github.com/tonykhbo/lambda-chatbot.git
```

Change directory to the project root 

```
cd lambda-chatbot
```

Pip install the requirements.txt file into a new folder named python in the base directory of the repo.

```
python3.9 -m pip install -r requirements.txt -t python
```

### AWS Credentials Setup

Follow the instructions in the following links to create an AWS Access Key: 

    - https://www.serverless.com/framework/docs/providers/aws/guide/credentials

    - [Video Guide on setting up credentials](https://www.youtube.com/watch?v=KngM5bfpttA)

Export them as environment variables so they would be accessible to Serverless and the AWS SDK in your shell:

```
export AWS_ACCESS_KEY_ID=<your-key-here>
export AWS_SECRET_ACCESS_KEY=<your-secret-key-here>
```

### Set Environment Variables in .env file

Clone the .env.example as .env - then modify the .env file with your values: 

```
WEBEX_CHATBOT_TOKEN=123456abc
SHEET_ID = '123456abc'
SHEET_NAME = 'blah'
```

### Deploy

Deploy the functions to AWS Lambda:

```
serverless deploy
```

### Modifying Environment variables after Deployment

    - Open the Functions page of the Lambda console.
    - Choose a function.
    - Choose Configuration, then choose Environment variables.
    - Under Environment variables, choose Edit.
    - Choose Add environment variable.
    - Enter a key and value.
    - Choose Save.
