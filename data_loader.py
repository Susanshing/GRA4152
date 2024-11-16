
import numpy as np
import pandas as pd
import ssl 
from statsmodels.datasets import get_rdataset
from statsmodels.api import datasets

import argparse


class Dataloader():
    def __init__(self):
        self.data=None
        self.x=None
        self.y=None
    

    @staticmethod   # Use a decorator of staticmethod here.
    def show_menu(): # The show_menu function does not use attributes or methods of any class and any instance.
        print('Please choose the following functions:')
        print('1: Load data.')
        print('2: Add constant:adds a vector of one to the matrix x.')
        print('3: Return varibale x.')
        print('4: Return varibale y.')
        print('5: Return the transpose of x.')


    def run(self):
        while True:      # use infinite loop to implement 'show_menu'function, and list the cooresponding functions.
            self.show_menu()  
            menu_num= int(input('Please insert the function number:'))
            if menu_num==1:
                data_info=input('Pleaser input the info of dataset:')
                self.load_data(data_info)
            elif menu_num==2:
                self.add_constant()
            elif menu_num==3:
                self.return_x()
            elif menu_num==4:
                self.return_y()
            elif menu_num==5:
                self.x_transpose()
            else:
                print('You insert wrong numbers')
                break


    def load_data(self):
        raise NotImplementedError  #subclass will implement later.   



    def add_constant(self):
        print('Adds a vector of one to the matrix x.')
        column_ones=np.ones((self.x.shape[0],1))
        self.x=np.concatenate((column_ones,self.x),axis=1)
        print('Add succssfully')
        
        

    def return_x(self):
        print('Return varibale x.')
        print(self.x)
        


    def return_y(self):
        print('Return varibale y.')
        print(self.y)

        

    def x_transpose(self):
        print('Return the transpose of x.')
        x_T=self.x.transpose()
        print(x_T)
         
    


class SM_loader(Dataloader):
    def __init__(self):
        super().__init__()
        

    def load_data(self,data_info):   # suppose the column 0 is y, and other columns are x.
        try:
            ssl._create_default_https_context = ssl._create_unverified_context
            self.data=sm.datasets.get_rdataset(data_info).data
            self.x=self.data.iloc[:,1:]
            self.y=self.data.iloc[:,0]
            print('Data loads successfully')
            
        except Exception as e:
            print('No such dataset found')
                

class CSV_loader(Dataloader):
    def __init__(self):
        super().__init__()
        

    def load_data(self,data_info):
        try:
            self.data=pd.read_csv(data_info)
            self.x=self.data.iloc[:,1:]
            self.y=self.data.iloc[:,0]
            print('Data loads successfully')
            
        except Exception as e:
            print('No such dataset found')

class URL_loader(Dataloader):
    def __init__(self):
        super().__init__()
        

    def load_data(self,data_info):
        try:
            ssl._create_default_https_context = ssl._create_unverified_context
            self.data=pd.read_csv(data_info)
            self.x=self.data.iloc[:,1:]
            self.y=self.data.iloc[:,0]
            print('Data loads successfully')
            
        except Exception as e:
            print('No such dataset found')
            


def main():
    parser=argparse.ArgumentParser(description="This program is used to load dataset.")
    parser.add_argument('--Dataloader',action='store_true',help='The top class.')
    parser.add_argument('--SM_loader',action='store_true',help='Getting data from statsmodels,and being inherit from Dalaloader.')
    parser.add_argument('--CSV_loader',action='store_true',help='Getting data from local path,and being inherit from Dalaloader.')
    parser.add_argument('--URL_loader',action='store_true',help='Getting data from a url,and being inherit from Dalaloader.')
    
    args=parser.parse_args()

    if args.SM_loader:
        sm=SM_loader()
        #sm.run('sunspots')
        sm.run()
    elif args.CSV_loader:
        csv=CSV_loader()
        #csv.run('/Users/shanxu/Desktop/spector.csv')
        csv.run()
    elif args.URL_loader:
        url=URL_loader()
        #url.run('https://raw.githubusercontent.com/BI-DS/GRA-4152/refs/heads/master/warpbreaks.csv')
        url.run()
    else:
        parser.print_help()        
    

if __name__== '__main__':
    main()    






