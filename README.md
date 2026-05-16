# ☁️ Cloud Resume Challenge - AWS

> **Archived project.** This was my personal resume site, previously live at cetienne.cloud. The site has since been rebuilt — this repo is preserved as a completed project demonstrating serverless AWS architecture and DevOps practices. Read the full writeup on [dev.to](https://dev.to/etienneci/serverless-cloud-resume-challenge-4ic7).

![Site Demo](assets/demo.gif)

## Overview
 
A serverless, full-stack resume site built on AWS as part of the [Cloud Resume Challenge](https://cloudresumechallenge.dev/docs/the-challenge/aws/) by Forrest Brazeal. The project covers cloud architecture, backend development, infrastructure as code, and CI/CD — all wired together into a working, deployed product.
 
**What it demonstrates:**
- Serverless AWS architecture (Lambda, DynamoDB, API Gateway)
- Infrastructure as Code via AWS SAM / CloudFormation
- Automated CI/CD with GitHub Actions
- Frontend/backend integration with a live visitor counter
- Unit testing with pytest


## Architecture

The solution implements a **serverless architecture** using AWS services:

### Frontend
- **S3 Static Hosting** - Website files storage and hosting
- **CloudFront CDN** - Global content delivery and HTTPS
- **Custom Domain** - Professional domain with Route 53 DNS

### Backend 
- **API Gateway** - RESTful API endpoints
- **Lambda Functions** - Python-based serverless compute
- **DynamoDB** - NoSQL database for visitor count persistence

### DevOps 
- **AWS SAM** - Infrastructure as Code templates
- **GitHub Actions** - Automated CI/CD pipeline
- **Unit Testing** - Automated testing for reliability

## Architecture Diagram

![Cloud Resume Architecture](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/u76smf6r6f8a6fundjm3.jpg)
*Serverless architecture designed with draw.io*

## Technologies Used

| Category | Technologies |
|----------|-------------|
| **Cloud Provider** | ![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat&logo=amazon-aws&logoColor=white) |
| **Infrastructure** | ![SAM](https://img.shields.io/badge/AWS_SAM-FF9900?style=flat&logo=amazon-aws&logoColor=white) ![CloudFormation](https://img.shields.io/badge/CloudFormation-FF4B4B?style=flat&logo=amazon-aws&logoColor=white) |
| **Backend** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) ![Lambda](https://img.shields.io/badge/AWS_Lambda-FF9900?style=flat&logo=aws-lambda&logoColor=white) ![DynamoDB](https://img.shields.io/badge/DynamoDB-4053D6?style=flat&logo=amazon-dynamodb&logoColor=white) |
| **Frontend** | ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black) |
| **CI/CD** | ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=github-actions&logoColor=white) |
| **Testing** | ![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=flat&logo=pytest&logoColor=white) |

## Key Features

- ✅ **Serverless Architecture** - No server management required
- ✅ **Real-time Visitor Counter** - Dynamic visitor tracking
- ✅ **Global CDN Distribution** - Fast worldwide access via CloudFront
- ✅ **Custom Domain & HTTPS** - Professional domain with SSL/TLS
- ✅ **Infrastructure as Code** - Reproducible infrastructure deployment
- ✅ **Automated CI/CD** - Continuous integration and deployment
- ✅ **Unit Testing** - Automated testing for code reliability
- ✅ **Cost Optimized** - Serverless pay-per-use model

## Project Structure

```
cloud-resume-challenge/
├── 📄 template.yaml          # SAM template defining AWS resources
├── 📁 infra/                 # Infrastructure components
│   ├── 📁 hello_world/       # Lambda function source code
│   │   ├── 🐍 app.py         # Main Lambda function logic
│   │   └── 📄 requirements.txt
│   ├── 📁 tests/             # Unit and integration tests
│   └── 📁 events/            # Test events for local development
├── 📁 website/               # Frontend static website
│   └── 📁 resume-site/       # Website files
│       ├── 🌐 index.html     # Main HTML file
│       ├── 📁 assets/        # CSS, JS, images
│       └── 📁 vendor/        # Third-party libraries
└── 📄 README.md              # Project documentation
```

## Tech Stack
 
| Layer | Technology |
|---|---|
| Cloud | AWS |
| IaC | AWS SAM, CloudFormation |
| Backend | Python, Lambda, DynamoDB, API Gateway |
| Frontend | HTML, CSS, JavaScript |
| CI/CD | GitHub Actions |
| Testing | pytest |


## 🔗 Useful Resources

| Resource | Description |
|----------|-------------|
| [ Cloud Resume Challenge](https://cloudresumechallenge.dev/docs/the-challenge/aws/) | The original challenge by Forrest Brazeal |
| [ AWS SAM Documentation](https://aws.amazon.com/serverless/sam/) | Serverless Application Model guide |
| [ Bootstrap Templates](https://bootstrapmade.com/) | Professional HTML/CSS templates |
| [ GitHub Actions](https://docs.github.com/en/actions) | CI/CD automation documentation |
| [ pytest Documentation](https://docs.pytest.org/) | Python testing framework |

## 📈 Project Metrics

- ** Deployment Time**: < 5 minutes via CI/CD
- ** Page Load Speed**: < 2 seconds globally
- ** Monthly Cost**: < $1 USD (within AWS Free Tier)
- ** CI/CD Pipeline**: Automated testing and deployment
- ** Uptime**: 99.9% availability via CloudFront

---

*Built as part of the [Cloud Resume Challenge](https://cloudresumechallenge.dev/) to demonstrate cloud engineering skills* 


