def friend_list(friend_dictionary):
    """
    Write a method named friendList that accepts a dictionary as a parameter and reads
    friend relationships and stores them into a new dictionary that is returned.
    You should create a new dictionary where each key is a person's name from the original
    simple dictionary, and the value associated with that key is a list of all friends of
    that person. Friendships are bi-directional:
    if Marty is friends with Danielle, Danielle is friends with Marty.

    The dictionary parameter contains one friend relationship per key/value pair,
    consisting of two names. If the dictionary parameter,friendMap looks like this:
    Marty: Cynthia
    Danielle: Marty
    Then the call of friendList(friendMap) should return a dictionary with the following
    contents:
    {Cynthia:[Marty], Danielle:[Marty], Marty:[Cynthia, Danielle]}
    """
    # new empty dictionary
    friendList = {}
    # append val in new dictionary a person can have multiple friends 
    # marty is a key and so is cynthia bc theyre friends with each other 
      # name = key; friend = value
      # sifting through the original dictionary 
    for name, friend in friend_dictionary.items():
        # add the person and their friend to the list
        if name not in friendList:
            friendList[name] = []
        friendList[name].append(friend)

        # friendship goes both ways
        if friend not in friendList:
            friendList[friend] = []
        friendList[friend].append(name)

    return friendList

assert friend_list({"Marty": "Cynthia", "Danielle": "Marty"})== {"Cynthia":["Marty"], "Danielle":["Marty"], "Marty":["Cynthia", "Danielle"]}, 'expected {"Cynthia":["Marty"], "Danielle":["Marty"], "Marty":["Cynthia", "Danielle"]}'
print("correct")

        