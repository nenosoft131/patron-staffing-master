import os
import csv

from model.model import DataModel
from collections import Counter

PATH = '/Users/muhammad/Desktop/test_Case/Test/logins.csv'
users = []

def update_model(data: str):
   model = DataModel(timestamp=data['timestamp'],account_id= data['account_id'], ipv4_address= data['ipv4_address'], success= data['success'])
   users.append(model)
   

def read_csv(filepath:str)->None:
    with open(filepath,"r") as file:
        reader = csv.DictReader(file)
        for da in reader:
            update_model(da)

def main():
    read_csv(PATH)
    l = [user.account_id for user in users if user.success=='False']
    
    counter = Counter(l)
    c = counter.most_common(2)
    for i, j in c:
        print(i,j)



if __name__ == "__main__":
    main()