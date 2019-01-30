#coding:utf-8
import requests
import json
from common.openpy_excel1 import ParseExcel
import os
class RunMethod:
	def post_main(self,url,data,header=None):
		res = None
		if header !=None:	
			res = requests.post(url=url,data=data,headers=header)
		else:
			res = requests.post(url=url,data=data)
		return res.json()

	def get_main(self,url,data=None,header=None):
		res = None
		if header !=None:	
			res = requests.get(url=url,data=data,headers=header,verify=False)
		else:
			res = requests.get(url=url,data=data,verify=False)
		return res.json()

	def run_main(self,method,url,data=None,header=None):
		res = None
		if method == 'Post':
			res = self.post_main(url,data,header)
		else:
			res = self.get_main(url,data,header)
		return json.dumps(res,ensure_ascii=False)
		#ensure_ascii=False为输出中文处理
		#return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)

if __name__ == "__main__":
	runtest = RunMethod()
	data_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	excelPath = os.path.join(data_path, "apitest.xlsx")
	ecl=ParseExcel()
	ecl.loadWorkBook(excelPath)
	elname = ecl.getSheetByName('jktest')
	maxrows = ecl.getRowsNumber(elname)
	print (maxrows)

	# for i in range(2,maxrows+1):
	# 	res_val = ecl.getCellOfValue(elname,i,2)
	#   url_val = ecl.getCellOfValue(elname,i,3)
	# 	type_val = ecl.getCellOfValue(elname,i,4)
	# 	header_val = ecl.getCellOfValue(elname,i,5)
	#   data_val = ecl.getCellOfValue(elname,i,6)
	# 	expect_val = ecl.getCellOfValue(elname,i,7)
	# 	print (res_val,header_val,expect_val)
	# 	if header_val == None:
	# 		results = runtest.run_main(type_val,url_val,data_val)
	# 	else:
	# 		results = runtest.run_main(type_val,url_val,data=data_val,header=header_val)
	# 	print (results)
	type_val = ecl.getCellOfValue(elname,3,4)
	url_val = ecl.getCellOfValue(elname,3,3)
	header_val = ecl.getCellOfValue(elname,3,5)
	data_val = ecl.getCellOfValue(elname,3,6)
	print (data_val)
	# results = runtest.get_main(url_val,data_val)
	results = runtest.run_main(type_val,url_val,data_val)
	# results = runtest.post_main(url_val,data_val,header_val)
	print (results)
	ecl.writeCell(elname,"pass",3,8,style = 'green')