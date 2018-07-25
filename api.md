# Files

## saml.yaml

This is the SAM template file that will be used to create our API gateway resource and Lambda function, hook them up together.
So that when you call the api endpoint, the api gateway invokes that lambda function for you.

## lambda_function.py 

The Lambda function code!

## buildspec.yml: 

This is used by CodeBuild in the build step of our pipeline. We will get to that later. It will tell codebuild what steps to run inside stage

## beta.json 
The CloudFormation staging file. This will be used by CloudFormation to pass parameters to our CloudFormation template.

WE ARE WATCHING YOU...