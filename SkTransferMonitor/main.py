'''
Created on Apr 28, 2013

@author: MT
'''
from src.Components.SkWebsite import SkWebsite
# from src.Components.SkWebService import SkWebService
# from src.Components.ListedSkPlayer import ListedSkPlayer
        
import threading

import datetime
import time

import logging

def main(argv):
    if len(argv) != 2:
        print "You must pass credentials: username and password."
    else:
        
        username = argv[0]
        password = argv[1]
                
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename='transfers.txt',level=logging.DEBUG)
        global skW
        skW = SkWebsite(username, password)
        skW.skLogin()
        print "Logged in to SK web page."
        skW.setLanguage("en")
        print "Lang set to eng."
#         skWS = SkWebService(username, password)
#         skWS.skLogin()
#         print "Logged in to SK web service."
        
        global monitoredPlayers
        global newPlayers
        global lock
        
        monitoredPlayers = []
        newPlayers = []
        lock = threading.Lock()
        
        thread1 = threading.Thread(target = monitorTransferList)
        thread2 = threading.Thread(target = monitorListedPLayers)
        thread1.setName("monitorTransferList")
        thread2.setName("monitorListedPlayers")
        thread1.start()
        thread2.start()
 
def monitorTransferList():
    while True:
        lock.acquire()
        start = datetime.datetime.now()
        sleepTime = 60
        logging.info("Loading playerCells...")
        try:
            pcs = skW.getPlayerCells()
        except:
            logging.error('Failed to load playerCells, attempting to re-login. Stack trace:\n %s', pcs)
            time.sleep(10)
            skW.skLogin()
            skW.setLanguage("en")
        else:
            logging.info("PlayerCells loaded.")
            endOfBiddings = []     
            for playerCell in pcs:
                endOfBiddings.append(datetime.datetime.strptime(playerCell.endOfBidding, '%Y-%m-%d %H:%M'))
                if len([monitoredPlayer for monitoredPlayer in monitoredPlayers if playerCell.ID == monitoredPlayer.ID]) == 0:
                    monitoredPlayers.append(playerCell)
                    logging.info("Successfully added player to monitor. ID: %s", str(playerCell.ID)) 
#                     playerXML = skWS.getPlayer(playerCell.ID)
#                     monitoredPlayers.append(ListedSkPlayer(playerXML["name"], playerXML["surname"], playerXML["countryID"], playerXML["age"], playerXML["height"], playerXML["weight"], playerXML["BMI"], playerXML["teamID"], playerXML["youthTeamID"], playerXML["value"], playerXML["wage"], playerXML["cards"], playerXML["goals"], playerXML["assists"], playerXML["matches"], playerXML["ntCards"], playerXML["ntGoals"], playerXML["ntAssists"], playerXML["ntMatches"], playerXML["injuryDays"], playerXML["national"], playerXML["skillForm"], playerXML["skillExperience"], playerXML["skillTeamwork"], playerXML["skillDiscipline"], playerCell.ID, playerCell.skillStamina, playerCell.skillPace, playerCell.skillTechnique, playerCell.skillPassing, playerCell.skillKeeper, playerCell.skillDefending, playerCell.skillPlaymaking, playerCell.skillScoring, playerCell.endOfBidding, playerCell.price))
             
                else:
                    continue
            maxEndOfBidding = max(endOfBiddings)
            sleepTime =  (maxEndOfBidding - datetime.datetime.now()).total_seconds()
            logging.info("Monitored players seen by monitorTransferList: %s", str(len(monitoredPlayers)))
             
            end = datetime.datetime.now()
            diff = end - start
#             print diff
             
        finally:
            lock.release()
        
        logging.info("Will check transfer list for: %s", str(sleepTime))     
        time.sleep(sleepTime)
         
def monitorListedPLayers():
    while True:
        lock.acquire()  
        try:
            for mPlayer in monitoredPlayers:
                if len([startedThread for startedThread in threading.enumerate() if mPlayer.ID == startedThread.name]) == 0:
                    threadMonitorPlayer = threading.Thread(target = monitorPlayer, args = (mPlayer,))
                    threadMonitorPlayer.setName(mPlayer.ID)
                    threadMonitorPlayer.start()
                    logging.info("Started monitoring player: %s", str(mPlayer.ID)) 
                    
        except:
            logging.error('Failed to read monitoredPlayers list. Stack trace:\n %s', monitoredPlayers)
         
        finally:
            lock.release()
            
def monitorPlayer(playerCell):
    while True:
        transfer = skW.getPlayerLastTransfer(playerCell)
        dateOfLastTransfer = transfer["dateOfLastTransfer"]
        endOfBidding = datetime.datetime.strptime(playerCell.endOfBidding.split(" ", 1)[0], '%Y-%m-%d')
        if datetime.datetime.now() > endOfBidding + datetime.timedelta(days=7):
            lock.acquire()
            try:
                monitoredPlayers.remove(playerCell)
                logging.info("Successfully removed player from monitoredPlayer list. ID: %s", str(playerCell.ID))
                return
            finally:
                lock.release()
                    
        if dateOfLastTransfer != "No transfers found...":
            dateOfLastTransfer = datetime.datetime.strptime(dateOfLastTransfer, '%Y-%m-%d')
            if dateOfLastTransfer >= endOfBidding:
                lock.acquire()
                try:
                    monitoredPlayers.remove(playerCell)
                    logging.info("Transfer completed. From: %s to: %s price: %s currency: %s. Time %s", str(transfer["clubSelling"]),  str(transfer["clubBuying"]), str(transfer["price"]), str(transfer["currency"]),  str(playerCell.endOfBidding))
                    return
                
                finally:
                    lock.release()
            
            else:
                logging.info("Will check player for 10 minutes. ID: %s", str(playerCell.ID))
                time.sleep(600)
            
        else:
            logging.info("Will check player for 10 minutes. ID: %s", str(playerCell.ID))
            time.sleep(600)
        
if __name__ == "__main__":
    main(["login", "password"])                     
