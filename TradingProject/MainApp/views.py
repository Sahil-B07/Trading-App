import json, mimetypes
import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'main/index.html')

def handleUpload(request):
    csvFile = request.FILES['csvFile']
    timeFrame = request.POST['timeFrame']
    df = pd.read_csv(csvFile, nrows=int(timeFrame))

    traDict = {}

    traDict['ID']=df['BANKNIFTY'][0]
    traDict['DATE'] = int(df['DATE'][0])
    traDict['TIME'] = df['TIME'][0]
    traDict['OPEN'] = int(df['OPEN'].iloc[0])
    traDict['HIGH'] = int(df['HIGH'].max())
    traDict['LOW'] = int(df['LOW'].min())
    traDict['CLOSE'] = int(df['CLOSE'].iloc[-1])
    traDict['VOLUME'] = int(df['VOLUME'].iloc[-1])

    with open("MainApp/static/main/media/sample.json", "w",encoding='utf-8') as outfile:
        json.dump(traDict, outfile)
 
    params = {'data': traDict}
    return render(request, 'main/download.html', params)
