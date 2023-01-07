import typer

from sqs_cli.app import validators


########################################
# App
########################################

app = typer.Typer(
    name="profiles",
    help="TODO",
)


########################################
# Autocompletion
########################################


def config_keys():
    return [
        "region",
        "endpoint_url",
        "access_key_id",
        "secret_access_key",
    ]


########################################
# Commands
########################################


@app.command(
    name="create",
    help="TODO",
)
def create_profile(
    profile_name: str = typer.Option(
        ...,
        "-n",
        "--name",
        prompt=True,
        callback=validators.string,
        help="TODO",
    ),
    access_key_id: str = typer.Option(
        ...,
        "-k",
        "--access-key-id",
        prompt=True,
        callback=validators.string,
        help="TODO",
    ),
    secret_key: str = typer.Option(
        ...,
        "-s",
        "--secret-access-key",
        prompt=True,
        callback=validators.string,
        help="TODO",
    ),
    region: str = typer.Option(
        ...,
        "-r",
        "--region",
        prompt=True,
        callback=validators.string,
        help="TODO",
    ),
    endpoint_url: str = typer.Option(
        ...,
        # "-u",
        # "--endpoint-url",
        prompt=True,
        callback=validators.string,
        help="TODO",
    ),
):
    print(endpoint_url)
    # from rich.console import Console
    # from rich.table import Table

    # table = Table(title="Star Wars Movies")

    # table.add_column("Released", style="cyan", no_wrap=True)
    # table.add_column("Title", style="magenta")
    # table.add_column("Box Office", justify="right", style="green")

    # table.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
    # table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
    # table.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")
    # table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")

    # console = Console()
    # console.print(table, justify="center")