"""
=================
Lorentzian Fitter
=================

The simplest and most useful model.

Until 12/23/2011, lorentzian fitting used the complicated and somewhat bloated
gaussfitter.py code.  Now, this is a great example of how to make your own
model!

"""
import model
import numpy 

def lorentzian(x,A,dx,w, return_components=False):
    """
    Returns a 1-dimensional lorentzian of the form
    A/(2*pi)*w/((x-dx)**2 + ((w/2)**2))
    
             1             w
        A ------- --------------------
           2  pi   (x-dx)^2 + (w/2)^2
    
     A = Amplitude
    dx = Center
     w = Full Width at Half Maximum
    
    Also known as the "Cauchy Distribution"
    
    Guesses should be of the form [amplitude,center,width]

    return_components does nothing but is required by all fitters
    
    Additional readings:
    http://mathworld.wolfram.com/CauchyDistribution.html
    https://en.wikipedia.org/wiki/Cauchy_distribution
    
    """
    x = numpy.array(x) # make sure xarr is no longer a spectroscopic axis
    return A/(2.0*numpy.pi)*w/((x-dx)**2 + (w/2.0)**2)

def lorentzian_fitter():
    """
    Generator for lorentzian fitter class
    """

    myclass =  model.SpectralModel(lorentzian, 3,
            parnames=['amplitude','shift','width'], 
            parlimited=[(False,False),(False,False),(True,False)], 
            parlimits=[(0,0), (0,0), (0,0)],
            shortvarnames=('A',r'\Delta x',r'\sigma'),
            )
    myclass.__name__ = "lorentzian"
    
    return myclass

