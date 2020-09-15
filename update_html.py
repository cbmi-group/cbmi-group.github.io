# encoding: utf-8
import os
import datetime
import json
import codecs
import markdown
import sys


def save_utf8(filename, text):
    with codecs.open(filename, 'w', encoding='utf-8')as f:
        f.write(text)


def load_utf8(filename):
    with codecs.open(filename, 'r', encoding='utf-8') as f:
        return f.read()


def savefinalhtml(filepath, finalhtml):
    output_file = codecs.open(filepath, "w", encoding="utf-8")
    output_file.write(finalhtml)
    output_file.close()
    print("success generate ", filepath)


# load templates
index = load_utf8("index_template.html")
banner = load_utf8("banner_template.html")
u8u4 = load_utf8("8u-4u.html")
personal = load_utf8("people/personal_template.html")

# siteMap = load_utf8("templates/sitemap.tm.xml")

# generate index
new_index = index.replace("{{TITLE}}", "CBMI Group")
index_body = ""
index_body = index_body + banner + u8u4

news = [
  ["images/er-segmentation.png", "Deep Learning-Based Segmentation of Biological Networks in Fluorescence Microscopy", "We developed a deep learning-based pipeline to study the effects of image pre-processing, loss functions and model architectures for accurate segmentation of biological networks in FLMI.", "./projects/er-segmentation.html"],
  ["images/feng3-p5-feng-large.gif", "Quality Assessment of Synthetic Fluorescence Microscopy Images for Image Segmentation", "We have developed a method to assess quality of synthetic fluorescence microscopy images and to evaluate their training performance in image segmentation.", "https://ieeexplore.ieee.org/abstract/document/8802971"],
  ["https://ars.els-cdn.com/content/image/1-s2.0-S221112471830860X-mmc6.mp4", "Whole-Cell Scale Dynamic Organization of Lysosomes Revealed by Spatial Statistical Analysis", "Our findings reveal whole-cell scale spatial organization of lysosomes and provide insights into how organelle interactions are mediated and regulated across the entire intracellular space.", "https://www.sciencedirect.com/science/article/pii/S221112471830860X", "https://ars.els-cdn.com/content/image/1-s2.0-S221112471830860X-mmc6.jpg"]
]
a_news_template = load_utf8("news_template.html")
a_new = a_news_template.replace("{{IMG_URL}}", news[0][0])
a_new = a_new.replace("{{RESEARCH_TITLE}}", news[0][1])
a_new = a_new.replace("{{RESEARCH_BRIEF}}", news[0][2])
a_new = a_new.replace("{{RESEARCH_LINK}}", news[0][3])

b_news_template = load_utf8("news_template.html")
b_new = b_news_template.replace("{{IMG_URL}}", news[1][0])
b_new = b_new.replace("{{RESEARCH_TITLE}}", news[1][1])
b_new = b_new.replace("{{RESEARCH_BRIEF}}", news[1][2])
b_new = b_new.replace("{{RESEARCH_LINK}}", news[1][3])

c_video_template = load_utf8("video_news.html")
c_new = c_video_template.replace("{{VIDEO_URL}}", news[2][0])
c_new = c_new.replace("{{RESEARCH_TITLE}}", news[2][1])
c_new = c_new.replace("{{RESEARCH_BRIEF}}", news[2][2])
c_new = c_new.replace("{{RESEARCH_LINK}}", news[2][3])
c_new = c_new.replace("{{VIDEO_IMG}}", news[2][4])


a_row = load_utf8("row_template.html")

index_body = index_body + a_row.replace("{{INNER}}", a_new + b_new + c_new)
# index_body = index_body + b_row.replace("{{INNER}}", c_new)
new_index = new_index.replace("{{BODY}}", index_body)
new_index = new_index.replace("{{COUNT}}", "")
savefinalhtml("index.html", new_index)


# generate research
pub = index.replace("{{TITLE}}", "Research")
pub_tem = load_utf8("style2_template.html")
publications = load_utf8("md/research.md")
publications = markdown.markdown(publications)
pub_content = pub_tem.replace("{{POST_TITLE}}", "Research Projects")
research_row = load_utf8("a_project_row.html")
pub_content = pub_content.replace("{{POST_CONTENT}}", publications + research_row.replace("{{INNER}}", a_new.replace('"4u"', '"6u"') + b_new.replace('"4u"', '"6u"') + c_new.replace('"4u"', '"6u"')))
pub = pub.replace("{{BODY}}", pub_content)
pub = pub.replace("{{COUNT}}", "research.html")
savefinalhtml("research.html", pub)

# generate people
pub = index.replace("{{TITLE}}", "Team")
my_people = load_utf8("md/people_template.html")
pub = pub.replace("{{BODY}}", my_people)
pub = pub.replace("{{COUNT}}", "people.html")
savefinalhtml("people.html", pub)

