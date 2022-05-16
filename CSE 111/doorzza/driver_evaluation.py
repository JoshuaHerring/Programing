import os

def main():
    choice = ''
    while choice.lower() != 'end':
        choice = input('What would you like to do? "drivers", "add", "delete", "file", "grade". Type end to finish. ')
        if choice.lower() == 'add':
            driver = input('What is the name of the driver you would like to add? ').capitalize()
            add_new_driver(driver)
        elif choice.lower() == 'delete':
            driver = input('Which driver would you like to delete? ').capitalize()
            delete_driver(driver)
        elif choice.lower() == 'file':
            driver = input('Which driver would you like to make a file for? ').capitalize()
            complaint = input(f'What would you like to file to {driver}\'s record ')
            score = input('On a scale of 1 being bad to 10 being good how would you grade this file? ')
            file_complaint(driver, complaint, score)
        elif choice.lower() == 'grade':
            driver = input('Which driver would you like to grade? ').capitalize()
            pull_drivers_grade(driver)
        elif choice.lower() == 'drivers':
            pull_list_of_drivers()
        else:
            if choice.lower() != 'end':
                print(f'"{choice.capitalize()}" was invalid. Please try again and double check your spelling.')



def add_new_driver(driver):
    open(f'doorzza/{driver}.csv', 'x')

def delete_driver(driver):
    os.remove(f'doorzza/{driver}.csv') 

def file_complaint(driver, complaint, score):
    with open (f'doorzza/{driver}.csv','a') as fileing:
        fileing.write(f'{complaint}, {score}\n')

def pull_drivers_grade(driver):
    with open (f'doorzza/{driver}.csv','r') as grading:
        list = []
        for line in grading:
            clean_line = line.strip()
            split_line = clean_line.split(',')
            list.append(split_line)
        list_of_scores = []
        for x in list:
            pre_score = x[1]
            float_pre_score = float(pre_score)
            list_of_scores.append(float_pre_score)
        print(list_of_scores)
        score = (sum(list_of_scores)/len(list_of_scores))
        grading.close()
    print(score)
def pull_list_of_drivers():
    directory = 'doorzza'
    for filename in os.listdir(directory):
        stripped_fileneame = filename.strip('.csv')
        print(stripped_fileneame)




if __name__ == '__main__':
    main()