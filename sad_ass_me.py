def change(personality):
    skeeper = []
    for i in personality:
        if len(i) > 5:
            skeeper.append('Skeeper is very angry')
        elif len(i) > 5:
            if i.startswith('C') == True:
                skeeper.append('Skeeper might be cool afterall')
            elif len(i) < 5:
                skeeper.append('Skeeper is okay')
            else:
                skeeper.append('Skeeper doesnt know')
        else:
            skeeper.append('Find skeeper, Talk to Him. He is not okay')

    for i in skeeper:
        print(i)


def tradeoffs()
        
personality = ['calm', 'cool', 'confused', 'angry', 'hurt', 'intimidated', 'frustrated', 'open-minded', 'nulls']

change(personality)

