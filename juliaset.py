import cmath;
import numpy;
import time;

class JuliaSet(object):
  
    def __init__(self, c, n=100, _d=0.001):
        self.c=c;
        self.set=numpy.array([]);
        self._d=_d;
        if(n>0):
            self.n=n;
        else:
            print "Reset n to 100";
        self._complexplane = numpy.array([]);
        
        
    def juliamap(self, z):
        return self.c+(z**2);
    
    
    def iterate(self, z):
        m=0;
        while(1>0):
            z=self.juliamap(z);
            m+=1;
            if(abs(z)>2):
                return m;
            elif(m>=self.n):
                return 0;
            
            
        
    def setcomplexplane(self, d=0):
        i =-2;
        if(d==self._d and len(self._complexplane)>1):
            return;

        if(d>0):
            self._d=d;
            increment = d;
        else:
            increment = self._d;
        arr = numpy.arange(-2,2,increment);
        q = numpy.ones(len(arr));
        w = numpy.array([]);
        for s in arr:
            g=q*s;
            w= numpy.append(w,g+(g*1j));   
        self._complexplane =w;

            
    def set_spacing(self, d):
        self.setcomplexplane(d);

    def generate(self):
        f =numpy.vectorize(self.iterate);
        self.set =f(self._complexplane);
        return self.set;
