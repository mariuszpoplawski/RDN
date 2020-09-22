import requests
from bs4 import BeautifulSoup
import sys
from datetime import date
import calendar

'''
example URL
URL = "https://towarowa-gielda-energii.cire.pl/st,8,38,me,0,0,0,0,0,rynek-dnia-nastepnego.html?Day=22&Month=09&Year=2020&button=poka%BF&typ=dzien"
'''
def GetDay(day,month,year):
	try:
		URL = "https://towarowa-gielda-energii.cire.pl/st,8,38,me,0,0,0,0,0,rynek-dnia-nastepnego.html?Day="+day+"&Month="+month+"&Year="+year+"&button=poka%BF&typ=dzien"

		resp = requests.get(URL)


		soup = BeautifulSoup(resp.content, "html.parser")
		rows = soup.find_all('tr')

		columns=[]
		for row in rows:
		    cols=row.find_all('td')
		    cols=[x.text.strip() for x in cols]
		    try:
		    	if int(cols[0]) in range(0,25):
		    		columns.append(cols)
		    except:
		    	pass
		if columns:
			return columns
		else:
			return 0
	except:
		return 0

def avgof5to16hr(hours):
	try:
		summary = 0.0

		for hour in hours:
			if int(hour[0]) in range(5,17):
				summary = summary + float(hour[1].replace(",","."))

		return summary / 12
	except:
		return 0

args = sys.argv

'''
print("Current year:", current_date.year)
print("Current month:", current_date.month)
print("Current day:", current_date.day)
'''
current_date = date.today() 


if args[1] == "srednia":
	day,month,year = args[3].split("/")
	if args[2] == "miesiac":
		monthDays = calendar.monthrange(int(year),int(month))[1]

		if int(month) == current_date.month:
			monthDays = current_date.day
		if int(month) > current_date.month and int(year) >= current_date.year:
			print("Data nie moze byc większa niż dzisiejsza: "+str(current_date.day)+"/"+str(current_date.month)+"/"+str(current_date.year)+"/")
			exit()
		suma = 0

		for i in range(1,monthDays+1):
			day = GetDay(str(i),month,year) 
			dayAVG = avgof5to16hr(day)
			suma = suma + dayAVG
			#print(str(i)+"/"+month+"/"+year)
			#print(dayAVG)
		suma = suma / monthDays
		print("Srednia RDN cen z miesiaca miedzy godzinami 5 a 16: "+month+"/"+year)
		print(suma)
		
	if args[2] == "dzien":
		day = GetDay(day,month,year) 
		print("Srednia RDN cena od 5 do 16 dnia "+str(args[3])+":")
		print(avgof5to16hr(day))
else:
	print("python3 RDN.py  srednia dzien 28/07/2019 - obliczanie sredniej z dnia dla godzin 5-16 (Czas pracy farm PV)")
	print("python3 RDN.py  srednia miesiac 01/06/2020 - obliczanie sredniej z miesiaca (czerwiec 06) dla godzin 5-16 (Czas pracy farm PV)")
	exit()


'''
exit() 
if not 0:
	for col in day:
		print(col)
'''
