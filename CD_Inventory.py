#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# Vgurasashvili, 2020-Sep-03, created file
# Vgurasashvili, 2020-Sep-07, added pseudocode to complete assignment 08
#------------------------------------------#

# -- DATA -- #
import pickle
strFileName = 'cdInventory.txt'
Bnr_Filename = 'cdInventory.dat'
lstOfCDObjects = []
CD_total = ''


class CD:
    """Stores data about a CD:    

        properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

        """

    """Add data to the table"""
    def __init__(self,data):
        self.__cd_id = data[0]
        self.__cd_title = data[1]
        self.__cd_artist = data[2]
    
    def __str__(self):
        return '{} {} {}'.format(self.__cd_id, self.__cd_title, self.__cd_artist)
    
    def apnd(self,table):
        data = self.__cd_id, self.__cd_title, self.__cd_artist
        table.append(data)
        return table

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        : -> None
        load_inventory(file_name): -> (a list of CD objects)"""
    @classmethod
    def read_file(cls,FileName, table):
        table.clear()
        with open(FileName, 'r') as objFile:
            for line in objFile:
                data = line.strip().split(',')
                table.append(data)

    """save_inventory(file_name, lst_Inventory)"""

    @classmethod
    def write_file(cls,FileName, lstTbl):
        # 3.6.2.1 save data
            objFile = open(FileName, 'a')
            for row in lstTbl:
                row = str(row)
                objFile.write(row + '\n')
            objFile.close()
            print('data successfully saved'.upper())
        
    @classmethod
    def pickle_processor_dump(cls,FileName, table):
        with open(FileName, 'wb') as objFile:
            pickle.dump(table, objFile)

    @classmethod
    def pickle_processor_load(cls,FileName, table):
        table.clear()
        try:
            with open(FileName, 'rb') as objFile:
                data = pickle.load(objFile)
                table.extend(data)
        except FileNotFoundError as e :
            print()
            print('File Not Found')
            print(e)
            print()
            print()
# -- PRESENTATION (Input/Output) -- #
class IO:
    
    """  Show menu to user """
    
    """  Main Menu  """
    @staticmethod
    def print_menu():
        print()
        print()
        print('{:*^60}'.format('Welcome To CD_Inventory Menu'))
        print()
        print('{:@^60}'.format('  Please Make Your Choice  '))
        print("""
              A) ADD NEW ENTRY
              
              I) DISPLAY CURRENT INVENTORY

              S) SAVE DATA TO fILE
              
              L) LOAD DATA FROM FILE
          
              B) LOAD/DUMP TO/FROM FILE IN BINARY MODE
              
              X) EXIT tHE PROGRAMM
                                              """)
      
        """  Get CD data from user """
    
    def menu_choice(self):
        while True :
            value = input('Which operation would you like to perform? [l, a, i, d, b, s or x]: ')
            if IO.__checkValue(value):
                self.__choice = value
                return self.__choice
                break
            else : print('You Incorrect Value')
    
    def __checkValue (value):
        if value in ['l', 'a', 'i', 'd', 's', 'x','b']: 
            return True
        else: return False
    
    
    def __user_input(self):
        self.__intID = ''
        self.__strTitle = '' 
        self.__stArtist = ''
        
    def setattr(self):
        while True:  
            try:
                self.__intID = int(input('Enter ID: ').strip())
                self.__strTitle = input('What is the CD\'s title? ').strip()
                self.__stArtist = input('What is the Artist\'s name? ').strip()
                break
            except ValueError as v:
                print()
                print('The Id You Entered Is Not A Number')
                print()
                print(v)
  
    def getattr(self):
        return self.__intID, self.__strTitle, self.__stArtist
    @staticmethod    
    def show_inventory(table):
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        CD.total = 0
        for i in table:
            CD.total+=1
            print('{:<6}{:^15}{:>10}'.format(i[0], i[1], i[2]).strip('(').strip(')'))
        print()
        print('Totla Entries Number is : {}'.format(CD.total))
        print('======================================')
    @staticmethod    
    def pickle_Choice():
        print(' please choose to load/dump data from/to file'.title())
        print()
        print('for save data to file press : "s"\n\n'.upper() + 'for load data press : "l"'.upper())
        print()
        Usr_Choice = input()
        return Usr_Choice.lower()

# -- Main Body of Script -- #
#FileProcessor.read_file(strFileName, lstTbl)
while True:
    
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
     # 3. Process menu selection
    dtpl = IO()
    strChoice = dtpl.menu_choice()
    
   # 3.1 process exit first
    if strChoice == 'x':
        break

    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled  :')
        if strYesNo.lower() == 'yes':
            lstOfCDObjects.clear()
            print('reloading...')
            FileIO.read_file(strFileName, lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')

#       continue  # start loop back at top.

    # 3.3 process add a CD
    elif strChoice == 'a':
#        dtpl = IO()
        dtpl.setattr()
        cd1=CD(dtpl.getattr())
        cd1.apnd(lstOfCDObjects)
        print(lstOfCDObjects)
        continue  # start loop back at top.

    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.

    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            FileIO.write_file(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    elif strChoice == 'b':        
        
        Usr_choice=IO.pickle_Choice()
       
        if Usr_choice == 's':
            FileIO.pickle_processor_dump(Bnr_Filename, lstOfCDObjects)
            continue
        
        elif Usr_choice == 'l':
            FileIO.pickle_processor_load(Bnr_Filename, lstOfCDObjects)
            continue
    else:
        print('General Error')


