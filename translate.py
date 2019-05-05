# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 13:56:10 2019

@author: tangyujie
"""
import os
from translate import Translator

def main():
    translator=Translator(from_lang="chinese",to_lang="english")
    print("请输入需要翻译的中文文本:")
    string=input("")
    translation = translator.translate(string)
    print(translation)
    os.system("pause")
if __name__=='__main__':
    main()