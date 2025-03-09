from dataclasses import dataclass


@dataclass
class User:
    name: str
    surname: str
    phone: str
    address: str
    metro: str
    delivery_date: str
    prolongation: str
    colour: str
    comment: str = None
