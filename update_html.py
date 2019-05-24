# encoding: utf-8
import os
import datetime
import json
import codecs
import markdown


def save_utf8(filename, text):
    with codecs.open(filename, 'w', encoding='utf-8')as f:
        f.write(text)


def load_utf8(filename):
    with codecs.open(filename, 'r', encoding='utf-8') as f:
        return f.read()


def savefinalhtml(filepath, finalhtml):
    output_file = codecs.open(filepath, "w", encoding="utf-8")
    output_file.write(finalhtml.decode("utf-8"))
    output_file.close()
    print("success generate ", filepath)

# load templates
index = load_utf8("index_template.html").encode("utf-8")
banner = load_utf8("banner_template.html").encode("utf-8")
u8u4 = load_utf8("8u-4u.html").encode("utf-8")


# siteMap = load_utf8("templates/sitemap.tm.xml").encode("utf-8")

# generate index
new_index = index.replace("{{TITLE}}", "CBCenter")
index_body = ""
index_body = index_body + banner + u8u4
new_index = new_index.replace("{{BODY}}", index_body)
savefinalhtml("index.html", new_index)


# generate research
pub = index.replace("{{TITLE}}", "Research")
pub_tem = load_utf8("style2_template.html").encode("utf-8")
publications = load_utf8("research.md").encode("utf-8")
publications = markdown.markdown(publications)
pub_content = pub_tem.replace("{{POST_TITLE}}", "Research Projects")
pub_content = pub_content.replace("{{POST_CONTENT}}", publications)
pub = pub.replace("{{BODY}}", pub_content)
savefinalhtml("research.html", pub)

# generate people
pub = index.replace("{{TITLE}}", "Team")
pub_tem = load_utf8("style2_template.html").encode("utf-8")
publications = load_utf8("people.md").encode("utf-8")
publications = markdown.markdown(publications)
pub_content = pub_tem.replace("{{POST_TITLE}}", "Our Team")
pub_content = pub_content.replace("{{POST_CONTENT}}", publications)
pub = pub.replace("{{BODY}}", pub_content)
savefinalhtml("people.html", pub)


# generate publications
pub = index.replace("{{TITLE}}", "Publications")
pub_tem = load_utf8("style2_template.html").encode("utf-8")
publications = load_utf8("publications_yangge.md").encode("utf-8")
publications = markdown.markdown(publications)
pub_content = pub_tem.replace("{{POST_TITLE}}", "Publications")
pub_content = pub_content.replace("{{POST_CONTENT}}", publications)
pub = pub.replace("{{BODY}}", pub_content)
savefinalhtml("publications.html", pub)

# generate positions
pub = index.replace("{{TITLE}}", "Open Positions")
pub_tem = load_utf8("style2_template.html").encode("utf-8")
publications = load_utf8("positions.md").encode("utf-8")
publications = markdown.markdown(publications)
pub_content = pub_tem.replace("{{POST_TITLE}}", "Open Positions")
pub_content = pub_content.replace("{{POST_CONTENT}}", publications)
pub = pub.replace("{{BODY}}", pub_content)
savefinalhtml("openpositions.html", pub)

# generate contacts 
contacts = index.replace("{{TITLE}}", "Contact Us")
contact_tem = load_utf8("contact_template.html").encode("utf-8")
contact_html = contacts.replace("{{BODY}}", contact_tem)
savefinalhtml("contact.html", contact_html)

