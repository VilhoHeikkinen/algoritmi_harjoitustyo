# Miinaharavan ratkaisija DSSP-algoritmilla

- [Määrittelydokumentti](dokumentaatio/määrittelydokumentti.md)
- [Toteutusdokumentti](dokumentaatio/toteutusdokumentti.md)
- [Testausdokumentti](dokumentaatio/testausdokumentti.md)

## Käyttöohje

1. Kopioi projekti komennolla ```git clone https://github.com/VilhoHeikkinen/algoritmi_harjoitustyo.git```
2. Siirry projektin koodien kansioon ```cd algoritmi_harjoitustyo/src```
3. Siirry virtuaaliseen ympäristöön komennolla ```poetry shell``` ja lataa riippuvuudet ```poetry install```
4. Algoritmi voidaan suorittaa ajamalla komento ```python3 run_dssp.py```

run_dssp.py syötteet:
```
usage: run_dssp.py [-h] [--difficulty DIFFICULTY] [--disable-gui]

options:
  -h, --help            show this help message and exit

Basic input stuff:
  --difficulty DIFFICULTY
                        The difficulty of the minesweeper game (b = beginner, i = intermediate, e = expert)
  --disable-gui         Disable pygame GUI and output the game to terminal
```

### Testien ajaminen
Testit voidaan toistaa ajamalla seuraavat komennot projektin juurihakemistossa:

```coverage run --branch -m pytest src```

```coverage report -m```
