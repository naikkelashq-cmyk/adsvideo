# Vector art: puskesmas backgrounds + characters (flat illustration)
SKIN = {'a': '#E8B48F', 'b': '#C98B62', 'c': '#D9A07A', 'd': '#B97C55'}

def cloud(id_, x, y, s=1.0, o=1):
    return (f'<g id="{id_}" transform="translate({x},{y}) scale({s})" opacity="{o}">'
            '<ellipse cx="0" cy="20" rx="110" ry="34" fill="#fff"/>'
            '<circle cx="-40" cy="5" r="42" fill="#fff"/><circle cx="20" cy="-12" r="56" fill="#fff"/>'
            '<circle cx="70" cy="10" r="36" fill="#fff"/></g>')

def tree(x, y, s=1.0, c1='#4FA574', c2='#3B8F60'):
    return (f'<g transform="translate({x},{y}) scale({s})">'
            '<path d="M-14 0 L-10 -150 Q0 -170 10 -150 L14 0 Z" fill="#8A5A3B"/>'
            '<path d="M-6 -120 L-50 -175 M6 -110 L46 -170" stroke="#8A5A3B" stroke-width="10" stroke-linecap="round"/>'
            f'<circle cx="0" cy="-230" r="95" fill="{c2}"/><circle cx="-70" cy="-180" r="70" fill="{c2}"/>'
            f'<circle cx="70" cy="-185" r="72" fill="{c2}"/><circle cx="-30" cy="-250" r="70" fill="{c1}"/>'
            f'<circle cx="45" cy="-245" r="62" fill="{c1}"/><circle cx="-80" cy="-195" r="45" fill="{c1}"/>'
            '<circle cx="-20" cy="-275" r="22" fill="#6CC08E" opacity=".6"/></g>')

def plant(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})">'
            '<path d="M-38 0 L38 0 L30 70 L-30 70 Z" fill="#C8643B"/><rect x="-42" y="-6" width="84" height="14" rx="6" fill="#B4532E"/>'
            '<path d="M0 0 C-10 -60 -60 -80 -70 -120 C-30 -110 -5 -70 0 -20 Z" fill="#3F9B66"/>'
            '<path d="M0 0 C10 -70 50 -90 66 -130 C30 -120 8 -80 0 -20 Z" fill="#53B07A"/>'
            '<path d="M0 0 C-4 -70 0 -120 6 -160 C20 -110 12 -60 0 0 Z" fill="#2F8556"/></g>')

