import requests
def extract_all_links(site):
    html=requests.get(site).text
    links=[links.get('href')]
    return links
site_link=input("enter URL of the site:")
all_links=extract_all_links(site_link)
print(all_links)

output:enter urlsite:http://ful.io
https://www.facebook.com/fulio.com/fuliotech/
https://www.linkedin.com/company/ful-io/
email/s-
support@ful.io
contact:
+1 343 303 666
