from dataclasses import dataclass
from pathlib import Path

import click
import dacite
from loguru import logger as log


@dataclass(kw_only=True)
class Options:
    filename: Path | None


@click.group()
def cli(**kwargs):
    pass


@cli.command()
@click.argument("filename")
def extract(**kwargs):
    config = dacite.Config(type_hooks={Path: lambda d: Path(d).expanduser().resolve()})
    options = dacite.from_dict(data_class=Options, data=kwargs, config=config)
    log.info(f"extracting from {options.filename}")
