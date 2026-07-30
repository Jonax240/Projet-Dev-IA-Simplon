import pandas as pd
import plotly.express as px


df = pd.read_csv("ventes.csv")


df.columns = ["date", "produit", "prix", "qte", "region"]


df["ca"] = df["prix"] * df["qte"]


df_ventes_produit = (
    df.groupby("produit", as_index=False)["qte"].sum().rename(columns={"qte": "total_qte"})
)

fig1 = px.bar(
    df_ventes_produit,
    x="produit",
    y="total_qte",
    title="Total des ventes par produit (Quantités)",
    labels={"produit": "Produit", "total_qte": "Quantité totale vendue"},
)

fig1.write_html("ventes-par-produit.html")


df_ca_produit = (
    df.groupby("produit", as_index=False)["ca"].sum().rename(columns={"ca": "total_ca"})
)

fig2 = px.bar(
    df_ca_produit,
    x="produit",
    y="total_ca",
    title="Chiffre d'affaires par produit",
    labels={"produit": "Produit", "total_ca": "Chiffre d'affaires (€)"},
)

fig2.write_html("chiffre-affaires-par-produit.html")

print("Graphiques générés avec succès !")