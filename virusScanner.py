import time
import os
import sys

rootdir = sys.argv[1]
filesToSearch = []
filesByte = []
filesToDelete = []

def search(startpath):
    global filesToSearch
    global filesByte
    for root, dirs, files in os.walk(startpath):
        #level = root.replace(startpath, '').count(os.sep)
        #indent = ' ' * 4 * (level)
        #print('{}{}/'.format(indent, os.path.basename(root)))
        #subindent = ' ' * 4 * (level + 1)
        for f in files:
            filePath = os.path.join(root, f)
            fileSize = os.path.getsize(filePath)      
            extention = f[len(f)-3:len(f)]
            #print('{}{} - {} bytes'.format(subindent, f,fileSize))
            if(extention == "exe"):
                if(fileSize>580000 and fileSize<=590000):
                    filesByte.append(fileSize)
                    filesToSearch.append(filePath)

print "Aranacak Klasor: ", rootdir
if(os.path.isdir(rootdir)):
    if("e" == raw_input("Devam edeyim mi? (e/h) ")):
        search(rootdir)
        print "Tarama tamamlandi... ", len(filesByte), " aday dosya bulundu..."
        if("e" == raw_input("Devam edeyim mi? (e/h) ")):
            if(len(filesByte)>0):
                for (i, item) in enumerate(filesByte):
                    filesMatching = filesToSearch[i].split("/")
                    folderName = filesMatching[-2] 
                    fileName = filesMatching[-1]
                    print folderName,fileName[:-4]
                    if(folderName == fileName[:-4]):
                        filesToDelete.append(filesToSearch[i])
                    #print i, item, filesToSearch[i]
                print "Ayiklama tamamlandi...%d dosya bulundu..." %(len(filesToDelete))
                fileOutput = open("output.txt","w")                
                for item in filesToDelete:
                    fileOutput.write("%s\n" % item)
                    if(os.path.getsize(item) == 585728):
                        os.remove(item)
                fileOutput.close()

else:
    print "Lokasyon hatali"

