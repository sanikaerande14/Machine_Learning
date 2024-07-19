import pickle
import json
import numpy as np
import config

class Medical_Insurance():
    def __init__(self,age,gender,bmi,children,smoker,region):
        self.age=age
        self.gender=gender.lower()
        self.bmi=bmi
        self.children=children
        self.smoker=smoker.lower()
        self.region="region_"+region

    def load_model(self):
        #we are reading the model and json file
        with open(config.MODEL_FILE_PATH,"rb") as file:
            self.model=pickle.load(file)

        with open(config.JOSN_FILE_PATH,"r") as file:
            self.json_data=json.load(file)

    def get_predicted_charges(self):
        self.load_model() #calling above method
        test_array=np.zeros(len(self.json_data["columns"]))
        test_array[0]=self.age
        test_array[1]=self.json_data["gender"][self.gender]
        test_array[2]=self.bmi
        test_array[3]=self.children
        test_array[4]=self.json_data["smoker"][self.smoker]
        region_index=self.json_data["columns"].index(self.region)
        test_array[region_index]=1

        predict_charges=self.model.predict([test_array])
        return predict_charges