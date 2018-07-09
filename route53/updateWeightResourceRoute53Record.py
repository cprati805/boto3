# More Information about function:
# https://docs.aws.amazon.com/cli/latest/reference/route53/change-resource-record-sets.html

import boto3
client = boto3.client('route53')
response = client.change_resource_record_sets(
    HostedZoneId='Z2HLXE45LA0EHZ',
    ChangeBatch={
        'Comment': 'Maintenance page failover',
        'Changes': [
            {
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': 'chrisprati.com',
                    'Type': 'A',
                    'SetIdentifier': 'maintenace page',
                    'Weight': 0,
                    'AliasTarget': {
                        'HostedZoneId': 'Z3BJ6K6RIION7M',
                        'DNSName': 's3-website-us-west-2.amazonaws.com',
                        'EvaluateTargetHealth': False
                    }
                },
            }
        ]
    }
)

