from PLC_Parser import PLC_Parser

class WaysideController ():
    def __init__(self):
        self.wayside_id = 0
        self.PLC_info = PLC_Parser()
        self.authority = []
        self.occupancy = []
        self.switch_positions = []
        self.railway_crossings = []
        self.light_colors = []
        self.statuses = []
        self.suggested_speed = [] #0b00010100 #20 in binary
        self.commanded_speed = []#0b00010100 #20 in binary

    def ParsePLC(self):
        changes = self.PLC_info.parse_PLC(self.switch_positions, self.occupancy, self.authority,self.suggested_speed, self.statuses)
        for change in changes:
            (typeS, bl, val) = change
            if typeS == "S":
                self.make_changes(change, self.switch_positions)
            elif typeS == "A":
                self.make_changes(change, self.authority)
            elif typeS == "R":
                self.make_changes(change, self.railway_crossings)
            elif typeS == "L":
                self.make_light_changes(change, self.light_colors)
            elif typeS == "F":
                self.make_changes(change, self.statuses)
            elif typeS == "CS":
                self.make_changes(change, self.commanded_speed)

    def make_changes(self, change, table):
        t= len(table)
        (typeS, bl, val) = change
        for row in range(t):
            (block, state) = table[row]
            if str(block) == bl:
                table[row] = (bl, val)

    def make_light_changes(self, change, table):
        t= len(table)
        (typeS, bl, val) = change
        if(val[0]=='1'):
            val1 = True
        else:
            val1 = False
        if(val[0]=='1'):
            val2 = True
        else:
            val2 = False

        for row in range(t):
            (block, state1, state2) = table[row]
            if str(block) == bl:
                table[row] = (bl, val1, val2)

    def RunTrackLogic ():
        print('Logic wow')

    #----setters----
    def set_wayside_id(self, wid):
        self.wayside_id = wid
    def set_authority(self, auth):
        self.authority = auth
    def set_occupancy(self, occ):
        self.occupancy = occ
    def set_switch_positions(self, sw):
        self.switch_positions = sw
    def set_railway_crossings(self, rc):
        self.railway_crossings = rc
    def set_light_colors(self, lc):
        self.light_colors = lc
    def set_statuses(self, st):
        self.statuses = st
    def set_suggested_speed(self, ss):
        self.suggested_speed = ss
    def set_commanded_speed(self, cs):
        self.commanded_speed = cs
    def set_PLC (self, plc):
        self.PLC_info.change_PLC_file(plc)

    #----getters----
    def get_wayside_id(self):
        return self.wayside_id
    def get_authority(self):
        return self.authority
    def get_occupancy(self):
        return self.occupancy
    def get_switch_positions(self):
        return self.switch_positions
    def get_railway_crossings(self):
        return self.railway_crossings
    def get_light_colors(self):
        return self.light_colors
    def get_statuses(self):
        return self.statuses
    def get_suggested_speed(self):
        return self.suggested_speed
    def get_PLC (self):
        return self.PLC_info.get_PLC_file()
    def get_commanded_speed (self):
        return self.commanded_speed