# Concept

![con](https://github.com/tonybutzer/assets/blob/master/0_cluster/parallel_cluster_concept_to_real.JPG?raw=true)
# WaterSMart Cluster

## IAC Journey

- bslurm2 tfinfra - ws-admin box - with butzer-devops role
- install pcluster 3.7.0
    - conda env aws-parallel-cluster - environment.yml
- install nodejs

## SO VPCs

#### WS

One VPC

- 2 CIDRS
- Important CIDR quasi-external = 10.12.64.0/21

The network `10.12.64.0/21` represents an IPv4 address range. In CIDR notation, the `/21` indicates that the first 21 bits are used for network addressing, leaving 11 bits for host addressing.

To find out how many IP addresses are in this network, you can use the following formula:

\[2^n - 2\]

where \(n\) is the number of bits available for host addressing. In this case, \(n = 11\).

So, the number of host addresses in this network is:

\[2^{11} - 2 = 2046\]

However, it's worth noting that in CIDR notation, two addresses are reserved for special purposes:

- The network address (in this case, `10.12.64.0`)
- The broadcast address (in this case, `10.12.71.255`)

Therefore, the usable host addresses in the network `10.12.64.0/21` are \(2046 - 2 = 2044\) addresses.
- 

---

#### 3 subnets

- B 10.12.68.0/23 - 510
- A 10.12.64.0/22 - 2**10 - 2 = 1022
- C 10.12.70.0/23

#### NLCD VPC

the NLCD shares the same "internal" vpc and three subnets, however; it also has a big ephemeral VPC

with four /18 slash18 subnets

each with 16382 network available non-routed addresses

our pcluster nodes will spin up here


## Availability Issues in the not quite infinite cloud

1. cant spin up c6i's currently BUMMER!
2. tony to mitigate one above
3. IP addresses - particularly in watersmart may be an issue.


## IAM Roles and Policies Cluster
