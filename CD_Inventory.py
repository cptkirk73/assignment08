#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# akirkland, 2021-March-09, created file
# akirkland, 2021-March-09, completed assignment 08
#------------------------------------------#

# -- DATA -- #
strFileName = 'CDInventory.txt'
lstOfCDObjects = []

class CD():
    """Stores data about a CD:
 
    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
   
    def __init__(self,cd):
        
        self.add_CD = cd
        
    def add_CD(cd_id, cd_title, cd_artist, table):
                
        #Adding to list of dictionaries
        intID = int(cd_id)
        dicRow = {'ID': intID, 'Title': cd_title, 'Artist': cd_artist}
        table.append(dicRow)

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
   
    def __init__(self, inv):
        self.save_inventory = inv
        self.load_inventory = inv
    
    
    @property
    def load_inventory(self, table):
        table.clar()
        objFile = open(strFileName, 'r')
        for line in objFile:
            data = line.strip().split(',')
            dicRow = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
            table.append(dicRow)
        objFile.close()
     
   
    @property
    
    def save_inventory(self,table):
        
        objFile = open(strFileName, 'w')
        strRow = ''
        for item in table:            
            strRow += ("{},{},{}\n".format(*item.values()))
            
        strRow = strRow[:-1] + '\n'
        objFile.write(strRow)
        objFile.close()

# -- PRESENTATION (Input/Output) -- #
class IO:
     
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
    
        choice = ' '
        while choice not in ['l', 'a', 'i','s', 'x']:
            try:
                choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
                print()  # Add extra space for layout
            except: 
                print('ERROR! Please select from the list')
        return choice
    
    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')
   
    @staticmethod    
    def newCdinput():
        
        ''' 
        Args:
            None.

        Returns:
             cd_id, cd_title, cd_artist
        '''

        #Taking in user input 

        while True:
            try:
                
                cd_id = int(input('Enter ID: ').strip())
                break
            except:
                print("ID must be an integer value")
        cd_title = input('What is the CD\'s title? ').strip()
        cd_artist = input('What is the Artist\'s name? ').strip()
        
        return cd_id, cd_title, cd_artist

    pass

# -- Main Body of Script -- #
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        try:
            if strYesNo.lower() == 'yes':
                print('reloading...')
                FileIO.load_inventory(strFileName,lstOfCDObjects)
                FileIO.show_inventory(lstOfCDObjects)
            else:
                input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
                IO.show_inventory(lstOfCDObjects)
            continue # start loop back at top.
        except:
            print('Error File not found')
    # 3.3 process add a CD
    elif strChoice == 'a':
        #Ask user for new ID, CD Title and Artist
        #process display current inventory
       
        cd_id, cd_title, cd_artist = IO.newCdinput()
        CD.add_CD(cd_id, cd_title, cd_artist, lstOfCDObjects)
        continue
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.

    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        try:
            strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        except:
            print('General Error')
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            FileIO.save_inventory(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    
    else:
        print('General Error')


