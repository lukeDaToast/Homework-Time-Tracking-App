'''
1	Get Assinement Name - done
2	Get Predicted time - done
3	Get # of questions - done
5	get date - done
6	predicted vs real time - not subtracting properly
7	ave number of assinments
8	ave number of questions
9	Calcualte time per question
10	calculate the average time per question
11	get total time per date
12	get average time per day
13	average time difference
14	average time per subject
15	ave number of questions per assinment
16	ave time per question
17	make a ui
'''
import csv
from datetime import *
import pytz


timezone = pytz.timezone('US/Eastern')
datetime.now(timezone)
times = open('times.txt', 'a+')
subjectFile = open('subjects.txt', 'a+')



def subjectIn():
  global subject
  subject = input('What is the subject: \n')
  global subjectList
  subjectList = []
  subjectList.append(subject)
  print(f'the subject list is {subjectList}')
  subjectFile.close()
  with open('subjects.txt', 'a+') as f:
    for line in subjectList:
      f.write(line)
      f.write('\n')
  subjectFile.close()
  
def nameIn():
  global name 
  name = input('What is the name of the assinement: \n')  
  global qNumb
  qNumb = input(f'How many questions are in {name}: \n')
  qNumb = int(qNumb)

def time():
  def predictedTime():
    global predictedTime
    predictedTime = input('What is the predicted time in HH:MM: \n')
    date = datetime.now().date()
    date = str(date)
    timeAndDate = predictedTime + ' ' + date
    print(timeAndDate)
    date_time = datetime.strptime(timeAndDate, '%H:%M %Y-%m-%d')
    global td
    td = timedelta(hours=date_time.hour, minutes=date_time.minute, seconds=date_time.second)
    print(td)
    
  def startTime():
    global begin
    begin = input("Press enter when you are ready to start the clock: ")
    global timeStart
    timeStart = datetime.now()
    print(timeStart)
  
  def endTime():
    global end
    end = input("Press enter when you are ready to stop the clock: ")
    global timeEnd
    timeEnd = datetime.now()
    print(timeEnd)
  
  def eleapsedTime():
    global elapse
    elapse = timeEnd - timeStart
    print(elapse)
    print(f'The total time is {elapse}')
  
  def date():
    global date
    date = datetime.now().date()
    print(date)
    
  predictedTime()
  startTime()
  endTime()
  eleapsedTime()
  date()

def combine():
  global combineList
  combineList = []
  combineList.append(subject)
  combineList.append(elapse)
  print(combineList)

def export():
  with open('export.csv', 'a+', newline='') as file:
    writer = csv.writer(file) 
    writer.writerow([subject, elapse, name,td,qNumb,date])


subjectIn()
nameIn()
time()
combine()
export()