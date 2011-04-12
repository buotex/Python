
import urllib, urllib2, re
from websupport import Websupport

class Mangafox(Websupport):
    
    #DIRECTORY = "http://www.mangafox.com/directory/all/"
    DIRECTORY = "http://www.mangafox.com/search.php?name_method=cw&name=help"

    def syncTitles(self):
        #
        response = urllib2.urlopen(Mangafox.DIRECTORY)
        data = response.read()
        numberpattern = re.search('Prev([<>a-z0-9/=". ])*', data).group(0)
        lastNumber = re.findall('>([0-9]+)<',numberpattern)[-1]

        print "phase 1 finished, " + lastNumber + " pages"
        for i in range(1,int(lastNumber)+1):
            response = urllib2.urlopen(Mangafox.DIRECTORY + str(i) + ".htm")
            data = response.read()
            print "timer"
            data = re.split('Latest Chapter', data,1)[1] 
            print "timer2"
            titles = re.findall('/manga/([^/]+)/v', data)
            titles = {}.fromkeys(titles).keys()
            self.mangaList.append(titles)
            print titles

        #print self.mangaList



test = Mangafox()
