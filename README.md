# IaC

# Flask Application Deployed on AWS using Terraform
This is a sample Flask application that has been deployed on AWS using Terraform. The application responds to GET and POST requests with "Hello, World!" and is accessible through an Application Load Balancer (ALB) fronting an ECS cluster.

# Architecture
The internet to app request flow will be as follows:

1. The user sends an HTTP request to the Application Load Balancer.
2. The ALB forwards the request to one of the instances in the Auto Scaling Group.
3. The instance receives the request and processes it using the Flask application.
4. The Flask application responds with "Hello World," and the response is sent back to the user through the ALB.

## The architecture consists of the following components:

1. An ECS cluster containing a single service running the Flask application as a task
2. An Application Load Balancer (ALB) that forwards traffic to the ECS service
3. An IAM role and policy for the ECS tasks to access the necessary resources
4. A security group to control traffic to the ALB and the ECS tasks


## Structure:

```
hello-world-app
├── hello-world-app.py
├── Dockerfile
├── requirements.txt
├── terraform
│   └── main.tf
└── README.md
```

`hello-world-app.py`: The Flask application code.
`Dockerfile`: The Dockerfile used to build the Docker image for the Flask application.
`requirements.txt`: The list of required Python packages for the Flask application.
`terraform`: The directory containing the Terraform file(s) for provisioning the ECS cluster and ALB on AWS.
`terraform/main.tf`: The file containing deployment automation using terraform
`README.md`: This file, which contains information about the project and how to use it.


`main.tf`: This Terraform code creates the following resources:

- Create a Flask App to run locally
- Docerize the App
- Create image repo on AWS ECR
- Push the image
- Create AWS ECS task
- Create AWS ECS service 
- Create a load balancer

Once you are in terraform dir you can run `terraform init`, `terraform plan`, and `terraform apply` to deploy the infrastructure. Once the infrastructure is deployed, you should be able to hit the LB name and see the "Hello World" message from your Flask application.


## How to Use

1. Clone git clone `https://github.com/gh325/IaC/hello-world-app.git`
2. Build the Docker image:  `docker build -t hello-world-app .`
3. Test Docker image: `docker run -p 5000:5000 hello-world-app`
4. Open a web browser and go to `http://localhost:5000` to verify that the Flask application is running.
5. Provision the infrastructure on AWS using Terraform. First, initialize Terraform:
```
cd terraform
terraform init
terraform validate
```
6. Apply all changes `terraform apply`
7. Once the infrastructure is created, visit the AWS Management Console to view the ECS cluster and ALB.
8. Visit the URL for the ALB to view the running Flask application.
9. Destroy the changes using `terraform destroy`

## Conclusion
This project demonstrates how to containerize a Flask application using Docker and deploy it on AWS Elastic Container Service with an Application Load Balancer, all provisioned using Terraform. This project can be used as a starting point for building more complex Flask applications on AWS.



