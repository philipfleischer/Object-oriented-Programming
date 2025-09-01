import logging
import sys

# NOTE: Dette gjør vi bare en gang i starten av filen
logging.basicConfig()

# logg-objekt å logge til
logger = logging.getLogger(name = "advarsels-logg")

#Skrive til loggen
logger.warning("Dette er en advarsel")
logger.info("DEtte er INFO")
logger.debug("DEtte er en debugger")

logger2 = logging.getLogger(name = "adversel-og-info-logg")
logger2.setLevel(logging.INFO) #nivå 1 og 2

logger2.warning("Dette er en advarsel")
logger2.info("DEtte er INFO")
logger2.debug("DEtte er en debugger")

logger3 = logging.getLogger(name = "adversel-og-debug-logg")
logger3.setLevel(logging.DEBUG) #nivå 1 og 2 og 3

logger3.warning("Dette er en advarsel")
logger3.info("DEtte er INFO")
logger3.debug("DEtte er en debugger")

smart_logger = logging.getLogger(name = "brukerbestemt-logg")
if len(sys.argv) > 1: 
    if sys.argv[1] == "INFO":
        smart_logger.setLevel(logging.INFO)
    elif sys.argv[1] == "DEBUG":
        smart_logger.setLevel(logging.DEBUG)

smart_logger.info("DEtte ser ikke brukeren vanligvis")
smart_logger.debug("DEtte ser ikke brukeren vanligvis")