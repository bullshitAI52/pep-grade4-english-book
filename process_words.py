import re

raw_text = """
Unit 1
*sorry /'sDri/ 对不起 p. 4
*late /leit/ 迟到; 迟发生 p. 4
*class /kla:s/ 课; 课程; 班; 班级 p. 4
hurry /'h^ri/ up /Mp/ 快点; 赶快 p. 4
ready /'redi/ 准备好 p. 4
rule /ru:l/ 规则; 规章 p. 5
*classroom /'kla:sru:m/ 教室 p. 5
turn /t3:n/ off /Df/ 关掉 p. 5
*light /lait/ 灯; 光 p. 5
*blackboard /'blækbD:d/ 黑板 p. 7
*desk /desk/ 书桌; 办公桌 p. 7
*chair /tJe9(r)/ 椅子 p. 7
*tidy /'taidi/ 整洁的; 整齐的; 使整洁; 整理 p. 7
*music /'mju:zik/ 音乐 p. 8
*wall /wD:l/ 墙; 壁 p. 8
*door /dD:(r)/ 门 p. 8
*window /'wind9u/ 窗 p. 8
*fan /fæn/ 风扇 p. 8
*when /wen/ 当……时; 什么时候 p. 9
understand /And9'stænd/ 懂; 理解 p. 9
newspaper /'nju:zpeip9(r)/ 报纸 p. 9
hand out /aut/ 分发 p. 9
workbook /w3:k/ 练习册; 作业本 p. 9

Unit 2
*watch /wDtJ/ 看 p. 16
TV /ti: 'vi:/ 电视 p. 16
homework /'h9umw3:k/ 家庭作业 p. 16
first /f3:st/ 首先; 首次; 第一 p. 16
wet /wet/ 湿的; 未干的 p. 16
*run /rAn/ 跑; 奔跑 p. 16
*house /haus/ 房子 p. 16
*safe /seif/ 安全的 p. 16
*word /w3:d/ 言语; 单词; 字 p. 17
*wash /wDJ/ 洗 p. 17
loud /laud/ 说话太大声的; 吵闹的 p. 19
*sleep /sli:p/ 睡觉 p. 19
bedroom /'bedru:m/ 卧室 p. 19
*kitchen /'kitJin/ 厨房 p. 19
living /'livin/ room 客厅; 起居室 p. 20
*study /'stAdi/ 书房 p. 20
bathroom /'ba:0ru:m/ 浴室; 洗手间 p. 20
*work /w3:k/ (花费时间和精力)做(某事); 工作 p. 21
*think /0ink/ 想; 思考 p. 21
*hard /ha:d/ 努力地; 费力地 p. 21
follow /'fpl9u/ 遵循, 听从 (忠告、指示等)
*feel /fi:l/ 觉得; 感到

Unit 3
*over /'9uv9(r)/ 结束(的) p. 28
*kid /kid/ 小孩 p. 28
*dinner /'din9(r)/ (中午或晚上吃的)正餐 p. 28
*art /a:t/ 美术; 艺术 p. 29
*lunch /lAntJ/ 午餐 p. 29
*maths /mæus/ 数学 p. 29
get up 起床 p. 31
go to school 上学 p. 31
go home 回家 p. 32
go to bed 上床睡觉 p. 32
*want /wpnt/ 想要 p. 33
*clock /klpK/ 时钟 p. 33
just /d3Ast/ 只是; 仅仅; 正要 p. 33
*minute /'minit/ 分钟 p. 33

Unit 4
*trousers /'trauz9z/ 裤子 p. 40
*pair /pe9(r)/ (由连在一起的相似两部分构成的)一条, 一副 p. 40
*clothes /kl9uDz/ 衣服; 服装 p. 40
*shorts /Jo:ts/ 短裤 p. 40
jacket /'d3ækit/ 夹克衫 p. 41
*skirt /sk3:t/ 裙子 p. 41
*dear /di9(r)/ 天哪 p. 43
expensive /ik'spensiv/ 昂贵的; 价格高的 p. 43
*take /teik/ 买下 p. 43
cheap /tJi:p/ 便宜的 p. 44
*shoe /Ju:/ 鞋 p. 44
*beautiful /'bju:tifl/ 美丽的 p. 44
hat /hæt/ 帽子 p. 44
*sunglasses /'sAngla:siz/ 太阳镜: 墨镜 p. 44
free /fri:/ 免费的 p. 45
large /la:d3/ (服装、食物、日用品等)大型号的 p. 45
size /saiz/ 尺码: 号 p. 45
list /list/ 清单; 目录 p. 45
try /trai/ on 试穿 p. 45
*any /'eni/ 任何的: 任一的 p. 45

Unit 5
*cow /kau/ 奶牛 p. 52
*horse /hD:s/ 马 p. 52
*sheep /Ji:p/ 绵羊 p. 52
*pig /pig/ 猪 p. 52
*chicken /'tJikm/ 鸡; 鸡肉 p. 52
*tomato /t9'ma:t9u/ 西红柿 p. 55
*bee /bi:/ 蜜蜂 p. 55
*mouse /maus/ (复数mice /mais/) 老鼠 p. 56
carrot /'kær9t/ 胡萝卜 p. 56
*potato /p9'teit9u/ 土豆 p. 56
green bean /bi:n/ 四季豆 p. 57
*can /kæn/ (盛食品或饮料的)金属罐 p. 57
a box of 一盒, 一箱(东西) p. 57

Unit 6
feed /fi:d/ 给(人或动物)食物; 饲养
pass /pa:s/ 给; 递
pick /pik/ 采; 摘
*milk /milk/ 挤奶
knife /naif/ 刀
fork /fp:k/ 餐叉 p. 67
chopstick /'tJppstik/ (常用复数)筷子 p. 67
waste /weist/ 浪费; 废品 p. 67
*food /fu:d/ 菜肴; 食物 p. 67
delicious /di'liJ9s/ 美味的; 可口的 p. 29
clear the table 收拾餐桌 p. 67
bowl /b9ul/ 碗 p. 68
spoon /spu:n/ 勺; 匙; 调羹 p. 68
set /set/ the table 摆放餐具 p. 68
*supermarket /'su:p9ma:kit/ 超市 p. 69
by oneself /wAn'self/ (某人)独立地; 单独 p. 69
*week /wi:k/ 周; 星期 p. 69
salad /'sæl9d/ 蔬菜沙拉 p. 69
ad /æd/ 广告 p. 70

Numbers
one /wAn/ 一
two /tu:/ 二
three /0ri:/ 三
four /fD:(r)/ 四
five /faiv/ 五
six /siks/ 六
seven /'sevn/ 七
eight /eit/ 八
nine /nain/ 九
ten /ten/ 十
eleven /i'levn/ 十一
twelve /twelv/ 十二
thirteen /03:'ti:n/ 十三
fourteen /fD:'ti:n/ 十四
fifteen /fif'ti:n/ 十五
sixteen /siks'ti:n/ 十六
seventeen /sevn'ti:n/ 十七
eighteen /ei'ti:n/ 十八
nineteen /nain'ti:n/ 十九
twenty /'twenti/ 二十
thirty /'03:ti/ 三十
forty /'fD:ti/ 四十
fifty /'fifti/ 五十
sixty /'siksti/ 六十
seventy /'sevnti/ 七十
eighty /'eiti/ 八十
ninety /'nainti/ 九十
hundred /'hAndr9d/ 百
"""

