from bs4 import BeautifulSoup as bs
import Parsing



def createTable(input):
    Req=list();
    t = 0;
    for captain in input:
        Req.append(captain.split('+'))
    #Добавление шапки таблицы
    replyPage=bs(open('templates/result.html', encoding='utf-8'),'html.parser')
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
            newHanderName = replyPage.new_tag('th')
            newHanderName.string = ('КОЛИЧЕСТВО')
            tr.append(newHanderName)
            newHanderName = replyPage.new_tag('th\n')
            newHanderName.string = ('Действия')
            tr.append(newHanderName)

        while t<len(Req):
            inputData = replyPage.new_tag('tr')
            inputData.insert(2, replyPage.new_tag('inputData'+str(t)))
            tg.append(inputData)
            for tg in replyPage.find_all('inputData'+str(t)):
                newData=replyPage.new_tag('td')
                newData.string=str(Req[t][1])
                tg.append(newData)
                newData = replyPage.new_tag('td')
                newData.string = str(Req[t][2])
                tg.append(newData)
                newData = replyPage.new_tag('td')
                newData.string = str(Req[t][3])
                tg.append(newData)
                newData = replyPage.new_tag('td')
                newData.string = str(Req[t][4])
                tg.append(newData)
                newData = replyPage.new_tag('td\n')
                newBot = replyPage.new_tag('button')
                newBot.string = 'Внести'
                newData.insert(2, newBot)
                newBot = replyPage.new_tag('button')
                newBot.string = 'Списать'
                newData.insert(2, newBot)
                tg.append(newData)
            t+=1


        # for data in replyPage.find_all('tr'):
        #     newRow=replyPage.new_tag('td')
        #     newRow.string='3000'
        #     data.append(newRow)
    replyPage.prettify(formatter="html")
    f = open('templates/reply.html', 'w', encoding='utf-8')
    f.write(str(replyPage))
    f.close()
    return

