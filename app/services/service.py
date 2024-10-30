import sys
import logging.config

from config import load_config

class Service :
    
    UPDATE_ACTION = 'update'
    DELETE_ACTION = 'delete'
    POST_ACTION = 'add'
    GET_ACTION = 'get'
    
    SUCCESS_STATE = 'Success'
    FAILED_STATE = 'Failed'
    NOT_FOUND_STATE = 'NotFound'
    
    def _generate_message(self,action: str, state:str,table) -> str:
        # Base message structure
        return f"view.{table}.{action}.{state}"

    def _return_exception(self,e:Exception,table:str, logger:logging) -> tuple:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        message = "bad thing happened: {} at line: {} on {} module".format(str(e), str(exc_tb.tb_lineno), table)
        logger.info(message)
        return message, None, 500
    
    def _return_success(self,data,message:str,logger:logging,table:str) -> tuple:
        log_message =  table + ' operation OK'
        logger.info(log_message)
        return message, data, 200
    
    def _return_not_found(self,data,message:str,logger:logging,table:str) -> tuple:
        log_message =  table + ' ressource not found'
        logger.info(log_message)
        return message, data, 404
    
    def _return_failure(self, response,message:str,logger:logging,table:str) -> tuple:
        log_message = 'operation on ' + table + ' : FAILED with error ' + str(response)
        logger.info(log_message)
        return message, None, 400

    def _job_payload_action(self,jobpayload:dict) -> tuple:
        
        return jobpayload.get('authenticate',None),jobpayload.get('payload',None)
    
    def _load_config(self) :
        return load_config()