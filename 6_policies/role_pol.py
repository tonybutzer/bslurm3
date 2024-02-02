import boto3

# Initialize a session using your AWS credentials
session = boto3.Session(
    #aws_access_key_id='YOUR_ACCESS_KEY',
    #aws_secret_access_key='YOUR_SECRET_KEY',
    region_name='us-west-2'
)

# Initialize IAM client
iam_client = session.client('iam')

# Name of the IAM role you want to inspect
role_name = 'YOUR_ROLE_NAME'
role_name = 'nlcd-developer-ec2-role'

# Get a list of attached policies for the specified role
response = iam_client.list_attached_role_policies(RoleName=role_name)

# Print the policies
for policy in response['AttachedPolicies']:
    print(f"Policy Name: {policy['PolicyName']}")
    print(f"Policy ARN: {policy['PolicyArn']}")
    print("\n")

