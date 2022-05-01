import click
from utils_cli import (
    get_api,
)
from configuration import (
    Configuration,
)


@click.command()
def list_tokens():
    """List all added tokens."""
    configuration = Configuration().load_configuration()
    api = get_api()

    tokens = api.list_tokens(configuration)
    click.echo('ETH')
    for token in tokens:
        click.echo('%s' % token)



