import numpy as np
from scipy.optimize import minimize
from scipy.stats import norm,bernoulli,poisson



class GLM():
    def __init__(self,x,y): 
        column_ones=np.ones((x.shape[0],1))
        self.x=np.concatenate((column_ones,x),axis=1) #add one column in matrix x
        self.y=y
        

    def mle(self,beta,x,y):  #mle is maximum likelihood estimator funcntion
        raise NotImplementedError     #use abstract method,let subclass will specify it later.



    def fit(self,x,y):
        init_beta=np.repeat(0.1,self.x.shape[1])
        mini=minimize(self.mle,init_beta,args=(self.x,self.y))
        self.beta=mini.x
        print(f'Estimated beta are:{self.beta}')
          

    def predict(self,x):    # according to different link funtion, it is implemented in subclass.
        raise NotImplementedError



class GLM_Normal(GLM):
    def __init__(self,x,y):
        super().__init__(x,y)
    
    def mle(self,beta,x,y):
        eta=np.matmul(self.x,beta)
        mu=eta
        log_lik=-np.sum(norm.logpdf(y,mu))
        return log_lik

    def predict(self,x):
        eta=np.matmul(self.x,self.beta)  # self.beta is calculate from fit function
        mu=eta  # use the identity function
        return mu


class GLM_Bernoulli(GLM):
    def __init__(self,x,y):
        super().__init__(x,y)

    def mle(self,beta,x,y):
        eta=np.matmul(self.x,beta)
        mu=1/(1+np.exp(-eta))  # getting from Bernoulli link function
        log_lik=-np.sum(bernoulli.logpmf(y,mu))
        return log_lik

    def predict(self,x):
        eta=np.matmul(self.x,self.beta)  # self.beta is calculate from fit function
        mu=1/(1+np.exp(-eta))  # getting from the link function
        return mu


class GLM_Poisson(GLM):
    def __init__(self,x,y):
        super().__init__(x,y)

    def mle(self,beta,x,y):
        eta=np.matmul(self.x,beta)
        mu=np.exp(eta)  # getting from Poisson link function
        log_lik=-np.sum(poisson.logpmf(y,mu))
        return log_lik

    def predict(self,x):
        eta=np.matmul(self.x,self.beta)  # self.beta is calculate from fit function
        mu=np.exp(eta)  # getting from the link function
        return mu
        
      
