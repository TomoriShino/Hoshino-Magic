from hoshino import Service,R
import requests
import random
sv = Service('wangyiyun', bundle='pcr娱乐', help_='''
来点网抑云 | 随机语录
'''.strip())

@sv.on_keyword(('来点网抑云'))
async def wangyiyun(bot, ctx):
    imgList = ['wangyiyun1.jpg']
    url = 'http://api.heerdev.top/nemusic/random'
    resp = requests.get(url=url, timeout=20)
    status_code = resp.status_code
    if status_code != 200:
        print(f'conn error status code{status_code}')
        await bot.send(ctx, f'conn error status code{status_code}')
    else:
        resp_json = resp.json()
        author = resp_json['from']
        text = resp_json['text']
        await bot.send(ctx, f'''{R.img(random.choice(imgList)).cqcode}\n用户:{author}\n语录:{text}''')