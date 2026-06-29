from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Loadout:
    weapon_id: int
    ammo_id: int