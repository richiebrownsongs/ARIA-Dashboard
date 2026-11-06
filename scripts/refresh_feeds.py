#!/usr/bin/env python3
"""Refresh the two public, attributed headline tiles. Standard library only."""
import datetime as dt
import json
import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

HEADERS={"User-Agent":"ARIA-Command-Center/1.0 (personal RSS display)"}
FOX="https://moxie.foxnews.com/google-publisher/latest.xml"
# Google News RSS search links back to original articles; used for team-specific aggregation.
GOOGLE_COWBOYS="https://news.google.com/rss/search?"+urllib.parse.urlencode({"q":"Dallas Cowboys site:bloggingtheboys.com OR site:espn.com","hl":"en-US","gl":"US","ceid":"US:en"})

def fetch_rss(url):
    req=urllib.request.Request(url,headers=HEADERS)
    with urllib.request.urlopen(req,timeout=18) as res: raw=res.read(1200000)
    root=ET.fromstring(raw)
    rows=[]
    for item in root.findall('.//item'):
        title=(item.findtext('title') or '').strip()
        link=(item.findtext('link') or '').strip()
        if not title or not link.startswith('https://'):continue
        rows.append({'title':re.sub(r'\s+',' ',title)[:190], 'url':link})
        if len(rows)>=12:break
    return rows

def main():
    target=Path(__file__).resolve().parent.parent/'feed-data.json'
    try: data=json.loads(target.read_text())
    except (OSError,ValueError):data={}
    changed=False
    for name,url in [('fox',FOX),('cowboys',GOOGLE_COWBOYS)]:
        try:
            items=fetch_rss(url)
            if not items:raise ValueError('empty feed')
            for item in items:item['source']='FOX NEWS' if name=='fox' else ('BLOGGING THE BOYS' if 'bloggingtheboys' in item['title'].lower() else 'COWBOYS NEWS')
            data[name]=items
            changed=True
            print(f'{name}: {len(items)} headlines')
        except Exception as exc:print(f'{name}: keeping prior headlines ({exc})')
    if changed:
        data['updated_utc']=dt.datetime.now(dt.timezone.utc).isoformat()
        target.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    if not data.get('fox') and not data.get('cowboys'):raise SystemExit('No feed available')

if __name__=='__main__':main()
