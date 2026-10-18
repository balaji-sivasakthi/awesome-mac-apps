from pathlib import Path
import json,re
from urllib.parse import urlsplit
root=Path(__file__).resolve().parents[1]
data=json.loads((root/'dist/catalog.json').read_text())
apps=data['apps']
assert len(apps)>2700
assert len({a['id'] for a in apps})==len(apps)
assert sum(a['name']=='NotchDude' for a in apps)==1
assert next(a for a in apps if a['name']=='Obsidian')['category']=='Writing & notes'
assert next(a for a in apps if a['name']=='Bitwarden')['category']=='Security & privacy'
excluded={'NotchMuse','Sonar','Agent Island','Atoll','CodexIsland','Boring Notch','DynamicHorizon','HeyMate','ILoveNotch','NotchNook','Notchly','Peninsula','Brink','Metrune'}
assert not excluded.intersection(a['name'] for a in apps)
for app in apps:
 assert app['name'] and app['description'] and app['category']
 assert urlsplit(app['url']).scheme in ('https','http')
 assert not re.search(r'[?&](?:via|ref|utm_\w+)=',app['url'])
for asset in ['index.html','styles.css','app.js','logo.svg']:
 assert (root/'dist'/asset).is_file(),asset
print(f'Site checks passed: {len(apps)} records, unique IDs, preserved exclusions, clean URLs, and complete assets.')
