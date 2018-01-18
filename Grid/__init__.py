class Grid():
    '''Create and manipulate grid object'''

    def __init__(self,rows=2,cols='',fill=0):
        if cols:
            self.__grid = [[fill for x in range(cols)] for x in range(rows)]
            self.fill = fill
        else:
            self.__grid = [[fill for x in range(rows)] for x in range(rows)]
            self.fill = fill

    def __repr__(self):
        return 'Grid(%d,%d)' % (len(self.__grid), len(self.__grid[0]))

    def show(self):
        '''Returns current grid'''

        return self.__grid

    def pshow(self):
        '''Pretty prints grid'''

        for i in range(len(self.__grid)):
            print(self.get_row(i))

    def add_row(self,row='end',num=1):
        '''Adds row(s) - defaults to 1 row at end of grid'''

        row_len = len(self.__grid[0])
        for i in range(num):
            if row == 'end':
                self.__grid.append([self.fill]*row_len)
            else:
                self.__grid.insert(row,[self.fill]*row_len)
        self.pshow()

    def add_col(self,col='end',num=1):
        '''Adds col(s) - defaults to 1 at end of grid'''

        for i in self.__grid:
            for j in range(num):
                if col == 'end':
                    i.append(self.fill)
                else:
                    i.insert(col,self.fill)
        self.pshow()

    def fill_headers(self,args):
        '''Adds headers'''

        try:

            if len(args) > len(self.__grid[0]):
                print('\nWarning: Not enough columns to capture data\nDiscarded: ' + str(args[len(self.__grid[0]):])+ '\n')

            for i,v in enumerate(self.__grid[0]):
                self.__grid[0][i] = args[i]

            self.pshow()

        except IndexError:
            pass

    def fill_col(self, col, args, exh=False):
        '''Fills specified rows with specified values'''

        try:

            if exh == True:
                if len(args) > len(self.__grid)-1:
                    print('\nWarning: Not enough columns to capture data\nDiscarded: ' + str(args[len(self.__grid)-1:])+ '\n')
            else:
                if len(args) > len(self.__grid):
                    print('\nWarning: Not enough columns to capture data\nDiscarded: ' + str(args[len(self.__grid):])+ '\n')

            for i,v in enumerate(self.__grid):
                if exh == True:
                    self.__grid[i+1][col] = args[i]
                else:
                    self.__grid[i][col] = args[i]

        except IndexError:
            pass

        self.pshow()

    def fill_col_all(self, col, val, exh=False):
        '''Fills specified column with single specified value'''

        try:
            if exh == True:
                for i,v in enumerate(self.__grid):
                    self.__grid[i+1][col] = val
            else:
                for i,v in enumerate(self.__grid):
                    self.__grid[i][col] = val

        except IndexError:
            pass

        self.pshow()

    def fill_row(self, row, args, exh = False):
        '''Fills specified row with specified values'''

        try:

            if exh == True:
                if len(args) > len(self.__grid[row])-1:
                    print('\nWarning: Not enough columns to capture data\nDiscarded: ' + str(args[len(self.__grid[0])-1:])+ '\n')
            else:
                if len(args) > len(self.__grid[row]):
                    print('\nWarning: Not enough columns to capture data\nDiscarded: ' + str(args[len(self.__grid[0]):])+ '\n')

            for i,v in enumerate(self.__grid[row]):
                if exh == True:
                    self.__grid[row][i+1] = args[i]
                else:
                    self.__grid[row][i] = args[i]

        except IndexError:
            pass

        self.pshow()

    def fill_row_all(self, row, val, exh=False):
        '''Fills specified row with single specified value'''

        try:

            if exh == True:
                for i,v in enumerate(self.__grid[row]):
                    self.__grid[row][i+1] = val
            else:
                for i,v in enumerate(self.__grid[row]):
                    self.__grid[row][i] = val

        except IndexError:
            pass

        self.pshow()

    def fill_cell(self, row, col, value):
        '''Fills specified cell (row,col) with specified value'''

        try:
            self.__grid[row][col] = value
            self.pshow()
        except IndexError:
            print('\nError: Cell (%d,%d) not in range of grid\n' % (row,col))

    def get_row(self,row):
        '''Retrieves specified row'''

        try:
            return self.__grid[row]
        except IndexError:
            print('\nError: Row %d does not exist\n' % (row))

    def get_col(self,col):
        '''Retrieves specified column'''

        try:
            column = [x[col] for x in self.__grid]
            return column
        except IndexError:
            print('\nError: Row %d does not exist\n' % (col))

    def get_cell(self, row, col):
        '''Retrieves specified cell'''

        try:
            return self.__grid[row][col]
        except IndexError:
            print('\nError: Cell (%d,%d) does not exist\n' % (row,col))

    def remove_row(self, row):
        '''Removes specified row'''

        if len(self.__grid) < 2:
            print('\nError: Cannot reduce rows to zero length\n')
        else:
            try:
                del self.__grid[row]
                self.pshow()

            except IndexError:
                print('\nRow %d does not exist\n' % (row))

    def remove_col(self, col):
        '''Removes specified column'''

        if len(self.__grid[0]) < 2:
            print('\nError: Cannot reduce columns to zero length\n')
        else:
            try:
                for i in self.__grid:
                    del i[col]
                self.pshow()

            except IndexError:
                print('\nRow %d does not exist\n' % (row))

    def clear_cell(self, row, col):
        '''Clears specified cell'''

        try:
            self.__grid[row][col] = self.fill
            self.pshow()

        except IndexError:
            print('\nCell (%d,%d) not in cell range\n')


    def get_attrs(self,attr=''):
        '''Retrieves current grid attribures'''

        attrs = {
                        'row-size': len(self.__grid),
                        'col-size': len(self.__grid[0]),
                        'headers': [x for x in self.__grid[0]]
        }

        if attr:
            try:
                return attrs[attr]
            except KeyError:
                print('\nError: Grid does not have attribute ' + attr + '\n')
        else:
            return attrs
