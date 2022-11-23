# lambda-chatbot

This is a WebEx chatbot that leverages AWS Lambda functions to listen for messages and responds to them.

### Setup & Installation

Install serverless package via npm. We'll use this to deploy our functions to AWS Lambda.

```
npm install -g serverless
```
Clone the repo

```
git clone https://github.com/tonykhbo/lambda-chatbot.git
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

Modify the .env file: 

```
functions:
  WEBEX_CHATBOT_TOKEN=changethis_12345678abcdefg
```

### Deploy

Change directory to the project root 

```
cd lambda-chatbot
```

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
