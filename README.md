# Cloud Resume Challenge - AWS

## Live Site

[![Button Icon]](https://cetienne.cloud)
[![Button Icon2]](https://dev.to/etienneci/serverless-cloud-resume-challenge-4ic7)

<!----------------------------------------------------------------------------->
[Link]: # 'Link with example title.'
<!---------------------------------[ Buttons ]--------------------------------->
[Button Icon]: https://img.shields.io/badge/Site-37a779?style=for-the-badge
[Button Icon2]: https://img.shields.io/badge/Blog-37a779?style=for-the-badge

## Project Overview

This project serves as a cloud-hosted resume with a visitor count feature, demonstrating my knowledge of AWS services, front-end and back-end development, and deployment automation. It is designed to showcase my skills in cloud infrastructure management and development with a full-stack approach.

## Key Components

- **SAM Template**: Defines resources and configurations.
- **Lambda Function**: Python-based Lambda function that interacts with DynamoDB to track and retrieve the visitor count.
- **Static Website**: HTML/CSS/JavaScript files hosted on S3, fronted by CloudFront, and connected to a custom domain.
- **Testing**: Unit tests for the Lambda function to ensure the function behaves as expected.

## Architecture

The architecture of this project includes:

- **Frontend**: A static website hosted on S3, served over HTTPS through Amazon CloudFront.
- **Backend**: An API Gateway and a Lambda function written in Python to update and retrieve a visitor count stored in DynamoDB.
- **Infrastructure as Code (IaC)**: The entire infrastructure is defined using AWS SAM (Serverless Application Model) templates.
- **Source Control**: Git for version control and GitHub as repository.
- **CI/CD**: GitHub Actions to trigger workflow on push.

<br>

**Diagram**
![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/u76smf6r6f8a6fundjm3.jpg)
*Made with draw.io*

<br>

## Some Links

- [The Challenge](https://cloudresumechallenge.dev/docs/the-challenge/aws/#7-javascript)
- [AWS SAM](https://aws.amazon.com/serverless/sam/)
- [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/install)
- [HTML/CSS Templates](https://bootstrapmade.com/)
- [Font Awesome Icons](https://fontawesome.com/icons)
- [CSS Snippets](https://freefrontend.com/css-cards/)


