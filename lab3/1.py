from dataclasses import dataclass, asdict
import json

@dataclass
class Person:

    first_name: str
    last_name: str
    age: int
    PESEL: int
    postal_code: str
    address: str

    def save_to_json(self, filename: str):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(asdict(self), f, ensure_ascii=False, indent=4)

    @classmethod
    def load_from_json(cls, filename: str):
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return cls(**data)

# test
p = Person("Jan", "Kowalski", 25, 12233256845, "03-255", "ul. Dąbrowskiego 10, Kraków")
p.save_to_json("person.json")

p2 = Person.load_from_json("person.json")
print(p2)