def generate_a_person(mdpath, pagetitle, htmlpath):
    pub = personal.replace("{{TITLE}}", pagetitle)
    pub_tem = load_utf8("style2_template.html")
    publications = load_utf8(mdpath)
    publications = markdown.markdown(publications)
    pub_content = pub_tem.replace("{{POST_TITLE}}", pagetitle)
    pub_content = pub_content.replace("{{POST_CONTENT}}", publications)
    pub = pub.replace("{{BODY}}", pub_content)
    count = htmlpath.replace("/", "%2F")
    pub = pub.replace("{{COUNT}}", count)
    savefinalhtml(htmlpath, pub)

person_infos = [
  # markdown_path, title, html_path
  ["md/yangge.md", "Ge Yang",       "people/geyang.html"],
  ["md/lwj.md",    "Wenjing",       "people/wenjingli.html"],
  ["md/gyh.md",    "Yuanhao Guo",   "people/yuanhaoguo.html"],
  ["md/jay.md",    "Jie Jin",       "people/jay.html"],
  ["md/yp.md",     "Ping Yang",     "people/pingyang.html"],
  ["md/mxy.md",    "Xiangyuan Mei", "people/xiangyuanmei.html"],
  ["md/lgl.md",    "Guole Liu",     "people/guoleliu.html"],
  ["md/zsh.md",    "Shuhao Zhang",  "people/shuhaozhang.html"],
  ["md/lyr.md",    "Yaoru Luo",     "people/yaoruluo.html"],
  ["md/zlq.md",    "Liqun Zhong",   "people/liqunzhong.html"],
  ["md/yb.md",     "Bo You",        "people/boyou.html"],
  ["md/xyp.md",    "Yunpeng Xiao",  "people/yunpengxiao.html"],
  ["md/wsy.md",    "Shiyu Wu",      "people/shiyuwu.html"],
  ["md/zyt.md",    "Yating Zhou",   "people/yatingzhou.html"],
  ["md/zyf.md",    "Yanfeng Zhou",  "people/yanfengzhou.html"],
  ["md/qmx.md",    "Mengxuan Qiu",  "people/mengxuanqiu.html"],
  ["md/zyd.md",    "Yudong Zhang",  "people/yudongzhang.html"],
  ["md/hj.md",     "Jia He",        "people/jiahe.html"],
]

# generate personal homepage.
for a_person in person_infos:
    generate_a_person(a_person[0], a_person[1], a_person[2])


# generate publications
pub = index.replace("{{TITLE}}", "Publications")
pub_tem = load_utf8("style2_template.html")
publications = load_utf8("md/publications_yangge.md")
publications = markdown.markdown(publications)
pub_content = pub_tem.replace("{{POST_TITLE}}", "Publications")
pub_content = pub_content.replace("{{POST_CONTENT}}", publications)
pub = pub.replace("{{BODY}}", pub_content)
pub = pub.replace("{{COUNT}}", "publications.html")
savefinalhtml("publications.html", pub)

# generate positions
pub = index.replace("{{TITLE}}", "Open Positions")
pub_tem = load_utf8("style2_template.html")
publications = load_utf8("md/positions.md")
publications = markdown.markdown(publications)
pub_content = pub_tem.replace("{{POST_TITLE}}", "Open Positions")
pub_content = pub_content.replace("{{POST_CONTENT}}", publications)
pub = pub.replace("{{BODY}}", pub_content)
pub = pub.replace("{{COUNT}}", "openpositions.html")
savefinalhtml("openpositions.html", pub)

# generate contacts
contacts = index.replace("{{TITLE}}", "Contact Us")
contact_tem = load_utf8("contact_template.html")
contact_html = contacts.replace("{{BODY}}", contact_tem)
contact_html = contact_html.replace("{{COUNT}}", "contact.html")
savefinalhtml("contact.html", contact_html)

project_tem = load_utf8("projects/project_template.html")
def generate_a_project(mdpath, pagetitle, htmlpath):
    pub = project_tem.replace("{{TITLE}}", pagetitle)
    article_tem = load_utf8("article_template.html")
    project_md = load_utf8(mdpath)
    project_content = markdown.markdown(project_md, extensions=['codehilite', 'fenced_code', 'extra'])
    article_content = article_tem.replace("{{POST_CONTENT}}", project_content)
    pub = pub.replace("{{BODY}}", article_content)
    count = htmlpath.replace("/", "%2F")
    pub = pub.replace("{{COUNT}}", count)
    savefinalhtml(htmlpath, pub)
# generate projects
projects_info = [
  # markdown_path, title, html_path
  ["md/er-segmentation.md", "ER Segmentation", "projects/er-segmentation.html"]
]

for a_project in projects_info:
    generate_a_project(a_project[0], a_project[1], a_project[2])
