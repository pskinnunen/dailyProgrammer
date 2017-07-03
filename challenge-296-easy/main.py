
twelvedays = [('First','Partrige in a Pear Tree'),
('Second','Turtle Doves'), ('Third','French Hens'),
('Forth','Calling Birds'), ('Fifth','Golden Rings'),
('Sixth','Geese a Laying'), ('Seventh','Swans a Swimming'),
('Eighth','Maids a Milking'),('Ninth', 'Ladies Dancing'),
('Tenth','Lords a Leaping'),('Elevnth','Pipers Piping'),
('Twelvth','Drummers Drumming')]

def twelvedaysofchristmas():
    print("Runing")
    for dayindex,day in enumerate(twelvedays):
         print ('On the {} day of Christmas my true love gave to me' .format(day[0]))
         for giftindex, gift in enumerate(twelvedays[dayindex::-1]):
             print ("{} {}".format(dayindex-giftindex +1, gift[1]))

twelvedaysofchristmas()
