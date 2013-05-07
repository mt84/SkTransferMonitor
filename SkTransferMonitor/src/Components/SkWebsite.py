'''
Created on Apr 30, 2013

@author: MT
'''
import  xml.etree.cElementTree as ElementTree
import re

from ..Components.SkAPI import SkAPI
from src.Components.PlayerCell import PlayerCell

class SkWebsite(SkAPI):
    """Represent SK web page."""
    def __init__(self, login, password):
        """ Initialize HTTP connection."""
        super(SkWebsite, self).__init__(login, password)

    def skLogin(self):
        """Login to SK page."""
        super(SkWebsite, self).skLogin("http://online.sokker.org/start")
    
    def setLanguage(self, lang):
        """Set language in SK page."""
        self.opener.open("http://online.sokker.org/office/lang/" + lang)

    def getPlayerCells(self):
        """Return PlayerCells objects derived from playerCell div nodes."""
        playerCellNodes = self._getPlayerCellNodes()
#         DOM java implementation
#         xpFactory = XPathFactory.newInstance()
#         xpath = xpFactory.newXPath()
        playerCells = []
        for pcn in playerCellNodes:
            ID = pcn.find("div").text.strip()
            skillStamina = pcn.find("div[4]/table/tr[1]/td/strong").text.strip()
            skillPace = pcn.find("div[4]/table/tr[2]/td/strong").text.strip()
            skillTechnique = pcn.find("div[4]/table/tr[3]/td/strong").text.strip()
            skillPassing = pcn.find("div[4]/table/tr[4]/td/strong").text.strip()
            skillKeeper = pcn.find("div[4]/table/tr[1]/td[2]/strong").text.strip()
            skillDefending = pcn.find("div[4]/table/tr[2]/td[2]/strong").text.strip()
            skillPlaymaking = pcn.find("div[4]/table/tr[3]/td[2]/strong").text.strip()
            skillScoring = pcn.find("div[4]/table/tr[4]/td[2]/strong").text.strip()
            endOfBidding = pcn.find("div[3]/span[4]").text.strip()
            bidOrUp = pcn.find("div[3]/span[3]").text.strip()
            price = re.sub("[^0-9]", "", pcn.find("div[3]/span[3]/span").text.strip())
