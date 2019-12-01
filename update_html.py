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
photo = load_utf8("labphoto.html")
personal = load_utf8("people/personal_template.html")

# siteMap = load_utf8("templates/sitemap.tm.xml")

# generate index
new_index = index.replace("{{TITLE}}", "CBMI Group")
index_body = ""
index_body = index_body + banner + u8u4
new_index = new_index.replace("{{BODY}}", index_body)
savefinalhtml("index.html", new_index)


# generate research
pub = index.replace("{{TITLE}}", "Research")
pub_tem = load_utf8("style2_template.html")
publications = load_utf8("md/research.md")
publications = markdown.markdown(publications)
pub_content = pub_tem.replace("{{POST_TITLE}}", "Research Projects")
pub_content = pub_content.replace("{{POST_CONTENT}}", publications)
pub = pub.replace("{{BODY}}", pub_content)
savefinalhtml("research.html", pub)


# generate people
pub = index.replace("{{TITLE}}", "Team")
my_people = load_utf8("md/people_template.html")
pub = pub.replace("{{BODY}}", my_people)
savefinalhtml("people.html", pub)


def generate_a_person(mdpath, pagetitle, htmlpath):
    pub = personal.replace("{{TITLE}}", "Personal Homepage")
    pub_tem = load_utf8("style2_template.html")
    publications = load_utf8(mdpath)
    publications = markdown.markdown(publications)
    pub_content = pub_tem.replace("{{POST_TITLE}}", pagetitle)
    pub_content = pub_content.replace("{{POST_CONTENT}}", publications)
    pub = pub.replace("{{BODY}}", pub_content)
    savefinalhtml(htmlpath, pub)

person_infos = [
  # markdown_path, title, html_path
  ["md/yangge.md", "Ge Yang",       "people/geyang.html"],
  ["md/lwj.md",    "Wenjing",       "people/wenjingli.html"],
  ["md/gyh.md",    "Yuanhao Guo",   "people/yuanhaoguo.html"],
  ["md/jay.md",    "Jie Jin",       "people/jay.html"],
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
savefinalhtml("publications.html", pub)

# generate positions
pub = index.replace("{{TITLE}}", "Open Positions")
pub_tem = load_utf8("style2_template.html")
publications = load_utf8("md/positions.md")
publications = markdown.markdown(publications)
pub_content = pub_tem.replace("{{POST_TITLE}}", "Open Positions")
pub_content = pub_content.replace("{{POST_CONTENT}}", publications)
pub = pub.replace("{{BODY}}", pub_content)
savefinalhtml("openpositions.html", pub)

# generate contacts
contacts = index.replace("{{TITLE}}", "Contact Us")
contact_tem = load_utf8("contact_template.html")
contact_html = contacts.replace("{{BODY}}", contact_tem)
savefinalhtml("contact.html", contact_html)
