from strawberry_py import controller, http_get, http_post, ControllerBase

@controller()
class HelloWorldController(ControllerBase):

  def test_method(self):
    return

  @http_get('/hello/world/{first_name}/{last_name}')
  def get_hello_world(self, first_name, last_name):
    self.response.headers['X-API-RES'] = 'HarrrHarrr'
    return 'Hello ' + last_name + ', ' + first_name + '!'

  @http_post('/hello/world/{first_name}', body_argument='contact_info')
  def post_hello_world(self, first_name, contact_info):
    return  'Hello ' + contact_info['last_name'] + ', ' + first_name + '!'
