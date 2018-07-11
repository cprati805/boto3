# This script will list all available ebs volumes by region
import boto3
from datetime import datetime, date, timedelta

ec2 = boto3.client("ec2")

# Get a list of all regions in AWS
regions = ec2.describe_regions().get('Regions',[])

print("This script will show you all volumes that are in-use in all regions")
print("-----------------------------------------------")

for region in regions:
    print("Looking at AWS Region: " + region['RegionName'])
    reg=region['RegionName']

    # Connect to region
    ec2 = boto3.client('ec2', region_name=reg)

    # Get all 'in-use' volumes
    volumes = ec2.describe_volumes( Filters=[{'Name': 'status', 'Values': ['available']}])
    
    if volumes['Volumes'] == []:
        print("There are no 'available' EBS volumes in this region")

    else:
        print("List of 'available' EBS Volumes in " + reg)
        for volume in volumes['Volumes']:
            print("EBS Volume ID: " + volume['VolumeId'])
    print("-----------------------------------------------")