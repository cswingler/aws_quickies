import boto3
import datetime

class AControl():
    ec2_client = boto3.client('ec2')

    def find_instances(self, search_name):
        """
        Returns a list of instance Dicts that match search_name.
        :param name: Name to search for (simple substring search)
        :return: List of matching instance IDs (empty list if no matches)
        """
        search_string = "*" + search_name + "*"
        filters = [
            {
                'Name': 'tag:Name',
                'Values': [
                    search_string
                ]
            }
        ]

        result = self.ec2_client.describe_instances(Filters = filters)

        found_instances = []
        # Really, this _is_ everything, we just need to filter out the data we want.
        for reservation in result['Reservations']:
            for instance in reservation['Instances']:
                found_instances.append(instance)
        return found_instances

    def filter_instance_data_human(self, instances):
        """
        Returns a simplified output of the requested data and fields, all human-readable.
        :param instances: a list returned from find_instances()
        :return:
        """

        return_l = []


        for i in instances:
            r_val = {}
            tags = i['Tags']
            for t in tags:
                if t['Key'] == 'Name':
                    r_val['Name'] = t['Value']
                if t['Key'] == 'Squad':
                    r_val['Squad'] = t['Value']
            r_val['InstanceType'] = i['InstanceType']
            r_val['InstanceAge'] = str(datetime.datetime.now(datetime.timezone.utc) - i['LaunchTime'])
            r_val['InstanceId'] = i['InstanceId']
            r_val['State'] = i['State']['Name']
            r_val['PrivateIpAddress'] = i['PrivateIpAddress']

            return_l.append(r_val)

        return return_l







