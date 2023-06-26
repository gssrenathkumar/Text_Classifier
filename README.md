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
8. Run the application: python app.py
 ```
   
9. Open your local host and port to access the application.

## Author

- G S SRENATH KUMAR
- Data Scientist
- Email: gssrenathkumar2002@gmail.com

## AWS CI/CD Deployment with GitHub Actions

To deploy the Text Summarization Application using AWS and GitHub Actions, follow these steps:

1. Login to the AWS console.
2. Create an IAM user for deployment with the following access:
- EC2 access: It is a virtual machine.
- ECR: Elastic Container Registry to save your Docker image in AWS.
3. Description of the deployment process:
- Build a Docker image of the source code.
- Push your Docker image to ECR.
- Launch your EC2 instance.
- Pull your image from ECR in EC2.
- Launch your Docker image in EC2.
4. Required IAM policies:
- AmazonEC2ContainerRegistryFullAccess
- AmazonEC2FullAccess
5. Create an ECR repository to store/save the Docker image. Save the URI: `566373416292.dkr.ecr.us-east-1.amazonaws.com/text-s`.
6. Create an EC2 machine (Ubuntu).
7. Install Docker in the EC2 machine:
- Optional:
  ```
  sudo apt-get update -y
  sudo apt-get upgrade
  ```
- Required:
  ```
  # Install Docker
  curl -fsSL
  ```



