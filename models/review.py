#!/usr/bin/python3
"""Review Module"""


from models.base_model import BaseModel


class review(BaseModel):
    """Review Class"""
    place_id = ""
    user_id = ""
    text = ""
