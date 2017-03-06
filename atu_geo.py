# -*- coding: utf-8 -*-

import simplejson
import urllib
import re
import sys
reload(sys)  
sys.setdefaultencoding('utf-8')


file_output = open('parsed.geojson','a')

#write the beginning of the file
file_output.write('{\n"type":"FeatureCollection",\n"crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },\n"features":[')

#define the parsing function
def json_parser(code):
    #file_output = open('parsed.txt','a')
    data = simplejson.loads(file.read())

    #define general attributes
    name_fullua = data['data']['name_fullua']
    geo_type = data['data']['wkb_geometry']['type']
    geo_coordinates = data['data']['wkb_geometry']['coordinates']
    koatuu = data['data']['koatuu']
    
    #define parent_list attributes
    try:
        region = data['data']['parent_list'][0]['name_fullua']
        district = data['data']['parent_list'][1]['name_fullua']
        rural_coun = data['data']['parent_list'][2]['name_fullua']
    except (IndexError, KeyError): #except errors for no parent_list attributes and 1 or 2 parent_list attributes
        pass
    
    #write the output file for every feature
    file_output.write('{"type":"Feature","properties":{"code":"'+str(code)+'","koatuu":"'+str(koatuu)+'","name_fullua":"'+name_fullua+'"')
    try:
        file_output.write(',"region":"'+region+'"')
        file_output.write(',"district":"'+district+'"')
        file_output.write(',"rural_coun":"'+rural_coun+'"')
        
    except:
        file_output.write('},')
    
    #write geometry
    file_output.write('"geometry":{"type":"'+geo_type+'",')
    file_output.write('"coordinates":'+str(geo_coordinates)+'}},')

for code in range (0,12050):
    try:
        file = open('json_'+str(code)+'.txt','r') #open every single txt file
        print 'Parsing feature with the code number: ', code
        json_parser(code)
    except IOError: #except errors if there is no file
        print 'No feature with code number', code

#write the end of file
file_output.write(']\n}')