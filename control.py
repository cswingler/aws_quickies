import boto3

class AControl():
    ec2_resource = boto3.resource('ec2')
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



