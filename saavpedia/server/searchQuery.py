#!/usr/bin/env python

################################################################################
# "SAAVpedia Annotation Javascript Library"
# Copyright (C) 2017 Young-Mook Kang <ymkang@thylove.org>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
################################################################################

import sys, json
import MySQLdb
import argparse
from ClassSAAVpediaInputParser import SAAVpediaInputParser

def main(theUrl, theUser, thePassword, theDB, theTable, theInput):
    parser = SAAVpediaInputParser()
    theInputFile = file(theInput)
    theInputText = theInputFile.read()
    #print theInputText
    parser.set(theInputText)
    theInputFile.close()

    # Open database connection
    db = MySQLdb.connect(theUrl, theUser, thePassword, theDB)

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute SQL query using execute() method.
    theCommand = 'SELECT * FROM {0} WHERE {1}'.format(theTable, parser.toSqlCondition())
    #print theCommand
    cursor.execute(theCommand)

    # Fetch a single row using fetchone() method.
    rows = splitRefAlt(dataTupleToDictList((cursor.fetchall())))
    #print rows
    print json.dumps(rows)
    return rows

def getRsOrCosmicLink(theID) :
    theRS = 'rs'
    theCosmic = 'cosm'

    if (len(theID) > len(theRS)):
        if (theID[0:2] == theRS):
            return "<a href='https://www.ncbi.nlm.nih.gov/projects/SNP/snp_ref.cgi?searchType=adhoc_search&type=rs&rs={0}' target='_blank'><span style='color:blue'>{0}</span></a>".format(theID)
    if (len(theID) > len(theCosmic)):
        if (theID[0:4].lower() == theCosmic):
            theCosmicNumber = theID[4:]
            return "<a href='http://cancer.sanger.ac.uk/cosmic/mutation/overview?id={0}' target='_blank'><span style='color:red'>{1}</span></a>".format(theCosmicNumber,theID)
    return theID

def applyNextprotLink(theID):
    if(theID[:3].upper() == 'NX_'):
        theParent = theID.split('-')[0]
        return "<a target='_blank' href='https://www.nextprot.org/entry/{0}/?isoform={1}'><b style='font-family:Noto Sans; color:#c50363'>{1}</b></a>".format(theParent, theID)
    else :
        return theID

def applyUniprotLink(theID):
    return "<a target='_blank' href='http://www.uniprot.org/uniprot/{0}'><b style='font-family:Noto Sans; color:#0d6f97'>{0}</b></a>".format(theID)

def applyPDBLink(theID):
    if theID == 'NA' or theID == 'N/A' or theID.lower() == 'none':
        return "<span style='color:LightGray'>{0}</span>".format(theID)

    theIDList = theID.replace('\"','').split(';')
    theNewIDList = []
    for ithID in theIDList:
        if ithID.lower() != 'none':
            theNewIDList.append("<a target='_blank' href='https://www.rcsb.org/structure/{0}'><b style='font-family:Noto Sans; color:#325880'>{0}</b></a>".format(ithID))
        pass
    return "<span style='color:#999'>;</span>".join(theNewIDList)

def applyENSPLink(theID):
    if theID == 'NA' or theID == 'N/A' or theID.lower() == 'none':
        return "<span style='color:LightGray'>{0}</span>".format(theID)

    theIDList = theID.replace('\"','').split(';')
    theNewIDList = []
    for ithID in theIDList:
        if ithID.lower() != 'none':
            theNewIDList.append("<a target='_blank' href='https://www.ensembl.org/id/{0}'><b style='font-family:Noto Sans; color:#336'>{0}</b></a>".format(ithID))
        pass
    return "<span style='color:#999'>;</span>".join(theNewIDList)

def applyENSTLink(theID):
    if theID == 'NA' or theID == 'N/A' or theID.lower() == 'none':
        return "<span style='color:LightGray'>{0}</span>".format(theID)

    theIDList = theID.replace('\"','').split(';')
    theNewIDList = []
    for ithID in theIDList:
        if ithID.lower() != 'none':
            theNewIDList.append("<a target='_blank' href='https://www.ensembl.org/id/{0}'><b style='font-family:Noto Sans; color:#336'>{0}</b></a>".format(ithID))
        pass
    return "<span style='color:#999'>;</span>".join(theNewIDList)


