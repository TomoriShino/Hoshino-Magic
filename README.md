# HoshinoBot

A qqbot for Princess Connect Re:Dive (and other usage :)

**2020年8月2日0点，qq机器人框架相继停止维护。**
**感谢 酷Q项目 和 CQHTTP插件 的开发者们！感谢他们让Hoshino得以诞生！**
**Hoshino不再对酷Q进行支持**


## 简介

**HoshinoBot:** 基于 [nonebot](http://nonebot.cqp.moe) 框架，开源、无公害、非转基因的QQ机器人。



## 功能介绍

HoshinoBot 的功能开发以服务 [公主连结☆Re:Dive](http://priconne-redive.jp) 玩家为核心，主要功能有：

- **转蛋模拟**：单抽、十连、抽一井
- **竞技场解法查询**：支持按服务器过滤，支持反馈点赞点踩
- **竞技场结算提醒**
- **公会战管理**：详细说明见[此文档](hoshino/modules/pcrclanbattle/clanbattle/README.md)
- **Rank推荐表搬运**
- **常用网址速查**
- **官方推特转发**
- **官方四格推送**
- **角色别称转换**
- **切噜语编解码**：切噜～♪
- **竞技场余矿查询**

> 由于bot的功能会快速迭代开发，使用方式这里不进行具体的说明，请向bot发送"help"或移步[此文件](hoshino/modules/botmanage/help.py)查看详细。会战管理功能的详细说明，请[点击这里](hoshino/modules/pcrclanbattle/clanbattle/README.md)

HoshinoBot 还具有以下通用功能：

- **[蜜柑计划](http://mikanani.me)番剧更新订阅**
- **入群欢迎**&**退群提醒**
- **复读**
- **掷骰子**
- **精致睡眠套餐**
- **机器翻译**
- **反馈发送**：反馈内容将由bot私聊发送给维护组

此外，HoshinoBot 为 [艦隊これくしょん](http://www.dmm.com/netgame/feature/kancolle.html) 玩家开发了以下功能：

- **官推转发**：「艦これ」開発/運営 & C2機関
- **时报**
- **演习时间提醒**
- **月度远征提醒**
- **舰娘信息查询**：`*晓改二`
- **装备信息查询**：`*震电改`
- **战果人事表查询**：`人事表191201`

> 艦これ相关功能由于个人精力实在有限，无法进行更多功能（如海图攻略）的开发/维护。
>
> 如果您有新的想法，欢迎联系我！即便您不会编程，您也可以在内容更新上帮到我们！

-------------

### 功能模块控制

HoshinoBot 的功能繁多，各群可根据自己的需要进行开关控制，群管理发送 `lssv` 即可查看功能模块的启用状态，使用以下命令进行控制：

```
启用 service-name
禁用 service-name
```







## ~~部署指南~~

**由于酷Q已停止维护，本指南已失效。您可以使用[CQHTTP Mirai](https://github.com/yyuueexxiinngg/cqhttp-mirai)或[go-cqhttp](https://github.com/Mrs4s/go-cqhttp)作为替代。由于当前mirai仍不稳定（甚至删库跑路），请自行参考相应的文档进行部署，本项目组不解答部署问题。**

本bot功能繁多，部分功能需要静态图片资源和带有认证的api key，恕不能公开。本指南将首先带领您搭建具有**模拟抽卡(纯文字版)**、**会战管理**功能的HoshinoBot。其他功能需额外配置，请参考本章**更进一步**的对应小节。

### 部署步骤

#### Windows 部署

安装下面的软件/工具
- Python 3.8：https://www.python.org/downloads/windows/
- Git：https://git-scm.com/download/win
- Notepad++：https://notepad-plus-plus.org/downloads/

点击资源管理器左上角的 `文件 -> 打开Windows Powershell`

```powershell
git clone https://github.com/TomoriShino/Hoshino-Magic.git
cd TomoriBot
py -3.8 -m pip install -r requirements.txt
```

```powershell
py -3.8 run.py
```

私聊机器人发送`在？`，若机器人有回复，恭喜您！您已经成功搭建起HoshinoBot了。之后您可以尝试在群内发送`!帮助`以查看会战管理的相关说明，发送`help`查看其他一般功能的相关说明，发送`pcr速查`查看常用网址等。

注意，此时您的机器人功能还不完全，部分功能可能无法正常工作。若希望您的机器人可以发送图片，或使用其他进阶功能，请参考本章**更进一步**的对应小节。



### 更进一步

现在，机器人已经可以使用`会战管理`、`模拟抽卡(纯文字版)`等基本功能了。但还无法使用`竞技场查询`、`番剧订阅`、`推特转发`等功能。这是因为，这些功能需要对应的静态图片资源以及相应的api key。相应资源获取有难有易，您可以根据自己的需要去获取。

下面将会分别介绍资源与api key的获取方法：



#### 静态图片资源

> 发送图片的条件：  
>
> 1. 静态图片资源

您可能希望看到更为精致的图片版结果，若希望机器人能够发送图片，首先需要您购买酷Q Pro版，其次需要准备静态图片资源，其中包括：

- 公主连接角色头像（来自 [干炸里脊资源站](https://redive.estertion.win/) 的拆包）
- 公主连接官方四格漫画
- 公主连接每月rank推荐表
- 表情包杂图
- setu库
- [是谁呼叫舰队](http://fleet.diablohu.com/)舰娘&装备页面截图
- 艦これ人事表



#### pcrdfans授权key

竞技场查询功能的数据来自 [公主连结Re: Dive Fan Club - 硬核的竞技场数据分析站](https://pcrdfans.com/) ，查询需要授权key。您可以向pcrdfans的作者索要。（注：由于最近机器人搭建者较多，pcrdfans的作者最近常被打扰，我们**不建议**您因本项目而去联系他，推荐您前往网站[pcrdfans.com](https://pcrdfans.com)进行查询）

若您已有授权key，在文件`hoshino/config/priconne.py`中填写您的key：

```python
class arena:
    AUTH_KEY = "your_key"
```



#### 蜜柑番剧 RSS Token

> 请先在`hoshino/config/__bot__.py`的`MODULES_ON`中取消`mikan`的注释  
> 本功能默认关闭，在群内发送 "启用 bangumi" 即可开启

番剧订阅数据来自[蜜柑计划 - Mikan Project](https://mikanani.me/)，您可以注册一个账号，添加订阅的番剧，之后点击Mikan首页的RSS订阅，复制类似于下面的url地址：

```
https://mikanani.me/RSS/MyBangumi?token=abcdfegABCFEFG%2b123%3d%3d
```

保留其中的`token`参数，在文件`hoshino/config/mikan.py`中填写您的token：

```python
MIKAN_TOKEN = "abcdfegABCFEFG+123=="
```

注意：`token`中可能含有url转义，您需要将`%2b`替换为`+`，将`%2f`替换为`/`，将`%3d`替换为`=`。



#### 时报文本

> 请先在`hoshino/config/__bot__.py`的`MODULES_ON`中取消`hourcall`的注释  
> 本功能默认关闭，在群内发送 "启用 hourcall" 即可开启

报时功能使用/魔改了艦これ中各个艦娘的报时语音，您可以在[舰娘百科](https://zh.kcwiki.org/wiki/舰娘百科)或[艦これ 攻略 Wiki](https://wikiwiki.jp/kancolle/)找到相应的文本/翻译，当然您也可以自行编写台词。在此，我们向原台词作者[田中](https://bbs.nga.cn/read.php?tid=9143913)[谦介](http://nga.178.com/read.php?tid=14045507)先生和他杰出的游戏作品表达诚挚的感谢！

若您已获取时报文本，在文件`hoshino/config/hourcall.py`中填写您的文本。

您可以编入多组报时文本，机器人会按`HOUR_CALLS_ON`中定义的顺序循环日替。



#### 推特转发

推特转发功能需要推特开发者账号，具体申请方法请自行[Google](http://google.com)。注：现在推特官方大概率拒绝来自中国大陆的新申请，自备海外手机号及大学邮箱可能会帮到您。

若您已有推特开发者账号，在文件`hoshino/config/twitter.py`中填写您的key：

```python
consumer_key = "your_consumer_key",
consumer_secret = "your_consumer_secret",
access_token_key = "your_access_token_key",
access_token_secret = "your_access_token_secret"
```



#### Tips：

部分插件需要修改路劲和API才能正常食用

**shebot_old**

**portune**

**tarot**

**picapi**

**ClanBattleReport**



##### **Discord**

Tomori#2906

