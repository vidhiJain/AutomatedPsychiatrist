import csv
import matplotlib.pyplot as plt
import enchant

enchant.request_dict("en_US")                        # get the dictionary

path_male = 'ANEW/male.csv'
path_female = 'ANEW/female.csv'
male_words = []
male_valence_mean = []
male_valence_std = []
male_arousal_mean = []
male_arousal_std = []
female_words = []
female_valence_mean = []
female_valence_std = []
female_arousal_mean = []
female_arousal_std = []

def create_data():
    """
    Adds all the data from csv files to the respective lists
    """
    global male_words
    with open(path_male) as f:
        mreader = csv.reader(f)
        for row in mreader:
            male_words.append(row[0])
            male_valence_mean.append(float(row[1]))
            male_valence_std.append(float(row[2]))
            male_arousal_mean.append(float(row[3]))
            male_arousal_std.append(float(row[4]))
    global female_words
    with open(path_male) as f:
        freader = csv.reader(f)
        for row in freader:
            female_words.append(row[0])
            female_valence_mean.append(float(row[1]))
            female_valence_std.append(float(row[2]))
            female_arousal_mean.append(float(row[3]))
            female_arousal_std.append(float(row[4]))

def word_list(string):
    """
    Extract indiviuals words from the string s
    """
#Problem1: if word appearing here is not in the same form of verb in the ANEW list
#           eg. 'winning' should be same as 'win'
#Problem2: Need to strip punctuation marks fromt the words
#           eg. 'win!' should be same as 'win'
    words = string.split()
    return words

def correct_list(wordsdic):
    for word in wordsdic:
        if d.check(word):
            pass
        elif not(d.check(word)):
            new=d.suggest(word)
            word=new[0] # if the word is not in dict the first suggestion will be choosen to replace the incorrect word
    return wordsdic



def anew_word_list(sex, speech):
    """
    Returns a list of indices of words in csv file that are in the entered speech.
    """
    all_words = word_list(speech)
    all_words = correct_list(all_words)
    relevant = []
    if sex == 'male':
        for word in all_words:
            if word in male_words:
                relevant.append(male_words.index(word))
        return relevant
    
    elif sex == 'female':
        for word in all_words:
            if word in female_words:
                relevant.append(female_words.index(word))
        return relevant
                
def total_valence(sex,indices_list):
    """
    Returns mean of valence by applying statistic mean of normal distributed data
    """
    num_sum = 0
    den_sum = 0
    if sex == 'male':
        for i in indices_list:
            num_sum = num_sum + (male_valence_mean[i]/male_valence_std[i])
            den_sum = den_sum + (1/male_valence_std[i])
        return (num_sum/den_sum)

    elif sex == 'female':
        for i in indices_list:
            num_sum = num_sum + (female_valence_mean[i]/female_valence_std[i])
            den_sum = den_sum + (1/female_valence_std[i])
        return (num_sum/den_sum)
    
def total_arousal(sex,indices_list):
    """
    Returns mean of arousal by applying statistic mean of normal distributed data
    """
    num_sum = 0
    den_sum = 0
    if sex == 'male':
        for i in indices_list:
            num_sum = num_sum + (male_arousal_mean[i]/male_arousal_std[i])
            den_sum = den_sum + (1/male_arousal_std[i])
        return (num_sum/den_sum)

    elif sex == 'female':
        for i in indices_list:
            num_sum = num_sum + (female_arousal_mean[i]/female_arousal_std[i])
            den_sum = den_sum + (1/female_arousal_std[i])
        return (num_sum/den_sum)

def visualize(valence,arousal):
    plt.figure()
    ax = plt.gca()
    ax.plot([valence-5],[arousal-5], marker='o', color='r')
    ax.set_xlim([-5,5])
    ax.set_ylim([-5,5])
    plt.draw()
    plt.grid()
    plt.show()
    """
    Plot valence, arousal point on a 2D plot with valence as x-axis and arousal as y-axis.
    Require matplotlib for the same. Will update the code for it.
    """


def emotion():
    sex = raw_input("Enter your sex(male/female) : ")
    if sex == 'male' or sex == 'female':
        pass
    else:
        print "please run the code again as sex you entered is not one we researched on "
        return
    speech = raw_input("How are you feeling? ")
    create_data()
    relevant_words = anew_word_list(sex,speech)
    if len(relevant_words) < 1:
        print "The text you entered is not sufficient for your emotion analysis. Please try being more expressive"
        input()
    else:
        valence = total_valence(sex,relevant_words)
        arousal = total_arousal(sex,relevant_words)
        print "valence level is = "+ str(valence-5) +" and arousal level is " + str(arousal-5)
        visualize(valence,arousal)
        input()

if __name__ == "__main__":
    emotion()
