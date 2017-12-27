#/usr/bin/env python

import saavpedia
import requests

if __name__ == '__main__':
    theSAAVpedia = saavpedia.SAAVpedia()

    url = theSAAVpedia.url
    r = requests.post(url, data={
        'saavpedia_dataset_name_option_id':'test',
        'Saavpedia_InputData_InputTextArea':'LEAK'
                                 })

    print theSAAVpedia.url
    theData = r.json()['data']

    for i in theData:
        print i
        for k in i.keys():
            print k, i[k]

    pass

