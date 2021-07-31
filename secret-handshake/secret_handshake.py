from typing import List

COMMANDS = {1: 'wink',
            2: 'double blink',
            4: 'close your eyes',
            8: 'jump'}


def commands(number: int) -> List[str]:
    '''Translate number to secret handshake.'''
    commands = [COMMANDS[command] for command in COMMANDS if number & command]
    return commands if not number & 16 else list(reversed(commands))
