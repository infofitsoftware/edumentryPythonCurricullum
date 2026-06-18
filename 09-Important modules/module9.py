"""
1. Working with OS and System Operations
os Module
The os module allows interaction with the operating system, handling environment variables, file operations, and process management.
"""

import os

# Get current working directory
print(os.getcwd())

# List files in a directory
print(os.listdir("."))

# Create and remove directories
os.mkdir("test_dir")
os.rmdir("test_dir")

# Run shell commands
os.system("ls -l")


"""sys Module
The sys module provides system-specific parameters and functions."""

import sys

print(sys.version)  # Get Python version
print(sys.platform)  # Get OS platform

# Command-line arguments
print(sys.argv)


"""2. Automating with Subprocess
The subprocess module is used for executing shell commands and interacting with system processes."""


import subprocess

# Run a command and get the output
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(result.stdout)

# Run a command and check return code
completed = subprocess.run(["echo", "Hello"], check=True)
print(completed.returncode)


"""3. Working with Environment Variables
os.environ"""

import os

# Get an environment variable
print(os.environ.get("HOME"))

# Set an environment variable
os.environ["MY_ENV"] = "DevOps"
print(os.environ["MY_ENV"])


from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("API_KEY"))  # Load from .env file


"""4. Networking and API Calls
requests Module"""


import requests

# GET request
response = requests.get("https://api.github.com")
print(response.status_code)
print(response.json())

# POST request
data = {"key": "value"}
response = requests.post("https://httpbin.org/post", json=data)
print(response.json())


"socket Module"

import socket

# Get IP address of a website
ip = socket.gethostbyname("google.com")
print(ip)


"""5> Docker and Kubernetes Automation
docker-py Module"""

import docker

client = docker.from_env()
containers = client.containers.list()
print(containers)



from kubernetes import client, config

config.load_kube_config()
v1 = client.CoreV1Api()
pods = v1.list_pod_for_all_namespaces(watch=False)
for pod in pods.items:
    print(pod.metadata.name)


"""6>Infrastructure as Code (IaC) with Python
Boto3 (AWS SDK)"""

import boto3

s3 = boto3.client("s3")
buckets = s3.list_buckets()

for bucket in buckets["Buckets"]:
    print(bucket["Name"])


from python_terraform import Terraform

tf = Terraform(working_dir="./terraform")
tf.init()
tf.apply()


"""
7. CI/CD Scripting with Python
Jenkins API
"""
from jenkinsapi.jenkins import Jenkins

jenkins = Jenkins("http://localhost:8080", username="admin", password="password")
job = jenkins["my-job"]
job.invoke(build_params={"BRANCH": "main"})


"""Git Automation with GitPython"""

import git

repo = git.Repo("/path/to/repo")
repo.git.pull()
repo.git.add(".")
repo.git.commit("-m", "Automated commit")
repo.git.push()







