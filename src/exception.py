import sys 
from logger import logging
# /this basically contains all the erros and exceptions of the systems 

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    # the exc_tb will contain all the arror detail 
    file_name=exc_tb.tb_frame.f_code.co_filename
    # getting the filename where the error has taken place //

    error_message="ERROR HAS OCCURRED IN PYTHON SCRIPT NAME [{0}] line number [{1}] error message [{2}]".format(file_name,exc_tb.tb_lineno,str(error))

    return error_message

class CustomException(Exception): 
    # doing inheritance of the main exception class 
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message    
    

if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("divide by 0 error")
        raise CustomException(e,sys)
            




