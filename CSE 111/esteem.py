def main():
    inform()
    answers = recieve_answers()
    points = score(answers)

    conclusion = (f'Your socre is {points}.\n\
        A score below 15 may indicate a problematic low self-esteem.')
    print(conclusion)

def inform():
    information = ('''This program is an implementation of the Rosenberg
Self-Esteem Scale. This program will show you ten
statements that you could possibly apply to yourself.
Please rate how much you agree with each of the
statements by responding with one of these four letters:

D means you strongly disagree with the statement.
d means you disagree with the statement.
a means you agree with the statement.
A means you strongly agree with the statement.''')
    print(information)

def recieve_answers():
    '''Recieves input from the user and outputs a list of answers called 'answers' '''
    question_1  = input('I feel that I am a person of worth, at least on an equal plane with others.')
    question_2  = input('I feel that I have a number of good qualities.')
    question_3  = input('All in all, I am inclined to feel that I am a failure.')
    question_4  = input('I am able to do things as well as most other people.')
    question_5  = input('I feel I do not have much to be proud of.')
    question_6  = input('I take a positive attitude toward myself.')
    question_7  = input('On the whole, I am satisfied with myself.')
    question_8  = input('I wish I could have more respect for myself.')
    question_9  = input('I certainly feel useless at times.')
    question_10 = input('At times I think I am no good at all.')
    answers = [question_1, question_2, question_4, question_6, question_7, question_3, question_5, question_8, question_9, question_10]
    return answers

def score(answers):
    '''recieves a list of answers and sepeerates the first half of the list as positive and the
    second half of the list as negative. Then it computes a score based on letter value
    from 0 to 3 depending on positive or negative asociation.
    
    returns 'score' '''
    length = len(answers)
    middle_seperation = length //2
    pos_answers = answers[:middle_seperation]
    neg_answers = answers[middle_seperation:]
    score = 0
    for x in pos_answers:
        if x == 'D':
            score += 0
        if x == 'd':
            score += 1
        if x == 'a':
            score += 2
        if x == 'A':
            score += 3
    for x in neg_answers:
        if x == 'D':
            score += 3
        if x == 'd':
            score += 2
        if x == 'a':
            score += 1
        if x == 'A':
            score += 0
    return score

if __name__ == "__main__":
    main()