from encodings import utf_8

txtfile1 = open("C:/Users/No Name/OneDrive/Desktop/Stylometry Project/Ljotic.txt", "r", encoding="utf_8")
Ljotic = txtfile1.read()
txtfile2 = open("C:/Users/No Name/OneDrive/Desktop/Stylometry Project/Nedic.txt", "r", encoding="utf_8")
Nedic = txtfile2.read()
txtfile3 = open("C:/Users/No Name/OneDrive/Desktop/Stylometry Project/Unknown.txt", "r", encoding="utf_8")
Unknown = txtfile3.read()



import nltk 

lower_case_Ljotic = Ljotic.lower()
lower_case_Nedic = Nedic.lower()
lower_case_Disputed = Unknown.lower()


lower_case_tokenized_Ljotic = nltk.word_tokenize(lower_case_Ljotic)
lower_case_tokenized_Nedic = nltk.word_tokenize(lower_case_Nedic)
lower_case_tokenized_Disputed = nltk.word_tokenize(lower_case_Disputed)


joint_corpus = (lower_case_tokenized_Ljotic + lower_case_tokenized_Nedic + lower_case_tokenized_Disputed)


frequent_words_list = nltk.FreqDist(joint_corpus)
most_common_words_joint = list(frequent_words_list.most_common(500))


#print(most_common_words_joint)

proportion_by_author = (len(lower_case_tokenized_Ljotic) / len(joint_corpus))

proportion_by_author_second_case = (len(lower_case_tokenized_Nedic) / len(joint_corpus))

chisquared = 0
chisquared2 = 0

for word,joint_count in most_common_words_joint:

    author_count = lower_case_tokenized_Ljotic.count(word)
    unknown_count = lower_case_tokenized_Disputed.count(word)


    expected_author_count = joint_count * proportion_by_author
    expected_unknown_count = joint_count * (1-proportion_by_author)

    chisquared += ((author_count - expected_author_count) * (author_count - expected_author_count) / expected_author_count)

    chisquared += ((unknown_count - expected_unknown_count) * (unknown_count - expected_unknown_count) / expected_unknown_count)

for words, second_joint_count in most_common_words_joint:
    author_second_count = lower_case_tokenized_Nedic.count(words)
    unknown_second_count = lower_case_tokenized_Disputed.count(words)

    expected_second_author_count = second_joint_count * proportion_by_author_second_case
    expected_second_unknown_count = second_joint_count * (1-proportion_by_author_second_case)

    chisquared2 += ((author_second_count - expected_second_author_count) * (unknown_second_count - expected_second_author_count) / expected_second_author_count)

    chisquared2 += ((unknown_second_count - expected_second_unknown_count) * (unknown_second_count - expected_second_unknown_count) / expected_second_unknown_count)




print('The expected Chi-squared statistic for candidate Ljotic is', chisquared, )
print('The expected Chi-squared statistic for candidate Nedic is', chisquared2, )

if chisquared < chisquared2:
    print("The author of the text is most likely Ljotic")
else:
    print('The author of the text is most likely Nedic')

