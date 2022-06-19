import dropbox


class Dropbox:
    def __init__(self, access_token):
        self.access_token = access_token
        self.dbx = dropbox.Dropbox(self.access_token)


    def check_auth(self):
        try:
            current_acc = self.dbx.users_get_current_account()
            print(current_acc)
            print("Connected to Dropbox successfully ")
        except Exception as e:
            print(str(e))

    def upload_files(self):
        try:
            file_from = r"D:/New folder/BizCompliancer/Dropbox/data/1.cpp"
            file_to = "/home/Apps/BizC/Test.cpp"
            with open(file_from, 'rb') as file:
                self.dbx.files_upload(file.read(), file_to)
            print('Your file uploaded successfully')
        except Exception as e:
            print("Error while uploading file to Dropbox :  " + str(e))

    def download_files(self):
        try:
            local_file_path = r"C:\Users\win10\Downloads"
            with open(local_file_path, "wb") as file:
                metadata, result = self.dbx_files_download(path= "/home/Apps/BizC/home/Apps/BizC/test.cpp")
                file.write(result.content)
        except Exception as e:
            print("File downloading failed" + str(e))




at = 'sl.BJ1g8CPCRgCgddsk-W3FSBcrI8KqC4Dt4bbjKJi4q661JH-VzYNKFJkHtT6LazZAQQZE2gC19_VsuAtjEhyZtkCgPi7CK3Tu729Q8_0zS6vW24c88WSeEIo_ccu7ErUofLEoECH5RIM'
user = Dropbox(at)
user.check_auth()
#user.upload_files()
user.download_files()

