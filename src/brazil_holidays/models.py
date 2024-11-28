from dataclasses import dataclass
import datetime

@dataclass(frozen=True)
class Holiday:
    date: datetime.date
    name: str
