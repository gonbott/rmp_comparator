#!/usr/bin/env python
import xml.etree.cElementTree as ET
import requests
import urllib.request
import os, shutil
#import PrettyTable
#----------------------------------------------------------------------
folder = 'C:/Users/U6033379/Desktop/python/rmp_comparator'
def parseXML(xml_file, xml_file2):
    """
    Parse XML with ElementTree
    """
    #tree = ET.ElementTree(file=xml_file)
    tree = ET.ElementTree(file=xml_file)
    #print (tree.getroot())
    root = tree.getroot()

    #tree2 = ET.ElementTree(file=xml_file2)
    tree2 = ET.ElementTree(file=xml_file2)
    root2 = tree2.getroot()

    #print ("tag=%s, attrib=%s" % (root.tag, root.attrib))
    from prettytable import PrettyTable
    t = PrettyTable(['N','Component', env, env2])
    count=1
    for child in root:
            for child2 in root2: 
                    if child.get('name') == child2.get('name'):                        
                        if child.get('version') != child2.get('version'):
                            if stg_filter == 1: 
                                if child.get('name')[:7].find("STAGING") != 0:
                                    #print(child.get('name')[:7].find("STAGING"))
                                    #print ("---------STABLE-------", child.get('name'),  "-->" , child.get('version'), "---------PROD-------",child2.get('name'),  "-->" , child2.get('version'))
                                    #print (child2.get('name'),  "------->" , child2.get('version'))
                                    #print("hola")
                                    #t.add_row([child.get('name'), child.get('version'), child2.get('version')])
                                    t.add_row([count,child.get('name'), child.get('version'), child2.get('version')])
                                    #t.add_row(['Bob', 19])
                                    count=count+1
                            else:
                                #print ("---------STABLE-------", child.get('name'),  "-->" , child.get('version'), "---------PROD-------",child2.get('name'),  "-->" , child2.get('version'))
                                #print (child2.get('name'),  "------->" , child2.get('version'))
                                #print("hola")
                                #t.add_row([child.get('name'), child.get('version'), child2.get('version')])
                                t.add_row([count,child.get('name'), child.get('version'), child2.get('version')])
                                #t.add_row(['Bob', 19])
                                count=count+1     
    print (t)
#----------------------------------------------------------------------
def getXML():
    #print('holas')    
    #url = "https://rmp.lstools.int.clarivate.com/pub/deployments_schedule.cgi?platform=Cortellis&env=stable-us-west-2&deployed=true"
    #r = requests.get(url)
    #print (r.content)

    #response = urllib.request.urlopen('https://rmp.lstools.int.clarivate.com/pub/deployments_schedule.cgi?platform=Cortellis&env=stable-us-west-2&deployed=true')
    #html = response.read()
    #print(html)

    #local_filename, headers = urllib.request.urlretrieve('https://rmp.lstools.int.clarivate.com/pub/deployments_schedule.cgi?platform=Cortellis&env=stable-us-west-2&deployed=true', filename='C:/Python/Python36-32/Scripts/xml_file.xml')
    #html = open(local_filename)
    #print(html)
    #print(headers)
    #html.close()
    local_filename, headers = urllib.request.urlretrieve('https://rmp.lstools.int.clarivate.com/pub/deployments_schedule.cgi?platform=Cortellis&env=' + env + '&deployed=true', filename=folder + '/' + env + '.xml')
    xml = open(local_filename)
    print ('https://rmp.lstools.int.clarivate.com/pub/deployments_schedule.cgi?platform=Cortellis&env=' + env + '&deployed=true')
    local_filename2, headers2 = urllib.request.urlretrieve('https://rmp.lstools.int.clarivate.com/pub/deployments_schedule.cgi?platform=Cortellis&env=' + env2 + '&deployed=true', filename=folder + '/' + env2 + '.xml')
    xml2 = open(local_filename2)

    parseXML(local_filename, local_filename2)
#----------------------------------------------------------------------   
def cleanAll():
    file_path = folder + '/' + env + '.xml'
    file_path2 = folder + '/' + env2 + '.xml'

    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        if os.path.isfile(file_path2):
            os.unlink(file_path2)
    except Exception as e:
        print(e)
#----------------------------------------------------------------------   
if __name__ == "__main__":
        
    stable = 'stable-us-west-2'
    perf   = 'perf-eu-west-1'
    prodeu = 'prodeu-eu-west-1'
    produs = 'produs-us-west-2'
    stg_filter = 0 #True=1 filter activated
   
    env  = prodeu
    env2 = produs
    getXML()
    cleanAll()