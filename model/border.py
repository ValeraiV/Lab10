from dataclasses import dataclass
from model.country import Country
@dataclass
class Border:
    _c1: Country
    _c2: Country

    @property
    def c1(self):
        return self._c1

    @property
    def c2(self):
        return self._c2

    def __hash__(self):
        return hash((self._c1.CCode, self._c2.CCode))

    def __str__(self):
        return f"Border: {self._c1} - {self._c2}"

