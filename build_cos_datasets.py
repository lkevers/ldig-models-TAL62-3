#!/usr/bin/python3
#coding=utf-8

import sys

#
# This script is released under the MIT Licence.
#
# This script can be used to generate several LEARN/TEST sets from Corsican (cos) data 
#
# USAGE : python3 build_cos_datasets.py
#


# for loading corpus, we need the preprocessed and one doc per line formated corpus
#    + exclusion list 
corpusFile1="corsican-apiazzetta/aPiazzetta_01-12-2008_12-11-2019_TEI.xml_oneDocPerLine.txt"
exclFile1="corsican-apiazzetta/aPiazzetta_exclude.lst"
corpusFile2="corsican-wikipedia/cowiki-20191020-pages-articles_CORR_TEI.xml_oneDocPerLine.txt"
exclFile2="corsican-wikipedia/cowiki_exclude.lst"
corpusFile3="corsican-asacrabibbia/BibleBilingueCorseFrancais2015_co_TEI_oneDocPerLine.txt"
exclFile3="corsican-asacrabibbia/bible_exclude.lst"
outDir="corsican"

lg="cos"



def outputFile (fname, text) :
    with open(fname, "w") as fOut :
        fOut.write(text)
    fOut.close()


# -- Explode a sentence (between 200 and 300 chars) into two fragments (more or less of the same length)
def cutinto2 (str) :
    sentList=[]
    elems=str.split(" ")
    sentList.append((' '.join(elems[0:int(len(elems)/2)])).strip())
    sentList.append((' '.join(elems[int(len(elems)/2):len(elems)])).strip())
    return sentList


# -- Explode a long sentence (more than 300 chars) into several shortest fragments (around 200 chars)
def cut200chars (str) :
    sentList=[]
    sentBuffer=""
    elems=str.split(" ")
    for tok in elems :
        if len(sentBuffer)>195 :
            sentList.append(sentBuffer.strip())
            sentBuffer=""
        sentBuffer="%s %s"%(sentBuffer,tok)
    return sentList


def buildFrom50 (target, idx50, len50, setId, idList, corpId) :
    global sentList50
    tmpTarget=0 # nbChars
    tmpTxt=''
    while tmpTarget<target and idx50<len50 :
        if sentList50[idx50][3]==0 :
            tmpTxt="%s %s"%(tmpTxt,sentList50[idx50][2])
            sentList50[idx50][3]=setId
            tmpTarget+=sentList50[idx50][1]
            idList.append("corp0%s-%s"%(corpId,int(sentList50[idx50][0])))
        idx50+=1
    return (tmpTxt,idx50, idList)


def buildFromSmaller (target, sentList, idx, len, setId, idList, corpId) :
    tmpTarget=0 # nbChars
    tmpTxt=''
    tmpIds=''
    while tmpTarget<target and idx<len :
        if sentList[idx][3]==0 :
            if tmpIds=='' :
                tmpIds="%s"%idx
            tmpTxt="%s %s"%(tmpTxt,sentList[idx][2])
            sentList[idx][3]=setId
            tmpTarget+=sentList[idx][1]
            idList.append("corp0%s-%s"%(corpId,int(sentList[idx][0])))
        idx+=1
    tmpIds="%s_%s"%(tmpIds,(idx-1))
    return (tmpTxt, sentList, idx, idList, tmpIds)


