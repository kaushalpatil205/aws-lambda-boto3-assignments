import boto3
from datetime import datetime
def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='ap-south-1')
    
    # Snapshot we just created via CLI
    SNAPSHOT_ID = 'snap-009bbd4042dd54dbc'
    
    ami_response = ec2.register_image(
        Name=f"Restore-AMI-{SNAPSHOT_ID}-{int(datetime.now().timestamp())}",
        Architecture='x86_64',
        RootDeviceName='/dev/xvda',
        BlockDeviceMappings=[{
            'DeviceName': '/dev/xvda',
            'Ebs': {'SnapshotId': SNAPSHOT_ID, 'VolumeType': 'gp2'}
        }]
    )
    ami_id = ami_response['ImageId']
    print(f"Created AMI: {ami_id}")
    return {'CreatedAMI': ami_id, 'SourceSnapshot': SNAPSHOT_ID}
