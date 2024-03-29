import re
import requests
import datetime
import csv
header={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}#模仿浏览器
url1 = 'https://healthcare.xqyk024.com/consult/diagnosis/doctors?pageNumber=1&pageSize=50&order=0'
response = requests.get(url1, headers=header)
response.encoding = 'utf-8'
html = response.text
# html = buff.decode()
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
def write_csv(num_date,num_name,num_sum):
    path  = "xq.csv"
    with open(path,'a+',newline='') as f:
        csv_write = csv.writer(f)
        data_row = [num_date,num_name,num_sum]
        csv_write.writerow(data_row)
        f.close()
def write_md(num_date,num_sum):
    path  = "README.md"
    with open(path,'a+',newline='') as f:
        f.write(str(num_date)+" "+str(num_sum)+"\n")
        f.close()        
write_csv(today,name_result,result_sum)
write_md(today,result_sum)
print(today,name_result,result_sum)
#print(name_list)
#print(result_int)
