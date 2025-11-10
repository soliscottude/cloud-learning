import boto3

ec2 = boto3.client("ec2", region_name="ap-southeast-2")
response = ec2.describe_instances()

for r in response["Reservations"]:
    for i in r["Instances"]:
        print(i["InstanceId"], i["State"]["Name"])
