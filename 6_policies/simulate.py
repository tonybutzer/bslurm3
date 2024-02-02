import boto3

def simulate_policy(policy_json, resource_arns):
    # Initialize a session using your AWS credentials
    session = boto3.Session(
        # aws_access_key_id='YOUR_ACCESS_KEY',
        # aws_secret_access_key='YOUR_SECRET_KEY',
        region_name='us-west-2'
    )

    # Initialize the Policy Simulator client
    simulator_client = session.client('policysimulator')

    # Define the simulation input
    simulation_input = {
        'ActionNames': [],
        'PolicySourceArn': 'arn:aws:iam::aws:policy/SimulateAPIAction',
        'ResourceArns': resource_arns,
        'ContextEntries': {},
        'ResourceHandlingOption': 'AllResources',
        'Effect': 'Allow',
        'PermissionsBoundaryPolicyInputList': [],
        'MaxItems': 1,
        'PolicyInputList': [
            {
                'ActionNames': [],
                'Effect': 'Allow',
                'PolicyDocument': policy_json,
                'Roles': [],
                'Groups': [],
                'Users': [],
            },
        ]
    }

    # Simulate the policy
    response = simulator_client.simulate_custom_policy(
        PolicyInputList=simulation_input['PolicyInputList'],
        ActionNames=simulation_input['ActionNames'],
        ResourceArns=simulation_input['ResourceArns'],
        ContextEntries=simulation_input['ContextEntries'],
        ResourceHandlingOption=simulation_input['ResourceHandlingOption'],
        Effect=simulation_input['Effect'],
        PermissionsBoundaryPolicyInputList=simulation_input['PermissionsBoundaryPolicyInputList'],
        PolicySourceArn=simulation_input['PolicySourceArn'],
        MaxItems=simulation_input['MaxItems']
    )

    return response

# Usage
policy_json = '''
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::example-bucket/*"
        }
    ]
}
'''

resource_arns = [
    'arn:aws:s3:::example-bucket/object-key',
    # Add more resource ARNs as needed
]

simulation_result = simulate_policy(policy_json, resource_arns)

# Process the simulation result
print(simulation_result)


