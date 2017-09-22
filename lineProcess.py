# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 10:56:48 2017

@author: Maddox.Meng
"""

#f = open(file,'r')
#result = open('game.of.thrones.txt','w+')
#i=1
#for line in f.readlines():
#    print line.split(',,')[1].split('&}')[-1].strip('\n')
#    result.write("%03d" % i+ '--' + line.split(',,')[1].split('&}')[-1])
#    print line.split(',,')[1].split('\N{')[0]+('\n')
#    result.write('   --'+line.split(',,')[1].split('\N{')[0].replace('-','- ')+('\n')+('\n'))
#    i+=1
    #print line.split(',,')[1].split('&}')[-1]
    
'''--------------------------------------------------------------------------'''    
#import chardet
#pathass = r'C:\Users\Maddox.Meng\MyWorkField\A+Doc\Reading_Materials\Game.of.Thrones.S01\Game.of.Thrones.S01E01.720p.BluRay.X264-REWARD.ass'
#fass = open(pathass,'rb')
##fencoding=chardet.detect(fass.read())
##print fencoding['encoding']
#
#import codecs
#encoded_text = open(pathass, 'rb').read()    #you should read in binary mode to get the BOM correctly
#bom= codecs.BOM_UTF16_LE                                      #print dir(codecs) for other encodings
#assert encoded_text.startswith(bom)                           #make sure the encoding is what you expect, otherwise you'll get wrong data
#encoded_text= encoded_text[len(bom):]                         #strip away the BOM
#decoded_text= encoded_text.decode('utf-16le').encode('utf-8')                 #decode to unicode
##print decoded_text
#
#i=1
#result = open('game.of.thrones.txt','w+')
#for line in decoded_text.split('\n'):
#    print line+'\n'
#    if line.startswith('Dialogue') and line.split(',,')[-1].startswith('{') is False:
#        print line.split(',,')[1].split('&}')[-1].strip('\n')
#        result.write("%03d" % i+ '--' + line.split(',,')[1].split('&}')[-1] + '\n')
#        print line.split(',,')[1].split('\N{')[0]+('\n')
#        result.write('   --'+line.split(',,')[1].split('\N{')[0].replace('-','- ')+('\n')+('\n'))
#        i+=1
##    if line.startswith('Dialogue'):
##        print line.split(',,')[1].split('&}')[-1].strip('\n')

import codecs

import chardet

def getCodec(path):
    
    f = open(path,'rb')
    fencoding=chardet.detect(f.read())
    return fencoding['encoding']
    f.close()


def decodeText(path, codec):
    encoded_text = open(path, 'rb').read()    #you should read in binary mode to get the BOM correctly
    if codec.find('16') !=-1:
        bom= codecs.BOM_UTF16_LE                                      #print dir(codecs) for other encodings
    if codec.find('8') !=-1:    
        bom=codecs.BOM_UTF8
    assert encoded_text.startswith(bom)                           #make sure the encoding is what you expect, otherwise you'll get wrong data
    encoded_text= encoded_text[len(bom):]                         #strip away the BOM
    #decoded_text= encoded_text.decode('utf-16le').encode('utf-8') 
    decoded_text= encoded_text.decode(codec).encode('utf-8')                 #decode to unicode
    
    return decoded_text


def genTxt(decoded_text,root,file):
    
    txt = os.path.join(root,file.replace('.ass', '.txt'))
    result = open(txt,'w+')
    i=1
    for line in decoded_text.split('\n'):
        #print line+'\n'
        if line.startswith('Dialogue') and line.split(',,')[-1].startswith('{') is False:
            #print line.split(',,')[1].split('&}')[-1].strip('\n')
            result.write("%03d" % i+ '--' + line.split(',,')[1].split('}')[-1] + '\n')
            # line.split(',,')[1].split('\N{')[0]+('\n')
            result.write('   --'+line.split(',,')[1].split('\N{')[0].replace('-','- ')+('\n')+('\n'))
            i+=1
    result.close()        



import os 
path = r'C:\Users\Maddox.Meng\MyWorkField\A+Doc\Reading_Materials\Game.of.Thrones.S05'

for root, dirs, files in os.walk(path):
    for file in files:
        if file.find('.ass') != -1:
            print file.decode('gbk')
            fullPath = os.path.join(root,file)
            codec = getCodec(fullPath)
#            decoded_text = decodeText(fullPath, codec)
#            genTxt(decoded_text,root,file)



