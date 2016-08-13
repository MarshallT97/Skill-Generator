import random

class Skills:
    ''' Create a new skill

        Use display_status method to create a description
        of the skill from what it skill name is,
        how much damage it can do,
        mana reqirement, and
        what level is require to use the skill     
    '''
    def __init__(self,name,damage,mana,available):
        self.name = name
        self.damage = damage
        self.mana = mana
        self.available = available
        
    def display_status(self):
        print()
        print(('Skill Name: ' + self.name))
        print()
        print(('Status of ' + self.name + ':'))
        print(('Damage: ' + str(self.damage)))
        print(('Mana: ' + str(self.mana)))
        print(('Level Reqirement: ' + str(self.available)))
        print()

def name_remover(names):
    ''' Returns and remove a random skill name from array of skills '''
    name = random.choice(name)
    names.remove(name)
    return name

def display_status(class_name):
    class_name.display_status()

def random_skills():
    ''' Takes names of skills from the the skillsname text file'''
    skill_names = []
    
    with open('skillsname.txt') as names:
        for lines in names:
            names_fix = lines.strip('\n')
            skill_names.append(names_fix)
        names.close()
    num = eval(input('How many skills you would like to generate?:'))
    
    try:
        int(num) + 1
    except:
        num = 1
        
    if int(num) > len(skill_names):
        num = len(skill_names)
        
    for x in range(int(num)):
        name = name_remover(skill_name)
        damage = random.randrange(100,300)
        mana = random.randrange(1,100)
        level = random.randrange(1,50)
        skill = Skills(name,damage,mana,level)
        display_status(skill)
 
random_skills()
