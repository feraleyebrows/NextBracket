# NextBracket

A simple plugin for Sublime Text that allows you to move the caret position to the next (or previous) line with a bracket. If there is more than one bracket on the same line, it will move to the last one.

## Installation
The easiest way is to use Package Control:
 - Type cmd+shift+p to bring up the command palette.
 - Search for Package Control: Install Package
 - Search for NextBracket and hit enter.

Otherwise `git clone` this directory to your Sublime Text packages folder. On Mac this is normally located at:
/Users/<YOUR USERNAME HERE>/Library/Application Support/Sublime Text/Packages

## Usage
"ctr+alt+super+down": next bracket
"ctrl+alt+super+up": previous bracket

(Super is the Command Key ⌘ on Mac and Windows Key on Windows)

These can be overwritten in your default keymap file. Just change the string in the keys array below:

```json
[
    {
        "keys": ["super+alt+ctrl+up"],
        "command": "next_bracket",
        "args": {"forward": false}
    },
    {
        "keys": ["super+alt+ctrl+down"], 
        "command": "next_bracket", 
        "args": {"forward": true}
    },
]
```

Works for all bracket types (curly, square, round, angle) as default. To change this, open the user settings file from 

"Preferences -> Package Settings -> NextBracket -> Settings - User". 

Alternatively you can create the file manually in your Sublime Text User directory. On Mac this is normally located at:

`/Users/<YOUR USERNAME HERE>/Library/Application Support/Sublime Text/Packages/User/NextBracket.sublime-settings`

Once you have the file open, copy the following and change the value to false for whichever brackets you want the plugin to ignore:

```json
{
    "include_square_brackets": true,
    "include_curly_brackets": true,
    "include_round_brackets": true,
    "include_angle_brackets": true
}
```