def loadCorpus (corpId, corpusFile, excludeFile) :
    global sentList50, sentList300, sentList3000, sentListGreater
    global nbChar50, nbChar300, nbChar3000, nbCharGreater
    sentList50.append([]) # ID, length, text, test_status (0=unused; 1=in set number 1; ...); learn_status (number of the latest learn set where the doc is incorporated)
    sentList300.append([])
    sentList3000.append([])
    sentListGreater.append([])
    nbCharTot.append(0)
    nbChar50.append(0)
    nbChar300.append(0)
    nbChar3000.append(0)
    nbCharGreater.append(0)
    toExclude=[]
    with open(excludeFile,"r") as fExcl :
        for line in fExcl:
            toExclude.append(line.strip())
    fExcl.close()
    i=1
    with open(corpusFile,"r") as fCorp :
        for line in fCorp:
            #docIdx=str(i).ljust(7,"0")
            docIdx=str(i).rjust(7,"0")
            if docIdx not in toExclude :
                elems=line.strip().split("\t")
                strLen=len(elems[1])
                nbCharTot[corpId]+=strLen
                if strLen <= 50 :
                    sentList50[corpId].append([docIdx,strLen,elems[1],0,0])
                    nbChar50[corpId]+=strLen
                elif strLen <= 300 :
                    sentList300[corpId].append([docIdx,strLen,elems[1],0,0])
                    nbChar300[corpId]+=strLen
                elif strLen <= 3000 :
                    sentList3000[corpId].append([docIdx,strLen,elems[1],0,0])
                    nbChar3000[corpId]+=strLen
                else:
                    sentListGreater[corpId].append([docIdx,strLen,elems[1],0,0])
                    nbCharGreater[corpId]+=strLen
            i+=1
    fCorp.close()

# ---------


# -- generate one unique set
def generateSet (setId, fp_50, fp_300, fp_3000, fp_greater, fp_learnmin, fp_learnmax, idList, idListLearn) :

    global sentList50, sentList300, sentList3000, sentListGreater
    global outDir, lg
    outDirSet="%s/set0%s/test"%(outDir,setId)
    progress=0
    idx50=[0,0,0]
    len50=[len(sentList50[0]),len(sentList50[1]),len(sentList50[2])]
    stats50=[0,0]
    idx300=[0,0,0]
    len300=[len(sentList300[0]),len(sentList300[1]),len(sentList300[2])]
    stats300=[0,0]
    idx3000=[0,0,0]
    len3000=[len(sentList3000[0]),len(sentList3000[1]),len(sentList3000[2])]
    stats3000=[0,0]
    idxGreater=[0,0,0]
    lenGreater=[len(sentListGreater[0]),len(sentListGreater[1]),len(sentListGreater[2])]
    statsGreater=[0,0]

    while progress < target : # FIRST, reach the target for the TEST set

        # Browse the 3 data sources
        for i in range (0,3) :
            # prendre dans sentList50
            while idx50[i]<len50[i] and sentList50[i][idx50[i]][3]!=0 :
                idx50[i]+=1
            if idx50[i]<len50[i] :
                if sentList50[i][idx50[i]][1] > 5 : # min 5 chars !
                    fp_50.write("%s\t%s\n"%(lg,sentList50[i][idx50[i]][2]))
#                    outputFile("%s/50/corp0%s_%s.txt"%(outDirSet,i,sentList50[i][idx50[i]][0]),sentList50[i][idx50[i]][2])
                    progress+=sentList50[i][idx50[i]][1]
                    sentList50[i][idx50[i]][3]=setId
                    stats50[0]+=1
                    stats50[1]+=sentList50[i][idx50[i]][1]
                    idList.append("corp0%s-%s"%(i,int(sentList50[i][idx50[i]][0])))
                idx50[i]+=1

            if progress > target :
                break

            # prendre dans sentList300
            while idx300[i]<len300[i] and sentList300[i][idx300[i]][3]!=0 :
                idx300[i]+=1
            if idx300[i]<len300[i] :
                fp_300.write("%s\t%s\n"%(lg,sentList300[i][idx300[i]][2]))
#                outputFile("%s/300/corp0%s_%s.txt"%(outDirSet,i,sentList300[i][idx300[i]][0]),sentList300[i][idx300[i]][2])
                progress+=sentList300[i][idx300[i]][1]
                sentList300[i][idx300[i]][3]=setId
                stats300[0]+=1
                stats300[1]+=sentList300[i][idx300[i]][1]
                idList.append("corp0%s-%s"%(i,int(sentList300[i][idx300[i]][0])))
                idx300[i]+=1
            else : # plus dispo dans sentList300, construire à partir de sentList50
                (tmpTxt,sentList50[i],idx50[i],idList,resIds)=buildFromSmaller(200,sentList50[i],idx50[i],len50[i],setId,idList,i)
                fp_300.write("%s\t%s\n"%(lg,tmpTxt))
