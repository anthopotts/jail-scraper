#!/usr/bin/env python3

import hashlib
import requests
import json
from datetime import datetime

class EASAgency(object):

    url = 'http://offendermiddleservice.offenderindex.com/api/Values'

    def __init__(self, county, host_url, ip):
        self.county = county
        self.r_body = None
        self.r_headers = {
                'host': 'offendermiddleservice.offenderindex.com',
                'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'en-US,en;q=0.5',
                'accept-encoding': 'gzip, deflate',
                'referer': host_url,
                'origin':  host_url,
                'dnt': '1',
                'connection': 'keep-alive',
                'cache-control': 'max-age=0',
                'content-type': 'application/json; charset=utf-8'
                }
        self.r_params = {
                'three': '1',
                'fnmeLetters': '',
                'lnmeLetters': '',
                'needDate': 'false',
                'startDate': '',
                'stopDate': '',
                'getImg': 'false',
                'agencyServiceIP': ip,
                'agencyServicePort': '9000',
                'take': '9999',
                'skip': '0',
                'page': '1',
                'pageSize': '9999'
                }


    def response(self):
        return requests.get(self.url,
                params = self.r_params,
                data = self.r_body,
                headers = self.r_headers)


    def get_anonymized_data(self):
        data = self.response().json()
        inmates = []
        for inmate in data['Inmates']:
            inmates.append({
                'IdentityHash':     self.identity(inmate),
                'InmateID':         inmate['InmateID'],
                'Age':              inmate['Age'],
                'ArrestDate':       inmate['ArrestDate'],
                'ArrestTime':       inmate['ArrestTime'],
                'ArrestingOfficer': inmate['ArrestingOfficer'],
                'ArrestingAgency':  inmate['ArrestingAgency'],
                'Sex':              inmate['Sex'],
                'BookedStatus':     inmate['BookedStatus'],
                'Height':           inmate['Height'],
                'Weight':           inmate['Weight'],
                'DaysInJail':       inmate['DaysInJail'],
                'Charges':          inmate['Charges'],
                'ReleaseDate':      inmate['ReleaseDate'],
                'ReleaseTime':      inmate['ReleaseTime'],
                'Bond':             inmate['Bond'],
                'Location':         inmate['Location'],
                'Visitation':       inmate['Visitation'],
                'History':          inmate['History']
                })
        return inmates


    def identity(self, inmate_json):
        m = hashlib.sha256()
        m.update(bytes(inmate_json['FirstName'], 'utf-8', 'replace'))
        m.update(bytes(inmate_json['LastName'], 'utf-8', 'replace'))
        m.update(bytes(inmate_json['Dob'], 'utf-8', 'replace'))
        return m.hexdigest()


    def save_json(self):
        timestamp = datetime.now().strftime('%F')
        filename = 'data/{}_{}.json'.format(self.county, timestamp)
        with open(filename, 'w') as outfile:
            json.dump(self.get_anonymized_data(), outfile)
        return filename


agencies = [
        EASAgency('atkinson', 'http://atkinsoncoga.offenderindex.com/', '209.164.231.48'),
        EASAgency('brooks', 'http://brookscoga.offenderindex.com/', '151.213.122.129'),
        EASAgency('catoosa', 'http://catoosacoga.offenderindex.com/', '64.18.111.72'),
        EASAgency('chatooga', 'http://chattoogacoga.offenderindex.com/', '96.38.37.134'),
        EASAgency('decatur', 'http://decaturcoga.offenderindex.com/', '64.39.159.3'),
        EASAgency('gilmer', 'http://gilmercoga.offenderindex.com/', '66.44.216.146'),
        EASAgency('gordon', 'http://gordoncoga.offenderindex.com/', '66.110.220.212'),
        EASAgency('haralson', 'http://haralsoncoga.offenderindex.com', '208.71.234.146'),
        EASAgency('jeffdavis','http://jacksoncoga.offenderindex.com','50.207.103.19'),
        EASAgency('newton','http://newtoncoga.offenderindex.com/','12.163.216.158'),
        EASAgency('pickens','http://pickenscoga.offenderindex.com','66.44.223.50'),
        EASAgency('pierce','http://piercecoga.offenderindex.com','216.81.104.6'),
        EASAgency('tift','http://tiftcoga.offenderindex.com','216.105.189.107'),
        EASAgency('towns','http://townscoga.offenderindex.com','66.119.110.147'),
        EASAgency('turner','http://turnercoga.offenderindex.com/','turnercoso.dyndns.biz'),
        EASAgency('ware','http://warecoga.offenderindex.com/','216.240.242.154')
        ]


for agency in agencies:
    print('Downloading %s' % (agency.county))
    print('Wrote file %s' % (agency.save_json()))
