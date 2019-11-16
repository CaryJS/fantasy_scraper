# Passing Keys
""" ["GP", "CMP", "ATT", "CMP%", "PASSYDS", "PASSAVG", "PASSTD", "INT", "PASSLNG", "SACK", "FUM", "RTG", "QBR" """

# Rushing Keys
""" ["GP", "RUSHATT", "RUSHYDS", "RUSHAVG", "RUSHTD", "RUSHLNG", "RUSHFD", "RUSHFUM", "RUSHLST"] """

# Receiving Keys
""" ["GP", "REC", "TGTS", "RECYDS", "RECAVG", "RECTD", "RECLNG", "RECFD", "RECFUM", "RECLST"] """

class PlayerBuilder:

    def __init__(self):
        self.player_stats = []

    def build_player_stats(self, player_names, player_years, rushing_stats, receiving_stats, passing_stats):
        '''
        This takes in all of the rushing, receiving, and passing stats, and is intended to build them into
        a format suitable for saving to file. Once saved to file, another method can be run to organize the
        file data into SQL Server. Delete the following items

        Rushing GP
        Receiving GP

        Build the following Master dict:
        {player ID, player name, year, passing stats, rushing stats, receiving stats}

        Each player is represented by a list of dicts, where each dict represents a year.

        In SQL, each table is a player, each column is a year, and each row is a key. Need the key source to be
        able to tell what stat that is.

        '''