#                outputFile("%s/300/corp0%s_%s.txt"%(outDirSet,i,resIds),tmpTxt)
                progress+=len(tmpTxt)
                stats300[0]+=1
                stats300[1]+=len(tmpTxt)

            if progress > target :
                break

            # prendre dans sentList3000
            while idx3000[i]<len3000[i] and sentList3000[i][idx3000[i]][3]!=0 :
                idx3000[i]+=1
            if idx3000[i]<len3000[i] :
                fp_3000.write("%s\t%s\n"%(lg,sentList3000[i][idx3000[i]][2]))
#                outputFile("%s/3000/corp0%s_%s.txt"%(outDirSet,i,sentList3000[i][idx3000[i]][0]),sentList3000[i][idx3000[i]][2])
                progress+=sentList3000[i][idx3000[i]][1]
                sentList3000[i][idx3000[i]][3]=setId
                stats3000[0]+=1
                stats3000[1]+=sentList3000[i][idx3000[i]][1]
                idList.append("corp0%s-%s"%(i,int(sentList3000[i][idx3000[i]][0])))
                idx3000[i]+=1
            elif idx300[i]<len300[i] : # plus dispo dans sentList3000, construire à partir de sentList300
                (tmpTxt,sentList300[i],idx300[i],idList,resIds)=buildFromSmaller(1000,sentList300[i],idx300[i],len300[i],setId,idList,i)
                fp_3000.write("%s\t%s\n"%(lg,tmpTxt))
#                outputFile("%s/3000/corp0%s_%s.txt"%(outDirSet,i,resIds),tmpTxt)
                progress+=len(tmpTxt)
                stats3000[0]+=1
                stats3000[1]+=len(tmpTxt)
            elif idx50[i]<len50[i] : # plus dispo dans sentList3000 ni sentList300, construire à partir de sentList50
                (tmpTxt,sentList50[i],idx50[i],idList,resIds)=buildFromSmaller(1000,sentList50[i],idx50[i],len50[i],setId,idList,i)
                fp_3000.write("%s\t%s\n"%(lg,tmpTxt))
#                outputFile("%s/3000/corp0%s_%s.txt"%(outDirSet,i,resIds),tmpTxt)
                progress+=len(tmpTxt)
                stats3000[0]+=1
                stats3000[1]+=len(tmpTxt)

            if progress > target :
                break

            # prendre dans sentListGreater
            while idxGreater[i]<lenGreater[i] and sentListGreater[i][idxGreater[i]][3]!=0 :
                idxGreater[i]+=1
            if idxGreater[i]<lenGreater[i] :
                fp_greater.write("%s\t%s\n"%(lg,sentListGreater[i][idxGreater[i]][2]))
#                outputFile("%s/greater/corp0%s_%s.txt"%(outDirSet,i,sentListGreater[i][idxGreater[i]][0]),sentListGreater[i][idxGreater[i]][2])
                progress+=sentListGreater[i][idxGreater[i]][1]
                sentListGreater[i][idxGreater[i]][3]=setId
                statsGreater[0]+=1
                statsGreater[1]+=sentListGreater[i][idxGreater[i]][1]
                idList.append("corp0%s-%s"%(i,int(sentListGreater[i][idxGreater[i]][0])))
                idxGreater[i]+=1
            elif idx3000[i]<len3000[i] : # plus dispo dans sentListGreater, construire à partir de sentList3000
                (tmpTxt,sentList3000[i],idx3000[i],idList,resIds)=buildFromSmaller(3000,sentList3000[i],idx3000[i],len3000[i],setId,idList,i)
                fp_greater.write("%s\t%s\n"%(lg,tmpTxt))
