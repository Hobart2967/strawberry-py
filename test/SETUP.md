# Tools needed
- `brew install yq`

# How this project was set up
1. `yarn init`

## Install Servc
2. `yarn add -D serverless serverless-offline serverless-offline-python`

```
# Define Service
yq n service 'strawberry-py-test' > serverless.yml
yq w -i serverless.yml provider.name aws
yq w -i serverless.yml provider.runtime python3.6

# Add Plugins
yq w -i serverless.yml plugins[0] 'serverless-offline-python'
yq w -i serverless.yml plugins[1] 'serverless-offline'

# Define Api Gateway and Lambda Functions
yq w -i serverless.yml custom.serverless-offline.resourceRoutes true
yq w -i serverless.yml functions.app.handler main.handler
yq w -i serverless.yml functions.app.events[0].http 'ANY /'
yq w -i serverless.yml functions.app.events[1].http 'ANY {proxy+}'
```