# Assignment 18: Autosave EC2 State Before Shutdown
## 🎯 Objective
Before an EC2 instance is shut down, automatically save its metadata state to an S3 bucket for auditing.
## 🏗️ Architecture
- **Amazon EventBridge**: Detects the `shutting-down` or `stopping` EC2 state change.
- **AWS Lambda**: Extracts the metadata and serializes it to JSON.
- **Amazon S3**: Stores the backup JSON record.
## 📋 Steps Followed
1. Created an S3 bucket to hold the state files.
2. Configured an EventBridge Rule targeting AWS API calls where EC2 state changes to `shutting-down`.
3. Created a Lambda function that receives the EventBridge payload, parses the instance ID, and dumps a JSON backup directly to S3.
4. Terminated a test instance, which triggered the flow and saved the JSON to S3 successfully.
## 💻 Code
See [lambda_function.py](./lambda_function.py)
## 📸 Screenshots
### A18_S1 - EventBridge Trigger Rule
![EventBridge Rule](./screenshots/A18_S1_eventbridge_rule.png)
### A18_S2 - State Saved to S3
![S3 State File](./screenshots/A18_S2_s3_json_state.png)