def process_line(line, unit):
    # Remove asterisk
    line = line.replace('*', '').strip()
    
    # Remove page numbers (p. X)
    line = re.sub(r'p\. ?\d+', '', line)
    
    # Remove phonetics /.../ 
    # Handle multiple phonetics (hurry /.../ up /.../)
    # Regex: match / followed by anything until /
    line = re.sub(r'\/[^\/]+\/', '', line)
    
    # Clean up double spaces
    line = re.sub(r'\s+', ' ', line).strip()
    
    # Separation: Find first Chinese char or specific symbols
    # We iterate and find split point
    split_index = -1
    for i, char in enumerate(line):
        # Check if char is Chinese or common separator not in English words
        # Chinese Unicode range roughly 4E00-9FFF
        # Also symbols like （ (full width) or ( followed by Chinese
        if '\u4e00' <= char <= '\u9fff' or char in '，。；（）：':
            split_index = i
            break
        # Heuristic: if we see ' (' then check if next is chinese?
        # "by oneself ... (某人)"
        if char == '(':
             # Look ahead
             if i+1 < len(line) and ('\u4e00' <= line[i+1] <= '\u9fff'):
                 split_index = i
                 break

    if split_index != -1:
        english = line[:split_index].strip()
        chinese = line[split_index:].strip()
    else:
        # Fallback for lines without Chinese? Or maybe "one /.../ 一" matched the range
        # "one 一" -> space then Chinese
         match = re.search(r'\s([\u4e00-\u9fff].*)', line)
         if match:
             english = line[:match.start()].strip()
             chinese = match.group(1).strip()
         else:
             # Just assume last word? No, probably English only or error
             english = line
             chinese = ""
             
    return english, chinese

lines = raw_text.split('\n')
current_unit = ""
table_data = []

for line in lines:
    line = line.strip()
    if not line:
        continue
        
    if line.startswith("Unit") or line.startswith("Numbers"):
        current_unit = line
        continue
        
    english, chinese = process_line(line, current_unit)
    if english:
        table_data.append(f"| {english} | {chinese} |")

# Write to file
with open('vocabulary_table.md', 'w') as f:
    f.write("| English | Chinese |\n")
    f.write("|---|---|\n")
    f.write("\n".join(table_data))

print("Done. Created vocabulary_table.md")
