import urllib
def read_text():
        quotes = open ('C:\Users\kero\Desktop\prank\shit.txt')
        contents_of_file =  quotes.read()
        #print (contents_of_file)
        quotes.close()
        molol(contents_of_file)

def molol(arg):
        connection = urllib.urlopen('http://www.wdylike.appspot.com/?q=' + arg)
        text = connection.read()
        #print (text)
        connection.close()
        if text == False:
           print ('there is no mistake')
        else:
           print ('the is a mistake')
        


read_text()
