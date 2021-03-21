import csv

from django.http import HttpResponseRedirect
from django.shortcuts import render

import diseaseprediction
count=0
sym=[]
chatrec=[]
response = []
clearchat=True

with open('templates/heart.csv', newline='') as f:
    reader = csv.reader(f)
    symptoms = next(reader)
    symptoms = symptoms[:len(symptoms) - 1]

def clear(req):
    global chatrec
    global sym
    chatrec=[]
    sym=[]
    response = []
    
    print('inside clear')
    return HttpResponseRedirect('/')

def addchat(req):
    ans = ""
    if 'sym' in req.POST:
        sym.append(req.POST.get('sym'))
        global symptoms,response
        response.append(req.POST.get('sym'))
        
        #symptoms.remove(req.POST.get('sym'))
        ans = {
            'type': 'ans',
            'msg': req.POST.get('sym')
        }
        

    else:

        ans = {
            'type': 'ans',
            'msg': req.POST.get('ans')
        }

    chatrec.append(ans)

    return HttpResponseRedirect('/')

def home(req):
    predict = 'false'
    global response
    if len(chatrec)==0:
        ques1 = {
            'type': 'ques',
            'sym': 'false',
            'predict':'false',
            'msg': 'Hey, I am your helper Doctor! Ans the following Questions'
        }

        chatrec.append(ques1)

    if len(response) == 13 :
        name = chatrec[1]
        #print(response)
        disease = diseaseprediction.dosomething(response)
        res = ""
        if disease[0] == 0:
            res = " Absence of heart disease in the patient "
        else:
            res = " Presence of heart disease in the patient "

        ques14 = {
            'type': 'ques',
            'sym': 'false',
            'predict':'true',
            'msg': res
        }
        predict='true'
        chatrec.append(ques14)
    elif (len(chatrec) == 1):


            ques1 = {
                'type': 'ques',
                'sym': 'true',
                'predict':'false',
                'msg': 'Q' + str(len(sym)+1) + '. What is your Age:  '
            }
            chatrec.append(ques1)
    elif (len(chatrec) == 3):

            ques2 = {
                'type': 'ques',
                'sym': 'true',
                'predict':'false',
                'msg': 'Q' + str(len(sym)+1) + '. What is your Gender: '
            }
            chatrec.append(ques2)

    elif (len(chatrec) == 5):
            ques3 = {
                'type': 'ques',
                'sym': 'true',
                'predict':'false',
                'msg': 'Q' + str(len(sym)+1) + '. Chest pain type ( in range 0-3 ): '
            }
            chatrec.append(ques3)
    elif (len(chatrec) == 7):


            ques4 = {
                'type': 'ques',
                'sym': 'true',
                'predict':'false',
                'msg':  'Q' + str(len(sym)+1) + '. Your resting blood pressure : '
            }
            chatrec.append(ques4)
    elif (len(chatrec) == 9):


            ques5 = {
                'type': 'ques',
                'sym': 'true',
                'predict':'false',
                'msg': 'Q' + str(len(sym)+1) + '. Serum cholestoral in mg/dl:  '
            }
            chatrec.append(ques5)

    elif (len(chatrec) == 11):


            ques6 = {
                'type': 'ques',
                'sym': 'true',
                'predict':'false',
                'msg': 'Q' + str(len(sym)+1) + '. fasting blood sugar > 120 mg/dl :  '
            }
            chatrec.append(ques6)
    elif (len(chatrec) == 13):


            ques7 = {
                'type': 'ques',
                'sym': 'true',
                'predict':'false',
                'msg': 'Q' + str(len(sym)+1) + '. resting electrocardiographic results (values 0,1,2): '
            }
            chatrec.append(ques7)

    elif (len(chatrec) == 15):


            ques8 = {
                'type': 'ques',
                'sym': 'true',
                'predict':'false',
                'msg': 'Q' + str(len(sym)+1) + '. Maximum heart rate achieved : '
            }
            chatrec.append(ques8)

    elif (len(chatrec) == 17):


            ques9 = {
                'type': 'ques',
                'sym': 'true',
                'predict':'false',
                'msg': 'Q' + str(len(sym)+1) + '. exercise induced angina : '
            }
            chatrec.append(ques9)

    elif (len(chatrec) == 19):


            ques10 = {
                'type': 'ques',
                'sym': 'true',
                'predict':'false',
                'msg': 'Q' + str(len(sym)+1) + ' oldpeak = ST depression induced by exercise relative to rest '
            }
            chatrec.append(ques10)

    elif (len(chatrec) == 21):


            ques11 = {
                'type': 'ques',
                'sym': 'true',
                'predict':'false',
                'msg': 'Q' + str(len(sym)+1) + '. the slope of the peak exercise ST segment: '
            }
            chatrec.append(ques11)

    elif (len(chatrec) == 23):


            ques12 = {
                'type': 'ques',
                'sym': 'true',
                'predict':'false',
                'msg': 'Q' + str(len(sym)+1) + '. number of major vessels (0-3) colored by flourosopy '
            }
            chatrec.append(ques12)

    elif (len(chatrec) == 25):


            ques13 = {
                'type': 'ques',
                'sym': 'true',
                'predict':'false',
                'msg': 'Q' + str(len(sym)+1) + '. thal: 3 = normal; 6 = fixed defect; 7 = reversable defect '
            }
            chatrec.append(ques13)
    

    return render(req,'index.html',{'chat':chatrec,'symptoms':symptoms,'predict':predict})