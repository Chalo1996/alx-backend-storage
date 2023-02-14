#!/usr/bin/env python3
"""9-insert_school module."""

from typing import List, Dict, Union, Any


def insert_school(mongo_collection: Dict[str, str], **kwargs: Any) -> str:
    """insert_school function."""
    return mongo_collection.insert_one(kwargs).inserted_id
