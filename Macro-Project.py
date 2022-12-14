# SPDX-FileCopyright Text: 2022 Jacob Stack 
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys: Firefox macros with weblink capabilty 

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                       # REQUIRED dict, must be named 'app'
    'name' : 'Firefox - Work', # Application name
    'macros' : [              # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x073079, '< Back', [Keycode.CONTROL, '[']),
        (0x090049, 'Fwd >', [Keycode.CONTROL, ']']),
        (0x072019, 'Label',[Keycode.CONTROL, 't', -Keycode.CONTROL,
                               'https://website.com\n']), # Input URL
        # 2nd row ----------
        (0x024960, '< Tab', [Keycode.CONTROL, Keycode.SHIFT, Keycode.TAB]),
        (0x071517, 'Tab >', [Keycode.CONTROL, Keycode.TAB]),
        (0x007200, 'Label', [Keycode.CONTROL, 't', -Keycode.CONTROL,
                              'https://website.com\n']), # Input URL
        # 3rd row ----------
        (0x000090, 'Reload', [Keycode.CONTROL, 'r']),
        (0x000090, 'Home', [Keycode.CONTROL, 'h']),
        (0x000090, 'Label', [Keycode.CONTROL, 't', -Keycode.CONTROL,
                               'https://website.com\n']), # Input URL
        # 4th row ----------
        (0x002400, 'Label', [Keycode.CONTROL, 't', -Keycode.CONTROL,
                           'https://website.com\n']), # Input URL
        (0x900090, 'Dev Mode', [Keycode.F12]),     # dev mode
        (0x002400, 'Label', [Keycode.CONTROL, 't', -Keycode.CONTROL,
                            'https://website.com\n']), # Input URL
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'w']) # Close window/tab
    ]
}
