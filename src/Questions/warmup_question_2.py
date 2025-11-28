'''
   _==_ _
 _,(",)|_|
  \/. \-|
__( :  )|_
Thanks for all your help!

Turns out the elves aren't done with their demands.

They always have a holiday together before December. All 400 of them!

                                     ________________________________________
                                ()==(                                       (@==()
                                     '______________________________________'|
                                       |                                    |
                                       |  Dear Solly the Snowman,           |
                                       |                                    |
                                       |  We heard about you sisters igloo  |
                                       |  resort. We love a chilly getaway! |
                                       |                                    |
                                       |  I have details of all our         |
                                       |  families in this envelope.        |
                                       |  [Data/elf_families]               |
                                       |  I hope you and Sam the Snowman    |
                                       |  can accommodate all of our        |
                                       |  requirements!                     |
                                       |                                    |
                                       |   Best of luck,                    |
                                       |          Norbet                    |
                                       |   (South American Present Manager) |
                                       |                                    |
                                       |  P.S. Here's some socks to say     |
                                       |       Thanks!                      |
                                       |                                    |
                                       |               [IIIII]              |
                                       |             [IIIII]=|              |
                                       |             |=====|=|              |
                                       |             |=====| |              |
                                       |             |     | |              |
                                       |             |     | |              |
                                       |             |     | ;              |
                                       |             |     ;  \             |
                                       |             |`'.   \  \            |
                                       |             \  ;    \  \           |
                                       |              \'      \.'|          |
                                       |               \    .'|_/           |
                                       |                '._:_/              |
                                       |                                    |
                                     __)____________________________________|
                                ()==(                                      (@==()
                                     '-------------------------------------'
   _==_ _
 _,(",)|_|
  \/. \-|
__( :  )|_
He's the worst. I don't even have feet!

Well, lets see what Sam can do. [RING RING, RING RING]]

     @
 _,(",) _
  \/¡ \/
__( :  )
Hey Solly, what's up?
   _==_ _
 _,(",)|_|
  \/. \-|
__( :  )|_
The elves want to stay at the retreat, but all they've given me is a list of families with pets and allergies?
     @
 _,(",) _
  \/¡ \/
__( :  )
Well we'll have to check how many we can house! And by we... I mean you. [HANGS UP]
   _==_ _
 _,("_)|_|
  \/. \-|
__( :  )|_
I can't do this on my own. Can you help?

( 2A. CREATE A FUNCTION THAT PRINTS OUT WHICH FAMILIES CAN BE HOUSED IN WHICH AREAS OF THE RESORT.
      BOTH THE ELF FAMILY LIST AND IGLOO LOCATIONS CAN BE FOUND IN THE DATA FOLDER.
      (TIP: YOU CAN USE THE BELOW TO GATHER THE DATA

      import json
      from pathlib import Path

      DATA_PATH = Path(__file__).parent.parent / "Data"

      with (DATA_PATH / 'igloo_locations.json').open() as f:
          igloo_locations = json.load(f)
      with (DATA_PATH / 'elf_families.json').open() as f:
          families = json.load(f)
      )
'''