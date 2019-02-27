import pandas
import numpy


def load_data(filepath):
    """
    :param filepath:
    :return: A numpy matrix of words appear numbers
    """
    data_frame = pandas.read_csv(filepath, encoding='ISO-8859-1')
    rows = len(data_frame)

    vector_set = []
    for i in range(rows):
        vector = data_frame.iloc[i:i+1, 4:]
        vector = numpy.array(vector).tolist()[0]
        vector_set.append(vector)
    print(len(vector_set))
    return numpy.mat(vector_set)


word_vector_set = load_data('../Part1/top_100_key_words_with_jobs.csv')
numpy.savetxt('csv/job_words.csv', word_vector_set, delimiter=',')
