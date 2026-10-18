from pathlib import Path
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode
import re,json,hashlib,html
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parents[1]/'dist'
apps=[];by_name={};by_url={}
def clean_url(url):
 p=urlsplit(url)
 tracking={'via','ref','referrer','aff','affiliate','affid','pt','ct','mt','campaign','cid','ls'}
 query=urlencode([(k,v) for k,v in parse_qsl(p.query) if not k.lower().startswith('utm_') and k.lower() not in tracking])
 return urlunsplit((p.scheme,p.netloc,p.path,query,p.fragment))
def plain(t):
 t=re.sub(r'\[([^]]+)\]\([^)]+\)',r'\1',t)
 return html.unescape(re.sub(r'<[^>]*>|[*_`~]','',t)).replace(r'\|','|').strip()
def canonical(u):
 p=urlsplit(u);return p.netloc.lower().removeprefix('www.')+p.path.lower().rstrip('/').removesuffix('.git')
groups={'Reading and Writing Tools':'Writing & notes','Developer Tools':'Developer tools','Terminal Apps':'Developer tools','Design and Product':'Design & creative','AI Tools':'AI tools','Communication':'Communication','Audio and Video Tools':'Audio & video','Utilities':'Productivity','Gaming Software':'Games','Finance':'Finance','Browsers':'Browsers','Cloud Storage':'Files & storage','Backup and Sync':'Files & storage','Download Management Tools':'Files & storage','Encryption':'Security & privacy','Security Tools':'Security & privacy','Proxy and VPN Tools':'Security & privacy','Remote Login Software':'Developer tools','QuickLook Plugins':'Utilities','Third Party App Markets':'Utilities','Mac App Download Sites':'Resources'}
for filename,kind in [('README.md','App'),('command-line-apps.md','CLI'),('editor-plugin.md','Plugin')]:
 major='';section='';group='Utilities'
 for line in (ROOT/filename).read_text().splitlines():
  if line.startswith('## '):
   major=line[3:].strip();section=major;group=groups.get(major,'Utilities')
  elif line.startswith('### '):section=line[4:].strip()
  if not re.match(r'^\| \[.*?\]\(https?://',line):continue
  cols=re.split(r'(?<!\\)\|',line)[1:-1]
  if len(cols)!=4:continue
  m=re.match(r'\s*\[(.*?)\]\((https?://[^)]+)\)',cols[0]);name,url=m.groups();name=plain(name);url=clean_url(url)
  if name=='Rectangle-app':name='Rectangle';url='https://rectangleapp.com/'
  if name=='Ghostty':url='https://ghostty.org/'
  group=groups.get(major,'Utilities')
  if section in ['Password Management']:group='Security & privacy'
  if section in ['File Organization Tools','Finder Tools','Backup and Sync']:group='Files & storage'
  if section in ['System Related Tools','Cleanup and Uninstall','General Tools','Quality of Life Improvements']:group='Utilities'
  if section in ['Text Editors','IDEs']:group='Developer tools'
  if kind=='CLI':group='Developer tools'
  if kind=='Plugin':group='Developer tools'
  source=re.search(r'\[Source\]\(([^)]+)\)',cols[3]);store=re.search(r'\[App Store\]\(([^)]+)\)',cols[3])
  norm=re.sub(r'[^a-z0-9]','',name.casefold())
  exists=by_name.get(norm) or by_url.get(canonical(url))
  if exists:
   if section not in exists['categories']:exists['categories'].append(section)
   if source and not exists['source']:exists['source']=source[1]
   continue
  item={'id':hashlib.sha1((name+url).encode()).hexdigest()[:12],'name':name,'url':url,'description':plain(cols[1]),'availability':plain(cols[2]),'source':source[1] if source else None,'store':store[1] if store else None,'native':'Native' in cols[3],'category':group,'categories':[section],'kind':kind}
  apps.append(item);by_name[norm]=item;by_url[canonical(url)]=item
(OUT/'catalog.json').write_text(json.dumps({'apps':apps,'updated':'October 18, 2026','listings':2825},ensure_ascii=False,separators=(',',':')))
print(f'Built {len(apps)} distinct app/tool/plugin records from 2,825 listings.')
