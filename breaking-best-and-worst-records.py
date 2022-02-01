l  = '10 5 20 20 4 5 2 25 1'
scores =list( map(int, l.split()))
def Result (scores):
    max_score_beaten = 0
    min_score_beaten = 0
    max_value = scores[0]
    min_value = scores[0]
    for i in scores:
        if i < min_value:
            min_score_beaten += 1
            min_value = i
        if i> max_value:
            max_score_beaten +=1
            max_value =i
    return[max_score_beaten, min_score_beaten]

x = Result(scores)
print(x)