# sprites_data.py
# Ported from claude-code-leaked-src/src/buddy/sprites.ts and types.ts
# ASCII art frames: each species has 3 frames, each frame is 5 lines of 12 chars.
# {E} is the eye placeholder — replaced at render time with the eye char.
# Line 0 is the hat slot; blank in frames 0–1, may have content in frame 2.

# ---------------------------------------------------------------------------
# Constants (from types.ts)
# ---------------------------------------------------------------------------

SPECIES = [
    'duck',
    'goose',
    'blob',
    'cat',
    'dragon',
    'octopus',
    'owl',
    'penguin',
    'turtle',
    'snail',
    'ghost',
    'axolotl',
    'capybara',
    'cactus',
    'robot',
    'rabbit',
    'mushroom',
    'chonk',
]

EYES = ['·', '✦', '×', '◉', '@', '°']

EYE_NAMES = {
    '·': 'dot',
    '✦': 'star',
    '×': 'cross',
    '◉': 'bullseye',
    '@': 'at',
    '°': 'circle',
}

HATS = ['none', 'crown', 'tophat', 'propeller', 'halo', 'wizard', 'beanie', 'tinyduck']

RARITIES = ['common', 'uncommon', 'rare', 'epic', 'legendary']

RARITY_WEIGHTS = {
    'common': 60,
    'uncommon': 25,
    'rare': 10,
    'epic': 4,
    'legendary': 1,
}

RARITY_FLOOR = {
    'common': 5,
    'uncommon': 15,
    'rare': 25,
    'epic': 35,
    'legendary': 50,
}

RARITY_STARS = {
    'common': '★',
    'uncommon': '★★',
    'rare': '★★★',
    'epic': '★★★★',
    'legendary': '★★★★★',
}

STAT_NAMES = ['DEBUGGING', 'PATIENCE', 'CHAOS', 'WISDOM', 'SNARK']

# ---------------------------------------------------------------------------
# Sprite bodies (from sprites.ts)
# Each entry: list of frames; each frame: list of 5 strings, 12 chars wide.
# ---------------------------------------------------------------------------

