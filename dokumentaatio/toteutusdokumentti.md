# Harjoitustyön toteutus

## Projektin yleisrakenne
Projekti jakautuu kahteen osaan: miinaharavaan ja DSSP-algoritmiin

### Miinaharavan toteutus

- Pelin toiminta toteutettu käyttäen apuna miinaharavan projektipohjaa [1], joka oli annettu harjoitustyön aihe-ehdoduksissa. Projektipohjasta otin vain vähän mallia,
  mutta silmäilin kuitenkin pelin perustoiminnot läpi.
  - Pelissä tallennetaan tilanne kolmeen kaksiulotteiseen listaan: values, opened ja marked. values sisältää kaikkien ruutujen arvot
    (siis epänegatiivinen numero jos kyseessä ei ole miina, -1 jos ruutu on miina). opened ja marked sisältävät tiedot avatuista ja merkatuista ruuduista.
  - Miinat generoidaan ensimmäisen avauksen jälkeen, jotta ensimmäinen ruutu ei voi olla miina, paitsi jos miinat annetaan mine_locations parametrin avulla syötteenä
  - Algoritmin toimimisen ja pelin pelaamisen kannalta tärkeä on metodi get_grid(), joka palauttaa pelikentän kaksiulotteisena taulukkona, siten että avatut, avaamattomat ja merkatut ruudut otetaan huomioon.
  - Pelin ja algoritmin välisenä rajapintana toimii minesweeperapp.py, joka myös toteuttaa pelille käyttöliittymän.
 
### Algoritmin toteutus

Projektissa käytetty algoritmi on DSSP (Double Set Single Point), jonka pääideana on kaksi settiä ruutuja, setti S ja setti Q. Setti S sisältää ruudut, jotka voidaan avata. Useimmiten nämä ruudut on siis
todettu tyhjiksi. Kuitenkin joskus ei löydetä yhtään varmoja tyhjiä ruutuja, jolloin joudutaan arvaamaan, ja tämä arvattu ruutu siirretään settiin S. Kun setistä S avataan ruutu, niin tutkitaan se, sekä muut
mahdollisesti auenneet ruudut. Jos näistä ei voida tietää, että ovatko niiden viereiset peitetyt ruudut tyhjiä, niin siirretään kyseiset ruudut settiin Q. Setin Q ruudut tutkitaan erikseen, ja näitä ei suoraan avata,
vaan siirretään settiin S, jos niistä ollaan varmoja [2].

- Viereisten ruutujen tutkiminen
  - Viereiset ruudut tutkitaan käyttämällä metodeja is_afn() (all free neighbours), is_amn() (all mine/mark neighbours) sekä unmarked_neighbours()
  - Kaikki näistä tutkivat ajassa O(1) yhden ruudun tilanteen viereisten ruutujen suhteen
  - unresolved_squares() etsii kaikki ruudut, joihin on laudalla suora yhteys (ei yhtään peitettyjä ruutuja välissä), rekursiivisesti ajassa O(nm), missä kentän koko on (n x m)
- Algoritmin arvaaminen on toteutettu täysin satunnaisesti, eli arvaustilanteessa valitaan joku avaamaton ruutu riippumatta sen sijainnista tai viereisistä ruuduuista

Implementoitu algoritmi on suorituskyvyltään seuraavanlainen (dokumentaatio/stats.txt):
```
Statsit 1000 ajolla:

Beginner wins: 709
Intermediate wins: 356
Expert wins: 0

Statsit 10 000 ajolla:

Beginner wins: 7115
Intermediate wins: 3805
Expert wins: 101
```

Huomataan siis, että beginner-tasolla peli voitetaan ~71% ajasta, intermediate tasolla ~38% ajasta ja expert-tasolla ~1% ajasta.

Algoritmi on siis suhteellisen hyvä pelaamaan miinaharavaa, ottaen huomioon miinaharavan luonteen. Miinaharavassa on joskus pakko arvata, mikä estää täydellisen voittoprosentin millään algoritmilla.

### Mahdollisia parannuksia

- Algoritmia voisi parantaa esimerkiksi parannetulla arvaamisella. Jos esimerkiksi on avattu ruutu, jonka arvo on 1, ja sen vieressä on kaksi avaamatonta ruutua, niin näistä toinen on miina 1/2 todennäköisyydellä.
  Jos taas saman arvoltaan 1 ruudun vieressä on kolme avaamatonta ruutua, niin näistä yksi on miina 1/3 todennäköisyydellä.
- Varsinkin algoritmin koodi voisi olla siistimpää, ja esimerkiksi naapurien hakemiseen voisi lisätä metodin, jotta metodeissa is_afn(), is_amn() ja unmarked_neighbours() ei haettaisi näitä erikseen.

### Tekoälyn käyttö

- En käyttänyt projektia tehdessä lainkaan laajoja kielimalleja.

# Lähteet
- [1] Miinaharavan valmis projektipohja [https://github.com/TiraLabra/minesweeper](https://github.com/TiraLabra/minesweeper)
- [2] David Becerran kandidaatin tutkielma [https://dash.harvard.edu/handle/1/14398552](https://dash.harvard.edu/handle/1/14398552)
