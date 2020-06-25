class Player:
    def __init__(self,name,health,maxhp,atk,defense,spd,luck,wallet,exp,level,*inventory):
        self.name=name
        self.hp=health
        self.maxhp=maxhp
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
        HP:{self.hp}
        Attack:{self.atk}
        Defense:{self.defense}
        Speed:{self.spd}
        Luck:{self.luck}
        Wallet:{self.wallet}
        Inventory:{self.inventory}
        EXP:{self.exp}
        Level:{self.level}
        ''')
    
    def use_item(self,item):
        if item in self.inventory:
            return(item.use(self))
        else:
           return('That item is not in your inventory!')


class Item:
    def __init__(self,name,message):
        self.name=name
        self.message=''
    
    def __repr__(self):
        None

    def use(self,target):
        return('This item cannot be used.')

class Potion(Item):
    def __init__(self,name,hp,message=None):
        self.hp=hp
        self.name=name
        self.message=f'Recovered {self.hp} HP!'
    def __repr__(self):
        return(f'Potion. Recovers {self.hp} HP.')
    def use(self,target):
        temp=target.hp
        temp+=self.hp
        if temp<target.maxhp:
            target.hp+=10
            return(self.message)
        else:
            return(super().use(target))


Potion=Potion('Potion',10)

test=Player('ww',11,12,11,11,11,11,11,11,11,*[Potion])
print(test.inventory)
print(Potion)
print(test.use_item(Potion))



