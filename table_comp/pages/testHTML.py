from bs4 import BeautifulSoup as bs
#import Parsing
import re
import sys
import importlib
importlib.reload(sys)
import locale

def createTable(input):
    for captain in input:
        print(input)
    t=0;
    #Добавление шапки таблицы
    replyPage=bs(open('result.html', encoding='utf-8'),'html.parser')
    for tg in replyPage.find_all('table'):
        newCaption=replyPage.new_tag('caption')
        newCaption.string=('ТАБЛИЦА КОМПОНЕНТОВ')
        tg.append(newCaption)
        newHander=replyPage.new_tag('tr')
        tg.append(newHander)
        for tr in replyPage.find_all('tr'):
            newHanderName=replyPage.new_tag('th')
            newHanderName.string=('ТИП')
            tr.append(newHanderName)
            newHanderName = replyPage.new_tag('th')
            newHanderName.string = ('НАИМЕНОВАНИЕ')
            tr.append(newHanderName)
            newHanderName = replyPage.new_tag('th')
            newHanderName.string = ('КОРПУС')
            tr.append(newHanderName)
            newHanderName = replyPage.new_tag('th\n')
            newHanderName.string = ('КОЛИЧЕСТВО')
            tr.append(newHanderName)

        while t<10:
            inputData = replyPage.new_tag('tr')
            inputData.insert(2, replyPage.new_tag('inputData'+str(t)))
            tg.append(inputData)
            for tg in replyPage.find_all('inputData'+str(t)):
                newData=replyPage.new_tag('td')
                newData.string='100'
                tg.append(newData)
                newData = replyPage.new_tag('td')
                newData.string = '100'
                tg.append(newData)
                newData = replyPage.new_tag('td')
                newData.string = '100'
                tg.append(newData)
                newData = replyPage.new_tag('td')
                newData.string = '100'
                tg.append(newData)
            t+=1


        # for data in replyPage.find_all('tr'):
        #     newRow=replyPage.new_tag('td')
        #     newRow.string='3000'
        #     data.append(newRow)
    replyPage.prettify(formatter="html")
    f = open('reply.html', 'w', encoding='utf-8')
    f.write(str(replyPage))
    f.close()