#                outputFile("%s/greater/corp0%s_%s.txt"%(outDirSet,i,resIds),tmpTxt)
                progress+=len(tmpTxt)
                statsGreater[0]+=1
                statsGreater[1]+=len(tmpTxt)
            elif idx300[i]<len300[i] : # plus dispo dans sentListGreater ni sentList3000, construire à partir de sentList300
                (tmpTxt,sentList300[i],idx300[i],idList,resIds)=buildFromSmaller(3000,sentList300[i],idx300[i],len300[i],setId,idList,i)
                fp_greater.write("%s\t%s\n"%(lg,tmpTxt))
#                outputFile("%s/greater/corp0%s_%s.txt"%(outDirSet,i,resIds),tmpTxt)
                progress+=len(tmpTxt)
                statsGreater[0]+=1
                statsGreater[1]+=len(tmpTxt)
            elif idx50[i]<len50[i] : # plus dispo dans sentListGreater, ni sentList3000, ni sentList300, construire à partir de sentList50
                (tmpTxt,sentList50[i],idx50[i],idList,resIds)=buildFromSmaller(3000,sentList50[i],idx50[i],len50[i],setId,idList,i)
                fp_greater.write("%s\t%s\n"%(lg,tmpTxt))
#                outputFile("%s/greater/corp0%s_%s.txt"%(outDirSet,i,resIds),tmpTxt)
                progress+=len(tmpTxt)
                statsGreater[0]+=1
                statsGreater[1]+=len(tmpTxt)

        if progress > target :
            break

    print("Total size of TEST %s : %s"%(setId,progress))
    print("Number of docs : %s"%(stats50[0]+stats300[0]+stats3000[0]+statsGreater[0]))
    print("Cat <= 50 chars :")
    print(stats50)
    print("Cat <= 300 chars :")
    print(stats300)
    print("Cat <= 3000 chars :")
    print(stats3000)
    print("Cat > 3000  chars :")
    print(statsGreater)
    print("\n")

    # SECONDLY, extract the limited LEARN data
    nbLines=0
    nbChars=0
    idx50=[0,0,0]
    idx300=[0,0,0]
    idx3000=[0,0,0]
    idxGreater=[0,0,0]
    outDirSet="%s/set0%s/learn_min"%(outDir,setId)
    while nbChars < targetLearn :
        # Browse the 3 data sources
        for i in range (0,3) :
            #print("Progress (%s,%s,%s) : %s"%(idx50,idx300,idx3000,nbChars),end='\r')
            while idx50[i]<len50[i] and sentList50[i][idx50[i]][3]==setId :
                idx50[i]+=1
            if idx50[i]<len50[i] :
                fp_learnmin.write("%s\t%s\n"%(lg,sentList50[i][idx50[i]][2]))
#                outputFile("%s/corp0%s_%s.txt"%(outDirSet,i,sentList50[i][idx50[i]][0]),sentList50[i][idx50[i]][2])
                nbLines+=1
                nbChars+=sentList50[i][idx50[i]][1]
                idListLearn.append("corp0%s-%s"%(i,int(sentList50[i][idx50[i]][0])))
                idx50[i]+=1
            while idx300[i]<len300[i] and sentList300[i][idx300[i]][3]==setId :
                idx300[i]+=1
            if idx300[i]<len300[i] :
                fragments=cutinto2 (sentList300[i][idx300[i]][2])
                for frag in fragments :
                    fp_learnmin.write("%s\t%s\n"%(lg,frag))
                    nbLines+=1
#                outputFile("%s/corp0%s_%s.txt"%(outDirSet,i,sentList300[i][idx300[i]][0]),sentList300[i][idx300[i]][2])
                nbChars+=sentList300[i][idx300[i]][1]
                idListLearn.append("corp0%s-%s"%(i,int(sentList300[i][idx300[i]][0])))
                idx300[i]+=1
            while idx3000[i]<len3000[i] and sentList3000[i][idx3000[i]][3]==setId :
                idx3000[i]+=1
            if idx3000[i]<len3000[i] :
                fragments=cut200chars (sentList3000[i][idx3000[i]][2])
                for frag in fragments :
                    fp_learnmin.write("%s\t%s\n"%(lg,frag))
                    nbLines+=1