#             DOM java implementation
#             ID = xpath.compile("/div/div/text()").evaluate(pcn, XPathConstants.STRING).strip()
#             skillStamina = xpath.compile("/div/div[4]/table/tr[1]/td/strong/text()").evaluate(pcn, XPathConstants.STRING).strip()
#             skillPace = xpath.compile("/div/div[4]/table/tr[2]/td/strong/text()").evaluate(pcn, XPathConstants.STRING).strip()
#             skillTechnique = xpath.compile("/div/div[4]/table/tr[3]/td/strong/text()").evaluate(pcn, XPathConstants.STRING).strip()
#             skillPassing = xpath.compile("/div/div[4]/table/tr[4]/td/strong/text()").evaluate(pcn, XPathConstants.STRING).strip()
#             skillKeeper = xpath.compile("/div/div[4]/table/tr[1]/td[2]/strong/text()").evaluate(pcn, XPathConstants.STRING).strip()
#             skillDefending = xpath.compile("/div/div[4]/table/tr[2]/td[2]/strong/text()").evaluate(pcn, XPathConstants.STRING).strip()
#             skillPlaymaking = xpath.compile("/div/div[4]/table/tr[3]/td[2]/strong/text()").evaluate(pcn, XPathConstants.STRING).strip()
#             skillScoring = xpath.compile("/div/div[4]/table/tr[4]/td[2]/strong/text()").evaluate(pcn, XPathConstants.STRING).strip()
#             endOfBidding = xpath.compile("/div/div[3]/span[4]/text()").evaluate(pcn, XPathConstants.STRING).strip()
#             bidOrUp = xpath.compile("/div/div[3]/span[3]/text()").evaluate(pcn, XPathConstants.STRING).strip()
#             price = re.sub("[^0-9]", "", xpath.compile("/div/div[3]/span[3]/span/text()").evaluate(pcn, XPathConstants.STRING).strip())
            playerCells.append(PlayerCell(ID, skillStamina, skillPace, skillTechnique, skillPassing, skillKeeper, skillDefending, skillPlaymaking, skillScoring, endOfBidding, {bidOrUp: price}))
        
        return playerCells
    
    def getPlayerDescription(self, playerCell):
        return
    
    def getPlayerLastTransfer(self, playerCell):
        """Return HTML div snippet containing player information from transfer list page."""
        response = self.opener.open("http://online.sokker.org/transfers_player/ID_human/" + playerCell.ID)
        print "http://online.sokker.org/transfers_player/ID_human/" + playerCell.ID
        lines = response.readlines()
        numberOfLines = len(lines)

        playerTransferDiv = []
        i = 0    
        while i < numberOfLines:
            if "content_open" in lines[i]:
                playerTransferDiv.append(lines[i].replace("&", "&amp;"))
                i = i + 1
                while "content_close" not in lines[i]:
                    playerTransferDiv.append(lines[i])
                    i = i + 1
                    if i == numberOfLines:
                        break  
            else:
                i = i + 1
                
        element = ElementTree.fromstring(''.join(playerTransferDiv))
        lastTransfer = {}
        dateOfLastTransfer = element.find("table/tr[2]/td[1]").text.strip()
        lastTransfer["dateOfLastTransfer"] = dateOfLastTransfer
        if dateOfLastTransfer != "No transfers found...":
            clubSelling = element.find("table/tr[2]/td[2]/a").attrib['href'].strip()
            clubSelling = clubSelling[clubSelling.rfind("/") + 1:]
            clubBuying = element.find("table/tr[2]/td[3]/a").attrib['href'].strip()
            clubBuying = clubBuying[clubBuying.rfind("/") + 1:]
            price = re.sub("[^0-9]", "", element.find("table/tr[2]/td[4]").text.strip())
            currency = re.sub("[0-9]", "", element.find("table/tr[2]/td[4]").text.strip())
            lastTransfer["clubSelling"] = clubSelling
            lastTransfer["clubBuying"] = clubBuying
            lastTransfer["price"] = price
            lastTransfer["currency"] = currency

        
        return lastTransfer
    
    def _getPLayerDivs(self):
        """Return HTML div snippet containing player information from transfer list page."""
        response = self.opener.open("http://online.sokker.org/transferSearch/trainer/0/pg/1/transfer_list/1/sort/end")
        lines = response.readlines()
        numberOfLines = len(lines)

        playerCellDivs = []
        i = 0    
        while i < numberOfLines:
            if "playerCell" in lines[i]:
                playerCellDiv = []
                playerCellDiv.append(lines[i])
                i = i + 1
                while "div style=\"clear:both" not in lines[i]:
                    playerCellDiv.append(lines[i].replace("&", "&amp;"))
                    i = i + 1
                    if i == numberOfLines:
                        break
                    
                playerCellDivs.append(''.join(playerCellDiv))
                    
            else:
                i = i + 1
                
        return playerCellDivs
        
    def _getPlayerCellNodes(self):
        """Return playerCell div nodes from HTML snippet."""
        playerCellDivs = self._getPLayerDivs()
        playerCellNodes = []
        for pcd in playerCellDivs:
            element = ElementTree.fromstring(pcd)
#             DOM java implementation
#             factoryXML = DocumentBuilderFactory.newInstance()
#             factoryXML.setNamespaceAware(True)
#             builderXML = factoryXML.newDocumentBuilder()
#             docXML = builderXML.parse(InputSource(ByteArrayInputStream(String(pcd).getBytes("utf-8"))))
            playerCellNodes.append(element)
            
        return playerCellNodes