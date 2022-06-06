from importlib import import_module
from pathlib import Path


def import_all():
    for f in Path(__file__).parent.glob('*.py'):
        if not f.stem.startswith('_'):
            import_module(f'.{f.stem}', __package__)


def setup():
    import_all()