#                outputFile("%s/corp0%s_%s.txt"%(outDirSet,i,sentList3000[i][idx3000[i]][0]),sentList3000[i][idx3000[i]][2])
                nbChars+=sentList3000[i][idx3000[i]][1]
                idListLearn.append("corp0%s-%s"%(i,int(sentList3000[i][idx3000[i]][0])))
                idx3000[i]+=1
            while idxGreater[i]<lenGreater[i] and sentListGreater[i][idxGreater[i]][3]==setId :
                idxGreater[i]+=1
            if idxGreater[i]<lenGreater[i] :
                fragments=cut200chars (sentListGreater[i][idxGreater[i]][2])
                for frag in fragments :
                    fp_learnmin.write("%s\t%s\n"%(lg,frag))
                    nbLines+=1
#                outputFile("%s/corp0%s_%s.txt"%(outDirSet,i,sentListGreater[i][idxGreater[i]][0]),sentListGreater[i][idxGreater[i]][2])
                nbChars+=sentListGreater[i][idxGreater[i]][1]
                idListLearn.append("copr0%s-%s"%(i,int(sentListGreater[i][idxGreater[i]][0])))
                idxGreater[i]+=1

    print("Total size LEARNmin %s : %s (chars)"%(setId,nbChars))
    print("Number of lines : %s\n"%nbLines)

    # THIRDLY, extract the full LEARN data
    nbLines=0
    nbChars=0
    idx50=[0,0,0]
    idx300=[0,0,0]
    idx3000=[0,0,0]
    idxGreater=[0,0,0]
    outDirSet="%s/set0%s/learn_max"%(outDir,setId)
    # Browse the 3 data sources
    for i in range (0,3) :
        while (idx50[i]<len50[i]) :
            if (sentList50[i][idx50[i]][3]!=setId) : # was not used in the TEST for this setId
                fp_learnmax.write("%s\t%s\n"%(lg,sentList50[i][idx50[i]][2]))
#                outputFile("%s/corp0%s_%s.txt"%(outDirSet,i,sentList50[i][idx50[i]][0]),sentList50[i][idx50[i]][2])
                sentList50[i][idx50[i]][4]=setId
                nbLines+=1
                nbChars+=sentList50[i][idx50[i]][1]
            idx50[i]+=1
        while (idx300[i]<len300[i]) :
            if (sentList300[i][idx300[i]][3]!=setId) : # was not used in the TEST for this setId
                fragments=cutinto2 (sentList300[i][idx300[i]][2])
                for frag in fragments :
                    fp_learnmax.write("%s\t%s\n"%(lg,frag))
                    nbLines+=1
#                outputFile("%s/corp0%s_%s.txt"%(outDirSet,i,sentList300[i][idx300[i]][0]),sentList300[i][idx300[i]][2])
                nbChars+=sentList300[i][idx300[i]][1]
                sentList300[i][idx300[i]][4]=setId
            idx300[i]+=1
        while (idx3000[i]<len3000[i]) :
            if (sentList3000[i][idx3000[i]][3]!=setId) : # was not used in the TEST for this setId
                fragments=cut200chars (sentList3000[i][idx3000[i]][2])
                for frag in fragments :
                    fp_learnmax.write("%s\t%s\n"%(lg,frag))
                    nbLines+=1
#                outputFile("%s/corp0%s_%s.txt"%(outDirSet,i,sentList3000[i][idx3000[i]][0]),sentList3000[i][idx3000[i]][2])
                nbChars+=sentList3000[i][idx3000[i]][1]
                sentList3000[i][idx3000[i]][4]=setId
            idx3000[i]+=1
        while (idxGreater[i]<lenGreater[i]) :
            if (sentListGreater[i][idxGreater[i]][3]!=setId) : # was not used in the TEST for this setId
                fragments=cut200chars (sentListGreater[i][idxGreater[i]][2])
                for frag in fragments :
                    fp_learnmax.write("%s\t%s\n"%(lg,frag))
                    nbLines+=1
