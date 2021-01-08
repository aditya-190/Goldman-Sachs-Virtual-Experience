import os

CURRENT_LOCATION = os.getcwd()
INPUT_FILE_LOCATION = os.path.join(CURRENT_LOCATION, r'Input/inputFile.txt')
OUTPUT_FILE_LOCATION = os.path.join(CURRENT_LOCATION, r'Output')
DICTIONARY_FILE_LOCATION = os.path.join(CURRENT_LOCATION, r'Dictionary/wordlist.txt')

hashedPassword = ""
with open(OUTPUT_FILE_LOCATION + "/crackIt.txt" , "a") as outputFile:
   with open(INPUT_FILE_LOCATION, "r") as inputFile:
      for line in inputFile:
         hashedPassword = line.strip().split(':')[1]
         outputFile.write(hashedPassword + "\n")

os.system("hashcat -m 0 " + OUTPUT_FILE_LOCATION + "/crackIt.txt " +  "-o " + OUTPUT_FILE_LOCATION + "/outputFile.txt " + DICTIONARY_FILE_LOCATION + "/wordlist.txt " + "--show")
print("Check Output Folder for cracked passwords :)")