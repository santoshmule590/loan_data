import numpy as np
import pandas as pd
import pickle
import json
import config

class LoanData():
    def __init__(self,credit_policy,purpose,int_rate,installment,log_annual_inc,dti,fico,days_with_cr_line,revol_bal,revol_util,inq_last_6mths,delinq_2yrs,pub_rec):
        self.credit_policy =credit_policy
        self.purpose = purpose
        self.int_rate = int_rate
        self.installment = installment
        self.log_annual_inc = log_annual_inc
        self.dti = dti
        self.fico = fico
        self.days_with_cr_line = days_with_cr_line
        self.revol_bal = revol_bal
        self.revol_util = revol_util
        self.inq_last_6mths =inq_last_6mths
        self.delinq_2yrs = delinq_2yrs
        self.pub_rec = pub_rec

    def load_model(self):
        
        with open (config.JSON_FILE_PATH,"r") as f:
            self.json_dict = json.load(f)
        with open (config.MODEL_FILE_PATH,"rb") as f:
            self.model = pickle.load(f)



        # with open (r"C:\Users\ADMIN\Desktop\Classification Algorithm\37_Santosh_Mule_Logistic_loan_data\Model\Loan_data.json","r") as f:
        #     self.json_dict=json.load(f)
        
        # with open (r"C:\Users\ADMIN\Desktop\Classification Algorithm\37_Santosh_Mule_Logistic_loan_data\Model\Loan_data.pkl","rb") as f:
        #     self.model=pickle.load(f)

    def get_loan_classification(self):
        self.load_model()

        array = np.zeros(len(self.json_dict["column"]))

        array[0] = self.credit_policy
        array[1] = self.json_dict['purpose'][self.purpose]
        array[2] = self.int_rate
        array[3] = self.installment
        array[4] = self.log_annual_inc
        array[5] = self.dti
        array[6] = self.fico
        array[7] = self.days_with_cr_line
        array[8] = self.revol_bal
        array[9] = self.revol_util
        array[10] = self.inq_last_6mths
        array[11] = self.delinq_2yrs
        array[12] = self.pub_rec

        print("Array ::\n",array)


        result = self.model.predict([array])[0]
        result1 = "Congratulations !!!, You are eligible to get Loan from our Organisation." if result == 1 else "Sorry , We are unble to proceed with your Request.. Please try again next time"

        return result1

if __name__ == "__main__":
    credit_policy = 1.000000
    purpose = "credit_card"
    int_rate = 0.093300
    installment = 87.880000
    log_annual_inc = 11.626254
    dti = 13.460000
    fico = 702.000000
    days_with_cr_line= 6120.000000
    revol_bal = 27786.000000
    revol_util = 85.500000
    inq_last_6mths = 2.000000
    delinq_2yrs = 0.000000
    pub_rec = 1.000000
   
    Obj = LoanData(credit_policy,purpose,int_rate,installment,log_annual_inc,dti,fico,days_with_cr_line,revol_bal,revol_util,inq_last_6mths,delinq_2yrs,pub_rec)
    result= Obj.get_loan_classification()
    print(result)

    
        

