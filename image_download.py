#import requests library
import requests 
#take url of image as input
a=input("Enter url")
#define function and pass the input value into it
def image_download(a):
     # create HTTP response object
    req=requests.get(a)
    # send a HTTP request to the server and save 
    # the HTTP response in a response object called req 
    with open("image.png",'wb')as f: # Saving received content as a png file
        f.write(req.content)
        # Saving received content as a png file
image_download(a) #calling function