import boto3
from datetime import datetime, timedelta

ec2 = boto3.client('ec2')
response = ec2.describe_instances(
    Filters=[
        {
            'Name': 'instance-state-code',
            'Values': ['16']
        }
    ]
)

for i in range(100):
    try:
        format = "%Y-%m-%d %H:%M:%S"
        instance_launch_time = response['Reservations'][i]['Instances'][0]['LaunchTime'].strftime(format)
        date_time_instance = datetime.strptime(instance_launch_time, '%Y-%m-%d %H:%M:%S')

        now = datetime.now() - timedelta(hours=3)
        time1 = now.strftime(format)
        date_time_now = datetime.strptime(time1, '%Y-%m-%d %H:%M:%S')
        print(date_time_instance)
        print(date_time_now)
        uptime = (date_time_now - date_time_instance).total_seconds() / 60

        print(uptime)
        if uptime >= -120.0:
            instance_id = response['Reservations'][i]['Instances'][0]['InstanceId']
            print(instance_id)
            """
            stop_response = ec2.stop_instances(
                InstanceIds=[
                    instance_id
                ],
                Force=True
            )
            """
    except:
        continue


#print(response['Reservations'][0])
#print(response['Reservations'][0]['Instances'][0]['LaunchTime'])

#print(response['Reservations'][1]['Instances'][0]['LaunchTime'])
