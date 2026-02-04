#!/usr/bin/env python3
import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
url = f'https://api.github.com/users/{GHUSER}/events'
response = requests.get(url)
r = json.loads(response.text)
print(f"Recent Activity for {GHUSER}")
for x in r[:5]:
    event_type = x['type']
    repo_name = x['repo']['name']
    print(f"{event_type} :: {repo_name}")