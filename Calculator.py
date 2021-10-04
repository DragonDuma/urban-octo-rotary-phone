meter = 3.2808399
def distance_in_meters(foot = 1):
    calculate = float(input('Enter your measurement in imperial:'))
    if calculate < 1:
        print(f'{calculate} of a foot is')
    if calculate == 1:
        print(f'{calculate} foot is')
    if calculate > 1:
        print(f'{calculate} feet is')
    print((foot * calculate) / meter, 'meters')

running = True
while running:
    distance_in_meters()

