import boto3
import json
from datetime import datetime
def lambda_handler(event, context):
    s3 = boto3.client('s3', region_name='ap-south-1')
    
    instance_id = event['detail']['instance-id']
    state = event['detail']['state']
    
    state_data = {
        'instance_id': instance_id,
        'state': state,
        'timestamp': datetime.now().isoformat()
    }
    
    bucket_name = 'a18-state-backup-561789488706'
    s3_key = f"ec2-states/{instance_id}.json"
    
    s3.put_object(
        Bucket=bucket_name,
        Key=s3_key,
        Body=json.dumps(state_data),
        ContentType='application/json'
    )
    print(f"State saved for {instance_id}")
    return {'saved_to': s3_key}
