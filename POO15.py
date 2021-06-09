import logging
from datetime import date

format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(filename=f'{date.today()}.log', level=logging.DEBUG, filemode='at',  format=format)
logger = logging.getLogger(__name__)

logger.info('Mensagem informativa!')

try:
    a = 1/0
except Exception as e:
    logging.exception(e)
