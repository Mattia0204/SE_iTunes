from dataclasses import dataclass

@dataclass
class Connessione:
    a1: int
    a2: int

    def __eq__(self, other):
        return self.a1 == other.a1 and self.a2 == other.a2

    def __str__(self):
        return f"{self.a1} ({self.a2})"

    def __repr__(self):
        return f"{self.a1} ({self.a2})"

