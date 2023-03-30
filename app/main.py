import pandas as pd
import argparse
import matplotlib.pyplot as plt

from model.model import predict_pipeline

if __name__ == '__main__':

    # defining input and output files as parameters to use with docker command
    parser = argparse.ArgumentParser(description='predict on a csv file')
    parser.add_argument('--input', type=str, help='input csv file', required=True)
    parser.add_argument('--output', type=str, help='output json file', required=True)
    parser.add_argument('--graph', type=str, help='distribution graph')
    args = parser.parse_args()

    # read csv file as pandas DataFrame
    data = pd.read_csv(args.input, header=None, on_bad_lines='skip')
    data.columns = ['Feedback']

    predictions = []

    # predict the text as positive or negative using predict_pipeline function from model/model.py/
    for text in data['Feedback']:
        prediction = predict_pipeline(text)[0]['label']
        predictions.append(prediction)

    data['PosOrNeg'] = predictions

    # write predictions to csv file
    data.to_csv(args.output, sep=',', encoding='utf-8-sig', index=False)

    # write predictions to pie chart
    dist = data['PosOrNeg'].value_counts()

    fig = plt.figure(figsize = (5, 5))
    plt.pie(dist, labels=dist.index, autopct='%1.1f%%')
    plt.title("YGA Survey Analysis")

    fig.savefig(args.graph)
      

