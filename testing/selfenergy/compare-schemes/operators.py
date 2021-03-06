# library to create operators
import numpy as np
from scipy.sparse import csc_matrix as csc

def interface1d(h,cut = 3.):
  dind = 1 # index to which divide the positions
  if h.has_spin:  dind *= 2 # duplicate for spin
  if h.has_eh:  dind *= 2  # duplicate for eh
  n = len(h.intra) # number of elments of the hamiltonian
  data = [] # epmty list
  for i in range(n): # loop over elements
    y = h.geometry.y[i/dind]
    if y < -cut:  data.append(-1.)
    elif y > cut: data.append(1.)
    else: data.append(0.)
  row, col = range(n),range(n)
  m = csc((data,(row,col)),shape=(n,n),dtype=np.complex)
  return m # return the operator



def bulk1d(h,p = 0.5):
  dind = 1 # index to which divide the positions
  if h.has_spin:  dind *= 2 # duplicate for spin
  if h.has_eh:  dind *= 2  # duplicate for eh
  n = h.intra.shape[0] # number of elments of the hamiltonian
  data = [] # epmty list
  cut = np.max(h.geometry.y)*p
  for i in range(n): # loop over elements
    y = h.geometry.y[i/dind]
    if y < -cut:  data.append(-1.)
    elif y > cut: data.append(1.)
    else: data.append(0.)
  row, col = range(n),range(n)
  m = csc((data,(row,col)),shape=(n,n),dtype=np.complex)
  return m # return the operator



def get_sz(h):
  """Operator for the calculation of Sz expectation value"""
  if h.has_eh: raise
  if not h.has_spin: raise
  if h.has_spin:
    op = np.zeros(h.intra.shape,dtype=np.complex) # initialize matrix
    for i in range(len(op)):   
      op[i,i] = (-1.)**i 
  if h.is_sparse: op = csc(op) # transform into sparse
  return op
 

def get_sx(h):
  """Operator for the calculation of Sz expectation value"""
  if h.has_eh: raise
  if not h.has_spin: raise
  if h.has_spin:
    op = np.zeros(h.intra.shape,dtype=np.complex) # initialize matrix
    for i in range(len(op)/2):   
      op[2*i,2*i+1] = 1.
      op[2*i+1,2*i] = 1.
  if h.is_sparse: op = csc(op) # transform into sparse
  return op



def get_sy(h):
  """Operator for the calculation of Sz expectation value"""
  if h.has_eh: raise
  if not h.has_spin: raise
  if h.has_spin:
    op = np.zeros(h.intra.shape,dtype=np.complex) # initialize matrix
    for i in range(len(op)/2):   
      op[2*i,2*i+1] = -1j
      op[2*i+1,2*i] = 1j
  return op


def get_z(h):
  """Operator for the calculation of z expectation value"""
  if h.intra.shape[0]==len(h.geometry.z): # if as many positions as entries
    op = np.zeros(h.intra.shape,dtype=np.complex) # initialize matrix
    for i in range(len(h.geometry.z)):
      op[i,i] = h.geometry.z[i]
    return op
  raise
  if h.has_eh: raise
  if not h.has_spin: raise
  if h.has_spin:
    op = np.zeros(h.intra.shape,dtype=np.complex) # initialize matrix
    for i in range(len(op)/2):   
      op[2*i,2*i+1] = -1j
      op[2*i+1,2*i] = 1j
  



def get_rop(h,fun):
  """Operator for the calculation of z expectation value"""
  if h.intra.shape[0]==len(h.geometry.z): # if as many positions as entries
    op = np.zeros(h.intra.shape,dtype=np.complex) # initialize matrix
    for i in range(len(h.geometry.z)):
      value = fun(h.geometry.r[i]) # evaluate function
      op[i,i] = value
    return op
  raise

