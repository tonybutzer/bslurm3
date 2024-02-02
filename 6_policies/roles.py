
import boto3

# Initialize a session using your AWS credentials
session = boto3.Session(
    # aws_access_key_id='YOUR_ACCESS_KEY',
    # aws_secret_access_key='YOUR_SECRET_KEY',
    region_name='us-west-2'
)

# Initialize IAM client
iam_client = session.client('iam')

# List roles
response = iam_client.list_roles()

# Print role names
for role in response['Roles']:
    print(f"Role Name: {role['RoleName']}")
    print(f"Role ARN: {role['Arn']}")
    print(f"Role ID: {role['RoleId']}")
    print(f"Assume Role Policy Document: {role['AssumeRolePolicyDocument']}")
    print("\n")

