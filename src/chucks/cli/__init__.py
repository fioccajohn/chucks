import click
from bindle.__about__ import __version__

# TODO:
# Create CLI utility for quick terminal looks.

@click.group(
    context_settings={"help_option_names": ["-h", "--help"]},
    invoke_without_command=True,
)
@click.version_option(version=__version__, prog_name="Chucks")
def chucks():
    click.echo("Hello world!")
