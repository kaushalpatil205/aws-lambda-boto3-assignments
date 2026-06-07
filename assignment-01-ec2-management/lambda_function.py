import boto3
def lambda_handler(event, context):
    """
    This function:
    1. Finds all EC2 instances tagged with Action=Auto-Stop and STOPS them
    2. Finds all EC2 instances tagged with Action=Auto-Start and STARTS them
    """
    # Initialize the EC2 client (connects to EC2 service in ap-south-1)
    ec2 = boto3.client('ec2', region_name='ap-south-1')
    # --- STOP instances tagged Auto-Stop ---
    # describe_instances filters by tag Action=Auto-Stop
    stop_response = ec2.describe_instances(
        Filters=[
            {'Name': 'tag:Action', 'Values': ['Auto-Stop']},
            {'Name': 'instance-state-name', 'Values': ['running']}
        ]
    )
    stop_ids = []
    for reservation in stop_response['Reservations']:
        for instance in reservation['Instances']:
            stop_ids.append(instance['InstanceId'])
    if stop_ids:
        ec2.stop_instances(InstanceIds=stop_ids)
        print(f"STOPPED instances: {stop_ids}")
    else:
        print("No running Auto-Stop instances found.")
    # --- START instances tagged Auto-Start ---
    start_response = ec2.describe_instances(
        Filters=[
            {'Name': 'tag:Action', 'Values': ['Auto-Start']},
            {'Name': 'instance-state-name', 'Values': ['stopped']}
        ]
    )
    start_ids = []
    for reservation in start_response['Reservations']:
        for instance in reservation['Instances']:
            start_ids.append(instance['InstanceId'])
    if start_ids:
        ec2.start_instances(InstanceIds=start_ids)
        print(f"STARTED instances: {start_ids}")
    else:
        print("No stopped Auto-Start instances found.")
    return {
        'statusCode': 200,
        'body': {
            'stopped': stop_ids,
            'started': start_ids
        }
    }
