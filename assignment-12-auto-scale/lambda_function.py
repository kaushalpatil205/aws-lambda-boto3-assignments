import boto3
import random
def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='ap-south-1')
    sns = boto3.client('sns', region_name='ap-south-1')
    
    account_id = context.invoked_function_arn.split(":")[4]
    SNS_TOPIC_ARN = f'arn:aws:sns:ap-south-1:{account_id}:aws-assignments-alerts'
    
    # Dynamically find the latest Amazon Linux 2 AMI in ap-south-1
    ami_id = ec2.describe_images(
        Owners=['amazon'],
        Filters=[{'Name': 'name', 'Values': ['amzn2-ami-hvm-*-x86_64-gp2']}, {'Name': 'state', 'Values': ['available']}]
    )['Images'][-1]['ImageId']
    
    # Simulating load metric 
    current_load = random.uniform(85, 95)  # Forcing high load (>80%) for demo
    
    if current_load > 80.0:
        response = ec2.run_instances(
            ImageId=ami_id, InstanceType='t2.micro', MinCount=1, MaxCount=1,
            TagSpecifications=[{'ResourceType': 'instance', 'Tags': [{'Key': 'Name', 'Value': 'A12-Scaled'}]}]
        )
        instance_id = response['Instances'][0]['InstanceId']
        msg = f"Load is {current_load:.1f}% (>80%). Launched new instance: {instance_id}"
        
        sns.publish(TopicArn=SNS_TOPIC_ARN, Subject="Auto-Scale: SCALE UP", Message=msg)
        return {'action': 'SCALE_UP', 'instance': instance_id}
