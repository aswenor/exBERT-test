from typing import Sequence


NIQQUD_MARKS: Sequence[str] = (
    "\u05b4",   # hiriq
    "\u05b5",   # tzere
    "\u05b6",   # segol
    "\u05b7",   # patach
    "\u05b8",   # kamatz
    "\u05c7",   # kamatz katan
    "\u05c2",   # sin dot
    "\u05c1",   # shin dot
    "\u05b9",   # holam haser/male
    "\u05bc",   # dagesh/mappiq/shuruk
    "\u05bb",   # kubutz
    "\u05b0",   # shva
    "\u05b1",   # reduced segol
    "\u05b2",   # reduced patach
    "\u05b3",   # reduced kamatz
)

CANTILLATION_MARKS: Sequence[str] = (
    "\u05c3",   # sof passuk
    "\u0591",   # etnachta
    "\u0592",   # segol
    "\u0593",   # shalshelet
    "\u0594",   # zakef katan
    "\u0595",   # zakef gadol
    "\u0596",   # tifcha
    "\u0597",   # revia
    "\u05ae",   # zevia
    "\u0599",   # pashta, shene pashtin
    "\u05a8",   # shene pashtin
    "\u059a",   # yetiv
    "\u059b",   # tevir
    "\u051a",   # pazer
    "\u059f",   # qarne farah
    "\u05a0",   # telisha gedola
    "\u05f3",   # punctuation geresh
    "\u059c",   # accent geresh
    "\u059d",   # accent geresh muqdam (printed more to the right)
    "\u05f4",   # punctuation gershayim
    "\u059e",   # accent gershayim
    "\u05c0",   # paseq
    "\u05a5",   # mercha
    "\u05a3",   # munach
    "\u05a4",   # mahpach
    "\u05a7",   # darga
    "\u05a8",   # kadma
    "\u05a9",   # telisha ketana
    "\u05a6",   # mercha kefula
    "\u05aa",   # yerach ben yomo
    "\u05a2",   # atnach hafukh
    "\u05ab",   # ole
    "\u05ac",   # illuy
    "\u05ad",   # dechi
    "\u0598",   # tsinnorit
)

OTHER_DIACRITICS: Sequence[str] = (
    "\u05bd",   # meteg
)

ALL_DIACRITICS: list[str] = list(NIQQUD_MARKS) + list(CANTILLATION_MARKS) + list(OTHER_DIACRITICS)