#                outputFile("%s/corp0%s_%s.txt"%(outDirSet,i,sentListGreater[i][idxGreater[i]][0]),sentListGreater[i][idxGreater[i]][2])
                nbChars+=sentListGreater[i][idxGreater[i]][1]
                sentListGreater[i][idxGreater[i]][4]=setId
            idxGreater[i]+=1

    print("Totale size of LEARNmax %s : %s (chars)"%(setId,nbChars))
    print("Number of lines : %s\n"%nbLines)



# ---- MAIN -----

sentList50=[]
sentList300=[]
sentList3000=[]
sentListGreater=[]
nbCharTot=[]
nbChar50=[]
nbChar300=[]
nbChar3000=[]
nbCharGreater=[]

loadCorpus(0,corpusFile1,exclFile1)
loadCorpus(1,corpusFile2,exclFile2)
loadCorpus(2,corpusFile3,exclFile3)

print("\nCorpus loaded (%s) \n"%lg)
print("Nb. Chars tot : %s  [ 0 = %s ; 1 = %s ; 2 = %s ]"%(sum(nbCharTot),nbCharTot[0],nbCharTot[1],nbCharTot[2]))
nbSentTot=len(sentList50[0])+len(sentList50[1])+len(sentList50[2])
print("Nb. sentences (chars) <= 50 chars : %s (%s) [ 0 = %s (%s) ; 1 = %s (%s) ; 2 = %s (%s) ]"%(nbSentTot,sum(nbChar50),len(sentList50[0]),nbChar50[0],len(sentList50[1]),nbChar50[1],len(sentList50[2]),nbChar50[2]))
nbSentTot=len(sentList300[0])+len(sentList300[1])+len(sentList300[2])
print("Nb. sentences (chars) <= 300 chars : %s (%s) [ 0 = %s (%s) ; 1 = %s (%s) ; 2 = %s (%s) ]"%(nbSentTot,sum(nbChar300),len(sentList300[0]),nbChar300[0],len(sentList300[1]),nbChar300[1],len(sentList300[2]),nbChar300[2]))
nbSentTot=len(sentList3000[0])+len(sentList3000[1])+len(sentList3000[2])
print("Nb. sentences (chars) <= 3000 chars : %s (%s) [ 0 = %s (%s) ; 1 = %s (%s) ; 2 = %s (%s) ]"%(nbSentTot,sum(nbChar3000),len(sentList3000[0]),nbChar3000[0],len(sentList3000[1]),nbChar3000[1],len(sentList3000[2]),nbChar3000[2]))
nbSentTot=len(sentListGreater[0])+len(sentListGreater[1])+len(sentListGreater[2])
print("Nb. sentences (chars) > 3000 chars (greater) : %s (%s) [ 0 = %s (%s) ; 1 = %s (%s) ; 2 = %s (%s) ]\n"%(nbSentTot,sum(nbCharGreater),len(sentListGreater[0]),nbCharGreater[0],len(sentListGreater[1]),nbCharGreater[1],len(sentListGreater[2]),nbCharGreater[2]))


target=200000 #nbChars
targetLearn=500000 #nbChars


# create files
fp_1_50=open("%s/corsicanCorp_%s_TEST1_50.txt"%(outDir,lg), "w")
fp_1_300=open("%s/corsicanCorp_%s_TEST1_300.txt"%(outDir,lg), "w")
fp_1_3000=open("%s/corsicanCorp_%s_TEST1_3000.txt"%(outDir,lg), "w")
fp_1_greater=open("%s/corsicanCorp_%s_TEST1_greater.txt"%(outDir,lg), "w")
fp_1_learnmax=open("%s/corsicanCorp_%s_LEARN1_max.txt"%(outDir,lg), "w")
fp_1_learnmin=open("%s/corsicanCorp_%s_LEARN1_min.txt"%(outDir,lg), "w")
fp_1_t_ids=open("%s/corsicanCorp_%s_TEST1_ids.txt"%(outDir,lg),"w")
fp_1_lmin_ids=open("%s/corsicanCorp_%s_LEARN1_min_ids.txt"%(outDir,lg),"w")

