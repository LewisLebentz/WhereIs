# WhereIs
<p align="center">
  <img src="https://raw.githubusercontent.com/LewisLebentz/lewislebentz.github.io/master/images/Screenshot%202018-09-23%20at%2021.12.42.png" alt="WhereIs - Slack Command"/> 
</p>

---

[![Build Status](https://travis-ci.com/LewisLebentz/WhereIs.svg?token=Usao5Q8RYnzQveEaz7e6&branch=master)](https://travis-ci.com/LewisLebentz/WhereIs)

---

**Slack slash command using Cisco Prime API to find people.**

Built with the [Serverless Framework](serverless.com), using AWS Lambda and API Gateway.


Setup
---

1. Clone the WhereIs repository and enter the directory.

       git clone https://github.com/LewisLebentz/WhereIs.git && cd WhereIs

2. If you haven't already, install the Serverless Framework.

       npm install serverless -g
 * You will need AWS credentials setup on your machine before being able to run Serverless commands. Follow the guide [here](https://serverless.com/framework/docs/providers/aws/guide/credentials).

3. Install the dependencies.

       npm install --save

       pip install pipenv

4. Update serverless.yml changing the region, securityGroupIds and subnetIds where applicable.

5. Update handler.py changing the url variable with your Cisco Prime IP/address.

6. Run the command to deploy.

       sls deploy


### Slack Setup ###

1. Login to Slack and navigate to the [Create a Slack App](https://api.slack.com/apps?new_app=1) page.

2. Give your app a name and choose the workspace you'd like to deploy it to.

   <img src="https://raw.githubusercontent.com/LewisLebentz/lewislebentz.github.io/master/images/Screenshot%202018-09-23%20at%2022.24.19.png" width="400">

3. Under 'Features' navigate to 'Slash Commands' and select 'Create New Command'. Call the command whatever you like, and for the Request URL enter the URL returned when the `sls deploy` command finished executing. Fill in the Description and Hint with something meaningful and save.

4. Now, under 'Settings' choose 'Install App' and install it to your workspace.

5. Finally, in Slack run `/whereis firstname.surname` and it should return the location from Prime!
