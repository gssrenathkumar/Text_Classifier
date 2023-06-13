<!DOCTYPE html>
<html>
<head>
    <title>End-to-end Text Summarizer Project</title>
</head>
<body>
    <h1>End-to-end Text Summarizer Project</h1>
    <h2>Workflows</h2>
    <ol>
        <li>Update <code>config.yaml</code></li>
        <li>Update <code>params.yaml</code></li>
        <li>Update entity</li>
        <li>Update the configuration manager in <code>src/config</code></li>
        <li>Update the components</li>
        <li>Update the pipeline</li>
        <li>Update <code>main.py</code></li>
        <li>Update <code>app.py</code></li>
    </ol>

    <h2>How to Run?</h2>
    <h3>Steps:</h3>
    <ol>
        <li>Clone the repository:</li>
        <pre><code>git clone https://github.com/entbappy/End-to-end-Text-Summarization](https://github.com/gssrenathkumar/Text_Summarization.git</code></pre>
        <li>Create a conda environment and activate it:</li>
        <pre><code>conda create -n summary python=3.8 -y
conda activate summary</code></pre>
        <li>Install the requirements:</li>
        <pre><code>pip install -r requirements.txt</code></pre>
        <li>Finally, run the following command:</li>
        <pre><code>python app.py</code></pre>
        <li>Open your local host and port to access the application.</li>
    </ol>

    <h2>Author:</h2>
    <p>G S SRENATH KUMAR<br>
    Data Scientist<br>
    Email: gssrenathkumar2002@gmail.com</p>

    <h2>AWS CI/CD Deployment with GitHub Actions</h2>
    <ol>
        <li>Login to AWS console.</li>
        <li>Create an IAM user for deployment with the following access:</li>
        <ul>
            <li>EC2 access: It is a virtual machine</li>
            <li>ECR: Elastic Container Registry to save your Docker image in AWS</li>
        </ul>
        <li>Description: About the deployment</li>
        <ol>
            <li>Build a Docker image of the source code</li>
            <li>Push your Docker image to ECR</li>
            <li>Launch your EC2 instance</li>
            <li>Pull your image from ECR in EC2</li>
            <li>Launch your Docker image in EC2</li>
        </ol>
        <li>Policies:</li>
        <ul>
            <li>AmazonEC2ContainerRegistryFullAccess</li>
            <li>AmazonEC2FullAccess</li>
        </ul>
        <li>Create an ECR repo to store/save the Docker image. Save the URI: <code>566373416292.dkr.ecr.us-east-1.amazonaws.com/text-s</code></li>
        <li>Create an EC2 machine (Ubuntu)</li>
        <li>Open EC2 and install Docker in the EC2 machine:</li>
        <ul>
            <li>Optional:</li>
            <pre><code>sudo apt-get update -y
sudo apt-get upgrade</code></pre>
            <li>Required:</li>
            <pre><code>
