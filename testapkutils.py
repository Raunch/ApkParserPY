#!/usr/bin/env python
# coding: utf-8

import zipfile
from xml.dom import minidom
from axmlparserpy.axmlprinter import AXMLPrinter
import os
import sys
from apkutils import APK
import json


def apk_parser(filename):
    apkf = APK(filename)
    # print (apkf.package)
    return apkf

    

def parse_apk_info(apkFilePath):
    apk = apk_parser(apkFilePath)
    apk.get_manifest()
    # if apk.get_manifest():
    #     print(json.dumps(apk.get_manifest(), indent=1))
    # elif apk.get_org_manifest():
    #     print(apk.get_org_manifest())
    print (apk.get_main_activities())

    # print("package name " + parser.package_name)
    # print("version name " + parser.version_name)
    # print("version code " +  parser.version_code)
    # permissions = parser.get_permissions()
    # for permission in permissions:
    #     print(permission)
    return


if __name__ == '__main__':
    apkFilePath = sys.argv[1]
    parse_apk_info(apkFilePath)