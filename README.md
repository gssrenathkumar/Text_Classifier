# Text Summarization Application

Welcome to our Text Summarization Application! We combine the power of modular coding, advanced machine learning models, and a user-friendly interface to deliver accurate and concise summaries from your text.

## Overview

Our application follows a well-defined process to ensure reliable and high-quality results. Here's how it works:

1. **Data Ingestion**: Your input text is seamlessly integrated into the system.
2. **Data Validation**: The data undergoes rigorous validation to ensure its integrity and quality.
3. **Data Transformation**: The information is transformed and preprocessed to optimize it for the summarization model.
4. **Summarization Model**: We leverage the cutting-edge Google Pegasus Daily Mail model, trained on the SAMSum dataset. This dataset comprises approximately 16,000 messenger-like conversations that have been carefully annotated with summaries. Our model is designed to generate concise summaries that capture the essence of your conversations.
5. **User Interface**: We have developed a user-friendly interface powered by Flask API. Simply input your text into the provided input box, and our application will process it through the summarization model.
6. **Summary Generation**: Within seconds, you will receive a well-crafted summary that distills the essential information from your text.

## Key Features

- The summaries are formulated in the third person, providing a comprehensive overview of the key topics discussed.
- The model is trained on a diverse dataset, reflecting real-life conversations in various styles and registers.
- The application is compatible with popular cloud platforms such as AWS and Azure, allowing for seamless integration into your existing infrastructure.

## How to Run?

To run the Text Summarization Application, follow these steps:
 ```
1. Clone the repository: https://github.com/gssrenathkumar/Text_Summarization.git
 ```

2. Create a conda environment and activate it:
 ```
conda create -n summary python=3.8 -y
conda activate summary
 ```
5. Install the requirements:
 ```
pip install -r requirements.txt
 ```
 ```   
6. Run the application: python app.py
 ```
   
7. Open your local host and port to access the application.

## Author

- G S SRENATH KUMAR
- Data Scientist
- Email: gssrenathkumar2002@gmail.com


# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/entbappy/End-to-end-Text-Summarization
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n summary python=3.8 -y
```

```bash
conda activate summary
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```


```bash
Author: Bappy Ahmed
Data Scientist
Email: entbappy73@gmail.com

```



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/text-s

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app


