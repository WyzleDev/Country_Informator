import requests
import click
import webbrowser
import os
import colorama
from colorama import Fore, Back

from click.testing import CliRunner

def test_sync():
    @click.group()
    @click.option('--debug/--no-debug', default=False)
    def cli(debug):
        click.echo('Debug mode is %s' % ('on' if debug else 'off'))

    @cli.command()
    def sync():
        click.echo('Syncing')

    runner = CliRunner()
    result = runner.invoke(cli, ['--debug', 'sync'])
    assert result.exit_code == 0
    assert 'Debug mode is on' in result.output
    assert 'Syncing' in result.output