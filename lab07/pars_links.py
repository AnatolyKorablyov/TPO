# -*- coding: UTF-8 -*-

import sys
import os
import re
import urllib
import urllib2
import cookielib
import requests
import urlparse

def connect_http(url):
    html = urllib.urlopen(url)
    return html.getcode()


def read_link(url, lst):

    print url
    cookiesTestDotCom = {
        'DOAAuthReferrer': 'http%3A//vk.com/away.php',
	'DOADFgsjnrSFgsg329gaFGa3ggs9434sgSGS43tsgSHSG35': '%23f81527457661943351b51b626e3f95f01c509fd5%23TPOU%231481447486%23137976361%23',
	'optimizelyEndUserId': 'oeu1480583491368r0.47219394644354806',
	'_ga': 'GA1.2.2101613610.1480583494'
    }
    session = requests.Session()
    html = session.get(url, cookies = cookiesTestDotCom).text
    
    links = re.findall('a .*?href="(.*?)"', html)
    for i in range(len(links)):
         a = links[i]
         if (a not in lst):
             lst.append(str(a))
    return lst

def write_url_to_file(url, return_code, path):
    fil = open(path, 'a')
    fil.write(url + ' ' + str(return_code) + '\n')
    fil.close()

def main(url):
    path = './download_sites/' 
    if not os.path.exists(path):
        os.mkdir(path)

    path_correct_urls = path + 'correct_urls'
    path_incorrect_urls = path + 'incorrect_urls'

    url_main = url
    lst_url = [url_main]
    host_name = urlparse.urlparse(url_main).hostname
    true_url_lst = [url_main]
    incorrect_url_lst = []
    count = 0
    while count != len(true_url_lst):
        print count, len(true_url_lst)
        if (host_name == urlparse.urlparse(true_url_lst[count]).hostname):
            lst_url = read_link(true_url_lst[count], lst_url)
            for i in range(len(lst_url)):
                replace_http = lst_url[i][0:4]
                a = lst_url[i]
                return_code = connect_http(url_main + a)
                if (replace_http in ['http', 'ftp:']):
                    return_code = connect_http(a)
                    if (return_code != 404):
                        if a not in true_url_lst:
                            true_url_lst.append(str(a))
                            write_url_to_file(a, return_code, path_correct_urls)
                    else:
                        incorrect_url_lst.append(a)
                        write_url_to_file(a, return_code, path_incorrect_urls)
                elif (return_code != 404):
                    if url_main + a not in true_url_lst:
                        true_url_lst.append(str(url_main + a))
                        write_url_to_file(str(url_main + a), return_code, path_correct_urls)
                elif a not in incorrect_url_lst:
                    incorrect_url_lst.append(a)
                    write_url_to_file(a, return_code, path_incorrect_urls)
                    
        count += 1
        
    
if (len(sys.argv) != 2):
    print u"Укажите адрес страницы в качестве параметра. Формат ввода pars_links.py http://path-to-site.com"
else:
    rl_re = re.compile(
        r'^https?://'
        r'(?:(?:[A-Z0-9-]+\.)+[A-Z]{2,6}|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|/\S+)$', 
    re.IGNORECASE)
    if (rl_re.match(sys.argv[1]) != None):
        main(sys.argv[1])
        print 'Complete'
    else:
        print u"Введенный адрес не является корректным URL. Пожалуйста, введите адрес в формате http://path-to-site.com"
