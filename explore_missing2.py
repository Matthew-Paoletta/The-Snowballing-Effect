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

# Let's look at missingness of turretplates vs result
print('turretplates missing by result (win/loss):')
print(teams.groupby('result')['turretplates'].apply(lambda x: x.isnull().mean()).round(3))

print('\nturretplates missing by side (blue/red):')
if 'side' in teams.columns:
    print(teams.groupby('side')['turretplates'].apply(lambda x: x.isnull().mean()).round(3))

print('\nturretplates missing by league (for modern data 2022+):')
modern_teams = teams[teams['year'] >= 2022]
print(modern_teams.groupby('league')['turretplates'].apply(lambda x: x.isnull().mean()).sort_values(ascending=False).head(10).round(3))

print('\n\nLet me check url column:')
print(f'url missing: {teams["url"].isnull().mean():.3f}')
print('\nurl missing by year:')
print(teams.groupby('year')['url'].apply(lambda x: x.isnull().mean()).round(3))

print('\nurl missing by result:')
print(teams.groupby('result')['url'].apply(lambda x: x.isnull().mean()).round(3))
