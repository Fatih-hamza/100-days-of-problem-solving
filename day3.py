# Day 3
# today's problem is the following: https://www.hackerrank.com/challenges/acm-icpc-team/problem?isFullScreen=true
# we have a list of binary strings, we should find the combinations of two strings that maximizes the number of 1s in the result of the bitwise or operator on them

# first of all, we're in the necessity to compare every couple of combinations, the best we can have is an O(n^2) time complexity
# the solution of today's problem is pretty straight forward

def combination(string1, string2):
    result = ""
    for i in range(len(string1)):
        if string1[i] == "1" or string2[i] == "1":
            result = result + "1"
        else:
            result = result + "0"
    return result

def acmTeam(topic):
    max_of_topics = 0
    number_of_teams = 0
    for i in range(len(topic)):
        for j in range(i+1, len(topic)):
            number_of_topics = combination(topic[i], topic[j]).count("1")
            
            if number_of_topics > max_of_topics:
                max_of_topics = number_of_topics
                number_of_teams = 1
            elif number_of_topics == max_of_topics:
                number_of_teams += 1
                
    return [max_of_topics, number_of_teams]

