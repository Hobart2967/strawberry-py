# strawberry-py

This framework is work in progress.

Aim is to avoid boilerplate WSGI layers when deploying python lambdas with multiple endpoints.
Frameworks like python-flask, connexion and others require developers to add an annoying wsgi layer on top of their api.
This casues the package to get bigger and bigger while also increasing the cold start times and runtime duration of a lambda.

![Idea of this frameowrk](docs/idea-background-transparent.png "How strawberry_py integrates into your application")

## Support
- LightWeight, no dependencies
- Easy to use for people knowing .NET Core Rest Apis, Java Springboot Applications and similar
- Supports Python 3.7 and higher
- Supports AWS Lambda
- Should support other Lambda function providers with small adjustments.
- Comes with an OpenApi Generator for easing documentation of REST APIs ✨

# Setting up the main lambda python file
```
from strawberry_py import ControllerHandler, AwsLambdaRequest, AwsLambdaResponse

#region Controllers
from .controllers.hello_world_controller import HelloWorldController
#endregion

def handler(event, context):
  request = AwsLambdaRequest(event, context)
  controller_handler = ControllerHandler.getinstance()
  response = controller_handler.handleRequest(request)

  return AwsLambdaResponse.from_response(response).get_lambda_result()
 ```

# Creating a controller
```
from strawberry_py import controller, http_get, http_post, ControllerBase

@controller(HelloWorldController)
class HelloWorldController(ControllerBase):

  def test_method(self):
    return

  @http_get('/hello/world/{firstName}/{lastName}')
  @path_parameter('firstName')
  @path_parameter('lastName')
  @query_string_parameter('greetInformal')
  def get_hello_world(self, first_name, last_name, greet_informal=False):
    greeting = 'Hello '
    if greet_informal:
      greeting = 'Yo, '
    return greeting + last_name + ', ' + first_name + '!'

  @http_post('/hello/world/{firstName}', body_argument='contact_info')
  @path_parameter('firstName')
  @body_parameter('contactInfo')
  def post_hello_world(self, first_name, contact_info):
    return  'Hello ' + contact_info['last_name'] + ', ' + first_name + '!'

```
