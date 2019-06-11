#!/usr/bin/env python3
import yaml

def ws_page_template(ws_id, ws_title):
    page_matter = "---\n"
    page_matter += "layout: page\n"
    page_matter += "ws_id: \""+ws_id+"\"\n"
    page_matter += "title: \""+ws_title+"\" \n"
    page_matter += "comments: true\n"
    page_matter += "invisible: true\n"
    page_matter += "---\n\n"

    page_content = "<p class=\"text-left\"><i>Organizers: {{ site.data.workshops.workshops[page.ws_id].organizers }} </i></p>\n"
    page_content += "<p class=\"text-left\"><i>Website: <a href= \"{{ site.data.workshops.workshops[page.ws_id].url }}\"> {{ site.data.workshops.workshops[page.ws_id].url }}</a></i></p>\n\n"

    page_content += "<p>\n {{ site.data.workshops.workshops[page.ws_id].abstract }}\n</p>"

    return page_matter+page_content

def read_data():
    with open("../../_data/workshops.yaml", 'r') as stream:
#    with open("../../_data/workshops_test.yaml", 'r') as stream:
        try:
            ws_data = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            exit(1)
    return ws_data
    
if __name__ == "__main__":
    
    ws_data = read_data()
    
    #print(ws_data)
    for key,item in ws_data["workshops"].items():
        page = ws_page_template(key, item["title"])
        file = open(key+".md", "w+")
        file.write(page)
        file.close()
                
