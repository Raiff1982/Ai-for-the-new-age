import matplotlib.pyplot as plt
import numpy as np
from skyfield.api import load, Topos
from skyfield.data import hipparcos

# Load star data
with load.open(hipparcos.URL) as f:
    df = hipparcos.load_dataframe(f)

# Define observer location and time
ts = load.timescale()
t = ts.utc(2023, 12, 8, 22, 0, 0)  # December 8, 2023 at 10:00 PM local time
observer = Topos('29.7604 N', '95.3698 W')  # Houston, TX

# Calculate star positions
eph = load('de421.bsp')
earth = eph['earth']
astrometric = (earth + observer).at(t).observe(df)
alt, az, distance = astrometric.apparent().altaz()

# Filter stars that are above the horizon
mask = alt.degrees > 0
alt = alt.degrees[mask]
az = az.degrees[mask]
names = df['proper'][mask]

# Create the plot
plt.figure(figsize=(10, 5))
plt.scatter(az, alt, c='white', s=10)
plt.gca().set_facecolor('black')

# Annotate a few stars
for i in range(min(5, len(names))):
    plt.text(az[i], alt[i], names.iloc[i], fontsize=8, color='yellow')

plt.title("Star Chart for Houston, TX on December 8, 2023")
plt.xlabel("Azimuth (degrees)")
plt.ylabel("Altitude (degrees)")
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.gca().invert_xaxis()  # Invert x-axis to match the sky view
plt.show()