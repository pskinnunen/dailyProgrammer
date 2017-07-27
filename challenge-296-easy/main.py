twelvedays = [
    ('first','Partridge in a Pear Tree'), ('second','Turtle Doves'),
    ('third','French Hens'),('forth','Calling Birds'),
    ('fifth','Golden Rings'),('sixth','Geese a Laying'),
    ('seventh','Swans a Swimming'),('eighth','Maids a Milking'),
    ('ninth', 'Ladies Dancing'),('tenth','Lords a Leaping'),
    ('eleventh','Pipers Piping'),('twelfth','Drummers Drumming')
    ]


def twelvedaysofchristmas():
    for dayindex,day in enumerate(twelvedays):
         print ('On the {} day of Christmas\nmy true love sent to me:' .format(day[0]))
         for giftindex, gift in enumerate(twelvedays[dayindex::-1]):
             print ("{}{} {}".format(('and ' if giftindex == dayindex and giftindex != 0 else '' ),
                                        dayindex-giftindex +1, gift[1]))
         print(' ')

if __name__ == '__main__':
    twelvedaysofchristmas()
