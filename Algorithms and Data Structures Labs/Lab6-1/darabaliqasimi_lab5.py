# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import ctypes
                                      # provides low-level arrays

class DynamicArray:
  """A dynamic array class akin to a simplified Python list."""

  def __init__(self):
    """Create an empty array."""
    self._n = 0                                    # count actual elements
    self._capacity = 1                             # default array capacity
    self._A = self._make_array(self._capacity)     # low-level array
    
  def __len__(self):
    """Return number of elements stored in the array."""
    return self._n
    
  def __getitem__(self, k):
    """Return element at index k."""
    if k >= self._n or k < 0-self._n:
      raise IndexError('invalid index')
    if k >= 0:
      return self._A[k]
    else:
      return self._A[self._n + k]
    return self._A[k]                              # retrieve from array
  
  def append(self, obj):
    """Add object to end of the array."""
    if self._n == self._capacity:                  # not enough room
      self._resize(2 * self._capacity)             # so double c apacity
    self._A[self._n] = obj
    self._n += 1

  def _resize(self, c):                            # nonpublic utitity
    """Resize internal array to capacity c."""
    B = self._make_array(c)                        # new (bigger) array
    for k in range(self._n):                       # for each existing value
      B[k] = self._A[k]
    self._A = B                                    # use the bigger array
    self._capacity = c

  def _make_array(self, c):                        # nonpublic utitity
     """Return new array with capacity c."""   
     return (c * ctypes.py_object)()               # see ctypes documentation

  def insert(self, k, value):

    if self._n == self._capacity:                  # not enough room
      self._resize(2 * self._capacity)             # so double capacity
    for j in range(self._n, k, -1):                # shift rightmost first
      self._A[j] = self._A[j-1]
    self._A[k] = value                             # store newest element
    self._n += 1

  def insertEfficient(self, k, value):
    if self._n == self._capacity:
      new_array = self._make_array(2*self._n)
      self._capacity = 2*self._capacity
      for i in range(k):
        new_array[i] = self._A[i]
      
      new_array[k] = value
      
      for j in range(k+1, self._n):
        new_array[j] = self._A[j+1]

      self._A = new_array
      self._n += 1
    else:
      for j in range(self._n, k, -1): 
        self._A[j] = self._A[j-1]
      self._A[k] = value
      self._n += 1
    return()

  def remove(self, value):
    """Remove first occurrence of value (or raise ValueError)."""
    # note: we do not consider shrinking the dynamic array in this version
    for k in range(self._n):
      if self._A[k] == value:         
        for j in range(k, self._n - 1):  
          self._A[j] = self._A[j+1]
        self._A[self._n - 1] = None      
        self._n -= 1                     
        return                             
    raise ValueError('value not found')    

  def remove_all(self, value):
    c = 0
    for k in range(self._n):
      if self._A[k] == value:           
        c += 1
        for j in range(k, self._n - 1):    
          self._A[j] = self._A[j+1]
        self._A[self._n - 1] = None        
        self._n -= 1                       
    self._resize(self._capacity-c)
    
    




      








  
      