def bg_exterior(sx=""):
    tiles = ''.join(f'<path d="M{150+i*0:.0f} {700+i*28} L{930} {700+i*28}" stroke="#B8432B" stroke-width="3" opacity=".55"/>' for i in range(1, 5))
    win = ''
    for x in (165, 285, 735, 855):
        win += (f'<g><rect x="{x-8}" y="912" width="106" height="136" rx="8" fill="#2E6F7A"/>'
                f'<rect x="{x}" y="920" width="90" height="120" rx="4" fill="#A7DCE8"/>'
                f'<path d="M{x+45} 920 V1040 M{x} 980 H{x+90}" stroke="#2E6F7A" stroke-width="6"/>'
                f'<path d="M{x+8} 1000 L{x+34} 928 L{x+42} 928 L{x+16} 1000 Z" fill="#fff" opacity=".45"/></g>')
    return f'''<svg class="bgsvg" viewBox="0 0 1080 1920" width="1080" height="1920" preserveAspectRatio="xMidYMid slice">
<defs><linearGradient id="sky{sx}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9FD9EA"/><stop offset="1" stop-color="#E9F7F1"/></linearGradient>
<radialGradient id="sun{sx}" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#FFE7A3"/><stop offset=".55" stop-color="#FFD98A" stop-opacity=".9"/><stop offset="1" stop-color="#FFD98A" stop-opacity="0"/></radialGradient>
<linearGradient id="yard{sx}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#EDE5D3"/><stop offset="1" stop-color="#DCCFB5"/></linearGradient></defs>
<rect width="1080" height="1250" fill="url(#sky{sx})"/>
<circle cx="860" cy="330" r="170" fill="url(#sun{sx})"/><circle cx="860" cy="330" r="70" fill="#FFE29A"/>
{cloud("cl1"+sx,230,300,1.0)}{cloud("cl2"+sx,760,520,0.7,.9)}{cloud("cl3"+sx,120,610,0.55,.8)}
<path d="M0 930 Q180 820 380 900 T760 880 T1080 900 V1250 H0 Z" fill="#B7E0C4"/>
<path d="M0 990 Q240 900 520 980 T1080 960 V1250 H0 Z" fill="#9ED3B4"/>
{tree(70,1190,1.05)}{tree(1015,1185,0.95,'#58AE7C','#3F9364')}
<rect x="0" y="1180" width="1080" height="740" fill="url(#yard{sx})"/>
<path d="M0 1180 H1080" stroke="#CDBE9E" stroke-width="6"/>
{''.join(f'<path d="M{x} 1190 L{x-120} 1920" stroke="#D6C8AA" stroke-width="3"/>' for x in range(-200,1400,180))}
{''.join(f'<path d="M0 {y} H1080" stroke="#D6C8AA" stroke-width="3"/>' for y in (1260,1370,1510,1690))}
<rect x="0" y="1180" width="120" height="740" fill="#8FCB8F"/><rect x="960" y="1180" width="120" height="740" fill="#8FCB8F"/>
<rect x="128" y="815" width="832" height="372" fill="#000" opacity=".06"/>
<rect x="120" y="820" width="840" height="365" fill="#FBF7EE"/>
<rect x="120" y="1095" width="840" height="90" fill="#2E9C8A"/><rect x="120" y="1095" width="840" height="10" fill="#26877A"/>
<rect x="120" y="820" width="840" height="22" fill="#2E9C8A"/>
<polygon points="80,832 1000,832 905,690 175,690" fill="#D9573B"/>{tiles}
<polygon points="80,832 1000,832 1000,846 80,846" fill="#B8432B"/>
{win}
<rect x="400" y="830" width="280" height="355" fill="#F2ECDF"/>
<polygon points="372,850 708,850 540,700" fill="#E0623F"/><polygon points="372,850 708,850 708,862 372,862" fill="#B8432B"/>
<rect x="408" y="776" width="264" height="62" rx="8" fill="#157A6E"/><text x="540" y="819" text-anchor="middle" font-family="Inter" font-weight="800" font-size="34" fill="#fff" letter-spacing="3">PUSKESMAS</text>
<rect x="478" y="955" width="124" height="230" rx="6" fill="#2E6F7A"/><rect x="486" y="963" width="52" height="222" fill="#8FD0DF"/><rect x="542" y="963" width="52" height="222" fill="#8FD0DF"/>
<path d="M494 1060 L520 975 L530 975 L504 1060Z" fill="#fff" opacity=".5"/><circle cx="532" cy="1080" r="5" fill="#2E6F7A"/><circle cx="548" cy="1080" r="5" fill="#2E6F7A"/>
<rect x="412" y="862" width="30" height="323" fill="#fff"/><rect x="436" y="862" width="6" height="323" fill="#E4DCCB"/>
<rect x="638" y="862" width="30" height="323" fill="#fff"/><rect x="662" y="862" width="6" height="323" fill="#E4DCCB"/>
<rect x="380" y="1185" width="320" height="22" fill="#E7E0D3"/><rect x="360" y="1207" width="360" height="22" fill="#DCD3C2"/>
{plant(380,1120,0.9)}{plant(700,1120,0.9)}
<rect x="1040" y="660" width="8" height="530" fill="#9AA3A8"/><circle cx="1044" cy="656" r="9" fill="#C9CED1"/>
<g id="flag{sx}"><rect x="980" y="668" width="60" height="22" fill="#E0322B"/><rect x="980" y="690" width="60" height="22" fill="#fff"/></g>
</svg>'''