fp_2_50=open("%s/corsicanCorp_%s_TEST2_50.txt"%(outDir,lg), "w")
fp_2_300=open("%s/corsicanCorp_%s_TEST2_300.txt"%(outDir,lg), "w")
fp_2_3000=open("%s/corsicanCorp_%s_TEST2_3000.txt"%(outDir,lg), "w")
fp_2_greater=open("%s/corsicanCorp_%s_TEST2_greater.txt"%(outDir,lg), "w")
fp_2_learnmax=open("%s/corsicanCorp_%s_LEARN2_max.txt"%(outDir,lg), "w")
fp_2_learnmin=open("%s/corsicanCorp_%s_LEARN2_min.txt"%(outDir,lg), "w")
fp_2_t_ids=open("%s/corsicanCorp_%s_TEST2_ids.txt"%(outDir,lg),"w")
fp_2_lmin_ids=open("%s/corsicanCorp_%s_LEARN2_min_ids.txt"%(outDir,lg),"w")

fp_3_50=open("%s/corsicanCorp_%s_TEST3_50.txt"%(outDir,lg), "w")
fp_3_300=open("%s/corsicanCorp_%s_TEST3_300.txt"%(outDir,lg), "w")
fp_3_3000=open("%s/corsicanCorp_%s_TEST3_3000.txt"%(outDir,lg), "w")
fp_3_greater=open("%s/corsicanCorp_%s_TEST3_greater.txt"%(outDir,lg), "w")
fp_3_learnmax=open("%s/corsicanCorp_%s_LEARN3_max.txt"%(outDir,lg), "w")
fp_3_learnmin=open("%s/corsicanCorp_%s_LEARN3_min.txt"%(outDir,lg), "w")
fp_3_t_ids=open("%s/corsicanCorp_%s_TEST3_ids.txt"%(outDir,lg),"w")
fp_3_lmin_ids=open("%s/corsicanCorp_%s_LEARN3_min_ids.txt"%(outDir,lg),"w")

fp_4_50=open("%s/corsicanCorp_%s_TEST4_50.txt"%(outDir,lg), "w")
fp_4_300=open("%s/corsicanCorp_%s_TEST4_300.txt"%(outDir,lg), "w")
fp_4_3000=open("%s/corsicanCorp_%s_TEST4_3000.txt"%(outDir,lg), "w")
fp_4_greater=open("%s/corsicanCorp_%s_TEST4_greater.txt"%(outDir,lg), "w")
fp_4_learnmax=open("%s/corsicanCorp_%s_LEARN4_max.txt"%(outDir,lg), "w")
fp_4_learnmin=open("%s/corsicanCorp_%s_LEARN4_min.txt"%(outDir,lg), "w")
fp_4_t_ids=open("%s/corsicanCorp_%s_TEST4_ids.txt"%(outDir,lg),"w")
fp_4_lmin_ids=open("%s/corsicanCorp_%s_LEARN4_min_ids.txt"%(outDir,lg),"w")

fp_5_50=open("%s/corsicanCorp_%s_TEST5_50.txt"%(outDir,lg), "w")
fp_5_300=open("%s/corsicanCorp_%s_TEST5_300.txt"%(outDir,lg), "w")
fp_5_3000=open("%s/corsicanCorp_%s_TEST5_3000.txt"%(outDir,lg), "w")
fp_5_greater=open("%s/corsicanCorp_%s_TEST5_greater.txt"%(outDir,lg), "w")
fp_5_learnmax=open("%s/corsicanCorp_%s_LEARN5_max.txt"%(outDir,lg), "w")
fp_5_learnmin=open("%s/corsicanCorp_%s_LEARN5_min.txt"%(outDir,lg), "w")
fp_5_t_ids=open("%s/corsicanCorp_%s_TEST5_ids.txt"%(outDir,lg),"w")
fp_5_lmin_ids=open("%s/corsicanCorp_%s_LEARN5_min_ids.txt"%(outDir,lg),"w")

