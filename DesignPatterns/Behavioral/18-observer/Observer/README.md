# Bug
Python runs managed code 
Uses reference counters for objects 
Set of observers holds references 
Need to detach each observer 
If not detached, reference count > 0 
Stops garbage collection

