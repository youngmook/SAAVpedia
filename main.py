#/usr/bin/env python

from saavpedia.server import SAAVpediaInputParser

if __name__ == '__main__':

    theParser = SAAVpediaInputParser()

    '''
    NDVDCAYLR
    WLEAK   Q7Z5L2  NX_Q7Z5L2-3
    PLEAK       Q7Z5L2  NX_Q7Z5L2-3 ENSG00000166024
    '''
    theInput = "NDVDCAYLR\nWLEAK\tQ7Z5L2\tNX_Q7Z5L2-3\nPLEAK\t\tQ7Z5L2\tNX_Q7Z5L2-3 ENSG00000166024\n"

    theParser.set(theInput)
    theQueryList = theParser.toQueryList()
    print theParser,"\n"
    for i in theQueryList:
        print i
    print "\n"

    theInput = "ALSQALTELGYK\n\
                GLVPLAGTDGETTTQGLDGLSER\n\
                QLLLTADDHVNPCIGGVILFHETLYQK\n\
                NLQTQQASLQSENTHFENENQK\n\
                WLPELVAHAK\n\
                VNFGTDFLTAVK\n\
                QEYFVVASTLQDIIR\n\
                EALATLKPQAGLIVPQAVPSSQPSVVGAGEPMDLGELVGMTPEIIEK\n\
                YFTLFMNLLNDCSEVGDESAQTGGR\n\
                ALPEDYEAQALAAFHHSVEIR"

    theParser.set(theInput)
    print theParser


    pass

