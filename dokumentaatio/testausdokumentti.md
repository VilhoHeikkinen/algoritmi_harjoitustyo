# Harjoitustyön testaus

## Kattavuusraportti
![image](https://github.com/user-attachments/assets/f04d48ff-806d-4b6c-b6de-6b166b022241)

## Testien toistaminen
Testit voidaan toistaa ajamalla seuraavat komennot projektin juurihakemistossa:

```coverage run --branch -m pytest src```

```coverage report -m```

## Yksikkötestatut ominaisuudet

### Miinaharavan metodit
- Testattu, että miinaharava generoi kentälle oikean määrän pommeja, sekä generoi pommit ensimmäisen klikkauksen jälkeen
- Virheen antaminen, kun syötteenä annetaan liikaa miinoja
- Kentän miinattomien ruutujen arvojen laskeminen. Tämä testatataan syöttämällä pelille miinat, ja tarkistetaan että kaikki ruudut saavat oikeat arvot
- Ruutujen avaus. Annetaan syötteenä miinojen paikat, ja tarkistetaan, että peli aukaisee viereiset miinattomat ruudut rekursiivisesti oikein

### DSSP-algoritmin metodit
- Algoritmin toiminta yleisesti. Syötteenä miinojen sijainnit, joilla DSSP onnistuu aina ratkaisemaan pelin, kun ensimmäinen avaus on vasen yläkulma.
  Sama peli ajetaan 100 kertaa, ja tarkistetaan, että aina tulee voitto. Testattuna myös, että algoritmi päättyy normaalisti, kun osutaan miinaan.

Naapureiden tutkimisen testaaminen on hoidettu käyttämällä samaa tilannetta:

![is_afn_testin_selitys](https://github.com/user-attachments/assets/c8f67fd3-79e3-4666-9a19-9fe324620dd2)
- is_afn() (all free neighbours), is_amn() (all mine/mark neighbours) sekä unmarked_neighbours() testattu tutkimalla peitettyjen ruutujen viereiset ruudut, ja varmistettu palautusarvot oikeiksi
- unresolved_squares() testattu aluksi avaamalla vasen yläkulma, ja tarkistettu että kaksi alinta riviä palautetaan. Testattu myös että merkkaukset ja uudet avaukset huomioidaan oikein,
  ja että kertaalleen tutkittuja ruutuja ei palauteta metodia ajettaessa uudestaan.

### Seuraavia EI yksikkötestattu:
- Miinaharavan käyttämiseen liittyvä "sovellus" minesweeperapp.py, joka toimii käytännössä rajapintana miinaharavan sekä algoritmin välillä
- Graafinen käyttöliittymä
- firstmove.py, joka valitsee ensimmäiseksi avattavaksi ruuduksi vain nurkan
- random_square.py, joka on triviaali metodi

## Empiirinen testaus

- Graafinen käyttöliittymä sekä terminaaliin printattu käyttöliittymä huomattu toimivaksi peliä ajettaessa
- Algoritmin suoriutuminen tilastollisesti (dokumentaatio/stats.txt)
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
David Becerran tutkielman [1] tilastot DSSP-algoritmin suoriutumisesta:

![image](https://github.com/user-attachments/assets/1c65b502-c05c-465e-9e0b-f815cf955b7d)

Tilastot ovat siis lähes samat.

## Lähteet
- [1] David Becerran kandidaatin tutkielma [https://dash.harvard.edu/handle/1/14398552](https://dash.harvard.edu/handle/1/14398552)
