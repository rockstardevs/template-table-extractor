from dataclasses import dataclass, field
from pathlib import Path

import pandas as pd

# from camelot.core import Table
from camelot.parsers import Stream


@dataclass(kw_only=True)
class TemplateCache:
    """Stores metadata and intermediate parsed data from a document."""

    markers: dict[str, list] = field(default_factory=dict)
    origins: dict[str, tuple[float, float]] = field(default_factory=dict)
    tables: list = field(default_factory=list)
    frames: dict[str, pd.DataFrame] = field(default_factory=dict)


@dataclass(kw_only=True)
class Document:
    """A document with tabulated secionts parsed from pdf format to Dataframes."""

    filename: Path
    line_margin: float = 0.475

    def __post_init__(self) -> None:
        self.parser = Stream()
        self.parser._generate_layout(self.filename, {"line_margin": self.line_margin})
        self.cache = TemplateCache()

    def reset_cache(self) -> None:
        self.cache = TemplateCache()