def bg_interior(wall='#E4F0EA', floor='#D9C6A8', tv=False):
    planks = ''.join(f'<path d="M0 {y} H1080" stroke="#C7B08C" stroke-width="3"/>' for y in (1380, 1480, 1600, 1750))
    blinds = ''.join(f'<path d="M680 {y} H990" stroke="#D7E6EC" stroke-width="5"/>' for y in range(360, 760, 34))
    board = ('<rect x="80" y="360" width="500" height="330" rx="14" fill="#5D6B73"/><rect x="94" y="374" width="472" height="302" rx="8" fill="#FDFEFE"/>'
             '<path d="M130 640 V430 M130 640 H530" stroke="#B9C4CA" stroke-width="5"/>'
             '<rect x="160" y="560" width="40" height="80" fill="#F4A261" opacity=".8"/><rect x="230" y="510" width="40" height="130" fill="#2E9C8A" opacity=".8"/>'
             '<rect x="300" y="590" width="40" height="50" fill="#E0533D" opacity=".8"/><rect x="370" y="470" width="40" height="170" fill="#2E9C8A" opacity=".8"/>'
             '<path d="M440 440 q30 -20 60 0 t60 0" stroke="#E0533D" stroke-width="5" fill="none"/><rect x="230" y="682" width="200" height="14" rx="4" fill="#8B979E"/>')
    if tv:
        board = ('<rect x="70" y="350" width="520" height="320" rx="16" fill="#1F2A33"/><rect x="86" y="366" width="488" height="288" rx="8" fill="#123B4A"/>'
                 '<circle cx="200" cy="510" r="80" fill="#2E9C8A"/><path d="M200 510 L200 430 A80 80 0 0 1 276 535 Z" fill="#F4A261"/>'
                 '<rect x="330" y="560" width="36" height="60" fill="#6CC6B0"/><rect x="384" y="500" width="36" height="120" fill="#6CC6B0"/><rect x="438" y="450" width="36" height="170" fill="#F4A261"/><rect x="492" y="420" width="36" height="200" fill="#6CC6B0"/>'
                 '<rect x="290" y="670" width="80" height="40" fill="#1F2A33"/>')
    return f'''<svg class="bgsvg" viewBox="0 0 1080 1920" width="1080" height="1920">
<rect width="1080" height="1320" fill="{wall}"/><rect y="1240" width="1080" height="80" fill="#000" opacity=".04"/>
<rect y="1300" width="1080" height="620" fill="{floor}"/>{planks}<rect y="1300" width="1080" height="16" fill="#B89C74"/>
<rect x="660" y="330" width="350" height="450" rx="10" fill="#FFFFFF"/><rect x="676" y="346" width="318" height="418" fill="#BFE6F0"/>
<circle cx="900" cy="440" r="46" fill="#FFE8A8"/><path d="M676 700 Q780 640 860 690 T994 670 V764 H676Z" fill="#9ED3B4"/>{blinds}
<rect x="650" y="774" width="370" height="20" rx="6" fill="#F3EEE4"/>
{board}
<circle cx="540" cy="215" r="58" fill="#fff" stroke="#5D6B73" stroke-width="8"/><path d="M540 215 V180 M540 215 L566 230" stroke="#33414A" stroke-width="7" stroke-linecap="round"/>
<rect x="760" y="900" width="250" height="400" rx="8" fill="#B98A5E"/><rect x="772" y="912" width="226" height="180" fill="#9C6F45"/><rect x="772" y="1104" width="226" height="184" fill="#9C6F45"/>
{''.join(f'<rect x="{782+i*36}" y="{940+(i%2)*14}" width="30" height="{150-(i%2)*14}" rx="3" fill="{c}"/>' for i,c in enumerate(["#2E9C8A","#E0533D","#F4A261","#3D6FB6","#2E9C8A","#F2B544"]))}
{''.join(f'<rect x="{782+i*36}" y="{1136+(i%3)*10}" width="30" height="{140-(i%3)*10}" rx="3" fill="{c}"/>' for i,c in enumerate(["#3D6FB6","#F2B544","#2E9C8A","#E0533D","#8E6BBF","#2E9C8A"]))}
{plant(120,1230,1.15)}
</svg>'''

