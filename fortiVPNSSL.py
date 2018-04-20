#!/usr/bin/python

import fortiosapi
import json

from json2table import convert

fg = fortiosapi.FortiOSAPI()
fg.login( host="417intfw01.trlm.com", username="admintest", password="admintest" )
#print ( fg.monitor( path="vpn", name="ssl" ) )

#print json.dumps( (fg.monitor(path="vpn", name="ssl")), indent=2  )

#json_object =  json.dumps( (fg.monitor(path="vpn", name="ssl")), indent=2  )
json_object = fg.monitor(path="vpn", name="ssl")

html = convert( json_object, build_direction="LEFT_TO_RIGHT", table_attributes={"style" : "width:100%",  "border" : 1} )

print(html)
