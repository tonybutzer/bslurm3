import boto3
import json

import sys

# arn = 'arn:aws:iam::aws:policy/AdministratorAccess'
arn = 'arn:aws:iam::081515586180:policy/developer-policy'

try:
    arn = sys.argv[1]
except:
    pass

iam = boto3.client('iam')
policy = iam.get_policy(
    PolicyArn = arn
)
policy_version = iam.get_policy_version(
    PolicyArn = arn, 
    VersionId = policy['Policy']['DefaultVersionId']
)

print(json.dumps(policy_version['PolicyVersion']['Document']))
print(json.dumps(policy_version['PolicyVersion']['Document']['Statement']))
