 Serverless File Processing with AWS Lambda (Python)

 Project Overview
This project demonstrates a **serverless architecture** using AWS Lambda, S3, and CloudWatch for file processing.  
When a file is uploaded to S3, a Lambda function processes it and stores metadata in another bucket.

 Tech Stack
- **Python 3.11**
- **AWS Lambda**
- **Amazon S3**
- **CloudWatch Logs**
- **Event-driven architecture**

  Project Structure
- `lambda_function.py` → Main Lambda function  
- `template.yaml` → AWS SAM template for deploying  
- `tests/` → Unit tests  

 ▶ Run Locally (Test)
```bash
pip install -r requirements.txt
pytest
☁️ Deploy to AWS
Using AWS SAM:

bash
Copy
Edit
sam build
sam deploy --guided
🔍 Logs
View Lambda logs:

bash
Copy
Edit
sam logs -n FileProcessorFunction --stack-name <stack-name> --tail
✅ Skills Demonstrated
Serverless architecture

Event-driven workflows

AWS Lambda + S3 integration

Debugging & error handling

Cloud automation
