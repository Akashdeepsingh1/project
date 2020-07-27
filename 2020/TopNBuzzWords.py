'''
You work on a team whose job is to understand the most sought after toys for the holiday season. A teammate of yours has built a webcrawler that extracts a list of quotes about toys from different articles. You need to take these quotes and identify which toys are mentioned most frequently. Write an algorithm that identifies the top N toys out of a list of quotes and list of toys.

Your algorithm should output the top N toys mentioned most frequently in the quotes.

Input:
The input to the function/method consists of five arguments:

numToys, an integer representing the number of toys
topToys, an integer representing the number of top toys your algorithm needs to return;
toys, a list of strings representing the toys,
numQuotes, an integer representing the number of quotes about toys;
quotes, a list of strings that consists of space-sperated words representing articles about toys

Output:
Return a list of strings of the most popular N toys in order of most to least frequently mentioned

Note:
The comparison of strings is case-insensitive. If the value of topToys is more than the number of toys, return the names of only the toys mentioned in the quotes. If toys are mentioned an equal number of times in quotes, sort alphabetically.

Example 1:

Input:
numToys = 6
topToys = 2
toys = ["elmo", "elsa", "legos", "drone", "tablet", "warcraft"]
numQuotes = 6
quotes = [
"Elmo is the hottest of the season! Elmo will be on every kid's wishlist!",
"The new Elmo dolls are super high quality",
"Expect the Elsa dolls to be very popular this year, Elsa!",
"Elsa and Elmo are the toys I'll be buying for my kids, Elsa is good",
"For parents of older kids, look into buying them a drone",
"Warcraft is slowly rising in popularity ahead of the holiday season"
];

Output:
["elmo", "elsa"]


'''



def solution(quotes, numToys,topToys, toys):
    from collections import defaultdict
    from heapq import heapify,heappush,nlargest
    import re
    working_dic = defaultdict(int)
    for line in quotes:
        temp = re.sub(r'''[,!.;'"]+'''," ",line).lower().split()
        for word in temp:
            if str(word) in toys:
                working_dic[word]+=1

    import operator
    sorted_d = sorted (working_dic.items (), key=operator.itemgetter (1))

    working_list = []
    heapify(working_list)

    for k,v in working_dic.items():
        heappush(working_list,(v,k))
        print('{}  {}'.format(k,v))
    t =  nlargest(topToys,working_list)
    final_list = []
    for each in t:
        final_list.append(each[1])
    return final_list

numToys = 6
topToys = 2
toys = ["elmo", "elsa", "legos", "drone", "tablet", "warcraft"]
numQuotes = 6
quotes = [
"Elmo is the hottest of the season! Elmo will be on every kid's wishlist!",
"The new Elmo dolls are super high quality",
"Expect the Elsa dolls to be very popular this year, Elsa!",
"Elsa and Elmo are the toys I'll be buying for my kids, Elsa is good",
"For parents of older kids, look into buying them a drone",
"Warcraft is slowly rising in popularity ahead of the holiday season"
]
print (solution (quotes, numToys, topToys, toys))