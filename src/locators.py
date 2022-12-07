"""
Name of element service, when we open context menu of the file
"""


class NameServiceContext:
    MONOSNAP = "Upload to Monosnap"
    FTP = "Upload via FTP"
    FTPS = "Upload via FTPS"
    SFTP = "Upload via SFTP"
    AMAZON = "Upload to AWS S3"
    S3 = "Upload to S3 Compatible"
    BOX = "Upload to Box.com"
    GOOGLE_DRIVE = "Upload to Google Drive"
    DIGITAL_OCEAN = "Upload to DigitalOcean Spaces"
    DROPBOX = ""
    ONE_DRIVE = ""
    WEBDAV = "Upload via WebDAV"


class NameServiceBurgerMenu:
    FTP = "FTP"
    FTPS = "FTPS"
    SFTP = "sFTP"
    WEBDAV = "WebDAV"
    AMAZON = "Amazon S3"
    BOX = "Box.com"
    DIGITAL_OCEAN = "DigitalOcean"
    DROPBOX = "Dropbox"
    GOOGLE_DRIVE = "Google Drive"
    ONE_DRIVE = "OneDrive"
    S3 = "S3 Compatible"

    PUBLIC_LINK = "Public"
    PRIVATE_LINK = "Private"


class TextNotification:
    UPLOAD = "File uploaded"
    CONNECT_SUCCESS = "Connection test succeeded"
    CONNECT_FAIL = "Connection test failed"


class NameFolderInDropzoneFolderList:
    UNSORTED = "Unsorted"
