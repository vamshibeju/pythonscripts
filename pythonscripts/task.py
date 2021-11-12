#Write a python script to calculate the total count of IP in the AWS Public IP Address Range and group it by service and region.
 #We may also ask you to list the IP ranges for specific regions or services OR list IP address that match a certain range.
import json 
file = open('ip-range.json')
data = json.load(file)
sumofips= []

for ips in data['prefixes']:
    if ips['region']== 'us-east-1':
        print(ips['region'])
        value=ips['ip_prefix']
        noofips= value.split('/')
        subnetvalue= noofips[1]
        totalnumberofips = 2 **(32-int(subnetvalue))
        sumofips.append(totalnumberofips)
        
        #print("The toal number of ips for subnet {} is {}".format(int(subnetvalue),totalnumberofips))
        print("total number of ips for the region is %s is %s"%((ips['region']),sum(sumofips)))   