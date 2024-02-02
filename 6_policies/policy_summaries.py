
import boto3

# Initialize a session using your AWS credentials
session = boto3.Session(
    # aws_access_key_id='YOUR_ACCESS_KEY',
    # aws_secret_access_key='YOUR_SECRET_KEY',
    region_name='us-west-2'
)

# Initialize IAM client
iam_client = session.client('iam')

# List policies
response = iam_client.list_policies(Scope='All')

# Print summary of policies
for policy in response['Policies']:
    print(f"Policy Name: {policy['PolicyName']}")
    print(f"Policy ARN: {policy['Arn']}")
    print(f"Policy ID: {policy['PolicyId']}")
    print(f"Default Version ID: {policy['DefaultVersionId']}")
    print(f"Attachment Count: {policy['AttachmentCount']}")
    print(f"Is Attachable: {policy['IsAttachable']}")
    try:
        print(f"Policy Description: {policy['Description']}")
    except:
        pass
    print("\n")

