import pandas as pd
from math import pi, pow


def calc_volume(diameter):
    return 4 * pi * pow(diameter / 2, 3) / 3


# Read the input file
df = pd.read_csv('/data/input/planets.csv')

# Perform the calculations
df['volume'] = df['diameter'].apply(calc_volume)

# Write the output file
df.to_csv('/data/output/planets_volume.csv', index=False)

print(df)
