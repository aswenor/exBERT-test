from typing import Sequence

NIQQUD_MARKS: Sequence[str] = (
    "\u05b4",   # POINT HIRIQ 
    "\u05b5",   # POINT TSERE 
    "\u05b6",   # POINT SEGOL 
    "\u05b7",   # POINT PATAH 
    "\u05b8",   # POINT QAMATS 
    "\u05c7",   # POINT QAMATS QATAN 
    "\u05c2",   # POINT SIN DOT 
    "\u05c1",   # POINT SHIN DOT 
    "\u05b9",   # POINT HOLAM 
    "\u05ba",   # POINT HOLAM HASER FOR VAV 
    "\u05bc",   # POINT DAGESH OR MAPIQ (= shuruq) 
    "\u05bb",   # POINT QUBUTS 
    "\u05b0",   # POINT SHEVA 
    "\u05b1",   # POINT HATAF SEGOL 
    "\u05b2",   # POINT HATAF PATAH 
    "\u05b3",   # POINT HATAF QAMATS 
    "\u05bf",   # POINT RAFE 
)

CANTILLATION_MARKS: Sequence[str] = (
    "\u05c3",   # PUNCTUATION SOF PASUQ 
    "\u0591",   # ACCENT ETNAHTA (= atnah) 
    "\u0592",   # ACCENT SEGOL (= segolta) 
    "\u0593",   # ACCENT SHALSHELET 
    "\u0594",   # ACCENT ZAQEF QATAN 
    "\u0595",   # ACCENT ZAQEF GADOL 
    "\u0596",   # ACCENT TIPEHA (= tarha, me'ayla) 
    "\u0597",   # ACCENT REVIA 
    "\u05ae",   # ACCENT ZINOR (= tsinor, zarqa) 
    "\u0599",   # ACCENT PASHTA 
    "\u059a",   # ACCENT YETIV 
    "\u059b",   # ACCENT TEVIR 
    "\u05a1",   # ACCENT PAZER (= pazer qatan) 
    "\u059f",   # ACCENT QARNEY PARA (= pazer gadol) 
    "\u05a0",   # ACCENT TELISHA GEDOLA 
    "\u05f3",   # PUNCTUATION GERESH 
    "\u059c",   # ACCENT GERESH (= teres) 
    "\u059d",   # ACCENT GERESH MUQDAM 
    "\u05f4",   # PUNCTUATION GERSHAYIM 
    "\u059e",   # ACCENT GERSHAYIM 
    "\u05c0",   # PUNCTUATION PASEQ (= legarmeh) 
    "\u05a5",   # ACCENT MERKHA (= yored) 
    "\u05a3",   # ACCENT MUNAH 
    "\u05a4",   # ACCENT MAHAPAKH 
    "\u05a7",   # ACCENT DARGA 
    "\u05a8",   # ACCENT QADMA (= azla) 
    "\u05a9",   # ACCENT TELISHA QETANA 
    "\u05a6",   # ACCENT MERKHA KEFULA 
    "\u05aa",   # ACCENT YERAH BEN YOMO 
    "\u05a2",   # ACCENT ATNAH HAFUKH 
    "\u05ab",   # ACCENT OLE 
    "\u05ac",   # ACCENT ILUY 
    "\u05ad",   # ACCENT DEHI 
    "\u0598",   # ACCENT ZARQA (= tsinorit, zinorit) 
    "\u05be",   # PUNCTUATION MAQAF 
    "\u05c6",   # PUNCTUATION NUN HAFUKHA 
    "\u05af",   # MARK MASORA CIRCLE 
    "\u05bd",   # POINT METEG (= siluq) 
)

OTHER_DIACRITICS: Sequence[str] = (
    "\u05c4",   # MARK UPPER DOT (punctum etraordinarium) 
    "\u05c5",   # MARK LOWER DOT (punctum etraordinarium) 
    "\ufb1e",   # JUDEO-SPANISH VARIKA 
)

ALL_DIACRITICS: list[str] = list(NIQQUD_MARKS) + list(CANTILLATION_MARKS) + list(OTHER_DIACRITICS)