# ---------------- characters ----------------
def _face(cx, cy, skin, mood, glasses=False, uid=''):
    eyes_open = (f'<g class="eyes"><ellipse cx="{cx-22}" cy="{cy+2}" rx="7" ry="9" fill="#2B2320"/><ellipse cx="{cx+22}" cy="{cy+2}" rx="7" ry="9" fill="#2B2320"/>'
                 f'<circle cx="{cx-20}" cy="{cy-1}" r="2.4" fill="#fff"/><circle cx="{cx+24}" cy="{cy-1}" r="2.4" fill="#fff"/></g>')
    blush = f'<ellipse cx="{cx-36}" cy="{cy+24}" rx="11" ry="6" fill="#E8836B" opacity=".35"/><ellipse cx="{cx+36}" cy="{cy+24}" rx="11" ry="6" fill="#E8836B" opacity=".35"/>'
    sad = (f'<g class="m-sad">{eyes_open}'
           f'<path d="M{cx-34} {cy-20} L{cx-12} {cy-26}" stroke="#3A2A22" stroke-width="5" stroke-linecap="round"/>'
           f'<path d="M{cx+34} {cy-20} L{cx+12} {cy-26}" stroke="#3A2A22" stroke-width="5" stroke-linecap="round"/>'
           f'<path d="M{cx-14} {cy+36} Q{cx} {cy+26} {cx+14} {cy+36}" stroke="#7A3B2E" stroke-width="5" fill="none" stroke-linecap="round"/>'
           f'<path class="sweat" d="M{cx+56} {cy-26} q8 14 0 20 q-8 -6 0 -20Z" fill="#7CC6E8"/></g>')
    happy = (f'<g class="m-hap" opacity="0">'
             f'<path d="M{cx-30} {cy+4} Q{cx-22} {cy-8} {cx-14} {cy+4}" stroke="#2B2320" stroke-width="5" fill="none" stroke-linecap="round"/>'
             f'<path d="M{cx+14} {cy+4} Q{cx+22} {cy-8} {cx+30} {cy+4}" stroke="#2B2320" stroke-width="5" fill="none" stroke-linecap="round"/>'
             f'<path d="M{cx-32} {cy-22} Q{cx-22} {cy-30} {cx-12} {cy-24}" stroke="#3A2A22" stroke-width="5" fill="none" stroke-linecap="round"/>'
             f'<path d="M{cx+12} {cy-24} Q{cx+22} {cy-30} {cx+32} {cy-22}" stroke="#3A2A22" stroke-width="5" fill="none" stroke-linecap="round"/>'
             f'<path d="M{cx-20} {cy+26} Q{cx} {cy+48} {cx+20} {cy+26} Z" fill="#7A3B2E"/><path d="M{cx-12} {cy+38} Q{cx} {cy+46} {cx+12} {cy+38}" fill="#E8836B"/></g>')
    nose = f'<path d="M{cx} {cy+8} q-6 10 2 14" stroke="{SKIN["d"]}" stroke-width="4" fill="none" stroke-linecap="round" opacity=".7"/>'
    gl = ''
    if glasses:
        gl = (f'<g fill="none" stroke="#2B2B2B" stroke-width="4.5"><rect x="{cx-44}" y="{cy-14}" width="38" height="30" rx="10"/>'
              f'<rect x="{cx+6}" y="{cy-14}" width="38" height="30" rx="10"/><path d="M{cx-6} {cy-2} H{cx+6}"/></g>')
    return blush + nose + sad + happy + gl