def applyENSGLink(theID):
    if theID == 'NA' or theID == 'N/A' or theID.lower() == 'none':
        return "<span style='color:LightGray'>{0}</span>".format(theID)

    theIDList = theID.replace('\"','').split(';')
    theNewIDList = []
    for ithID in theIDList:
        if ithID.lower() != 'none':
            theNewIDList.append("<a target='_blank' href='https://www.ensembl.org/id/{0}'><b style='font-family:Noto Sans; color:#336'>{0}</b></a>".format(ithID))
        pass
    return "<span style='color:#999'>;</span>".join(theNewIDList)

def applyPubMedLink(theID):
    if theID == 'NA' or theID == 'N/A' or theID.lower() == 'none':
        return "<span style='color:LightGray'>{0}</span>".format(theID)

    theIDList = theID.replace('\"','').split(';')
    theNewIDList = []
    for ithID in theIDList:
        if ithID.lower() != 'none':
            theNewIDList.append("<a target='_blank' href='https://www.ncbi.nlm.nih.gov/pubmed/{0}'><b style='font-family:Noto Sans; color:#369'>{0}</b></a>".format(ithID))
        pass
    return "<span style='color:#999'>;</span>".join(theNewIDList)

def applyChemblLink(theID):
    if theID == 'NA' or theID == 'N/A' or theID.lower() == 'none':
        return "<span style='color:LightGray'>{0}</span>".format(theID)

    theIDList = theID.replace('\"','').split(';')
    theNewIDList = []
    for ithID in theIDList:
        if ithID.lower() != 'none':
            theNewIDList.append("<a target='_blank' href='https://www.ebi.ac.uk/chembldb/target/inspect/{0}'><b style='font-family:Noto Sans; color:#006666'>{0}</b></a>".format(ithID))
        pass
    return "<span style='color:#999'>;</span>".join(theNewIDList)


def applyPharmGKBLink(theID):
    if theID == 'NA' or theID == 'N/A' or theID.lower() == 'none':
        return "<span style='color:LightGray'>{0}</span>".format(theID)

    theIDList = theID.replace('\"','').split(';')
    theNewIDList = []
    for ithID in theIDList:
        if ithID.lower() != 'none':
            theNewIDList.append("<a target='_blank' href='https://www.pharmgkb.org/gene/{0}'><b style='font-family:Noto Sans; color:#497de3'>{0}</b></a>".format(ithID))
        pass
    return "<span style='color:#999'>;</span>".join(theNewIDList)

def applyVegaLink(theID):
    if theID == 'NA' or theID == 'N/A' or theID.lower() == 'none':
        return "<span style='color:LightGray'>{0}</span>".format(theID)

    theIDList = theID.replace('\"','').split(';')
    theNewIDList = []
    for ithID in theIDList:
        if ithID.lower() != 'none':
            theNewIDList.append("<a target='_blank' href='http://vega.archive.ensembl.org/homo_sapiens/Gene/Summary?g={0}'><b style='font-family:Noto Sans; color:#369'>{0}</b></a>".format(ithID))
        pass
    return "<span style='color:#999'>;</span>".join(theNewIDList)


def applyENALink(theID):
    if theID == 'NA' or theID == 'N/A' or theID.lower() == 'none':
        return "<span style='color:LightGray'>{0}</span>".format(theID)

    theIDList = theID.replace('\"','').split(';')
    theNewIDList = []
    for ithID in theIDList:
        if ithID.lower() != 'none':
            theNewIDList.append("<a target='_blank' href='https://www.ebi.ac.uk/ena/data/view/{0}'><b style='font-family:Noto Sans; color:#4a7474'>{0}</b></a>".format(ithID))
        pass
    return "<span style='color:#999'>;</span>".join(theNewIDList)

def applyOMIMLink(theID):
    if theID == 'NA' or theID == 'N/A' or theID.lower() == 'none':
        return "<span style='color:LightGray'>{0}</span>".format(theID)

    theIDList = theID.replace('\"','').split(';')
    theNewIDList = []
    for ithID in theIDList:
        if ithID.lower() != 'none':
            theNewIDList.append("<a target='_blank' href='https://www.ncbi.nlm.nih.gov/omim/{0}'><b style='font-family:Noto Sans; color:#369'>{0}</b></a>".format(ithID))
        pass
    return "<span style='color:#999'>;</span>".join(theNewIDList)

