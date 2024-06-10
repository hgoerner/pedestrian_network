from sklearn.preprocessing import StandardScaler
import numpy as np

# Beispiel-Daten
data = np.array([[0, 0], [0, 0], [1, 1], [1, 1]])
print(data)
# Scaler-Instanz erstellen
scaler = StandardScaler()

# Daten transformieren
scaled_data = scaler.fit_transform(data)

# Transformierte Daten ausgeben
print(scaled_data)