
import pandas as pd


def create_diameters():
    raw_data = {'planet': ['Mercury', 'Venus', 'Earth',
                           'Mars', 'Jupiter', 'Saturn',
                           'Uranus', 'Neptune', 'Pluto'],
                'diameter': [4878, 12104, 12760, 6787, 139822,
                             120500, 51120, 49530, 2301]
                }
    df = pd.DataFrame(raw_data, columns=['planet', 'diameter'])
    df.to_csv('/data/inputs/planets.csv', index=False)


if __name__ == "__main__":
    create_diameters()
