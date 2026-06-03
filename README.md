# Job Application Portal (Serverless AWS Project)

## Project Overview
This is a serverless Job Application Portal built using AWS services.

## Architecture
- Frontend: HTML/CSS/JavaScript hosted on Nginx (VPS)
- Backend: AWS Lambda
- API Layer: Amazon API Gateway
- Database: Amazon DynamoDB

## Features
- Job details page
- Job application form
- Form validation
- Stores applications in DynamoDB
- Serverless backend (no traditional server)

## AWS Services Used
- AWS Lambda
- API Gateway
- DynamoDB
- CloudWatch Logs

## How it works
User → VPS (Nginx) → API Gateway → Lambda → DynamoDB

## API Endpoint
POST /apply

## Status
Project completed successfully
