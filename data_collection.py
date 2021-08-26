import requests_with_caching
import json
def get_movies_from_tastedive(w):
    d={'q':w,'type':'movies','limit':5}
    page=requests_with_caching.get("https://tastedive.com/api/similar",params=d)
    return page.json()

def extract_movie_titles(m):
    l=[]
    sim=m['Similar']['Results']
    for i in sim:
        j=i['Name']
        l.append(j)
    return l

def get_related_titles(movies):
    li_mo=[]
    for m in movies:
        dic=get_movies_from_tastedive(m)
        #print(dic)
        re_mo=extract_movie_titles(dic)
        #print(re_mo)
        for i in re_mo:
            if i not in li_mo:
                li_mo.append(i)
    return (li_mo)







def get_movie_data(w):
    d={'t':w,'r':'json'}
    page=requests_with_caching.get("http://www.omdbapi.com/",params=d)
    return page.json()

def get_movie_rating(dic):
    if 'Ratings' in dic.keys():
        rt=dic['Ratings']
        for i in rt:
            if i['Source'] is 'Rotten Tomatoes':
                rating=i['Value'].replace('%','')
                return int(rating)
    else:
        return 0
#rate=get_movie_rating(dic)
#print(rate)

def get_sorted_recommendations(li_mo):
    emp_dic={}
    for m in li_mo:
        d_m=get_movie_data(m)
        print(d_m)
        emp_dic[m]=get_movie_rating(d_m)
    print(emp_dic)
    sort_li=sorted(emp_dic,key=lambda k:(emp_dic[k],k),reverse=True)
    return sort_li
ti=get_related_titles(["Bridesmaids", "Sherlock Holmes"])
print(ti)
so=get_sorted_recommendations(ti)
print(so)
