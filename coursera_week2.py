medal_count = {"United States":70,"Great Britain":38,"China":45,"Russia":30,"Germany":17}
for key in medal_count.values():
    print(key)



swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4}
swimmers["Phelps"]=23
print(swimmers)

sports_periods = {'baseball': 9, 'basketball': 4, 'soccer': 4, 'cricket': 2}
sports_periods['hockey']=3
print(sports_periods)

golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27, "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}
# golds['Spain'] = golds.get('Spain')+2
# print(golds)
lst =list(golds.keys())
print(lst)

medal_count2 = {'United States': 70, 'Great Britain':38, 'China':45, 'Russia':30, 'Germany':17, 'Italy':22, 'France': 22, 'Japan':26, 'Australia':22, 'South Korea':14, 'Hungary':12, 'Netherlands':10, 'Spain':5, 'New Zealand':8, 'Canada':13, 'Kazakhstan':8, 'Colombia':4, 'Switzerland':5, 'Belgium':4, 'Thailand':4, 'Croatia':3, 'Iran':3, 'Jamaica':3, 'South Africa':7, 'Sweden':6, 'Denmark':7, 'North Korea':6, 'Kenya':4, 'Brazil':7, 'Belarus':4, 'Cuba':5, 'Poland':4, 'Romania':4, 'Slovenia':3, 'Argentina':2, 'Bahrain':2, 'Slovakia':2, 'Vietnam':2, 'Czech Republic':6, 'Uzbekistan':5}
for key in medal_count2.keys():
    if key =='Belarus':
        belarus = medal_count2[key]
print(belarus)

st = "its a new file of fifo that is being study under an observation"
disc = {}
for c in st:
    if c not in disc:
        disc[c]=0
        disc[c]=disc[c]+1
print(disc)
keys = list(disc.keys())
print(keys)
min_val = keys[0]
for i in keys:
    if i<min_val:
        print(i)


medal_count2 = {'...COUNTRY...':'..MEDALS..','United States': 70, 'Great Britain':38, 'China':45, 'Russia':30, 'Germany':17, 'Italy':22, 'France': 22, 'Japan':26, 'Australia':22, 'South Korea':14, 'Hungary':12, 'Netherlands':10, 'Spain':5, 'New Zealand':8, 'Canada':13, 'Kazakhstan':8, 'Colombia':4, 'Switzerland':5, 'Belgium':4, 'Thailand':4, 'Croatia':3, 'Iran':3, 'Jamaica':3, 'South Africa':7, 'Sweden':6, 'Denmark':7, 'North Korea':6, 'Kenya':4, 'Brazil':7, 'Belarus':4, 'Cuba':5, 'Poland':4, 'Romania':4, 'Slovenia':3, 'Argentina':2, 'Bahrain':2, 'Slovakia':2, 'Vietnam':2, 'Czech Republic':6, 'Uzbekistan':5}
for key , value in medal_count2.items():
    print(key,value)


Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
credits=0
for valu in Junior.values():
    credits+= valu
print(credits)

str1 = "peter piper picked a peck of pickled peppers"
freq ={}
for word in str1:
    freq[word]=freq.get(word,0)+1
    # if word not in freq:
    #     freq[word]=0
    # freq[word]=freq[word]+1
print(freq)

str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
lst =str1.split()
print(lst)
freq_words = {}
for word in lst:
    freq_words[word]=freq_words.get(word,0)+1
print(freq_words)


sally = "sally sells sea shells by the sea shore"
characters = {}
for c in sally:
    characters[c]=characters.get(c,0)+1
# print(characters)
keyy = list(characters.keys())
# print(keyy)
best_char = keyy[0]
for key in keyy:
    if characters[key]>characters[best_char]:
        best_char= key
print(best_char)

string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
string2=string1.lower()
print(string2)
letter_count={}
for c in string2:
    letter_count[c]=letter_count.get(c,0)+1
print(letter_count)


def sublist(lst):
    sub = []
    item = 0
    while item<4:
        sub.append(lst[item])
        item = item+1
    return sub
print(sublist([12,46,29,39,11,10,]))  



def check_nums(sub):
    lst= []
    n=0
    while sub[n] != 7:
        lst.append(sub[n])
        n=n+1 
    return lst     
print(check_nums([11,23,53,64,75,76,7,8,9,0]))


def f(a,l=[]):
    l.append(a)
    return l
print(f(2))
print(f(7))
print(f(5))
print(f(2,["hello"]))
print(f(5,["ello"]))

        