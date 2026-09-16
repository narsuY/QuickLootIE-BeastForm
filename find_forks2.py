import urllib.request
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = urllib.request.Request('https://api.github.com/search/repositories?q=CommonLibSSE+user:doodlum+user:alandtse+user:powerof3&sort=updated', headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, context=ctx) as response:
        data = json.loads(response.read().decode())
        for item in data.get('items', [])[:10]:
            print(f"- {item['full_name']} (Pushed: {item['pushed_at']})")
except Exception as e:
    print(f"Error: {e}")
