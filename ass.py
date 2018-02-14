#Accept the AWS credentials to connect to AWS account (Use AWS boto python library)

conn = boto.ec2.connect_to_region("us-west-1", aws_access_key_id= "AKIAJJOXJRFY4X6NEGCQ", aws_secret_access_key="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")


#List down all VM available on the AWS
 reservations = ec2_connection.get_all_reservations()
 for reservation in reservations:    for instance in reservation.instances:
 print(instance.id, instance.instance_type)
 
 
 #Print details of the particular VM.
 
 reservations = ec2_connection.get_all_instances(instance_ids=['i-0c905eb10be579bd5'])
 vm = reservations[0].instances[0]
  dir(vm)
  ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_in_monitoring_element', '_placement', 
'_previous_state', '_state', '_update', 'add_tag', 'add_tags', 'ami_launch_index', 'architecture', 'block_device_mapping', 'client_token', 'confirm_product', 'connection', 'create_image', 'dns_name', 'ebs_optimized', 'endElement', 'eventsSet', 'get_attribute', 'get_console_output', 'group_name', 'groups', 'hypervisor', 'id', 'image_id', 'instance_profile', 'instance_type', 'interfaces', 
'ip_address', 'item', 'kernel', 'key_name', 'launch_time', 'modify_attribute', 'monitor', 'monitored', 'monitoring', 'monitoring_state', 'persistent', 'placement', 'placement_group', 'placement_tenancy', 'platform', 'previous_state', 'previous_state_code', 'private_dns_name', 'private_ip_address', 'product_codes', 'public_dns_name', 'ramdisk', 'reason', 'reboot', 'region', 'remove_tag', 
 'remove_tags', 'requester_id', 'reset_attribute', 'root_device_name', 'root_device_type', 'sourceDestCheck', 'spot_instance_request_id', 'start', 'startElement', 'state', 'state_code', 'state_reason', 'stop', 'subnet_id', 'tags', 'terminate', 'unmonitor', 'update', 'use_ip', 'virtualization_type', 'vpc_id']
 print(vm.ip_address)
 print(vm.id)
 print(vm.image_id)
 
 #List down VPC and Subnet. 
 
 conn = boto.vpc.connect_to_region("us-east-1", aws_access_key_id="AKIAJJOXJRFY4X6NEGCQ", aws_secret_access_key="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")
 
 conn.get_all_vpcs()
 [VPC:vpc-1331d86b]    
 
  conn.get_all_subnets()
  [Subnet:subnet-e3af88ef, Subnet:subnet-9531f7de, Subnet:subnet-863b93e2, Subnet:subnet-5dad6362, Subnet:subnet-7ad8de56, Subnet:subnet-1cebd046]