BODIES = {
    'duck': [
        [
            '            ',
            '    __      ',
            '  <({E} )___  ',
            '   (  ._>   ',
            '    `--´    ',
        ],
        [
            '            ',
            '    __      ',
            '  <({E} )___  ',
            '   (  ._>   ',
            '    `--´~   ',
        ],
        [
            '            ',
            '    __      ',
            '  <({E} )___  ',
            '   (  .__>  ',
            '    `--´    ',
        ],
    ],
    'goose': [
        [
            '            ',
            '     ({E}>    ',
            '     ||     ',
            '   _(__)_   ',
            '    ^^^^    ',
        ],
        [
            '            ',
            '    ({E}>     ',
            '     ||     ',
            '   _(__)_   ',
            '    ^^^^    ',
        ],
        [
            '            ',
            '     ({E}>>   ',
            '     ||     ',
            '   _(__)_   ',
            '    ^^^^    ',
        ],
    ],
    'blob': [
        [
            '            ',
            '   .----.   ',
            '  ( {E}  {E} )  ',
            '  (      )  ',
            '   `----´   ',
        ],
        [
            '            ',
            '  .------.  ',
            ' (  {E}  {E}  ) ',
            ' (        ) ',
            '  `------´  ',
        ],
        [
            '            ',
            '    .--.    ',
            '   ({E}  {E})   ',
            '   (    )   ',
            '    `--´    ',
        ],
    ],
    'cat': [
        [
            '            ',
            '   /\\_/\\    ',
            '  ( {E}   {E})  ',
            '  (  ω  )   ',
            '  (")_(")   ',
        ],
        [
            '            ',
            '   /\\_/\\    ',
            '  ( {E}   {E})  ',
            '  (  ω  )   ',
            '  (")_(")~  ',
        ],
        [
            '            ',
            '   /\\-/\\    ',
            '  ( {E}   {E})  ',
            '  (  ω  )   ',
            '  (")_(")   ',
        ],
    ],
    'dragon': [
        [
            '            ',
            '  /^\\  /^\\  ',
            ' <  {E}  {E}  > ',
            ' (   ~~   ) ',
            '  `-vvvv-´  ',
        ],
        [
            '            ',
            '  /^\\  /^\\  ',
            ' <  {E}  {E}  > ',
            ' (        ) ',
            '  `-vvvv-´  ',
        ],
        [
            '   ~    ~   ',
            '  /^\\  /^\\  ',
            ' <  {E}  {E}  > ',
            ' (   ~~   ) ',
            '  `-vvvv-´  ',
        ],
    ],
    'octopus': [
        [
            '            ',
            '   .----.   ',
            '  ( {E}  {E} )  ',
            '  (______)  ',
            '  /\\/\\/\\/\\  ',
        ],
        [
            '            ',
            '   .----.   ',
            '  ( {E}  {E} )  ',
            '  (______)  ',
            '  \\/\\/\\/\\/  ',
        ],
        [
            '     o      ',
            '   .----.   ',
            '  ( {E}  {E} )  ',
            '  (______)  ',
            '  /\\/\\/\\/\\  ',
        ],
    ],
    'owl': [
        [
            '            ',
            '   /\\  /\\   ',
            '  (({E})({E}))  ',
            '  (  ><  )  ',
            '   `----´   ',
        ],
        [
            '            ',
            '   /\\  /\\   ',
            '  (({E})({E}))  ',
            '  (  ><  )  ',
            '   .----.   ',
        ],
        [
            '            ',
            '   /\\  /\\   ',
            '  (({E})(-))  ',
            '  (  ><  )  ',
            '   `----´   ',
        ],
    ],
    'penguin': [
        [
            '            ',
            '  .---.     ',
            '  ({E}>{E})     ',
            ' /(   )\\    ',
            '  `---´     ',
        ],
        [
            '            ',
            '  .---.     ',
            '  ({E}>{E})     ',
            ' |(   )|    ',
            '  `---´     ',
        ],
        [
            '  .---.     ',
            '  ({E}>{E})     ',
            ' /(   )\\    ',
            '  `---´     ',
            '   ~ ~      ',
        ],
    ],
    'turtle': [
        [
            '            ',
            '   _,--._   ',
            '  ( {E}  {E} )  ',
            ' /[______]\\ ',
            '  ``    ``  ',
        ],
        [
            '            ',
            '   _,--._   ',
            '  ( {E}  {E} )  ',
            ' /[______]\\ ',
            '   ``  ``   ',
        ],
        [
            '            ',
            '   _,--._   ',
            '  ( {E}  {E} )  ',
            ' /[======]\\ ',
            '  ``    ``  ',
        ],
    ],
    'snail': [
        [
            '            ',
            ' {E}    .--.  ',
            '  \\  ( @ )  ',
            '   \\_`--´   ',
            '  ~~~~~~~   ',
        ],
        [
            '            ',
            '  {E}   .--.  ',
            '  |  ( @ )  ',
            '   \\_`--´   ',
            '  ~~~~~~~   ',
        ],
        [
            '            ',
            ' {E}    .--.  ',
            '  \\  ( @  ) ',
            '   \\_`--´   ',
            '   ~~~~~~   ',
        ],
    ],
    'ghost': [
        [
            '            ',
            '   .----.   ',
            '  / {E}  {E} \\  ',
            '  |      |  ',
            '  ~`~``~`~  ',
        ],
        [
            '            ',
            '   .----.   ',
            '  / {E}  {E} \\  ',
            '  |      |  ',
            '  `~`~~`~`  ',
        ],
        [
            '    ~  ~    ',
            '   .----.   ',
            '  / {E}  {E} \\  ',
            '  |      |  ',
            '  ~~`~~`~~  ',
        ],
    ],
    'axolotl': [
        [
            '            ',
            '}~(______)~{',
            '}~({E} .. {E})~{',
            '  ( .--. )  ',
            '  (_/  \\_)  ',
        ],
        [
            '            ',
            '~}(______){~',
            '~}({E} .. {E}){~',
            '  ( .--. )  ',
            '  (_/  \\_)  ',
        ],
        [
            '            ',
            '}~(______)~{',
            '}~({E} .. {E})~{',
            '  (  --  )  ',
            '  ~_/  \\_~  ',
        ],
    ],
    'capybara': [
        [
            '            ',
            '  n______n  ',
            ' ( {E}    {E} ) ',
            ' (   oo   ) ',
            '  `------´  ',
        ],
        [
            '            ',
            '  n______n  ',
            ' ( {E}    {E} ) ',
            ' (   Oo   ) ',
            '  `------´  ',
        ],
        [
            '    ~  ~    ',
            '  u______n  ',
            ' ( {E}    {E} ) ',
            ' (   oo   ) ',
            '  `------´  ',
        ],
    ],
    'cactus': [
        [
            '            ',
            ' n  ____  n ',
            ' | |{E}  {E}| | ',
            ' |_|    |_| ',
            '   |    |   ',
        ],
        [
            '            ',
            '    ____    ',
            ' n |{E}  {E}| n ',
            ' |_|    |_| ',
            '   |    |   ',
        ],
        [
            ' n        n ',
            ' |  ____  | ',
            ' | |{E}  {E}| | ',
            ' |_|    |_| ',
            '   |    |   ',
        ],
    ],
    'robot': [
        [
            '            ',
            '   .[||].   ',
            '  [ {E}  {E} ]  ',
            '  [ ==== ]  ',
            '  `------´  ',
        ],
        [
            '            ',
            '   .[||].   ',
            '  [ {E}  {E} ]  ',
            '  [ -==- ]  ',
            '  `------´  ',
        ],
        [
            '     *      ',
            '   .[||].   ',
            '  [ {E}  {E} ]  ',
            '  [ ==== ]  ',
            '  `------´  ',
        ],
    ],
    'rabbit': [
        [
            '            ',
            '   (\\__/)   ',
            '  ( {E}  {E} )  ',
            ' =(  ..  )= ',
            '  (")__(")  ',
        ],
        [
            '            ',
            '   (|__/)   ',
            '  ( {E}  {E} )  ',
            ' =(  ..  )= ',
            '  (")__(")  ',
        ],
        [
            '            ',
            '   (\\__/)   ',
            '  ( {E}  {E} )  ',
            ' =( .  . )= ',
            '  (")__(")  ',
        ],
    ],
    'mushroom': [
        [
            '            ',
            ' .-o-OO-o-. ',
            '(__________)',
            '   |{E}  {E}|   ',
            '   |____|   ',
        ],
        [
            '            ',
            ' .-O-oo-O-. ',
            '(__________)',
            '   |{E}  {E}|   ',
            '   |____|   ',
        ],
        [
            '   . o  .   ',
            ' .-o-OO-o-. ',
            '(__________)',
            '   |{E}  {E}|   ',
            '   |____|   ',
        ],
    ],
    'chonk': [
        [
            '            ',
            '  /\\    /\\  ',
            ' ( {E}    {E} ) ',
            ' (   ..   ) ',
            '  `------´  ',
        ],
        [
            '            ',
            '  /\\    /|  ',
            ' ( {E}    {E} ) ',
            ' (   ..   ) ',
            '  `------´  ',
        ],
        [
            '            ',
            '  /\\    /\\  ',
            ' ( {E}    {E} ) ',
            ' (   ..   ) ',
            '  `------´~ ',
        ],
    ],
}

