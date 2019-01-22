# -*- coding: utf-8 -*-

from .equipment import lt_equipment
from .spell import lt_spell_lxy, lt_spell_zle, lt_spell_lyr, lt_spell_an
from .monster import lt_monster
from .zone import lt_zone

doc_data = dict(
    lt_equipment=lt_equipment,
    lt_spell_lxy=lt_spell_lxy,
    lt_spell_zle=lt_spell_zle,
    lt_spell_lyr=lt_spell_lyr,
    lt_spell_an=lt_spell_an,
    lt_monster=lt_monster,
    lt_zone=lt_zone,
)