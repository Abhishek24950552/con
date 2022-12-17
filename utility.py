import pickle
import json
import config
import numpy as np

class ConStrength():

    def __init__(self,user_data):
        self.model_path=config.model_path
        self.user_data=user_data
        
    
    def load_saved_data(self):
        with open(self.model_path,'rb') as f:
            self.model=pickle.load(f)

        with open(config.proj_data_path,'r') as f:
            self.project_data=json.load(f)

    def predict_strength(self):
        self.load_saved_data()

        Cement=self.user_data['Cement']
        Blast_Furnace_Slag=self.user_data['Blast_Furnace_Slag']
        Fly_Ash	= self.user_data['Fly_Ash']
        Water=self.user_data['Water']
        Superplasticizer=self.user_data['Superplasticizer']
        Coarse_Aggregate=self.user_data['Coarse_Aggregate']
        Fine_Aggregate=self.user_data['Fine_Aggregate']
        Age=self.user_data['Age']

        cnt= len(self.project_data['columns'])
        test = np.zeros(cnt)
        test[0] = Cement
        test[1] = Blast_Furnace_Slag
        test[2] = Fly_Ash
        test[3] = Water
        test[4] = Superplasticizer
        test[5] = Coarse_Aggregate
        test[6] = Fine_Aggregate
        test[7] = Age

        pre_strength= np.around(self.model.predict([test])[0],3)
        print('precicted strength is :',pre_strength)
        return pre_strength
    
if __name__=='__main__':
    strength=ConStrength()
    strength