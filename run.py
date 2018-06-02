import requests

n = 1

while True:
    if n == 404:
        n += 1
    url = 'https://xkcd.com/{}/info.0.json'.format(n)
    r = requests.get(url)
    if r.status_code == 404:
        break
    d = r.json()
    n = d['num']
    t = d['safe_title']
    u = d['img']
    print('{}: {}'.format(n, t))
    if u.endswith('.png'):
        ext = 'png'
    if u.endswith('.jpg'):
        ext = 'jpg'
    if u.endswith('.gif'):
        ext = 'gif'
    x = 'comics/{}-{}.{}'.format(n, t.replace(' ', '_').replace('/', '-'), ext)
    with open(x, "wb") as f:
        c = requests.get(u)
        f.write(c.content)
    n += 1
