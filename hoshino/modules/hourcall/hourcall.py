import pytz
from datetime import datetime
import hoshino
from hoshino import Service

sv = Service('hourcall', enable_on_default=True, help_='时报')
tz = pytz.timezone('Asia/Shanghai')

def get_hour_call():
    """挑出一组时报，每日更换，一日之内保持相同"""
    cfg = hoshino.config.hourcall
    now = datetime.now(tz)
    hc_groups = cfg.HOUR_CALLS_ON
    g = hc_groups[ now.day % len(hc_groups) ]
    return cfg.HOUR_CALLS[g]


@sv.scheduled_job('cron', hour='*')
async def hour_call():
    now = datetime.now(tz)
    if 2 <= now.hour <= 4:
        return  # 宵禁 免打扰
    msg1 = get_hour_call()[(2*now.hour)]
    msg2 = get_hour_call()[(2*now.hour)+1]
    await sv.broadcast(msg1, 'hourcall', 0)
    await sv.broadcast(msg2, 'hourcall', 0)
