import baseScreen
import os

class loseScreen(baseScreen.Screen):

    def display(self):

        os.system('cls')
        print("""
 __     __           _               _     _ 
 \ \   / /          | |             | |   | |
  \ \_/ /__  _   _  | |     ___  ___| |_  | |
   \   / _ \| | | | | |    / _ \/ __| __| | |
    | | (_) | |_| | | |___| (_) \__ \ |_  |_|
    |_|\___/ \__,_| |______\___/|___/\__| (_)
              """)

        print("""
                            ,--.
                           K,   }
                          /  ~Y`
                     ,   /   /
                    {_'-K.__/
                      `/-.__L._
                      /  ' /`\_}
                     /  ' /
             ____   /  ' /
      ,-'~~~~    ~~/  ' /_
    ,'             ``~~~  ',
   (                        Y
  {                         I
 {      -                    `,
 |       ',                   )
 |        |   ,..__      __. Y
 |    .,_./  Y ' / ^Y   J   )|
 \           |' /   |   |   ||
  \          L_/    . _ (_,.'(
   \,   ,      ^^""' / |      )
     \_  \          /,L]     /
       '-_~-,       ` `   ./`
          `'{_            )
              ^^\..___,.--`
              """)
# feel free to remove the skull, i thought it was funny


