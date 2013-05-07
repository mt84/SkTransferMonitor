'''
Created on May 2, 2013

@author: MT
'''
import  xml.etree.cElementTree as ElementTree

from ..Components.SkAPI import SkAPI

class SkWebService(SkAPI):
    """Represent SK XML web service."""
    def __init__(self, login, password):
        """ Initialize HTTP connection."""
        super(SkWebService, self).__init__(login, password)

    def skLogin(self):
        """Login to SK XML web service."""
        super(SkWebService, self).skLogin("http://online.sokker.org/start.php?session=xml")
        
    def getPlayer(self, ID):
        """Return player attributes from SK web service."""
        response = self.opener.open("http://online.sokker.org/xml/player-" + ID + ".xml")
        element = ElementTree.fromstring(''.join(response.readlines()))
        
        playerXML = {}
        for child in element:
            playerXML[child.tag] = child.text
        
#         DOM java implementation
#         factoryXML = DocumentBuilderFactory.newInstance()
#         factoryXML.setNamespaceAware(True)
#         builderXML = factoryXML.newDocumentBuilder()
#         Remove xml definition line - otherwise getting Premature end of file exception
#         px = []
#         for line in response.readlines():
#             if "standalone" not in line:
#                 px.append(line)
#         playerXML = ''.join(px).strip()
#         playerNode = builderXML.parse(InputSource(ByteArrayInputStream(String(playerXML).getBytes("utf-8"))))
        
        return playerXML