def character(cid, kind):
    """kind: kapus | bidan | dokter | perawat. viewBox 0 0 300 720, feet at ~700."""
    skin = {'kapus': '#E2AE88', 'bidan': '#D9A07A', 'dokter': '#C98B62', 'perawat': '#D49A72'}[kind]
    cx, cy = 150, 135
    parts = []
    shadow = '<ellipse cx="150" cy="702" rx="110" ry="16" fill="#000" opacity=".12"/>'
    if kind in ('kapus', 'bidan'):
        hij = {'kapus': ('#1F3A6B', '#17305A'), 'bidan': ('#E77FA6', '#D4668F')}[kind]
        top = {'kapus': '#C9A86A', 'bidan': '#F4A7C3'}[kind]
        top2 = {'kapus': '#B8965A', 'bidan': '#E992B2'}[kind]
        bottom = {'kapus': '#6B5536', 'bidan': '#F4A7C3'}[kind]
        # legs / skirt
        if kind == 'kapus':
            parts.append(f'<path d="M78 430 L222 430 L240 690 L60 690 Z" fill="{bottom}"/><path d="M150 440 V688" stroke="#5A4629" stroke-width="3"/>')
            parts.append('<ellipse cx="108" cy="694" rx="34" ry="12" fill="#2B2320"/><ellipse cx="192" cy="694" rx="34" ry="12" fill="#2B2320"/>')
        else:
            parts.append(f'<rect x="88" y="430" width="58" height="250" rx="16" fill="{bottom}"/><rect x="154" y="430" width="58" height="250" rx="16" fill="{bottom}"/>'
                         f'<path d="M150 430 V600" stroke="{top2}" stroke-width="4"/>')
            parts.append('<ellipse cx="116" cy="690" rx="36" ry="13" fill="#FFFFFF"/><ellipse cx="184" cy="690" rx="36" ry="13" fill="#FFFFFF"/>'
                         '<ellipse cx="116" cy="694" rx="36" ry="8" fill="#D8D8D8"/><ellipse cx="184" cy="694" rx="36" ry="8" fill="#D8D8D8"/>')
        # torso
        parts.append(f'<path d="M62 300 Q66 238 150 232 Q234 238 238 300 L230 460 Q150 476 70 460 Z" fill="{top}"/>')
        if kind == 'kapus':
            parts.append('<path d="M150 250 V462" stroke="#A88850" stroke-width="3"/>'
                         + ''.join(f'<circle cx="150" cy="{y}" r="5" fill="#8C6D3A"/>' for y in (300, 350, 400))
                         + '<rect x="176" y="300" width="44" height="40" rx="5" fill="none" stroke="#A88850" stroke-width="3"/>'
                         + '<rect x="86" y="306" width="46" height="12" rx="3" fill="#1F3A6B"/><rect x="180" y="282" width="34" height="10" rx="3" fill="#E0B23A"/>')
        else:
            parts.append(f'<path d="M120 250 L150 300 L180 250" fill="none" stroke="{top2}" stroke-width="6"/><rect x="96" y="320" width="44" height="40" rx="6" fill="{top2}"/>'
                         '<rect x="104" y="312" width="5" height="22" fill="#3D6FB6"/>')
        # hijab drape over shoulders
        parts.append(f'<path d="M150 40 C82 40 70 110 74 170 C70 220 86 262 150 290 C214 262 230 220 226 170 C230 110 218 40 150 40 Z" fill="{hij[0]}"/>'
                     f'<path d="M150 290 C110 278 90 250 84 222 C110 250 190 250 216 222 C210 250 190 278 150 290Z" fill="{hij[1]}"/>')
        parts.append(f'<ellipse cx="{cx}" cy="{cy+6}" rx="58" ry="66" fill="{skin}"/>')
        parts.append(f'<path d="M92 100 C100 60 200 60 208 100 C190 84 110 84 92 100 Z" fill="{hij[1]}"/>')
    else:
        shirt = {'dokter': '#BFD8F2', 'perawat': '#2E9C8A'}[kind]
        shirt2 = {'dokter': '#A7C6E8', 'perawat': '#25867A'}[kind]
        pants = {'dokter': '#4A5560', 'perawat': '#2E9C8A'}[kind]
        parts.append(f'<rect x="84" y="430" width="62" height="252" rx="16" fill="{pants}"/><rect x="154" y="430" width="62" height="252" rx="16" fill="{pants}"/>')
        parts.append('<ellipse cx="114" cy="692" rx="38" ry="13" fill="#2B2320"/><ellipse cx="186" cy="692" rx="38" ry="13" fill="#2B2320"/>')
        parts.append(f'<rect x="128" y="190" width="44" height="60" fill="{skin}"/>')
        parts.append(f'<path d="M58 300 Q62 240 150 234 Q238 240 242 300 L234 462 Q150 478 66 462 Z" fill="{shirt}"/>')
        if kind == 'dokter':
            parts.append('<path d="M126 240 L150 290 L174 240" fill="#fff"/><path d="M146 262 L154 262 L160 370 L150 384 L140 370Z" fill="#2F5C8E"/>'
                         '<path d="M58 300 Q62 240 128 236 L150 300 L128 560 L64 556 Z" fill="#FFFFFF"/><path d="M242 300 Q238 240 172 236 L150 300 L172 560 L236 556 Z" fill="#FFFFFF"/>'
                         '<path d="M150 300 L128 560 M150 300 L172 560" stroke="#DCE3E8" stroke-width="4"/>'
                         '<path d="M112 262 C96 330 110 380 140 390 C170 380 186 330 170 262" stroke="#3C4A55" stroke-width="6" fill="none"/><circle cx="140" cy="396" r="12" fill="#9AA6AF" stroke="#3C4A55" stroke-width="4"/>'
                         '<rect x="186" y="330" width="40" height="44" rx="5" fill="none" stroke="#DCE3E8" stroke-width="3"/><rect x="194" y="322" width="5" height="22" fill="#3D6FB6"/>')
        else:
            parts.append(f'<path d="M120 246 L150 296 L180 246" fill="none" stroke="{shirt2}" stroke-width="6"/><rect x="160" y="320" width="44" height="40" rx="6" fill="{shirt2}"/>'
                         '<rect x="96" y="318" width="46" height="12" rx="3" fill="#fff"/>')
        parts.append(f'<ellipse cx="{cx-58}" cy="{cy+10}" rx="12" ry="18" fill="{skin}"/><ellipse cx="{cx+58}" cy="{cy+10}" rx="12" ry="18" fill="{skin}"/>')
        parts.append(f'<ellipse cx="{cx}" cy="{cy+6}" rx="58" ry="68" fill="{skin}"/>')
        hair = '#1E1A18'
        if kind == 'dokter':
            parts.append(f'<path d="M90 120 C84 60 120 50 150 52 C190 50 220 70 212 122 C206 96 190 86 160 90 C130 94 110 86 90 120Z" fill="{hair}"/>')
        else:
            parts.append(f'<path d="M92 118 C86 70 116 48 152 50 C196 52 216 78 208 118 C200 98 196 92 186 86 C160 100 120 96 104 88 C98 96 94 104 92 118Z" fill="{hair}"/>')
    # arms
    sleeve = {'kapus': '#C9A86A', 'bidan': '#F4A7C3', 'dokter': '#FFFFFF', 'perawat': '#2E9C8A'}[kind]
    parts.append(f'<g class="armL"><path d="M66 290 Q40 360 48 440" stroke="{sleeve}" stroke-width="44" stroke-linecap="round" fill="none"/><circle cx="50" cy="452" r="22" fill="{skin}"/></g>')
    parts.append(f'<g class="armR"><path d="M234 290 Q260 360 252 440" stroke="{sleeve}" stroke-width="44" stroke-linecap="round" fill="none"/><circle cx="250" cy="452" r="22" fill="{skin}"/></g>')
    if kind == 'kapus':
        parts.append('<g class="prop"><rect x="196" y="380" width="70" height="92" rx="6" fill="#E0533D" transform="rotate(-8 230 426)"/><rect x="204" y="390" width="54" height="72" rx="4" fill="#fff" opacity=".9" transform="rotate(-8 230 426)"/></g>')
    parts.append(_face(cx, cy + 6, skin, 'sad', glasses=(kind == 'dokter')))
    body = ''.join(parts)
    return (f'<svg id="{cid}" class="chr" viewBox="0 0 300 720" width="300" height="720">{shadow}'
            f'<g class="bob">{body}</g></svg>')
