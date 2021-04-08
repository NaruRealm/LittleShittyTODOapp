import os
from json import load, dump
import time


def getinfo(ToGet):
    with open('Todo.json') as f:
        x = load(f)
        Todo = x['Todo']
        Done = x['Done']
        if ToGet == "Todo":
            return Todo
        elif ToGet == "Done":
            return Done
        else:
            return x


def changeinfo(x):
    with open('Todo.json', 'w+') as f:
        dump(x, f, indent=4)


def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def Back(Point):
    if Point == 'Todo':
        Todo()
    else:
        Done()


def Reset(ToReset):
    TODO = getinfo("x")
    if ToReset == 'all':
        confirm = input('Are you  sure? Y/n: ')
        if confirm == 'n':
            print('Cancelled')
            time.sleep(1)
            return
        Resetting = TODO['Todo']
        Resetting.clear()
        TODO['Todo'] = Resetting
        Resetting = TODO['Done']
        Resetting.clear()
        TODO['Done'] = Resetting
        changeinfo(TODO)
        return
    confirm = input('Are you  sure? Y/n: ')
    if confirm == 'n':
        print('Cancelled')
        time.sleep(1)
        Back(ToReset)
    Resetting = TODO[ToReset]
    Resetting.clear()
    TODO[ToReset] = Resetting
    changeinfo(TODO)
    Back(ToReset)


def Add(ToAdd):
    TODO = getinfo("x")
    Adding = TODO[ToAdd]
    AddNote = input('Type the note: ')
    Adding.append(AddNote)
    TODO[ToAdd] = Adding
    changeinfo(TODO)
    Back(ToAdd)

def Remove(List):
    ToRemove = input('Enter the number of the item to remove (default last): ')
    if ToRemove == '':
        ToRemove = -1
    TODO = getinfo("x")
    Removing = TODO[List]
    try:
        Removing.pop(int(ToRemove)-1)
    except IndexError:
        Back(List)
        return
    except ValueError:
        print('Cancelled')
        time.sleep(1)
        Back(List)
        return
    TODO[List] = Removing
    changeinfo(TODO)
    Back(List)


def Move(ToMove):
    NB = input('Enter the number of the item to move (default first): ')
    if NB == '':
        NB = 1
    try:
        NB= int(NB)
    except ValueError:
        print('Cancelled')
        time.sleep(1)
        if ToMove == 'Done':
            Back('Todo')
        else:
            Back('Done')
        return
    TODO = getinfo("x")
    Todo = TODO['Todo']
    Done = TODO['Done']
    if ToMove == 'Done':
        Done.append(Todo[NB-1])
        Todo.pop(NB-1)
    else:
        Todo.append(Done[NB-1])
        Done.pop(NB-1)
    TODO['Todo'] = Todo
    TODO['Done'] = Done
    changeinfo(TODO)
    if ToMove=='Done':
        Back('Todo')
    else:
        Back('Done')


def Todo():
    Clear()
    counter = 1
    Todo = getinfo("Todo")
    print('|-----------------TodoList-----------------|')
    for x in Todo:
        space = " "
        if counter < 10:
            nbspace = 39 - len(x)
        elif counter > 9:
            nbspace = 38 - len(x)
        else:
            nbspace = 37 - len(x)
        print(f"| {counter}-" + x + space * nbspace + "|")
        counter += 1
    chose = input('''|-----------------Settings-----------------|
| 1-Move to Done                           |
| 2-Add item                               |
| 3-Remove item                            |
| 4-Clear                                  |
| 5-Back                                   |
|__________________________________________|
>>> ''')
    if chose == '1':
        Move('Done')

    elif chose == '2':
        Add('Todo')

    elif chose == '3':
        Remove('Todo')

    elif chose == '4':
        Reset('Todo')

    elif chose == '5':
        return


def Done():
    Clear()
    counter = 1
    Done = getinfo("Done")
    print('|-----------------DoneList-----------------|')
    for x in Done:
        space = " "
        if counter < 10:
            nbspace = 39 - len(x)
        elif counter > 9:
            nbspace = 38 - len(x)
        else:
            nbspace = 37 - len(x)
        print(f"| {counter}-" + x + space * nbspace + "|")
        counter += 1
    chose = input('''|-----------------Settings-----------------|
| 1-Move to Todo                           |
| 2-Add item                               |
| 3-Remove item                            |
| 4-Clear                                  |
| 5-Back                                   |
|__________________________________________|
>>> ''')
    if chose == '1':
        Move('Todo')

    elif chose == '2':
        Add('Done')

    elif chose == '3':
        Remove('Done')

    elif chose == '4':
        Reset('Done')

    elif chose == '5':
        return


def rootmenu():
    Clear()
    # 41 white space
    chose = input('''
|-------------------TODO-------------------|
| 1-Todo                                   |
| 2-Done                                   |
| 3-Reset                                  |
|__________________________________________|
>>> ''')
    if chose == "1":
        Todo()

    elif chose == "2":
        Done()

    elif chose == "3":
        Reset('all')


while True:
    rootmenu()
