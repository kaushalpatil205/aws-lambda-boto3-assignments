import boto3
def lambda_handler(event, context):
    sns = boto3.client('sns', region_name='ap-south-1')
    
    # Auto-extract your account ID from the running context
    account_id = context.invoked_function_arn.split(":")[4]
    SNS_TOPIC_ARN = f'arn:aws:sns:ap-south-1:{account_id}:aws-assignments-alerts'
    
    for record in event['Records']:
        event_name = record['eventName']
        table_name = record['eventSourceARN'].split('/')[1]
        
        if event_name == 'MODIFY':
            old_item = record['dynamodb'].get('OldImage', {})
            new_item = record['dynamodb'].get('NewImage', {})
            msg = f"✏️ ITEM MODIFIED in {table_name}:\nOLD: {old_item}\nNEW: {new_item}"
            
            sns.publish(
                TopicArn=SNS_TOPIC_ARN,
                Subject=f"DynamoDB Alert: {event_name} on {table_name}",
                Message=msg
            )
            print("Alert Sent via SNS!")
            
    return {'statusCode': 200, 'body': 'Processed records'}
