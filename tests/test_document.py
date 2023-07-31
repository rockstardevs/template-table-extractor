from pathlib import Path

from extractor.core.document import Document, TemplateCache


def test_init():
    d = Document(filename=Path("testdata/test_sample_1.pdf"))
    assert d.parser is not None
    assert d.cache is not None


def test_reset_cache():
    c = TemplateCache(
        markers={"test": []}, origins={"test": []}, tables=[], frames={"test": None}
    )
    d = Document(filename=Path("testdata/test_sample_1.pdf"))
    d.cache = c
    d.reset_cache()
    assert d.cache.markers == {}
    assert d.cache.origins == {}
    assert d.cache.tables == []
    assert d.cache.frames == {}
