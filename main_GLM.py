
from GLM import *
import argparse
import pandas as pd

df_normal=pd.read_csv('Duncan.csv')
df_bernoulli=pd.read_csv('spector.csv')
df_poisson=pd.read_csv('warpbreaks.csv')

x_n=df_normal[['education','prestige']].values
y_n=df_normal['income'].values

x_p=df_poisson[['wool','tension']].values
y_p=df_poisson['breaks'].values

x_b=df_bernoulli[['GPA','TUCE','PSI']].values
y_b=df_bernoulli['GRADE'].values



def main():
    parser=argparse.ArgumentParser(description="This program is used to test Generalized Linear Models.")
    parser.add_argument('--GLM',action='store_true',help='The super class.')
    parser.add_argument('--GLM_Normal',action='store_true',help="Normal Distribution class, which inherits from GLM.")
    parser.add_argument('--GLM_Bernoulli',action='store_true',help="Bernoulli Distribution class, which inherits from GLM.")
    parser.add_argument('--GLM_Poisson',action='store_true',help="Poisson Distribution class, which inherits from GLM.")
    args=parser.parse_args()

    if args.GLM_Normal:
        normal=GLM_Normal(x_n,y_n)
        normal.fit(x_n,y_n)
        y_n_predict=normal.predict(x_n)
        print(f'The prediction of Normal Distribution Model is:{y_n_predict}')
        
    elif args.GLM_Bernoulli:
        bernoulli=GLM_Bernoulli(x_b,y_b)
        bernoulli.fit(x_b,y_b)
        y_b_predict=bernoulli.predict(x_b)
        print(f'The prediction of Bernoulli Distribution Model is:{y_b_predict}')
        
    elif args.GLM_Poisson:
        poisson=GLM_Poisson(x_p,y_p)
        poisson.fit(x_p,y_p)
        y_p_predict=poisson.predict(x_p)
        print(f'The prediction of Poisson Distribution Model is:{y_p_predict}')
        
    else:
        parser.print_help()
        
    

if __name__== '__main__':
    main()    
