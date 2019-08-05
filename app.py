#!/usr/bin/env python3
import random
import uuid
from dataclasses import field
from typing import (
    ClassVar,
    Optional,
    Type,
)

import hug
import marshmallow as mm
from marshmallow.fields import (
    UUID,
)
from marshmallow_dataclass import dataclass


DOG_TYPES_TO_ABBREVIATIONS = {
    'Australian Cattle Dog': 'ACD',
    'German Shepherd Dog': 'GSD',
    'Pomeranian': None,
}


@dataclass
class Dog:
    """Dog type contract."""
    id: str = field(metadata={'marshmallow_field': UUID()})
    name: str
    abbreviation: Optional[str]
    Schema: ClassVar[Type[mm.Schema]]


@hug.cli()
@hug.get('/dogs')
def dogs() -> Dog.Schema(many=True):
    """A fake index of dog resources that is randomly generated."""
    return [
        Dog(id=uuid.uuid1(), name=name, abbreviation=abbrev)
        for name, abbrev in (
            random.choice(list(DOG_TYPES_TO_ABBREVIATIONS.items()))
            for idx in range(10)
        )
    ]


@hug.cli()
@hug.get('/dogs/{id}')
def dog(id: UUID()) -> Dog.Schema():
    """A fake dog resource that echos and randomly generates a dog."""
    name = random.choice(list(DOG_TYPES_TO_ABBREVIATIONS))
    abbrev = DOG_TYPES_TO_ABBREVIATIONS[name]
    return Dog(id=id, name=name, abbreviation=abbrev)


if __name__ == '__main__':
    hug.API(__name__).cli()
