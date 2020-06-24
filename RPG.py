class Player:
    def __init__(self,name,atk,defense,spd,luck,wallet,exp,level,*inventory):
        self.name=name
        self.atk=atk
        self.defense=defense
        self.spd=spd
        self.luck=luck
        self.wallet=wallet
        self.inventory=list(inventory)
        self.exp=exp
        self.level=level
    
    def __repr__(self):
        return(f'''
        {self.name}
        Attack:{self.atk}
        Defense:{self.defense}
        Speed:{self.spd}
        Luck:{self.luck}
        Wallet:{self.wallet}
        Inventory:{self.inventory}
        EXP:{self.exp}
        Level:{self.level}
        ''')

#class Item(self,name)