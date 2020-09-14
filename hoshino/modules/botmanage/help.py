from hoshino import Service, priv
from hoshino.typing import CQEvent

sv = Service('_help_', manage_priv=priv.SUPERUSER, visible=False)

TOP_MANUAL = '''
=====================
- 藻藻使用说明 -
=====================
发送方括号[]内的关键词即可触发
※功能采取模块化管理，群管理可控制开关

[!帮助] 会战管理v2
[怎么拆日和] 竞技场查询
[pcr速查] 常用网址
[官漫132] 四格漫画（日）
[切噜一下] 切噜语转换
[lssv] 查看功能模块的开关状态（群管理限定）
[来杯咖啡] 联系主人

发送以下关键词查看更多：
[#帮助pcr会战]
[#帮助pcr查询]
[#帮助pcr娱乐]
[#帮助pcr订阅]
[#帮助kancolle]
=====================
[启用 hourcall]时报功能
[启用 bangumi]蜜柑番剧
=====================
FFXIV功能发送以下命令查看
[/help]
[/占卜]
=====================
※除这里中写明外 另有其他隐藏功能:)
※部分功能检修
※有时候命令未响应不是藻藻的问题，信息可能会被腾讯屏蔽
※※调教时请注意使用频率，您的滥用可能会导致bot账号被封禁
'''.strip()

def gen_bundle_manual(bundle_name, service_list, gid):
    manual = [bundle_name]
    service_list = sorted(service_list, key=lambda s: s.name)
    for sv in service_list:
        if sv.visible:
            spit_line = '=' * max(0, 18 - len(sv.name))
            manual.append(f"|{'○' if sv.check_enabled(gid) else '×'}| {sv.name} {spit_line}")
            if sv.help:
                manual.append(sv.help)
    return '\n'.join(manual)


@sv.on_prefix(('#help', '#帮助', '#幫助'))
async def send_help(bot, ev: CQEvent):
    bundle_name = ev.message.extract_plain_text().strip()
    bundles = Service.get_bundles()
    if not bundle_name:
        await bot.send(ev, TOP_MANUAL)
    elif bundle_name in bundles:
        msg = gen_bundle_manual(bundle_name, bundles[bundle_name], ev.group_id)
        await bot.send(ev, msg)
    # else: ignore
