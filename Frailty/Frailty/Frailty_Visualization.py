import matplotlib.pyplot as plt
import seaborn as sns
plt.bar(df["Frailty"].unique(),df["Frailty"].value_counts())
plt.xlabel("Frailty data")
plt.ylabel("Height")
sns.scatterplot(x=df["Age"],y=df["Gripstrength"])
sns.histplot(df["Height"])
