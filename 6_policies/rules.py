
import boto3
import json

def list_policy_rules(policy_arn):
    # Initialize a session using your AWS credentials
    session = boto3.Session(
        #aws_access_key_id='YOUR_ACCESS_KEY',
        #aws_secret_access_key='YOUR_SECRET_KEY',
        region_name='us-west-2'
    )

    # Initialize IAM client
    iam_client = session.client('iam')

    # Get the policy document
    policy = iam_client.get_policy(
        PolicyArn=policy_arn
    )

    # Extract the policy document
    policy_document = policy['Policy']['DefaultVersion']['Document']

    # Decode the policy document from JSON
    policy_json = json.loads(policy_document)

    # Extract the rules
    return policy_json['Statement']

# Usage
# policy_arn = 'arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess'
policy_arn = 'arn:aws:iam::081515586180:policy/developer-policy'
rules = list_policy_rules(policy_arn)

# Print the rules
for i, rule in enumerate(rules):
    print(f"Rule {i+1}:")
    print(f"Effect: {rule['Effect']}")
    print(f"Action: {', '.join(rule['Action'])}")
    print(f"Resource: {', '.join(rule['Resource'])}")
    print()

