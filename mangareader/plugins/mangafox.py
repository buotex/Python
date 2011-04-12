
import urllib, urllib2, re
from websupport import Websupport

class Mangafox(Websupport):
    
    ALLDIRECTORY = "http://www.mangafox.com/directory/all/"
    QUERY = "http://www.mangafox.com/search.php?name_method=bw&name="
    MANGA = "http://www.mangafox.com/manga/"

    def lookFor(self, name):
        #
        name = re.sub(r'\s', '+', name)
        response = urllib2.urlopen(Mangafox.QUERY + name)
        data = response.read()
        numberpattern = re.search('Prev([^A-Z])*', data).group(0)
        lastNumber = re.findall('>([0-9]+)<',numberpattern)[-1]
        mangaList = []
        for i in range(1,int(lastNumber)+1):
            response = urllib2.urlopen(Mangafox.QUERY + name + "&page=" + str(i))
            data = response.read()
            data = re.split('Latest Chapter', data,1)[1] 
            titles = re.findall('/manga/([^/]+)/[vc]', data)
            mangaList.extend(titles)
        return mangaList

    def indexChapters(self, name):
        response = urllib2.urlopen(Mangafox.MANGA + name)
        data = response.read()
        data = re.split('Date Added', data,1)[1]
        chapterLinks = [re.sub('[^/]+$','',url) for url in re.findall('/manga/([^"]+)', data)]
        return chapterLinks

    def extractImages(self, chapter):
        response = urllib2.urlopen(Mangafox.MANGA + chapter)
        data = response.read()
        data = re.split('Pages', data,1)[1]
        pageLinks = re.findall('>([0-9]+)<', data)
        imgLinks = []
        for num in pageLinks:
            pageUrl = chapter + num + ".html"
            print chapter
            print num
            response = urllib2.urlopen(Mangafox.MANGA + pageUrl)
            print Mangafox.MANGA + pageUrl
            data = response.read()
            imgLinks.append(re.search('(http://[^/]+/store/manga/[^\"]*)', data).group(0))
        return imgLinks    
       

#test = Mangafox()
#print test.lookFor("kimi")
#print test.indexChapters("the_world_god_only_knows")
#print test.extractImages("http://www.mangafox.com/manga/the_world_god_only_knows/v14/c134/")

test = Mangafox()
test.downloadFiles(
    test.extractImages(
        test.indexChapters(
            test.lookFor('The World God Only')[0]
        )[0]
    )
,   "KamiNomi/"
)
