import boto3

def get_permissions_boundary(entity_name):
    # Initialize a session using your AWS credentials
    session = boto3.Session(
        # aws_access_key_id='YOUR_ACCESS_KEY',
        # aws_secret_access_key='YOUR_SECRET_KEY',
        region_name='us-west-2'
    )

    # Initialize IAM client
    iam_client = session.client('iam')

    # Get the IAM entity (user or role)
    try:
        response = iam_client.get_user(
            UserName=entity_name
        )
    except iam_client.exceptions.NoSuchEntityException:
        try:
            response = iam_client.get_role(
                RoleName=entity_name
            )
        except iam_client.exceptions.NoSuchEntityException:
            print(f"The IAM entity {entity_name} does not exist.")
            return None

    # Get the permissions boundary
    permissions_boundary = response.get('User', {}).get('PermissionsBoundary', None)
    if not permissions_boundary:
        permissions_boundary = response.get('Role', {}).get('PermissionsBoundary', None)

    return permissions_boundary

# Usage
entity_name = 'nlcd-developer-ec2-role'
permissions_boundary = get_permissions_boundary(entity_name)

if permissions_boundary:
    print(f"The permissions boundary for {entity_name} is: {permissions_boundary}")


