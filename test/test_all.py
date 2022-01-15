import unittest
import numpy as np
import fdasrsf as fs  

class TestFDASRSF(unittest.TestCase): 
  
    # Returns True or False.  
    def test_reparm(self):  
        M = 101
        q1 = np.sin(np.linspace(0,2*np.pi,M))
        timet = np.linspace(0,1,M)
        gam = fs.optimum_reparam(q1, timet, q1)       
        self.assertAlmostEqual(sum(gam-timet),0)
    
    def test_warp_f_gamma(self):  
        M = 101
        q1 = np.sin(np.linspace(0,2*np.pi,M))
        timet = np.linspace(0,1,M)
        gam = fs.optimum_reparam(q1, timet, q1)   
        q1a = fs.warp_f_gamma(timet, q1, gam)    
        self.assertAlmostEqual(sum(q1-q1a),0)
    
    def test_warp_q_gamma(self):  
        M = 101
        q1 = np.sin(np.linspace(0,2*np.pi,M))
        timet = np.linspace(0,1,M)
        gam = fs.optimum_reparam(q1, timet, q1)   
        q1a = fs.warp_q_gamma(timet, q1, gam)    
        self.assertAlmostEqual(sum(q1-q1a),0)
    
    def test_reparm1(self):  
        M = 101
        q1 = np.sin(np.linspace(0,2*np.pi,M))
        timet = np.linspace(0,1,M)
        gam = fs.optimum_reparam(q1, timet, q1, method="DP")       
        self.assertAlmostEqual(sum(gam-timet),0)
    
    def test_rlbgs(self):
        M = 101
        q1 = np.sin(np.linspace(0,2*np.pi,M))
        timet = np.linspace(0,1,M)
        gam = fs.optimum_reparam(q1, timet, q1, method="RBFGS")       
        self.assertAlmostEqual(sum(gam-timet),0)
    
    def test_f_to_srvf(self):
        M = 101
        f1 = np.sin(np.linspace(0,2*np.pi,M))
        timet = np.linspace(0,1,M)
        q1 = fs.f_to_srsf(f1,timet)
        f1a = fs.srsf_to_f(q1,timet)
        self.assertAlmostEqual(sum(f1-f1a),0,4)
    
    def test_elastic_distance(self):
        M = 101
        f1 = np.sin(np.linspace(0,2*np.pi,M))
        timet = np.linspace(0,1,M)
        da, dp = fs.elastic_distance(f1, f1, timet)
        self.assertLessEqual(da, 1e-10)
        self.assertLessEqual(dp, 1e-6)
    
    def test_smooth(self):
        M = 101
        q1 = np.zeros((M,1))
        q1[:,0] = np.sin(np.linspace(0,2*np.pi,M)).T
        q1a = fs.smooth_data(q1,1)
        q1b = fs.smooth_data(q1,1)
        self.assertAlmostEqual(sum(q1a.flatten()-q1b.flatten()),0)
    
    def test_edistance(self):
        M = 101
        q1 = np.sin(np.linspace(0,2*np.pi,M))
        timet = np.linspace(0,1,M)
        dy, dx = fs.elastic_distance(q1, q1, timet)
        self.assertAlmostEqual(sum(dy+dx),0)
    
    def test_invgamma(self):
        M = 101
        gam = np.linspace(0,1,M)
        gami = fs.invertGamma(gam)
        self.assertAlmostEqual(sum(gam-gami),0)
    

  
if __name__ == '__main__': 
    unittest.main() 