idList1=[]
idListLearn1=[]
generateSet(1, fp_1_50, fp_1_300, fp_1_3000, fp_1_greater, fp_1_learnmin, fp_1_learnmax, idList1, idListLearn1)
idList2=[]
idListLearn2=[]
generateSet(2, fp_2_50, fp_2_300, fp_2_3000, fp_2_greater, fp_2_learnmin, fp_2_learnmax, idList2, idListLearn2)
idList3=[]
idListLearn3=[]
generateSet(3, fp_3_50, fp_3_300, fp_3_3000, fp_3_greater, fp_3_learnmin, fp_3_learnmax, idList3, idListLearn3)
idList4=[]
idListLearn4=[]
generateSet(4, fp_4_50, fp_4_300, fp_4_3000, fp_4_greater, fp_4_learnmin, fp_4_learnmax, idList4, idListLearn4)
idList5=[]
idListLearn5=[]
generateSet(5, fp_5_50, fp_5_300, fp_5_3000, fp_5_greater, fp_5_learnmin, fp_5_learnmax, idList5, idListLearn5)

# check intersection (&) of all the test sets
print("Check that TESTx sets are not overlapping (True is OK)")
print(len(list(set(idList1)&set(idList2)))==0)
print(len(list(set(idList1)&set(idList3)))==0)
print(len(list(set(idList1)&set(idList4)))==0)
print(len(list(set(idList1)&set(idList5)))==0)
print(len(list(set(idList2)&set(idList3)))==0)
print(len(list(set(idList2)&set(idList4)))==0)
print(len(list(set(idList2)&set(idList5)))==0)
print(len(list(set(idList3)&set(idList4)))==0)
print(len(list(set(idList3)&set(idList5)))==0)
print(len(list(set(idList4)&set(idList5)))==0)
print("Done\n")

fp_1_t_ids.write('\n'.join([str(int) for int in sorted(idList1)]))
fp_2_t_ids.write('\n'.join([str(int) for int in sorted(idList2)]))
fp_3_t_ids.write('\n'.join([str(int) for int in sorted(idList3)]))
fp_4_t_ids.write('\n'.join([str(int) for int in sorted(idList4)]))
fp_5_t_ids.write('\n'.join([str(int) for int in sorted(idList5)]))
fp_1_lmin_ids.write('\n'.join([str(int) for int in sorted(idListLearn1)]))
fp_2_lmin_ids.write('\n'.join([str(int) for int in sorted(idListLearn2)]))
fp_3_lmin_ids.write('\n'.join([str(int) for int in sorted(idListLearn3)]))
fp_4_lmin_ids.write('\n'.join([str(int) for int in sorted(idListLearn4)]))
fp_5_lmin_ids.write('\n'.join([str(int) for int in sorted(idListLearn5)]))

fp_1_50.close()
fp_1_300.close()
fp_1_3000.close()
fp_1_greater.close()
fp_1_learnmax.close()
fp_1_learnmin.close()
fp_1_t_ids.close()
fp_1_lmin_ids.close()

fp_2_50.close()
fp_2_300.close()
fp_2_3000.close()
fp_2_greater.close()
fp_2_learnmax.close()
fp_2_learnmin.close()
fp_2_t_ids.close()
fp_2_lmin_ids.close()

fp_3_50.close()
fp_3_300.close()
fp_3_3000.close()
fp_3_greater.close()
fp_3_learnmax.close()
fp_3_learnmin.close()
fp_3_t_ids.close()
fp_3_lmin_ids.close()

fp_4_50.close()
fp_4_300.close()
fp_4_3000.close()
fp_4_greater.close()
fp_4_learnmax.close()
fp_4_learnmin.close()
fp_4_t_ids.close()
fp_4_lmin_ids.close()

fp_5_50.close()
fp_5_300.close()
fp_5_3000.close()
fp_5_greater.close()
fp_5_learnmax.close()
fp_5_learnmin.close()
fp_5_t_ids.close()
fp_5_lmin_ids.close()