# ---------------------------------------------------------------------------
# Hat lines (from sprites.ts)
# Each hat line replaces line 0 of the sprite when a hat is worn.
# ---------------------------------------------------------------------------

HAT_LINES = {
    'none': '',
    'crown': '   \\^^^/    ',
    'tophat': '   [___]    ',
    'propeller': '    -+-     ',
    'halo': '   (   )    ',
    'wizard': '    /^\\     ',
    'beanie': '   (___)    ',
    'tinyduck': '    ,>      ',
}

# ---------------------------------------------------------------------------
# Rendering functions
# ---------------------------------------------------------------------------

def render_sprite(species: str, eye: str, hat: str, frame: int = 0) -> list[str]:
    """Return the sprite as a list of strings with eye substituted and hat applied.

    Matches the renderSprite logic from sprites.ts:
    - Substitutes {E} with the eye char.
    - Overlays the hat line on line 0 if hat != 'none' and line 0 is blank.
    - Drops the blank hat-slot row when no frame in the species uses it
      (avoids oscillating height during animation).
    """
    frames = BODIES[species]
    body = [line.replace('{E}', eye) for line in frames[frame % len(frames)]]
    lines = list(body)

    # Apply hat only when line 0 is empty
    if hat != 'none' and not lines[0].strip():
        lines[0] = HAT_LINES[hat]

    # Drop blank hat slot when ALL frames have blank line 0
    if not lines[0].strip() and all(not f[0].strip() for f in frames):
        lines = lines[1:]

    return lines


def render_face(species: str, eye: str) -> str:
    """Return a compact one-line face string for the species.

    Ported from renderFace() in sprites.ts.
    """
    if species in ('duck', 'goose'):
        return f'({eye}>'
    elif species == 'blob':
        return f'({eye}{eye})'
    elif species == 'cat':
        return f'={eye}ω{eye}='
    elif species == 'dragon':
        return f'<{eye}~{eye}>'
    elif species == 'octopus':
        return f'~({eye}{eye})~'
    elif species == 'owl':
        return f'({eye})({eye})'
    elif species == 'penguin':
        return f'({eye}>)'
    elif species == 'turtle':
        return f'[{eye}_{eye}]'
    elif species == 'snail':
        return f'{eye}(@)'
    elif species == 'ghost':
        return f'/{eye}{eye}\\'
    elif species == 'axolotl':
        return f'}}{eye}.{eye}{{'
    elif species == 'capybara':
        return f'({eye}oo{eye})'
    elif species == 'cactus':
        return f'|{eye}  {eye}|'
    elif species == 'robot':
        return f'[{eye}{eye}]'
    elif species == 'rabbit':
        return f'({eye}..{eye})'
    elif species in ('mushroom', 'chonk'):
        # mushroom and chonk share the same face format
        if species == 'mushroom':
            return f'|{eye}  {eye}|'
        else:
            return f'({eye}.{eye})'
    raise ValueError(f'Unknown species: {species}')


# ---------------------------------------------------------------------------
# Quick smoke test
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    test_cases = [
        ('duck',     '·',  'none',   0),
        ('dragon',   '✦',  'crown',  0),
        ('blob',     '◉',  'wizard', 1),
        ('cat',      '@',  'tophat', 0),
        ('axolotl',  '×',  'none',   2),
        ('mushroom', '°',  'halo',   0),
    ]

    for species, eye, hat, frame in test_cases:
        lines = render_sprite(species, eye, hat, frame)
        face  = render_face(species, eye)
        print(f'--- {species}  eye={eye}  hat={hat}  frame={frame}  face={face} ---')
        for line in lines:
            print(repr(line))
        print()