def applyLink(theID, theUrlPrefix, theColor):
    if theID == 'NA' or theID == 'N/A' or theID.lower() == 'none':
        return "<span style='color:LightGray'>{0}</span>".format(theID)

    theIDList = theID.replace('\"','').split(';')
    theNewIDList = []
    for ithID in theIDList:
        if ithID.lower() != 'none':
            theNewIDList.append("<a target='_blank' href='{0}{1}'><b style='font-family:Noto Sans; color:{2}'>{1}</b></a>".format(theUrlPrefix, ithID, theColor))
        pass
    return "<span style='color:#999'>;</span>".join(theNewIDList)


#https://genome.ucsc.edu/cgi-bin/hgLinkIn?resource=uniprot&id=P50897
#http://version10.string-db.org/newstring_cgi/show_network_section.pl?limit=0&targetmode=proteins&caller_identity=gene_cards&network_flavor=evidence&identifiers=9606.ENSP00000417764%0D%0A9606.ENSP00000264933%0D%0A9606.ENSP00000058691%0D%0A9606.ENSP00000371236%0D%0A9606.ENSP00000405573%0D%0A9606.ENSP00000364475%0D%0A9606.ENSP00000468690%0D%0A9606.ENSP00000364486%0D%0A9606.ENSP00000410833%0D%0A9606.ENSP00000337746%0D%0A9606.ENSP00000286621%0D%0A9606.ENSP00000306817%0D%0A9606.ENSP00000425809%0D%0A9606.ENSP00000371393%0D%0A9606.ENSP00000298198%0D%0A9606.ENSP00000265447%0D%0A9606.ENSP00000379678%0D%0A9606.ENSP00000360124%0D%0A9606.ENSP00000350785%0D%0A9606.ENSP00000258975%0D%0A9606.ENSP00000383392%0D%0A9606.ENSP00000265729%0D%0A9606.ENSP00000340736%0D%0A9606.ENSP00000370555%0D%0A9606.ENSP00000296444%0D%0A9606.ENSP00000411825%0D%0A
#https://www.ncbi.nlm.nih.gov/nuccore/NG_001019
#https://www.ncbi.nlm.nih.gov/omim/103850
#https://www.ebi.ac.uk/ena/data/view/L19605
#http://vega.archive.ensembl.org/homo_sapiens/Gene/Summary?g=OTTHUMG00000018604
#https://www.pharmgkb.org/gene/PA24825/overview

def colorDNA(theString):
    theNewString = ''
    for ithChar in theString:
        theChar = str(ithChar).upper()
        if theChar == 'A':
            #theNewString = theNewString + "<span style='color:#5050ff'>{0}</span>".format(theChar)
            theNewString = theNewString + "<b style='color:blue'>{0}</b>".format(theChar)
            pass
        elif theChar == 'T':
            #theNewString = theNewString + "<span style='color:#E6E600'>{0}</span>".format(theChar)
            theNewString = theNewString + "<b style='color:#f4ad24'>{0}</b>".format(theChar)
            pass
        elif theChar == 'G':
            #theNewString = theNewString + "<span style='color:#00C000'>{0}</span>".format(theChar)
            #theNewString = theNewString + "<span style='color:#27ae60 '>{0}</span>".format(theChar)
            theNewString = theNewString + "<b style='color:#009900;'>{0}</b>".format(theChar)
            pass
        elif theChar == 'C':
            #theNewString = theNewString + "<span style='color:#E00000'>{0}</span>".format(theChar)
            theNewString = theNewString + "<b style='color:red'>{0}</b>".format(theChar)
            pass
        else:
            theNewString = theNewString + "<span style='color:Gray'>{0}</span>".format(theChar)
            pass
        pass
    return theNewString

