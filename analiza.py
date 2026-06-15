import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Učitavanje podataka
try:
    df = pd.read_csv('podaci.csv')
    print("✅ Podaci su uspešno učitani!\n")
except FileNotFoundError:
    print("❌ Greška: Fajl 'podaci.csv' nije pronađen.")
    exit()

# Podešavanje stila za lepši izgled grafikona
sns.set_theme(style="whitegrid")

# --- GRAFIKON 1: Distribucija godina pacijenata (Histogram) ---
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x='Godine', kde=True, color='skyblue', bins=10)
plt.title('Distribucija godina pacijenata u uzorku', fontsize=14, fontweight='bold')
plt.xlabel('Godine starosti', fontsize=12)
plt.ylabel('Broj pacijenata', fontsize=12)
plt.tight_layout()
plt.savefig('1_distribucija_godina.png') # Čuva grafikon kao sliku
plt.close()
print("📊 Grafikon 1 sačuvan kao '1_distribucija_godina.png'")

# --- GRAFIKON 2: Nivo glukoze u odnosu na hroničnu bolest (Box-plot) ---
plt.figure(figsize=(8, 5))
# Menjamo 0 i 1 u čitljive labele na grafikonu
df['Status_Bolesti'] = df['Hronicna_Bolest'].map({0: 'Zdravi', 1: 'Oboleli'})

sns.boxplot(data=df, x='Status_Bolesti', y='Glukoza_mmol_L', palette='Set2')
plt.title('Poređenje nivoa glukoze kod zdravih i obolelih pacijenata', fontsize=14, fontweight='bold')
plt.xlabel('Zdravstveni status', fontsize=12)
plt.ylabel('Glukoza (mmol/L)', fontsize=12)
plt.tight_layout()
plt.savefig('2_glukoza_boxplot.png')
plt.close()
print("📊 Grafikon 2 sačuvan kao '2_glukoza_boxplot.png'")

# --- GRAFIKON 3: Matrica korelacije zdravstvenih faktora (Heatmap) ---
plt.figure(figsize=(10, 8))
# Selektujemo samo numeričke kolone za korelaciju
numericke_kolone = df[['Godine', 'BMI', 'Krvni_Pritisak_Sistolni', 'Holesterol_mmol_L', 'Glukoza_mmol_L', 'Hronicna_Bolest']]
matrica_korelacije = numericke_kolone.corr()

sns.heatmap(matrica_korelacije, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Matrica korelacije javnozdravstvenih faktora rizika', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('3_faktori_rizika_heatmap.png')
plt.close()
print("📊 Grafikon 3 sačuvan kao '3_faktori_rizika_heatmap.png'")

print("\n🎉 Uspešno! Svi grafikoni su generisani i sačuvani u tvom folderu.")