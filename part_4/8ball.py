import random

messages = ['Absolutely',
            'Maybe',
            'Ask again later',
            'Outlook hazy, try again',
            'My reply is no',
            'Outlook does not look good',
            'Doubtful'
            ]

print( messages[ random.randint( 0, len( messages ) -1) ] + '.' )
