print('To play this game type the bolded words in all caps to choose your option.')


opt1=input('You find yourself waking up, stranded in the middle of the forest.\n\
            You can hear the river flowing up hill and downhill through the trees you can see the ocean.\n\
            Do you climb to the "RIVER" walk down to the "OCEAN" or do you "SIT"still and do nothing?')

if opt1 == ('RIVER'):
    opt2a=input('As you approach the river you find yourself incredibly thirsty and discover\n\
                a small dilapatated shack on the other side.\n\
                Do you "DRINK" from the river or do you cross the river and enter the "SHACK"')
elif opt1 == ('OCEAN'):
    opt2b=input('As you come to the ocean you find yourself incredibly thirsty\n\
            it was a furthur walk than you thought. As you look around there is an\n\
            endless ocean in front of you and endless forested beaches on either side of you.\n\
            Do you drink from the "WATER" or "WANDER" the beaches?')
elif opt1 == ('SIT'):
    print('As your frined screeches "FOUND YOU" unbearably loud your memories come rushing back.\n\
                Your in the forest behind your house playing hide and go seek with You, Are, and Dumb;)')
else:
    print('You wake up from your nightmare in a cold sweat.')

if opt1 == ('RIVER'):
    if opt2a == ('DRINK'):
        opt3a = input('You feel your thirst quenched but the water tasted somewhat tinged.\n\
                 After you gag from the taste you tunr around and see a bear only 20 feet away from you.\n\
                   Do you "ATTACK" the bear or "FLEE" from it?')
    elif opt2a == ('SHACK'):
        opt3b = input('As you creep into the shack it is as you expected... empty.\n\
                  On your way out you catch your hand on a rusty nail and it sears in pain.\n\
                      Do you "SCREAM" or try and "WASH" it in the river.')
else:
        print('You wake up from your nightmare in a cold sweat.')

if opt1 == ('OCEAN'):
    if opt2b == ('WATER'):
        print('You feel your insides welch in upon themselves making you only more thirsty so you keep drinking\n\
          until you cant drink anymore and you eventually die of dehydration.')
    elif opt2b == ('WANDER'):
        opt3c = input('You go off wandering the beach leaving behind the sound of the river.\n\
                 You continue in one direction until you can hear the sound of another river.\n\
                 Your feeling tired, do you continue to "MEANDER" or do you go to the "RIVER"?')
    else:
        print('You wake up from your nightmare in a cold sweat.')

if opt1 == ('RIVER'):
    if opt2a == ('DRINK'):
        if opt3a == ('ATTACK'):
            print('You charge at the bear and beat it and as you do you hear it begin to scream.\n\
        It turns out it was a human in a bear costume. You get sent off to jail for assault.')
        if opt3a == ('FLEE'):
            print('You turn and you sprint as fast as you can. You think that it was wierd that the bear did not chase you.\n\
        You think nothing of it as you run and never look back, never to be heard from again.')
else:
    print('You wake up from your nightmare in a cold sweat.')

if opt1 == ('RIVER'):
    if opt2a == ('shack'):
        if opt3b == ('SCREAM'):
            print('As you scream in pain a bear comes tumbling into the shack. You scream even louder\n\
        before it takes off it\'s head and it is just a man in a costume. He takes you to the hospital\n\
        where the infection kills you.')
        if opt3b == ('WASH'):
            print('You wash your wound and then you realize you can hear cars. You reach the road\n\
       where you get a ride to the hospital and you get fixed before you head back home.')
else:
    print('You wake up from your nightmare in a cold sweat.')

if opt1 == ('OCEAN'):
    if opt2b == ('WANDER'):
        if opt3c == ('MEANDER'):
            print('You meader the beach untill you hear the osund of cars. Exasperatingly you make your way to the sound\n\
            As you get within sight of the road just inside the tree line you collapse of exauhstion.\n\
                There your body is found a week later.')
        if opt3c == ('RIVER'):
            print('As you proceed to the river you remember your surroundings. This is where you started.\n\
        Exausted you collapse and contemplate everything you\'ve done before you give up the ghost.')
else:
    print('You wake up from your nightmare in a cold sweat.')