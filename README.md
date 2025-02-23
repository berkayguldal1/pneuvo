                                                                        
![pneuvo_logo](https://github.com/user-attachments/assets/794023f6-3e66-4d87-acb8-bf35a49f8617)

Pronounced as ***pɯnyvo***

## Pneuvo
Pneuvo is a terminal simulator which lets people do WHATEVER they could want. (as long as there is an app but at that point you make one)
Pneuvo also has app support, dev and user accounts (dev is kinda like root and user is user)

Pneuvo is not a "oh i write neofetch and its fake neofetch" kind of experience.
Pneuvo is a platform for using/making apps and will try its best to do anything right.

## Apps

Apps are just ".py" files, but they support taking parameters. Pnuevo has its apps on the "fs/apps" and "fs/pakage" folders.
They can be read from either but we recommend putting your own apps into "fs/apps".
Parameters work by splitting the spaces and putting them into newlines.
So if my input is "pakage install neofetch" then the parameters.dll (they work as .txt files) will be "Pakage\nInstall\nNeofetch" 

## Package Manager

The default package manager is pakage. (Fun fact : Pakage was a pakage manager made by me!)
Its located in fs/apps/pakage.py and the install command works as this:

    1. Read parameters.dll to get the function and pakage name.
    2. If the functions "install", download the same package from Github. (berkayguldal1/quntal/pakage/*.py)
    3. Move that file to "fs/apps/*.py"
    
There is no repository support yet. If you made an app or ported one, Just open a issue about it and i will add it.
-------
<sup><sub>pneuvo is a continuation of quntal which is continuation of nest which is the continuation of lush which is the continuation of arckonsole</sub></sup>
    
