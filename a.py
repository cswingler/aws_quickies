#!/usr/bin/env python3

# This is just a thing to make formatting/searching for things in the aws command line quicker.

import click
import control
from beautifultable import BeautifulTable

@click.group()
@click.pass_context
def cli(ctx):
    """
    A command line tool to quickly look up information in AWS.
    \f
    :param ctx: Context
    :return: Nothing
    """

@cli.command()
@click.pass_context
@click.argument('instance_name_search')
def ec2info(ctx, instance_name_search):
    """
    instance_info NAME
    Prints out the instance(s) that match NAME.
    \f
    :param ctx:
    :return:
    """
    c = control.AControl()
    instances = c.find_instances(instance_name_search)
    formatted= c.filter_instance_data_human(instances)

    table = BeautifulTable(max_width=200)

    # In order of output:
    columns = [
        'Name',
        'PrivateIpAddress',
        'InstanceType',
        'InstanceAge',
        'InstanceId',
        'Squad',
        'State',
        'InfoLink'
    ]
    table.column_headers = columns
    for f in formatted:
        f['InfoLink'] = 'https://www.ec2instances.info/?filter=' + f['InstanceType']
        output_l = []
        for c in columns:
            output_l.append(f[c])
        table.append_row(output_l)

    table.sort('Name')
    table.set_style(BeautifulTable.STYLE_COMPACT)
    click.echo(table)

if __name__ == "__main__":
    cli(obj = {})
