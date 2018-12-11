from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

import urllib.request
import shutil
import os

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '19banGgNQayCv90X4E9fX4ObpeKuKJh0yQ4ZTpyDmGrQ'
SAMPLE_RANGE_NAME = 'bseindiacodestest'

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])
    sheet.update_cell('P2', 'Done')
    if not values:
        print('No data found.')
    else:
        for row in values:
          if(row[4]=="A"):
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s' % (row[0]))
            directory="c://srinivas//PythonWorkspace//GroupA//" + str(row[0])
            print(directory)
            if not os.path.exists(directory):
              os.makedirs(directory)
            for x in range(10, 18):
              #url = "https://beta.bseindia.com/bseplus/AnnualReport/500002/5000021210.pdf"
              url = "https://beta.bseindia.com/bseplus/AnnualReport/"+str(row[0])+"/"+str(row[0])+ str(row[9]) + str(x) + ".pdf"
              print(url)  
              try:
                output_file = directory + "//"+str(row[0])+ str(row[9]) + str(x) + ".pdf"
                with urllib.request.urlopen(url,timeout=10) as response, open(output_file, 'wb') as  out_file:
                  shutil.copyfileobj(response, out_file)
              except:
                pass

if __name__ == '__main__':
    main()