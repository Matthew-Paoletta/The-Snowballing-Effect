import pandas as pd
import numpy as np
from pathlib import Path

data_path = Path('data')
csv_files = sorted(data_path.glob('*.csv'))
dfs = [pd.read_csv(f, low_memory=False) for f in csv_files]
lol_data = pd.concat(dfs, ignore_index=True)

teams = lol_data[lol_data['position'] == 'team'].copy()
teams = teams[teams['gamelength'] >= 900]
teams = teams.dropna(subset=['golddiffat15', 'xpdiffat15', 'csdiffat15'])

print('Checking for year/date column:')
print('year' in teams.columns)
print('date' in teams.columns)

if 'year' in teams.columns:
    print('\nYear value counts:')
    print(teams['year'].value_counts().sort_index())
    
    print('\nturretplates missing by year:')
    print(teams.groupby('year')['turretplates'].apply(lambda x: x.isnull().mean()).round(3))
    
    print('\nturretplates missing by league (top 10):')
    print(teams.groupby('league')['turretplates'].apply(lambda x: x.isnull().mean()).sort_values(ascending=False).head(10).round(3))

print('\n\nChecking other columns:')
print('Available columns:', list(teams.columns[:50]))
