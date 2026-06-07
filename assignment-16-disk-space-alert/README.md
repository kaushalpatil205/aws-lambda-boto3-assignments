# Assignment 16: EC2 Disk Space Utilization Alerts
## 🎯 Objective
Set up a Lambda function that checks EC2 instances for disk space utilization, sending an SNS alert if utilization exceeds 85%.
## 🏗️ Architecture
- **CloudWatch Agent (EC2)**: Pushes OS-level disk metrics to CloudWatch.
- **AWS Lambda**: Checks the `CWAgent` metric namespace.
- **Amazon SNS**: Dispatches the high-disk warning email.
## 📋 Steps Followed
1. Configured an IAM role allowing Lambda to read CloudWatch metrics and publish to SNS.
2. Wrote Python code using the boto3 SNS client to dispatch an alert if disk usage breaches the 85% threshold.
3. Validated the alarm mechanism by simulating a high disk usage metric data point.
4. Received the correct threshold breach notification via SNS.
## 💻 Code
See [lambda_function.py](./lambda_function.py)
## 📸 Screenshots
### A16_S1 - SNS Disk Space Alert
![SNS Alert](./screenshots/A16_S1_disk_alert.png)
