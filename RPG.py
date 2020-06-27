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
        self.name=''
        self.message=''
    def __repr__(self):
        None
    def use(self,target):
        return('This item cannot be used.')

class Potion(Item):
    def __init__(self):
        self.hp=10
        self.name='Potion'
        self.message=f'Recovered {self.hp} HP!'
    def __repr__(self):
        return(self.name)
    def use(self,target):
        temp=target.hp
        temp+=self.hp
        if temp!=target.maxhp:
            if temp<target.maxhp:
                target.hp+=self.hp
                return(self.message)
            elif temp>target.maxhp:
                temp-=target.maxhp
                target.hp+=temp
                return(self.message)
        else:
            return(super().use(target))

class SuperPotion(Potion):
    def __init__(self):
        self.hp=25
        self.name='Super Potion'
    def __repr__(self):
        return(super().__repr__())
    

Potion=Potion()
SuperPotion=SuperPotion()
test=Player('ww',11,182,11,11,11,11,11,11,11,*[SuperPotion])
print(SuperPotion)
print(test.use_item(SuperPotion))



