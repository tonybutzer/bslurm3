#!/usr/bin/env python
# coding: utf-8

import os
import subprocess
import json
import pandas as pd

def unicorn():
    uni = r'''


                             \
                              \
                               \\
                                \\
                                 >\/7
                             _.-(6'  \
                            (=___._/` \
                                 )  \ |
                                /   / |
                               /    > /
                              j    < _\
                          _.-' :      ``.
                          \ r=._\        `.
                         <`\\_  \         .`-.
                          \ r-7  `-. ._  ' .  `\
                           \`,      `-.`7  7)   )
                            \/         \|  \'  / `-._
                                       ||    .'
eco                                     \\  (
butzer                                   >\  >
                                     ,.-' >.'
                                    <.'_.''
                                      <'

'''
    print (uni)


def describe_instances_to_dataframe():
    # Run AWS CLI command to describe instances
    command = "aws ec2 describe-instances"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    # Check for errors
    if result.returncode != 0:
        print("Error:", result.stderr)
        return None

    # Parse JSON output
    try:
        instances_data = json.loads(result.stdout)
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
        return None

    # Extract relevant information for DataFrame
    instances_list = []
    for reservation in instances_data.get('Reservations', []):
        for instance in reservation.get('Instances', []):
            instance_info = {
                'InstanceId': instance.get('InstanceId', ''),
                'InstanceType': instance.get('InstanceType', ''),
                'State': instance.get('State', {}).get('Name', ''),
                'PublicIpAddress': instance.get('PublicIpAddress', ''),
                'PrivateIpAddress': instance.get('PrivateIpAddress', ''),
                # Add more fields as needed
            }
            instances_list.append(instance_info)

    # Create Pandas DataFrame
    df = pd.DataFrame(instances_list)
    return df

unicorn()
# Run the function
df = describe_instances_to_dataframe()

# Display the DataFrame
if df is not None:
    print(df)


import boto3

def get_instance_name(instance_id):
    # Specify the region
    region = 'us-west-2'  # Replace with your AWS region, e.g., 'us-east-1'

    # Create EC2 client
    ec2 = boto3.client('ec2', region_name=region)

    try:
        # Describe the instance to get its tags
        response = ec2.describe_instances(InstanceIds=[instance_id])

        # Extract the "Name" tag value
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                for tag in instance.get('Tags', []):
                    if tag['Key'] == 'Name':
                        return tag['Value']

        # If the instance has no "Name" tag
        return f"No 'Name' tag found for instance {instance_id}"

    except Exception as e:
        return f"Error: {str(e)}"

# Replace 'your-instance-id' with the actual instance ID
# instance_id = 'i-05eca5a0ba83f964b'
# instance_name = get_instance_name(instance_id)

# print(f"The 'Name' tag for instance {instance_id} is: {instance_name}")

# for i,r in df.iterrows():
    # print(r['InstanceId'])
    # Name = get_instance_name(r['InstanceId'])
    # print(Name)

df['InstanceName'] = df['InstanceId'].apply(get_instance_name)

selected_rows = df[df['InstanceName'].isin(['HeadNode', 'Compute'])]

print(selected_rows)

compute_df = selected_rows[selected_rows['InstanceName'].isin(['Compute', 'Compute'])]

print(compute_df)

c_list = compute_df['PrivateIpAddress'].to_list()

print(c_list)

while True:

    cnt=0
    for ip in c_list:
        print(cnt, ip)
        cnt=cnt+1

    data = input("Please enter Compute Number: \n")
    ipcnt = int(data)
    ip=c_list[ipcnt]
    cmd = f'ssh -i /home/ec2-user/butzer.pem {ip}'
    os.system(cmd)




