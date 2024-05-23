import pickle
import argparse

if __name__ == '__main__':
    # Define the command line arguments
    parser = argparse.ArgumentParser(description='Model Prediction')
    parser.add_argument('--age', type=int, help='Age of the person')
    parser.add_argument('--sex', type=str, choices=['M', 'F'], help='Sex of the person, F for female and M for male')
    parser.add_argument('--height', type=float, help='Height of the person (in cm)')

    # Parse the command line arguments
    args = parser.parse_args()

    # Access the input values
    age = args.age
    sex = args.sex
    sex = 0 if sex == 'F' else 1
    height = args.height

    # Load the chosen model
    with open('svm.pickle', 'rb') as file:
        loaded_model = pickle.load(file)

    # Perform prediction using the loaded model
    prediction = loaded_model.predict([[age, height, sex]])

    # Print the prediction
    print('Prediction:', round(prediction[0]/7, 3))

def predict_model(age, height, sex):
    sex = 0 if sex == 'F' else 1
    # Load the chosen model
    with open('svm.pickle', 'rb') as file:
        loaded_model = pickle.load(file)

    # Perform prediction using the loaded model
    prediction = loaded_model.predict([[age, height, sex]])

    # Print the prediction
    return round(prediction[0]/7, 3)
