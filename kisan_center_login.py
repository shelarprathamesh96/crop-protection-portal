import pyrebase
from flask import request


class Login_Kisan(object):

    def __init__(self):
        
        self.config = {
            "apiKey": "AIzaSyCxkC1z40IDfqXlT9DOo06zmmZrPAN3_nU",
             "authDomain": "cropprotectionportal-ea544.firebaseapp.com",
             "databaseURL": "https://cropprotectionportal-ea544-default-rtdb.asia-southeast1.firebasedatabase.app",
             "projectId": "cropprotectionportal-ea544",
             "storageBucket": "cropprotectionportal-ea544.appspot.com",
             "messagingSenderId": "117731761791",
             "appId": "1:117731761791:web:0c4b1cb3fe04c56ee3694a",
             "measurementId": "G-X0B2CMBWQ5"
        }


        self.firebase = pyrebase.initialize_app(self.config)

        self.auth = self.firebase.auth()

    def kisan_center_login(self):

        if request.method == 'POST':
            email = request.form['email']
            password = request.form['pass']
            try:
                user = self.auth.sign_in_with_email_and_password(email, password)
                # user['id']
                return 'successful',email
            except:
                return 'unsuccessful'