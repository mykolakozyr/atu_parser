# -*- coding: utf-8 -*-

import simplejson
import urllib
import re
import time
import sys
reload(sys)  
sys.setdefaultencoding('utf-8')


def atu_parser(code):
    file_nonfound = open('nonfound_2.txt','a')
    try:
        url = 'http://atu.minregion.gov.ua/api/format/region_template/ato.ato_level_territory_view/atoid/'+str(code)+'/wkb_geometry,name_fullua,district_list,parent_list,koatuu'
        
        #read the appropriate data
        handler = urllib.urlopen(url).read()
        result = re.search(r'"data":{"wkb_geometry"(.*)', handler)
        json = str(result.group(0))

        #create a json file
        output_json = open('json_'+str(code)+'.txt','w')
        
        output_json.write('{')
        output_json.write(json)
    except:
        print 'Cannot parse feature with the code: ', code
        file_nonfound.write(str(code)+',')


 #define the parsing code for nonfound objects
file = open('nonfound.txt','r')
for line in file:
    line = line.split(',')
    for code in line:
        print 'Parsing feature with the code number: ', code
        atu_parser(code)
        time.sleep(5)