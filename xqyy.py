import re
import urllib.request as urllib2
import datetime
header={"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}#模仿浏览器
request = urllib2.Request('https://healthcare.xqyk024.com/consult/diagnosis/doctors?pageNumber=1&pageSize=20&order=0',headers=header)
response = urllib2.urlopen(request)
buff = response.read()
html = buff.decode()
#print(html)
result = re.findall("consultCount\":\d+",html)
result_string = ",".join(result)
result_score_list = re.findall(r"\d+",result_string)
result_int = list(map(int,result_score_list))
result_sum=sum(result_int)
name = re.findall("employeeName\":\"[\u4E00-\u9FA5]+",html)
name_string = ",".join(name)
name_list = re.findall(r"[\u4E00-\u9FA5]+",name_string)
name_result = []
for i in range(0,len(name_list)):
    name_result1 = name_list[i] + ' ' + result_score_list[i]
    name_result.append(name_result1)
today = datetime.date.today()
print(name_result)
#print(name_list)
#print(result_int)
print(date，result_sum)
