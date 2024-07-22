import sys


class customexception(Exception):
    def __init__(self, error_message,error_details:sys):
         self.error_message=error_message
         _,_,exc_tb=error_details.exc_info()
         self.lineno=exc_tb.tb_lineno
    
    def __str__(self):
         return " Error occured in python script"
         self.lineno, str(self.error_message)
    
if __name__=='__main__':
      try:
            1/0
      
      except Exception as e:
            raise customexception(e,sys)
