import pandas as pd
import numpy as np
from math import pi, pow


def create_diameters():
    raw_data = {'planet': ['Mercury', 'Venus', 'Earth',
                           'Mars', 'Jupiter', 'Saturn',
                           'Uranus', 'Neptune', 'Pluto'],
                'diameter': [4878, 12104, 12760, 6787, 139822,
                             120500, 51120, 49530, 2301]
                }
    df = pd.DataFrame(raw_data, columns=['planet', 'diameter'])
    df.to_csv('/data/input/planets.csv', index=False)

def calc_volume(diameter):
    return 4 * pi * pow(diameter / 2, 3) / 3

# Yes, the "imaginary" csv, was created with python
# create_diameters()

# Read the input file
df = pd.read_csv('/data/input/planets.csv')

# Perform the calculations
df['volume'] = df['diameter'].apply(calc_volume)

# Write the output file
df.to_csv('/data/output/planets_volume.csv', index=False)

# Profit
print(df)



