
from sklearn.model_selection import train_test_split

def train_test_wrangle(data, target):
    # Train 80% / Test 20%
    train, test = train_test_split(data, train_size=0.8, test_size=0.2, random_state=42)
    # Train 75% / Val 25% (default)
    train, val = train_test_split(train, train_size=0.75, test_size=0.25, random_state=42)

    X_train = train.drop(columns=target)
    y_train = train[target]
    X_val = val.drop(columns=target)
    y_val = val[target]
    X_test = test.drop(columns=target)

    return X_train, y_train, X_val, y_val, X_test


if __name__ == "__main__":
    # only run the code below IF this script is invoked from the command-line
    # not if it is imported from another script
    print("This code should be run convert a dataframe into a train validate and test split")