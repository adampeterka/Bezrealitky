import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import json
import sys
import simplejson
import asyncio
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import urllib

class bezrea_Web:
    '''
    class with functions extracting values of interest for each offer
    '''
    def __init__(self,link,allowLog=True):
        self.allowLog = allowLog
        self.link = link
        r = requests.get(link)
        r.encoding='UTF-8'
        self.soup = BeautifulSoup(r.text,'lxml')
        if self.allowLog:
            print('Success!')
    
    def parseType(self):
        '''
        extract types of offers
        '''
        pdTbl = pd.read_html(self,attrs= {"class":"table"})
        atype = pdTbl[0][1][2]
        return atype
    
    def parseRegion(self):
        '''
        extract region of offer
        '''
        web = urllib.request.urlopen(self)
        soup = BeautifulSoup(web,'lxml')
        region = soup.findAll("span", attrs = {"itemprop":"title"})[3].text.strip()
        return region
    
    def parseDistrict(self):
        '''
        extract district of offer
        '''
        web = urllib.request.urlopen(self)
        soup = BeautifulSoup(web,'lxml')
        district = soup.findAll("span", attrs = {"itemprop":"title"})[4].text.strip()
        return district