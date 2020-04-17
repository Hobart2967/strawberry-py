# strawberry-py

This framework is work in progress.

Aim is to avoid boilerplate WSGI layers when deploying python lambdas with multiple endpoints. 
Frameworks like python-flask, connexion and others require developers to add an annoying wsgi layer on top of their api.
This casues the package to get bigger and bigger while also increasing the cold start times and runtime duration of a lambda.

## Support
- Supports Python 3.7 and higher
- Supports AWS Lambda
- Should support other Lambda function providers with small adjustments.
