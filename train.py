import argparse
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--n_estimators', type=int, default=-1)
    parser.add_argument("--train", type=str, default=os.environ.get("SM_CHANNEL_TRAIN"))
    parser.add_argument("--model_dir", type=str, default=os.environ.get("SM_MODEL_DIR"))
    args = parser.parse_args()
    print(f"Training data directory: {args.train}")
    print(f"Training data directory: {args.n_estimators}")
    print(f"Training data directory: {args.model_dir}")
 
    #Take the set of files and read them all into a single pandas dataframe
    input_files = [ os.path.join(args.train, file) for file in os.listdir(args.train) ]
    if len(input_files) == 0:
        raise ValueError(('There are no files in {}.\n' +
                          'This usually indicates that the channel ({}) was incorrectly specified,\n' +
                          'the data specification in S3 was incorrectly specified or the role specified\n' +
                          'does not have permission to access the data.').format(args.train, "train"))
    raw_data = [ pd.read_csv(file, header=None, engine="python", skiprows=1) for file in input_files ]
    train_data = pd.concat(raw_data)
    

    #labels are in the first column
    train_y = train_data.iloc[:, 4]
    train_x = train_data.iloc[:, :-1]
    print(train_x)
    print(train_y)

    #Train model
    n_estimators = args.n_estimators
    model = RandomForestClassifier(n_estimators=20)
    model.fit(train_x, train_y)

    #Print the coefficients of the trained classifier, and save the coefficients
    joblib.dump(model, os.path.join(args.model_dir, "model.joblib"))

def model_fn(model_dir):
    """Deserialized and return fitted model

    Note that this should have the same name as the serialized model in the main method
    """
    model = joblib.load(os.path.join(model_dir, "model.joblib"))
    return model