# WhereIs
<p align="center">
  <img src="https://raw.githubusercontent.com/LewisLebentz/lewislebentz.github.io/master/images/Screenshot%202018-09-23%20at%2021.12.42.png" alt="WhereIs - Slack Command"/> 
</p>

---

[![Build Status](https://travis-ci.com/LewisLebentz/WhereIs.svg?token=Usao5Q8RYnzQveEaz7e6&branch=master)](https://travis-ci.com/LewisLebentz/WhereIs)

---

**Slack slash command using Cisco Prime API to find people. Built with the [Serverless Framework](serverless.com), using AWS Lambda and API Gateway.**


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

5. Run the command to deploy.

	sls deploy
