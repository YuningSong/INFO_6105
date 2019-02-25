import pandas
import numpy


def load_data(filepath):
    """
    :param filepath:
    :return: A numpy matrix of words appear numbers which jobs contain 'fintech' keyword
    """
    data_frame = pandas.read_csv(filepath)
    rows = len(data_frame)

    vector_set = []
    for i in range(rows):
        vector = []
        if data_frame.loc[i][35] != 0:  # select jobs have 'fintech' keyword
            for j in range(100):
                vector.append(data_frame.loc[i][j+4])
            vector_set.append(vector)
    print(len(vector_set))
    return numpy.mat(vector_set)


word_vector_set = load_data('../Part1/top_100_key_words_with_jobs.csv')
numpy.savetxt('csv/job_words_with_fintech.csv', word_vector_set, delimiter=',')
