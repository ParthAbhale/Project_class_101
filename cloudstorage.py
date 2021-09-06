import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
    
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = input('Enter Your Access Token: ')
    transferData = TransferData(access_token)

    file_from = input("Enter The File Which You Have to Upload: ")
    file_to = input("Enter The Path Where You Have to Upload: ")  

    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()