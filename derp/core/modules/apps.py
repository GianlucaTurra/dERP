"""Utility module for apps data
"""
from dataclasses import dataclass
from typing import List


@dataclass
class EndPoint:
    """Class to carry data of single endpoints of an app
    Each EndPoint its a single entry in the second menu opened
    through the first one (installed apps)
    """
    name: str
    url: str


@dataclass
class App:
    """Class to carry data from installed app (modules) for menus
    """
    name: str
    endpoints: List[EndPoint]


installed_apps = [
    App(
        name='Items',
        endpoints=[
            EndPoint('Master File', '/items/master'),
            EndPoint('Create Item', '/items/new'),
        ]
    ),
    App(
        name='Wearhouse',
        endpoints=[
            EndPoint('Master File', 'wearhouse/master'),
        ]
    )
]
