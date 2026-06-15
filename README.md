# 🏥 Biostatistička Analiza Faktora Rizika 

Ovaj projekat predstavlja simulaciju epidemiološkog istraživanja kakva se sprovode u **Zdravstvenim ustanovama**. Cilj projekta je identifikacija i analiza ključnih faktora rizika (poput BMI, glukoze, holesterola i navika) koji doprinose razvoju hroničnih nezaraznih bolesti u populaciji.

## 🛠️ Tehnologije i Biblioteke
- **Python** (Glavni programski jezik)
- **Pandas & NumPy** (Učitavanje, čišćenje i deskriptivna statistika)
- **Matplotlib & Seaborn** (Medicinska vizuelizacija i grafički prikazi)

## 📊 Rezultati Deskriptivne Statistike
Na osnovu analize uzorka dobijeni su sledeći epidemiološki indikatori:
- **Prevalenca hroničnih bolesti:** 46.7% ispitanika u uzorku ima dijagnostikovano oboljenje.
- **Udeo pušača:** 43.3% populacije su aktivni pušači, što predstavlja visok faktor rizika.

## 📈 Vizuelizacija i Interpretacija Podataka

### 1. Starosna struktura populacije
Analizom distribucije godina utvrđeno je da uzorak obuhvata pacijente od rane mladosti do duboke starosti, sa izraženim pikom u uzrastu preko 50 godina, što je karakteristično za populacije sa povišenim rizikom od hroničnih oboljenja.

### 2. Uticaj glukoze na zdravstveni status
Kroz *Box-plot* dijagram jasno je uočljiva statistički značajna razlika u nivoima glukoze. Kod grupe obolelih, medijana i vrednosti glukoze su znatno povišene i prelaze granicu od 6.0 mmol/L, za razliku od zdrave populacije.

### 3. Korelacija faktora rizika
*Heatmap* matrica korelacije je pokazala najsnažniju pozitivnu povezanost između hroničnih oboljenja i faktora kao što su **indeks telesne mase (BMI)**, **godine starosti** i **glukoza**. Povišen BMI pokazuje jasnu spregu sa skokom sistolnog krvnog pritiska.

## 🚀 Kako pokrenuti projekat?
1. Klonirati repozitorijum.
2. Instalirati biblioteke: `pip install pandas numpy matplotlib seaborn`
3. Pokrenuti skriptu: `python analiza.py`