def colorAminoAcid(theString):
    theSmallNonPoler = ['G','A','S','T']
    theHydrophobic = ['C', 'V', 'I', 'L', 'P', 'F', 'Y', 'M', 'W']
    thePolar = ['N', 'Q', 'H']
    theNegativelyCharged = ['D', 'E']
    thePositivelyCharged = ['K', 'R']
    theNewString = ''
    for ithChar in theString:
        theChar = str(ithChar).upper()
        if theChar in theSmallNonPoler:
            #theNewString = theNewString + "<span style='color:#5050ff'>{0}</span>".format(theChar)
            theNewString = theNewString + "<b style='color:orange'>{0}</b>".format(theChar)
            pass
        elif theChar in theHydrophobic:
            #theNewString = theNewString + "<span style='color:#E6E600'>{0}</span>".format(theChar)
            theNewString = theNewString + "<b style='color:Green'>{0}</b>".format(theChar)
            pass
        elif theChar in thePolar:
            #theNewString = theNewString + "<span style='color:#00C000'>{0}</span>".format(theChar)
            #theNewString = theNewString + "<span style='color:#27ae60 '>{0}</span>".format(theChar)
            theNewString = theNewString + "<b style='color:Magenta;'>{0}</b>".format(theChar)
            pass
        elif theChar in theNegativelyCharged:
            #theNewString = theNewString + "<span style='color:#E00000'>{0}</span>".format(theChar)
            theNewString = theNewString + "<b style='color:Red'>{0}</b>".format(theChar)
            pass
        elif theChar in thePositivelyCharged:
            #theNewString = theNewString + "<span style='color:#E00000'>{0}</span>".format(theChar)
            theNewString = theNewString + "<b style='color:Blue'>{0}</b>".format(theChar)
            pass
        else:
            theNewString = theNewString + "<span style='color:Gray'>{0}</span>".format(theChar)
            pass
        pass
    return theNewString

def colorNA(theRows):
    for ithRow in theRows:
        theKeys = ithRow.keys()
        for ithKey in ithRow:
            if ithRow[ithKey] == 'NA' or ithRow[ithKey] == 'N/A':
                ithRow[ithKey] = "<span style='color:LightGray ;'>{0}</span>".format(ithRow[ithKey])
                pass
            pass
        pass
    pass

def colorNAString(theNA):
    if theNA == 'NA' or theNA == 'N/A':
        return "<span style='color:LightGray ;'>{0}</span>".format(theNA)
    return theNA

