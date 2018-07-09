import boto3
ec2 = boto3.resource('ec2', region_name='us-west-2')
instanceName = 'webServer'
filters = [{'Name': 'tag:Name', 'Values': [instanceName]}]
instances = ec2.instances.filter(Filters=filters)
print("---------------------------------")
for instance in instances:
   for tag in instance.tags:
       if tag["Key"] == 'Name':
           print("Instance Name: " , tag['Value'])
   print("Instance ID: ", instance.id)
   print("Instance Private IP: ", instance.private_ip_address)
   print("Instance State: ", instance.state['Name'])
   print("This instance will be rebooted")
   instance.reboot()
   print("---------------------------------")