from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mov_cli.plugins import PluginHookData

from .hianime.scraper import *
from .animepahe.scraper import *

plugin: PluginHookData = {
    "version": 1,
    "package_name": "myanimeplugin",
    "scrapers": {
        "DEFAULT": HiAnimeScraper,
        "hianime": HiAnimeScraper,
        "animepahe": AnimePaheScraper
    }
}

__version__ = "0.1.0"