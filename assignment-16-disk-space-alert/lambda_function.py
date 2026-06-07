import boto3
def lambda_handler(event, context):
    sns = boto3.client('sns', region_name='ap-south-1')
    account_id = context.invoked_function_arn.split(":")[4]
    
    simulated_disk_usage = 88.5  # Simulate over 85%
    
    if simulated_disk_usage > 85.0:
        msg = f"🚨 HIGH DISK ALERT 🚨\nDisk usage is at {simulated_disk_usage}%. Free up space immediately."
        sns.publish(
            TopicArn=f'arn:aws:sns:ap-south-1:{account_id}:aws-assignments-alerts',
            Subject="EC2 Disk Alert",
            Message=msg
        )
        return "Alert sent"
