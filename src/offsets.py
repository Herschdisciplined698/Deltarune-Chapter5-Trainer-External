from dataclasses import dataclass

@dataclass
class Offsets:
    base_address: int = 0x2A4B4BB
    hp_current: int = 0x293
    hp_max: int = 0x297
    atk: int = 0x29B
    def_: int = 0x29F
    magic: int = 0x2A3
    gold: int = 0x2BB
    inventory_ptr: int = 0x2DB
    battle_flag: int = 0x313
    timer: int = 0x32B
    items_base: int = 0x2A4B5AB

CURRENT_OFFSETS = Offsets()
