# This script will return all 'available' EBS volumes in the 'us-west-2' region
import boto3
from datetime import datetime, timedelta
region = "us-west-2"
ec2 = boto3.resource("ec2", region_name=region)
def get_available_volumes():
    available_volumes = ec2.volumes.filter(
        Filters=[{'Name': 'status', 'Values': ['available']}]
    )
    for volume in available_volumes:
        print(volume)

get_available_volumes()

