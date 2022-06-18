import dropbox


class Dropbox:
    def __init__(self, access_token):
        self.access_token = access_token
        self.dbx = dropbox.Dropbox(self.access_token)


    def check_auth(self):
        current_acc = self.dbx.users_get_current_account()
        print(current_acc)

    def upload_files(self):
        file_from = r"D:/New folder/BizCompliancer/Dropbox/data/1.cpp"
        file_to = "/home/Apps/BizC/Test.cpp"
        with open(file_from, 'rb') as file:
            self.dbx.files_upload(file.read(), file_to)
        print('Your file uploaded successfully')



at = 'sl.BJwsQDbdSKNsM3nsMdGQrnWyLaUR24R3Iy4ky_Mn-Yc6OM86l86ozq5r2brfR0LqzeEENUaLpCmfQI7RUOlHu2sY5g3sORW8ahhlZGzeogVkqXDNAU-NtSg-pCsA0yldoPkenXk'
user = Dropbox(at)
user.check_auth()
user.upload_files()

