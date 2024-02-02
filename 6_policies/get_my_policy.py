
import boto3

# Initialize a session using your AWS credentials
session = boto3.Session(
    #aws_access_key_id='YOUR_ACCESS_KEY',
    #aws_secret_access_key='YOUR_SECRET_KEY',
    region_name='us-west-2'
)

# Initialize EC2 client
ec2_client = session.client('ec2')

# Get a list of instances
instances = ec2_client.describe_instances()

# Iterate through instances and get attached policies
for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']

        # Get the IAM profile associated with the instance
        iam_instance_profile = instance.get('IamInstanceProfile', {}).get('Arn')

        if iam_instance_profile:
            iam_client = session.client('iam')
            policies = iam_client.list_attached_role_policies(RoleName=iam_instance_profile.split('/')[-1])

            if 'AttachedPolicies' in policies:
                print(f"Policies attached to instance {instance_id}:")
                for policy in policies['AttachedPolicies']:
                    print(f"- {policy['PolicyName']}")
            else:
                print(f"No policies attached to instance {instance_id}")
        else:
            print(f"No IAM instance profile associated with instance {instance_id}")


