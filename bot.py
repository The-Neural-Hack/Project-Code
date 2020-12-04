from bs4 import BeautifulSoup
import requests

base_url = "http://questions.menstrupedia.com"

def make_query():
    user_query = input ("What do you want to know regarding menstrutation: ")
    query = user_query.split(" ")
    query = "+".join(query)
    return query

def fetch_questions(query):
    url = base_url + "/search/?q="+query+"&Submit=search&t=question"
    page  = requests.get(url)
    data = BeautifulSoup(page.content, "html.parser")
    ques = data.findAll(class_="question-summary-wrapper")

    c=0
    url_list = []
    if len(ques) == 0:
        print ("No questions found")
    for i in ques:
        if c == 5:
            break
        c+=1
        Q = i.find("h2").get_text()
        print(str(c)+". "+ Q)
        h = i.find("a")
        print(h["title"]+"\n")
        ans_url = (base_url + h["href"]+"\n")
        url_list.append(ans_url)
        print("\n$$$*****************************************************************************$$$\n")
    return url_list

def fetch_answer(url_list):
    user_ans = int(input("How many answers you would like to have (max=5): "))
    ans_page = requests.get(url_list[user_ans-1])
    ans_data = BeautifulSoup(ans_page.content, "html.parser")
    ans = ans_data.findAll(class_="answer-body")

    if len(ans) == 0:
        print ("No Answer found")

    number_of_answers = 0
    for i in ans:
        if (number_of_answers==5):
            break
        number_of_answers += 1
        A = i.find("p").get_text()
        print (str(number_of_answers)+ ". " + A + "\n")
        print ("\n$$$----------------------Others also answered-----------------------------------------$$$\n")


query = make_query()
question_urls = fetch_questions(query)
if len(question_urls) > 0:
    fetch_answer(question_urls)