def splitRefAlt(theRows):
    import copy
    theNewRows = []
    for ithRow in theRows:
        theSplitedRefAltList = ithRow['col12'].split(':')
        ithNewRow = copy.deepcopy(ithRow)

        ithNewRow['VSA_QS'] = colorNAString('NA')
        ithNewRow['VSA_Pval'] = colorNAString('NA')
        ithNewRow['VSA_filter'] = colorNAString('NA')
        ithNewRow['VSA_Pos'] = colorNAString(ithRow['col11'])
        ithNewRow['VSA_Ref'] = colorAminoAcid(theSplitedRefAltList[0])
        ithNewRow['VSA_Alt'] = colorAminoAcid(theSplitedRefAltList[1])

        ithNewRow['ID'] = ithRow['col0']
        ithNewRow['VSN_Chr'] = ithRow['col1']
        ithNewRow['VSN_Pos'] = ithRow['col2']
        ithNewRow['VSN_Ref'] = colorDNA(ithRow['col3'])
        ithNewRow['VSN_Alt'] = colorDNA(ithRow['col4'])
        ithNewRow['VSN_Strand'] = colorNAString(ithRow['col5'])
        ithNewRow['VSN_ID'] = getRsOrCosmicLink(ithRow['col6'])
        ithNewRow['BRP_Nextprot'] = applyNextprotLink(ithRow['col7'])
        ithNewRow['BRP_Uniprot'] = applyUniprotLink(ithRow['col8'])
        ithNewRow['BRG_Ensembl_Gen'] = applyENSGLink(ithRow['col9'])
        ithNewRow['BRT_Ensembl_Tra'] = applyENSTLink(ithRow['col10'])
        ithNewRow['VSA_Pos'] = colorNAString(ithRow['col11'])

        ithNewRow['VSA_RS'] = colorAminoAcid(ithRow['col13'])
        ithNewRow['VSA_AS'] = colorAminoAcid(ithRow['col14'])
        ithNewRow['VSA_EC'] = colorNAString(ithRow['col15'])

        ithNewRow['VSN_1000G_OC'] = colorNAString(ithRow['col19'])
        ithNewRow['VSN_ESP_OC'] = colorNAString(ithRow['col20'])
        ithNewRow['VSN_ExAC_OC'] = colorNAString(ithRow['col21'])
        ithNewRow['VSN_ESP_AF_MAF'] = colorNAString(ithRow['col22'])
        ithNewRow['VSN_ESP_EU_MAF'] = colorNAString(ithRow['col23'])
        ithNewRow['VSN_1000G_T_MAF'] = colorNAString(ithRow['col24'])
        ithNewRow['VSN_1000G_EAS_MAF'] = colorNAString(ithRow['col25'])
        ithNewRow['VSN_1000G_AMR_MAF'] = colorNAString(ithRow['col26'])
        ithNewRow['VSN_1000G_AFR_MAF'] = colorNAString(ithRow['col27'])
        ithNewRow['VSN_1000G_EUR_MAF'] = colorNAString(ithRow['col28'])
        ithNewRow['VSN_1000G_SAS_MAF'] = colorNAString(ithRow['col29'])
        ithNewRow['VSN_VT'] = colorNAString(ithRow['col30'])
        ithNewRow['VSC_Phenotype'] = ithRow['col31']

        ithNewRow['VSC_Source'] = colorNAString(ithRow['col33'])
        ithNewRow['VSC_OID'] = colorNAString(ithRow['col34'])

        ithNewRow['VSC_Phe_CLS'] = colorNAString(ithRow['col36'])
        ithNewRow['VSD_DB'] = applyLink(ithRow['col37'], "https://www.drugbank.ca/drugs/", "#ff00b8")
        ithNewRow['VSD_DN'] = colorNAString(ithRow['col38'])
        ithNewRow['VSD_DT'] = colorNAString(ithRow['col39'])

        ithNewRow['VSD_PGT'] = colorNAString(ithRow['col41'])

        ithNewRow['BRP_Ensembl_Pro'] = applyENSPLink(ithRow['col43'])
        ithNewRow['BRDR_PharmGKB'] = applyPharmGKBLink(ithRow['col44'])

        ithNewRow['BRDR_CHEMBL'] = applyChemblLink(ithRow['col46'])
        ithNewRow['BRB_STRING'] = colorNAString(ithRow['col47'])
        ithNewRow['BRP_PDB'] = applyPDBLink(ithRow['col48'])
        ithNewRow['BRG_HGNC'] = applyLink(ithRow['col49'], "https://www.genenames.org/cgi-bin/gene_symbol_report?hgnc_id=", "#13a")
        ithNewRow['BRG_GS'] = applyLink(ithRow['col50'], "https://www.genenames.org/cgi-bin/search?search_type=all&search=", "#13a")
        ithNewRow['BRG_GD'] = colorNAString(ithRow['col51'])
        ithNewRow['BRG_GF'] = colorNAString(ithRow['col52'])
        ithNewRow['BRB_ENA'] = applyENALink(ithRow['col57'])
        ithNewRow['BRG_Entrez'] = applyLink(ithRow['col54'], "https://www.ncbi.nlm.nih.gov/gene/", "#369")
        ithNewRow['BRB_Vega'] = applyVegaLink(ithRow['col55'])
        ithNewRow['BRG_UCSC'] = colorNAString(ithRow['col56'])
        ithNewRow['BRG_ERA'] = applyENALink(ithRow['col57'])
        ithNewRow['BRG_RefSeq'] = applyLink(ithRow['col58'], "https://www.ncbi.nlm.nih.gov/nuccore/", "#369")
        ithNewRow['BRL_PMID'] = applyPubMedLink(ithRow['col59'])
        ithNewRow['BRG_GCosmic'] = applyLink(ithRow['col60'], "http://cancer.sanger.ac.uk/cosmic/gene/analysis?ln=", "#28446f")
        ithNewRow['BRPH_Omim'] = applyOMIMLink(ithRow['col61'])

        theNewRows.append(ithNewRow)
        pass
    #colorNA(theNewRows)
    return theNewRows

def dataTupleToDictList(theTuple):
    theList = []
    for ithData in theTuple:
        theData = dict()
        idx = 0
        for jth in ithData:
            theData['col'+str(idx-1)] = jth
            idx = idx+1
            pass
        theList.append(theData)
        pass
    return theList



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Search query data from SAAVpedia DB')
    parser.add_argument('--url', dest='url', help='DB url')
    parser.add_argument('--user', dest='user', help='username')
    parser.add_argument('--password', dest='password', help='password')
    parser.add_argument('--db', dest='db', help='Database name')
    parser.add_argument('--table', dest='table', help='Table name')
    parser.add_argument('--input', dest='input', help='Input data')
    args = parser.parse_args(sys.argv[1:])
    #print '????'+str(args.input)
    if not args.url or not args.user or not args.password or not args.db or not args.table or not args.input:
        parser.print_help()
    else :
        main(theUrl=args.url, theUser=args.user, thePassword=args.password, theDB=args.db, theTable=args.table, theInput=args.input)
    pass


