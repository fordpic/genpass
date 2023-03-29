import click
from app import application

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    pass


@cli.command()
@click.option('-l', '--length', type=int, help='Length of password to generate')
def generate(length):
    """generates a random password of given length"""
    logo = """
    +-----------------------------+
    |     Genpass thanks you!     |
    +-----------------------------+
    """

    # generate password
    password = application.generate(int(length))

    click.echo(password)
    click.echo(logo)
