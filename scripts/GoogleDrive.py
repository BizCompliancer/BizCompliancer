import os
from pydrive.auth import GoogleAuth  # pydrive help us to download and upload files to google drive.
from pydrive.drive import GoogleDrive


class GoogleDrive:
    folder = '1S_b2h-CV8eiyZAUgDTwmNar_BptkcOkx'  # Google drive folder paath

    directory = "D:/New folder/BizCompliancer/data"  # Directory path of which we want to upload the file

    gauth = GoogleAuth()
    drive = GoogleDrive(gauth)

    def upload_file(self):
        for f in os.listdir(self.directory):  # os.listdir() is used to iterate the list of file in the directory of which path is provided in directory variable
            file_path = os.path.join(self.directory, f)  # os.path.join(folder_path, file_name) - this function is used to merge the path and file.
            print(file_path)
            print(f)
            gfile = self.drive.CreateFile({'parents': [{'id': self.folder}], 'title': f})  # drive.CreateFile() - used to create a file for Google Drive.

            gfile.SetContentFile(file_path)  # SetContentFile() - Used to set file.
            gfile.Upload()  # .Upload - used to upload file.

    def download_files(self):
        file_list = self.drive.ListFile({'q': f"'{self.folder}' in parents and trashed  = false"}).GetList()  # doubt

        for index, file in enumerate(file_list):  # doubt in enumerate()
            file.GetContentFile(file['title'])  # to download the file

            print(index + 1, 'File downloaded: ', file['title'])


file = GoogleDrive()

#file.upload_file()
file.download_files()
