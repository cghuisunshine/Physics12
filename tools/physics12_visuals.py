"""Embedded, original SVG teaching pictures with text equivalents and predictions.

Coordinates are schematic unless a figure explicitly supplies numerical axes.
Every concept and derivation is mapped explicitly; missing pictures fail builds.
"""
import html
import math

INK, TEAL, BLUE, GOLD, RED = '#182f40', '#076c68', '#245fa6', '#966016', '#a43e35'
PALE, LINE = '#edf6f3', '#b6c8cc'
VISUALS = {}


def text(x, y, value, color=INK, size=17, anchor='start'):
    lines = str(value).split('\n')
    return (f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" text-anchor="{anchor}">'
            + ''.join(f'<tspan x="{x}" dy="{0 if i == 0 else 23}">{html.escape(s)}</tspan>' for i, s in enumerate(lines)) + '</text>')


def path(d, color=TEAL, width=3, fill='none', dash=False):
    return f'<path d="{d}" stroke="{color}" stroke-width="{width}" fill="{fill}"' + (' stroke-dasharray="7 5"' if dash else '') + '/>'


def line(x1, y1, x2, y2, color=LINE, width=2, dash=False):
    return path(f'M{x1} {y1}L{x2} {y2}', color, width, dash=dash)


def arrow(x1, y1, x2, y2, color=TEAL, width=3):
    angle = math.atan2(y2-y1, x2-x1)
    pts = [(x2-12*math.cos(angle) + sign*5*math.sin(angle), y2-12*math.sin(angle)-sign*5*math.cos(angle)) for sign in [-1, 1]]
    return line(x1, y1, x2, y2, color, width) + path(f'M{pts[0][0]:.1f} {pts[0][1]:.1f}L{x2} {y2}L{pts[1][0]:.1f} {pts[1][1]:.1f}', color, width)


def rect(x, y, w, h, fill=PALE, color=TEAL, radius=8):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{color}" stroke-width="2"/>'


def circle(x, y, r, fill=PALE, color=TEAL, dash=False):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{color}" stroke-width="2"' + (' stroke-dasharray="6 5"' if dash else '') + '/>'


def axes(xlabel, ylabel, x=75, y=235, right=565, top=45):
    return (arrow(x, y, right, y, INK, 2) + arrow(x, y, x, top, INK, 2)
            + text(right, y+28, xlabel, anchor='end') + text(x, top-15, ylabel))


def curve(fn, x1=75, x2=550, y0=235, scale=170, color=TEAL):
    pts = [(x1+(x2-x1)*i/100, y0-scale*fn(i/100)) for i in range(101)]
    return path(' '.join(('M' if i == 0 else 'L') + f'{x:.2f} {y:.2f}' for i, (x,y) in enumerate(pts)), color)


def flow(labels, footer=''):
    n = len(labels); w = (580-(n-1)*28)/n
    body = ''
    for i, label in enumerate(labels):
        x = 30+i*(w+28)
        body += rect(x, 85, w, 115) + text(x+w/2, 127, label, anchor='middle')
        if i < n-1: body += arrow(x+w+3, 142, x+w+25, 142, BLUE, 2)
    return body + text(320, 250, footer, anchor='middle')


def register(key, title, drawing, guide, question, answer):
    assert key not in VISUALS
    VISUALS[key] = dict(title=title, svg=drawing, guide=guide, question=question, answer=answer)


# Measurement, kinematics, and vectors.
register('1-1', 'A model keeps the features needed for a question',
    rect(45, 95, 170, 65)+circle(80, 170, 17)+circle(180, 170, 17)+text(130, 70, 'Real car', anchor='middle')
    +arrow(245, 132, 345, 132, BLUE)+circle(445, 132, 9, TEAL)+arrow(455, 132, 570, 132)
    +text(445, 70, 'Particle model', anchor='middle')+text(510, 112, 'v', BLUE)
    +text(320, 240, 'Position and travel time: keep the centre’s motion.', anchor='middle'),
    'The car becomes a dot for a travel-time problem. The arrow is its velocity v; this model has no wheel radius or wheel rotation.',
    'Could this dot model predict how fast a wheel spins?', 'No. Add a wheel model with radius and angular velocity to answer that question.')
register('1-2', 'An uncertainty gives a range of plausible values',
    line(70, 160, 570, 160, INK)+line(170, 140, 170, 180, BLUE)+line(470, 140, 470, 180, BLUE)
    +line(170, 160, 470, 160, BLUE, 7)+circle(320, 160, 7, TEAL)
    +text(170, 210, '2.48 m', anchor='middle')+text(320, 110, '2.50 ± 0.02 m', anchor='middle')+text(470, 210, '2.52 m', anchor='middle'),
    'The dot is the reported length. The blue interval runs from 2.50 − 0.02 to 2.50 + 0.02 m; it expresses the stated uncertainty, not extra calculator digits.',
    'Is a result of 2.60 m inside this stated interval?', 'No. The interval shown is 2.48 to 2.52 m; investigate the uncertainty assumptions or the measurements.')
register('1-3', 'Cancel units before calculating',
    flow(['1 km / hour\ninitial speed', '1000 m / km\n1 hour / 3600 s', '0.2778 m/s\n= 1/3.6 m/s'], 'Multiply by ratios equal to one; km and hour cancel.'),
    'The middle card contains conversion factors. Their numerator and denominator describe the same length or time, so the physical speed does not change.',
    'Is 36 km/h closer to 1, 10, or 100 m/s?', '10 m/s. Dividing 36 by 3.6 is also a useful scale check before using motion equations.')
register('2-1', 'Displacement records endpoints; distance records the path',
    arrow(65, 155, 570, 155, INK)+arrow(150, 105, 460, 105, BLUE)+arrow(460, 200, 300, 200, GOLD)
    +circle(150, 155, 5, TEAL)+circle(300, 155, 5, TEAL)+circle(460, 155, 5, TEAL)
    +text(150, 145, '0 m', anchor='middle')+text(300, 145, '2 m', anchor='middle')+text(460, 145, '4 m', anchor='middle')
    +text(300, 70, 'Walk 0 → 4 m → 2 m', anchor='middle')+text(320, 255, 'Displacement = +2 m; distance = 4 + 2 = 6 m', anchor='middle'),
    'Blue shows the outward leg; gold shows the return. Position x increases rightward. The final position is 2 m to the right of the start, regardless of the detour.',
    'Over 3 s, what are average velocity and average speed?', 'Average velocity is +2/3 m/s. Average speed is 6/3 = 2 m/s. They use different numerators.')
register('2-2', 'Slope gives acceleration; area gives displacement',
    axes('time t / s', 'velocity v / (m/s)')+path('M75 185L475 85L475 235L75 235Z', fill='#ddecf8', color=BLUE, width=1)
    +line(75,185,475,85,BLUE,4)+line(75,185,475,185,LINE,2,True)
    +text(53,190,'2',anchor='end')+text(53,90,'6',anchor='end')+text(475,261,'4',anchor='middle')
    +text(175,215,'rectangle: 8 m')+text(270,145,'triangle: 8 m')+text(325,45,'slope a = (6 − 2)/4 = 1 m/s²',anchor='middle'),
    'The line rises from 2 to 6 m/s in 4 s, so acceleration is +1 m/s². Area is the 2 × 4 rectangle plus the ½ × 4 × 4 triangle: total displacement 16 m.',
    'If the initial velocity were zero, which area would remain?', 'Only the triangle, ½at². The rectangle v₀t would vanish.')
register('2-3', 'Zero velocity at the top does not mean zero acceleration',
    arrow(110,245,110,45,INK)+text(95,35,'+y')+circle(245,190,9)+circle(320,90,9)+circle(405,190,9)
    +arrow(245,175,245,110,BLUE)+arrow(405,205,405,265,BLUE)
    +arrow(270,190,270,240,GOLD)+arrow(345,90,345,140,GOLD)+arrow(430,190,430,240,GOLD)
    +text(195,85,'v upward',BLUE)+text(320,58,'v = 0',BLUE,anchor='middle')+text(430,105,'v downward',BLUE)
    +text(320,290,'Gold arrows: a = −g at all three moments.',GOLD,anchor='middle'),
    'The three balls represent successive moments of one vertical throw. Blue velocity changes sign; each equal gold arrow is the same downward gravitational acceleration.',
    'Immediately after the top, which way does the velocity point?', 'Downward. The continuing downward acceleration changes velocity from zero to a negative value.')
register('3-1', 'A vector is the sum of perpendicular components',
    arrow(100,230,510,230,INK)+arrow(100,230,100,45,INK)+arrow(100,230,450,65,TEAL,4)
    +arrow(100,230,450,230,BLUE)+arrow(450,230,450,65,GOLD)+line(100,65,450,65,LINE,1,True)
    +text(290,256,'Aₓ = A cos θ',BLUE,anchor='middle')+text(470,160,'Aᵧ = A sin θ',GOLD)
    +text(280,112,'A',TEAL,22)+path('M150 230A50 50 0 0 0 145 208',INK,2)+text(160,215,'θ'),
    'The teal diagonal A equals the blue horizontal component followed by the gold vertical component. The right triangle defines the sine and cosine factors.',
    'For an arrow pointing up and left, what signs do its components have?', 'Aₓ is negative and Aᵧ is positive when right and up are the positive axes.')
register('3-2', 'Horizontal and vertical motion share one clock',
    axes('horizontal position x', 'height y')+path('M75 235Q310 -100 545 235',TEAL,3)
    +''.join(circle(75+470*u,235-670*u*(1-u),6,TEAL) for u in [0,.25,.5,.75,1])
    +arrow(192,110,252,110,BLUE)+arrow(310,67,370,67,BLUE)+arrow(428,110,488,110,BLUE)
    +arrow(310,80,310,137,GOLD)+text(425,54,'vₓ constant',BLUE)
    +text(355,155,'aᵧ = −g',GOLD)+text(320,288,'Dots: equal time intervals; horizontal gaps are equal.',anchor='middle'),
    'Each dot is a later position of the same ideal projectile. Equal time intervals give equal horizontal displacement. Gravity changes vertical velocity, including at the top.',
    'Does a larger downward acceleration change vₓ in this model?', 'No. With no horizontal force, aₓ = 0. It changes the flight time and therefore the range.')
register('3-3', 'The range shortcut needs equal launch and landing height',
    line(50,220,590,220,INK)+path('M65 220Q300 -40 535 220',TEAL)
    +arrow(65,260,535,260,BLUE)+text(300,286,'R = horizontal range',BLUE,anchor='middle')
    +circle(65,220,6,TEAL)+circle(535,220,6,TEAL)+text(70,190,'launch')+text(505,190,'landing')
    +text(320,55,'Same reference height: Δy = 0',anchor='middle')+text(320,100,'T = 2v₀ sin θ / g',anchor='middle'),
    'The two endpoint dots lie on the same horizontal line. Setting the vertical displacement to zero gives a nonzero landing time, which determines horizontal range.',
    'Can you use this flight-time shortcut for a launch from a cliff?', 'No. Use the actual landing displacement in Δy = v₀ᵧt − ½gt² and choose the positive physical time.')

# Forces, energy, momentum, rotation, and equilibrium.
register('4-1', 'Third-law forces act on different objects',
    circle(190,140,50)+circle(450,140,50)+text(190,145,'A',anchor='middle')+text(450,145,'B',anchor='middle')
    +arrow(240,120,340,120,BLUE)+arrow(400,165,300,165,GOLD)
    +text(285,85,'Force on A by B',BLUE,anchor='middle')+text(345,215,'Force on B by A',GOLD,anchor='middle')
    +text(320,270,'Equal magnitudes; opposite directions; different bodies.',anchor='middle'),
    'For an attractive interaction, B pulls A rightward and A pulls B leftward. These forces do not cancel in A’s own free-body diagram; only the force on A belongs there.',
    'If A has twice B’s mass, are the interaction forces different?', 'No. The forces have equal magnitude, but the larger mass has the smaller acceleration for this interaction.')
register('4-2', 'A free-body diagram isolates one object',
    rect(260,120,100,80)+line(80,200,560,200)+arrow(310,120,310,45,BLUE)+arrow(310,200,310,275,GOLD)
    +arrow(360,160,530,160,TEAL)+arrow(260,160,150,160,RED)
    +text(328,62,'N',BLUE)+text(328,273,'mg',GOLD)+text(470,140,'pull',TEAL)+text(115,140,'friction',RED)
    +text(310,100,'vertical balance: N = mg',anchor='middle'),
    'The box slides right on a level floor. The normal force N and weight mg balance vertically; pull minus kinetic friction is the horizontal net force. Arrow lengths are schematic.',
    'Which force changes if the pull tilts upward?', 'The normal force decreases when there is no vertical acceleration: N = mg − F_pull sin θ. Friction then changes too.')
register('4-3', 'Resolve weight along and perpendicular to a slope',
    path('M100 235L500 75L500 235Z',LINE,2,PALE)+circle(300,155,10,TEAL)
    +arrow(300,155,300,265,GOLD)+arrow(300,155,262,170,RED)+arrow(300,155,338,250,BLUE)
    +line(262,170,300,265,RED,1,True)+line(338,250,300,265,BLUE,1,True)
    +arrow(300,155,265,67,TEAL)+text(155,190,'mg sin θ',RED)+text(345,240,'mg cos θ',BLUE)
    +text(305,288,'mg',GOLD)+text(245,54,'N',TEAL)+text(320,35,'Axes follow the surface.',anchor='middle'),
    'The gold weight splits into a downhill red component and a blue component into the surface. The normal is perpendicular outward. Components are parts of weight, not additional forces.',
    'On a frictionless slope, what is the downhill acceleration?', 'g sin θ, because the downhill net force is mg sin θ and division by mass cancels m.')
register('5-1', 'Circular motion needs an inward acceleration',
    circle(270,155,100,'none',LINE,True)+circle(270,155,10,TEAL)+circle(370,155,8,TEAL)
    +arrow(370,145,370,45,BLUE)+arrow(358,155,290,155,GOLD)+line(270,155,365,155,LINE,1,True)
    +text(390,65,'v tangent',BLUE)+text(400,180,'a inward',GOLD)+text(290,185,'r')
    +text(320,290,'Speed may stay fixed while the velocity direction changes.',anchor='middle'),
    'At the rightmost point, tangent velocity points upward and radial acceleration points left. Their perpendicular directions let the object turn without changing speed.',
    'If speed doubles at fixed radius, how does radial acceleration change?', 'It quadruples because aᵣ = v²/r. The required inward resultant force also quadruples at fixed mass.')
register('5-2', 'In a vertical circle, inward changes direction',
    circle(320,145,88,'none',LINE,True)+circle(320,57,8,TEAL)+circle(320,233,8,TEAL)
    +arrow(295,57,295,112,TEAL)+arrow(345,57,345,112,GOLD)
    +arrow(295,233,295,178,TEAL)+arrow(345,233,345,285,GOLD)
    +text(125,83,'TOP: both inward')+text(125,108,'T + mg = mv²/r')
    +text(410,206,'BOTTOM:')+text(410,231,'T − mg = mv²/r')+text(100,280,'teal: tension T; gold: weight mg'),
    'At the top, both tension and weight point toward the centre. At the bottom, tension points inward but weight points outward. Write a fresh radial equation at each point.',
    'For the same speed at top and bottom, where is the required tension larger?', 'At the bottom: T_bottom = mv²/r + mg, while T_top = mv²/r − mg. A string can pull but cannot supply negative tension.')
register('5-3', 'Radius connects gravity, orbital speed, and period',
    circle(215,150,40)+circle(215,150,75,'none',BLUE,True)+circle(215,150,120,'none',LINE,True)
    +circle(290,150,6,BLUE)+circle(335,150,6,TEAL)+text(215,155,'M',anchor='middle')
    +text(390,90,'r measured from centre')+text(390,135,'g = GM/r²')+text(390,175,'v = √(GM/r)')+text(390,215,'T² ∝ r³'),
    'Both circular paths orbit the same central mass M. A larger orbital radius weakens gravity, lowers circular speed, and increases the time to complete an orbit.',
    'If orbital radius doubles, by what factor does the period change?', 'T becomes 2^(3/2) ≈ 2.83 times as large, because T² is proportional to r³.')
register('6-1', 'Only the force component along displacement does work',
    rect(125,155,80,55)+arrow(170,155,380,65,TEAL)+arrow(170,155,380,155,BLUE)
    +line(380,65,380,155,LINE,1,True)+arrow(160,245,510,245,INK)
    +text(395,70,'F',TEAL)+text(290,180,'F cos θ',BLUE,anchor='middle')+text(270,120,'θ')
    +text(320,275,'displacement d →',anchor='middle')+text(450,120,'W = Fd cos θ'),
    'The applied force is diagonal, but the box’s displacement is horizontal. The blue projection is the component that transfers energy through work.',
    'What is the work if the force is perpendicular to displacement?', 'Zero, because cos 90° = 0. A perpendicular force can still change the direction of motion.')
register('6-2', 'Energy moves between stores without disappearing',
    rect(60,50,160,170)+rect(250,50,160,170)+rect(440,50,160,170)
    +rect(100,80,32,110,'#dbe7f7',BLUE)+rect(290,135,32,55,'#dbe7f7',BLUE)+rect(332,135,32,55,'#cce5dc',TEAL)
    +rect(480,168,32,22,'#dbe7f7',BLUE)+rect(522,140,32,50,'#cce5dc',TEAL)+rect(564,152,22,38,'#f1dfbd',GOLD)
    +text(140,250,'initial: all U',anchor='middle')+text(330,250,'later: U + K',anchor='middle')+text(520,250,'with friction',anchor='middle')
    +text(320,285,'Blue = potential U; teal = kinetic K; gold = thermal.',anchor='middle'),
    'Each panel represents the same total energy, divided into stores. In the first two panels mechanical energy is conserved. The last includes thermal energy produced by friction; bar heights are schematic.',
    'Does friction destroy energy?', 'No. It transfers mechanical energy into thermal and other internal stores. Include those stores when counting total energy.')
register('6-3', 'Power compares the rate of the same energy transfer',
    flow(['Lift mass m\nthrough height h', 'Work = mgh\nfor either lift', 'Power = mgh/t\nfaster → greater P'], 'Same endpoints, same work; different times, different power.'),
    'For equal start and end speeds, each lift increases gravitational energy by mgh. Power measures how quickly this transfer occurs, not just its size.',
    'If a lift takes half the time for the same load and height, what happens to average power?', 'It doubles: P_avg = W/Δt, while the work mgh stays the same.')
register('7-1', 'Impulse is area under a force–time graph',
    axes('time t', 'force F')+rect(130,85,100,150,'#dbe7f7',BLUE,0)+rect(320,160,200,75,'#f1dfbd',GOLD,0)
    +text(180,65,'short stop',BLUE,anchor='middle')+text(420,140,'longer stop',GOLD,anchor='middle')
    +text(320,290,'Equal shaded areas = equal impulse = equal Δp',anchor='middle'),
    'The rectangles have equal area. The blue stop has twice the average force over half the time; the gold stop produces the same momentum change more gradually.',
    'For the same change in momentum, what happens if stopping time triples?', 'Average net force becomes one third as large: F_avg = Δp/Δt.')
register('7-2', 'Choose both colliding objects as one system',
    rect(55,105,135,70)+rect(240,105,135,70)+arrow(75,75,165,75,BLUE)+text(310,75,'at rest',anchor='middle')
    +arrow(400,140,450,140,INK)+rect(475,105,130,70)+line(540,105,540,175,INK)
    +arrow(490,75,570,75,TEAL)+text(215,235,'BEFORE: p = m₁v₁',anchor='middle')+text(505,235,'AFTER: (m₁+m₂)v',anchor='middle'),
    'Two carts stick. When external impulse is negligible, total momentum before equals total momentum after. Their internal contact forces exchange momentum within the chosen two-cart system.',
    'Do the carts retain all their original kinetic energy when they stick?', 'Generally no. Some becomes deformation, sound, and internal energy, even while total momentum is conserved.')
register('7-3', 'The centre of mass lies closer to the larger mass',
    line(110,165,530,165,INK)+circle(110,165,20)+circle(530,165,35)+circle(425,165,7,RED)
    +text(110,105,'m at x = 0',anchor='middle')+text(530,105,'3m at x = 4 m',anchor='middle')
    +arrow(110,230,425,230,BLUE)+text(425,205,'CM: x = 3 m',RED,anchor='middle')
    +text(320,285,'x_CM = (m·0 + 3m·4)/(4m) = 3 m',anchor='middle'),
    'The red dot is the mass-weighted average position. Three times as much mass on the right shifts the centre of mass toward that side.',
    'Where would the centre of mass be if the two masses were equal?', 'At the midpoint, x = 2 m. The formula averages positions with mass as the weight.')
register('8-1', 'Radians connect angular and linear motion',
    circle(255,155,100,'none',LINE)+line(255,155,355,155,INK)+line(255,155,305,68,INK)
    +path('M355 155A100 100 0 0 0 305 68',TEAL,5)+text(275,140,'θ')+text(310,180,'r')
    +arrow(310,65,255,32,BLUE)+text(395,95,'arc s = rθ')+text(395,140,'v_t = rω')+text(395,185,'a_t = rα'),
    'The teal arc has length s and subtends angle θ in radians at the centre. At larger radius, the same angular change corresponds to more travel.',
    'Two points share the same ω; one is twice as far from the axis. How do their speeds compare?', 'The outer point has twice the tangential speed because v_t = rω.')
register('8-2', 'Torque uses the perpendicular lever arm',
    circle(100,175,9,INK)+line(100,175,480,175,INK,7)+arrow(480,175,480,65,TEAL)
    +line(480,45,480,250,LINE,1,True)+arrow(110,235,480,235,BLUE)
    +text(100,135,'pivot',anchor='middle')+text(500,90,'F',TEAL)+text(290,265,'lever arm r⊥',BLUE,anchor='middle')
    +text(320,40,'τ = F r⊥; I = Σmr²',anchor='middle'),
    'The force acts upward along the dashed line. Its shortest distance from the pivot is the horizontal lever arm r⊥, so it creates a turning effect.',
    'What happens to torque if the same perpendicular force acts twice as far from the pivot?', 'Torque doubles. For a given rotational inertia I, angular acceleration doubles too.')
register('8-3', 'Rolling combines translation and rotation',
    circle(310,145,85,'none',TEAL)+line(65,230,570,230,INK)+circle(310,230,6,RED)
    +arrow(310,145,365,145,BLUE)+arrow(310,60,365,60,BLUE)+arrow(365,60,420,60,GOLD)
    +text(390,150,'v_CM = Rω',BLUE)+text(310,32,'top speed = 2v_CM',anchor='middle')
    +text(310,275,'Contact point: ground-frame velocity = 0',RED,anchor='middle'),
    'The wheel rolls right without slipping on stationary ground. Blue represents translation; gold adds the top point’s rotational velocity. Translation and clockwise rotation cancel at the contact point and add at the top.',
    'Is the ground-frame velocity of the contact point equal to the centre velocity?', 'No. It is momentarily zero for pure rolling. The centre moves at v_CM, and the top moves at 2v_CM.')
register('9-1', 'A balanced beam must balance force and torque',
    line(70,140,570,140,INK,7)+path('M300 150L270 205H330Z',TEAL,2,PALE)
    +arrow(150,140,150,220,GOLD)+arrow(450,140,450,220,GOLD)+arrow(300,140,300,55,BLUE)
    +text(150,250,'F₁',GOLD,anchor='middle')+text(450,250,'F₂',GOLD,anchor='middle')+text(320,65,'support N',BLUE)
    +text(320,290,'Equal arms: balance requires F₁ = F₂ and N = F₁ + F₂.',anchor='middle'),
    'The upward support balances the total load. Equal forces at equal distances from the pivot also make clockwise and counterclockwise torques cancel. The beam’s own weight is neglected here.',
    'Can two equal opposite forces turn an object?', 'Yes. If they act along different lines, they form a couple: zero net force but nonzero net torque.')
register('9-2', 'A support base must contain the weight’s line of action',
    rect(80,85,130,135)+circle(145,140,7,RED)+arrow(145,140,145,255,GOLD)+line(50,220,265,220,INK)
    +path('M390 220L435 65L555 100L510 255Z',TEAL,2,PALE)+circle(475,140,7,RED)
    +arrow(475,140,475,275,GOLD)+line(360,220,435,220,INK)+text(145,55,'supported',anchor='middle')
    +text(485,45,'tipping begins',anchor='middle')+text(320,295,'Gold line: weight through the centre of mass.',anchor='middle'),
    'On the left, the vertical weight line passes within the base. On the right, the tilted object is supported only at its edge and the weight line lies outside that support, creating a tipping torque.',
    'Why does widening the base usually improve stability?', 'It allows a larger tilt before the weight line passes outside the support region.')
register('9-3', 'Stress stretches a material; strain measures the fraction',
    rect(120,90,170,35)+rect(120,165,260,35)+arrow(380,183,510,183,BLUE)+text(115,70,'original length L₀')
    +arrow(290,235,380,235,INK,2)+text(335,260,'ΔL',anchor='middle')+line(290,140,290,225,LINE,1,True)+line(380,140,380,225,LINE,1,True)
    +text(490,150,'pull F',BLUE,anchor='middle')+text(320,285,'stress = F/A; strain = ΔL/L₀; Y = stress/strain',anchor='middle'),
    'The lower bar is the same specimen under tension; the extension is exaggerated. Cross-sectional area A sets stress, while the original length L₀ sets the strain denominator.',
    'For the same material, load, and length, how does doubling area change extension?', 'It halves extension in the linear elastic regime: ΔL = FL₀/(AY).')

# Fluids, oscillations, sound, and thermal physics.
register('10-1', 'Pressure increases with depth',
    rect(100,55,250,205,'#edf4fc',BLUE)+line(100,90,350,90,BLUE)+text(390,90,'surface: P₀')
    +arrow(140,100,140,210,INK)+text(155,160,'depth h')+circle(280,210,6,TEAL)
    +arrow(350,210,425,210,BLUE)+text(440,215,'P₀ + ρgh')+text(320,290,'Same depth in the same resting fluid → same pressure.',anchor='middle'),
    'Depth h is measured downward from the surface, where pressure is P₀. The weight of water above a point accounts for the additional pressure ρgh. Density ρ and g are constant here.',
    'At twice the depth, does the absolute pressure always double?', 'No. The gauge pressure ρgh doubles, but absolute pressure also includes the unchanged surface pressure P₀.')
register('10-2', 'Floating means buoyancy balances weight',
    rect(90,115,290,145,'#edf4fc',BLUE)+line(90,115,380,115,BLUE)+rect(180,70,110,110,'#f5f4ef',TEAL)
    +rect(180,115,110,65,'#cfe4ef',BLUE,0)+arrow(235,115,235,30,TEAL)+arrow(235,150,235,240,GOLD)
    +text(310,55,'F_b upward',TEAL)+text(310,225,'mg downward',GOLD)+text(425,135,'Shaded volume:')
    +text(425,160,'displaced fluid')+text(425,200,'F_b = ρ_fluid gV_sub'),
    'The immersed part of the object occupies the volume that fluid would otherwise fill. In floating equilibrium, the weight of that displaced fluid equals the object’s whole weight.',
    'An object has half the fluid’s average density. What fraction of its volume floats below the surface?', 'One half: V_sub/V = ρ_object/ρ_fluid = ½, for equilibrium in the uniform fluid.')
register('10-3', 'A narrow flow section needs a larger speed',
    path('M55 80H200L330 125H585M55 220H200L330 175H585',BLUE,4)
    +arrow(90,150,175,150,TEAL)+arrow(360,150,540,150,TEAL)+text(115,55,'A₁ large')+text(425,100,'A₂ small')
    +text(90,260,'v₁ lower')+text(395,230,'v₂ higher')+text(320,290,'Steady incompressible flow: A₁v₁ = A₂v₂',anchor='middle'),
    'The same fluid volume crosses each section every second. With smaller cross-sectional area A₂, speed v₂ must rise. At equal height, ideal Bernoulli flow has lower static pressure in the narrow section.',
    'If the cross-sectional area halves, how does the speed change?', 'It doubles for steady incompressible flow, because Av must remain constant.')
register('11-1', 'A spring’s restoring force points toward equilibrium',
    line(80,155,550,155,INK)+line(320,55,320,240,LINE,2,True)
    +circle(145,155,15)+circle(320,155,15)+circle(495,155,15)
    +arrow(165,130,255,130,TEAL)+arrow(475,130,385,130,TEAL)
    +text(145,205,'x = −A',anchor='middle')+text(320,205,'x = 0',anchor='middle')+text(495,205,'x = +A',anchor='middle')
    +text(320,70,'equilibrium',anchor='middle')+text(320,270,'At centre: speed largest; at ends: speed zero.',anchor='middle'),
    'The three dots are three positions of one oscillator. At either end, F = −kx points back toward x = 0. A larger displacement produces a larger restoring force.',
    'Is acceleration zero where speed is greatest?', 'Yes, in ideal spring SHM it is zero at x = 0 because the restoring force vanishes there. Speed is changing least rapidly at that instant.')
register('11-2', 'A pendulum restores; damping removes energy',
    circle(135,45,5,INK)+line(135,45,135,210,LINE,1,True)+line(135,45,205,195,INK,3)+circle(205,195,15)
    +text(160,120,'ℓ')+text(150,85,'θ')+arrow(195,215,150,235,TEAL)
    +axes('time', 'displacement',340,235,600,55)
    +curve(lambda u:.45*math.exp(-2*u)*math.sin(8*math.pi*u),350,590,150,140,BLUE)
    +line(350,150,590,150,LINE,1,True)+text(337,155,'0',size=14,anchor='end')
    +text(135,280,'Small-angle restoring motion',anchor='middle')+text(475,280,'Damping shrinks amplitude',anchor='middle'),
    'Left: gravity has a tangential component back toward the lowest point. Right: the oscillation amplitude decreases as damping transfers mechanical energy to other stores. The sketch is schematic.',
    'Does making an ideal small-angle pendulum heavier change its period?', 'No. Mass cancels from the equation of motion; T ≈ 2π√(ℓ/g). Length and g set the period.')
register('11-3', 'Standing-wave nodes fix the allowed wavelengths',
    line(95,100,555,100,LINE)+path('M95 100Q325 -30 555 100',BLUE,3)
    +line(95,220,555,220,LINE)+path('M95 220Q210 90 325 220Q440 350 555 220',TEAL,3)
    +''.join(circle(x,y,5,INK) for x,y in [(95,100),(555,100),(95,220),(325,220),(555,220)])
    +text(325,35,'n = 1: L = λ/2',BLUE,anchor='middle')+text(325,165,'n = 2: L = λ',TEAL,anchor='middle')
    +text(325,295,'Black dots are nodes; the string is fixed at both ends.',anchor='middle'),
    'Each curve shows one instant of a standing wave. Nodes never move. The fundamental fits half a wavelength; the second mode fits a full wavelength in the same length L.',
    'At the same wave speed, how do these mode frequencies compare?', 'The n = 2 frequency is twice the fundamental because its wavelength is half as long.')
register('12-1', 'Sound carries compressions through a medium',
    ''.join(line(x,95,x,190,BLUE,2) for x in [60,70,80,90,100,140,180,220,230,240,250,260,300,340,380,390,400,410,420,460,500,540,550,560,570,580])
    +arrow(160,55,475,55,TEAL)+text(320,35,'wave travels right',anchor='middle')
    +text(82,225,'compression',anchor='middle')+text(175,260,'rarefaction',anchor='middle')
    +arrow(275,255,345,255,GOLD)+arrow(345,275,275,275,GOLD)+text(420,270,'air oscillates ↔',GOLD),
    'Close lines represent high-pressure compressions; spread lines represent lower-pressure rarefactions. The pattern travels, while a small parcel of air oscillates around its local equilibrium.',
    'Do the same air molecules travel all the way from the speaker to your ear?', 'No. Local oscillations pass the disturbance and energy along; bulk transport of the air is not required.')
register('12-2', 'Closed and open ends impose different boundaries',
    path('M85 65H550M85 150H550M85 65V150',INK,3)+curve(lambda u:math.sin(.5*math.pi*u),85,550,108,35,BLUE)
    +path('M85 195H550M85 280H550M85 195V280',INK,3)+curve(lambda u:math.sin(1.5*math.pi*u),85,550,238,35,TEAL)
    +circle(85,108,5,INK)+circle(85,238,5,INK)+circle(395,238,5,INK)
    +text(320,35,'Displacement patterns in a pipe closed on the left',anchor='middle')
    +text(320,175,'fundamental: L = λ/4; next mode: L = 3λ/4',anchor='middle'),
    'The closed left end is a displacement node; the open right end is a displacement antinode. The curves show displacement amplitude patterns, not the path taken by air through the pipe.',
    'Why is the second allowed frequency 3f₁ rather than 2f₁?', 'A node-to-antinode pipe must contain an odd number of quarter wavelengths. Its ideal modes are f₁, 3f₁, 5f₁, and so on.')
register('12-3', 'A moving source crowds wavefronts ahead',
    circle(200,150,125,'none',BLUE)+circle(225,150,90,'none',BLUE)+circle(250,150,55,'none',BLUE)
    +circle(275,150,8,TEAL)+arrow(275,150,360,150,TEAL)+text(380,150,'source moves →')
    +text(120,290,'Behind: longer λ',anchor='middle')+text(440,250,'Ahead: shorter λ',anchor='middle'),
    'Each circle is a wavefront emitted when the source was farther left. The source moves right slower than sound, so front wavefronts are closer together while rear wavefronts are farther apart.',
    'Which side hears a higher frequency if listeners are at rest in the medium?', 'The side ahead. Sound speed in the medium is unchanged, so the shorter wavelength gives larger f = v/λ.')
register('13-1', 'Thermal expansion is a small fractional length change',
    rect(90,95,330,35)+rect(90,175,400,35,'#f1dfbd',GOLD)
    +line(420,75,420,235,LINE,1,True)+line(490,155,490,235,LINE,1,True)
    +text(90,75,'cooler: length L₀')+text(90,155,'warmer: L₀ + ΔL',GOLD)
    +text(455,255,'ΔL',anchor='middle')+text(320,290,'ΔL = αL₀ΔT; extension exaggerated for visibility.',anchor='middle'),
    'The warmer bar is slightly longer in a material with positive expansion coefficient α. The extra length depends on the original length and temperature increase, not just on final temperature.',
    'For equal material and temperature rise, which expands more: a 1 m or a 2 m bar?', 'The 2 m bar has twice the extension because ΔL is proportional to L₀ in this model.')
register('13-2', 'Molecular collisions exert pressure on a wall',
    rect(75,55,310,205,'#f8fafc',BLUE)+circle(225,145,10,TEAL)+arrow(235,125,370,125,TEAL)
    +arrow(370,170,235,170,GOLD)+line(385,55,385,260,INK,6)
    +text(430,110,'Incoming: +mvₓ',TEAL)+text(430,165,'Outgoing: −mvₓ',GOLD)
    +text(320,290,'Each collision transfers momentum to the wall.',anchor='middle'),
    'The molecule reverses its perpendicular velocity in an elastic wall collision. The wall receives the opposite momentum change; many impacts per second produce a steady average pressure.',
    'At fixed volume and molecule count, why does heating an ideal gas raise pressure?', 'Molecules have larger mean squared speed. Their faster, stronger momentum transfers increase P = Nm⟨v²⟩/(3V).')
register('13-3', 'Equal temperature means equal average translational energy',
    circle(165,135,14)+circle(440,135,30)+arrow(165,135,300,135,BLUE)+arrow(440,135,508,135,GOLD)
    +text(165,80,'light molecule: m',anchor='middle')+text(440,80,'heavy molecule: 4m',anchor='middle')
    +text(165,210,'v_rms = v',BLUE,anchor='middle')+text(440,210,'v_rms = v/2',GOLD,anchor='middle')
    +text(320,275,'Same T → same mean K = 3k_B T/2',anchor='middle'),
    'Compare two ideal gases at the same temperature. A molecule four times heavier has half the rms speed, so ½m⟨v²⟩ is unchanged. Arrows compare rms values, not individual trajectories.',
    'Do all molecules in one gas have exactly the rms speed?', 'No. There is a distribution of speeds; rms is the square root of the mean squared speed.')
register('14-1', 'Heat is a transfer, not a substance stored inside a body',
    rect(60,80,170,120,'#f1dfbd',GOLD)+rect(410,80,170,120,'#dbe7f7',BLUE)+arrow(245,140,395,140,RED)
    +text(145,120,'hot body',anchor='middle')+text(145,160,'internal U',anchor='middle')
    +text(495,120,'cool body',anchor='middle')+text(495,160,'internal U',anchor='middle')+text(320,115,'heat Q',RED,anchor='middle')
    +text(320,260,'Energy flows because of a temperature difference.',anchor='middle'),
    'Internal energy U belongs to each body’s microscopic state. The arrow Q denotes energy crossing the boundary because the bodies have different temperatures.',
    'When both bodies reach the same temperature, is all internal energy gone?', 'No. Net heat transfer stops at thermal equilibrium, but both bodies still have internal energy.')
register('14-2', 'During a phase change, heating need not raise temperature',
    axes('energy added Q', 'temperature T')+path('M75 220L235 145H395L550 60',TEAL,4)
    +text(145,175,'solid warms',size=15)+text(315,125,'melting',anchor='middle')+text(475,100,'liquid warms',size=15)
    +text(320,290,'Sloped parts: Q = mcΔT; flat part: Q = mL',anchor='middle'),
    'This ideal fixed-pressure heating curve has a plateau while solid becomes liquid. Energy supplied on the plateau changes the phase fraction rather than the temperature.',
    'Should you use mcΔT to calculate the energy needed on the melting plateau?', 'No. ΔT is zero there but energy is still required; use the latent heat term mL for the amount that melts.')
register('14-3', 'Three ways to transfer thermal energy',
    rect(30,85,170,95)+arrow(45,125,185,125,RED)+text(115,65,'conduction',anchor='middle')+text(115,225,'through matter',anchor='middle')
    +rect(235,85,170,95,'#edf4fc',BLUE)+path('M270 160V110H365V160H270',GOLD,3)+text(320,65,'convection',anchor='middle')+text(320,225,'moving fluid',anchor='middle')
    +curve(lambda u:.15*math.sin(8*math.pi*u),445,600,125,100,RED)+arrow(445,155,600,155,RED)
    +text(525,65,'radiation',anchor='middle')+text(525,225,'can cross vacuum',anchor='middle'),
    'Conduction transfers energy through microscopic interactions without bulk flow. Convection carries energy with a moving fluid. Radiation transports energy as electromagnetic waves and needs no material medium.',
    'Which mechanism carries sunlight across space to Earth?', 'Radiation. Conduction and convection require matter along the transfer route.')
register('15-1', 'The first law accounts for energy crossing a boundary',
    rect(220,75,200,150)+text(320,135,'SYSTEM',anchor='middle')+text(320,175,'internal energy U',anchor='middle')
    +arrow(60,150,205,150,RED)+arrow(435,150,580,150,BLUE)+text(115,120,'heat Q in',RED,anchor='middle')+text(515,120,'work W out',BLUE,anchor='middle')
    +text(320,275,'ΔU = Q − W; signs refer to this system.',anchor='middle'),
    'Heat entering the boundary adds internal energy; work done by the system transfers energy outward. The equation uses W > 0 for work done by the system.',
    'If Q = +80 J enters and W = +30 J leaves as work, what is ΔU?', '+50 J. The system gains the energy that enters minus the energy it sends out.')
register('15-2', 'The area on a P–V diagram is expansion work',
    axes('V', 'pressure P')+path('M145 100H495V235H145Z',BLUE,1,'#dbe7f7')
    +arrow(145,100,495,100,BLUE)+line(145,100,145,235,LINE,1,True)+text(145,261,'Vᵢ',anchor='middle')+text(495,261,'V_f',anchor='middle')
    +text(320,170,'W = P(V_f − Vᵢ)',anchor='middle')+text(320,285,'Constant-pressure path: area is work by the gas.',anchor='middle'),
    'For this quasistatic constant-pressure expansion, each small volume increase contributes P dV. The shaded rectangle has area PΔV and units joules.',
    'What is the boundary work on a vertical constant-volume P–V path?', 'Zero. With ΔV = 0, there is no area under the path in the volume direction and no piston boundary work.')
register('15-3', 'An engine must reject some heat',
    rect(70,35,190,60,'#f1dfbd',GOLD)+rect(70,135,190,60)+rect(70,235,190,50,'#dbe7f7',BLUE)
    +arrow(165,95,165,130,RED)+arrow(165,195,165,230,BLUE)+arrow(265,165,525,165,TEAL)
    +text(165,73,'hot reservoir T_H',anchor='middle')+text(165,173,'cyclic engine',anchor='middle')+text(165,267,'cold reservoir T_C',anchor='middle')
    +text(290,115,'Q_H enters')+text(290,230,'Q_C rejected')+text(445,145,'work W_out',TEAL,anchor='middle'),
    'The engine returns to its initial state each cycle, so W_out = Q_H − Q_C. Heat rejected to the cold reservoir is required by the second law; a reversible engine sets the maximum efficiency.',
    'Can a reversible engine between 600 K and 300 K have 75% efficiency?', 'No. Its Carnot limit is 1 − 300/600 = 50%. A real engine is no more efficient than this limit.')

# Electrostatics, circuits, magnetism, and electromagnetic waves.
register('16-1', 'Charging transfers electrons and conserves total charge',
    rect(55,75,190,140)+rect(395,75,190,140)
    +''.join(circle(x,y,8,'#dbe7f7',BLUE)+text(x,y+5,'−',BLUE,14,'middle') for x,y in [(90,110),(130,110),(440,110),(480,110),(520,110),(440,155),(480,155),(520,155)])
    +arrow(265,145,375,145,BLUE)+text(320,115,'electrons',BLUE,anchor='middle')
    +text(150,250,'loses electrons → +',anchor='middle')+text(485,250,'gains electrons → −',anchor='middle'),
    'The two objects initially have equal positive and negative charge overall. Transferring electrons rightward leaves a positive deficit on the left and an equal negative excess on the right. Positive ion cores are omitted.',
    'Does rubbing create a new net charge for the isolated pair?', 'No. It redistributes charge. The total charge of the two-object isolated system is unchanged.')
register('16-2', 'Electric-field direction uses a positive test charge',
    circle(135,145,38)+text(135,155,'+',TEAL,32,'middle')+circle(365,145,10,TEAL)+arrow(365,145,535,145,BLUE)
    +text(135,80,'source +Q',anchor='middle')+text(440,110,'E outward',BLUE,anchor='middle')+text(365,205,'test location',anchor='middle')
    +text(320,270,'Positive q: F with E. Negative q: F opposite E.',anchor='middle'),
    'A positive source creates an outward electric field at the marked point. The field belongs to the source configuration; the force on a test particle is F = qE and depends on its charge sign.',
    'Which way does an electron accelerate at this point if the electric force is the only force?', 'Left, toward +Q, because its negative charge makes its force opposite the rightward field.')
register('16-3', 'A Gaussian surface counts enclosed charge through flux',
    circle(245,150,95,'none',BLUE,True)+circle(245,150,20)+text(245,156,'+Q',anchor='middle',size=16)
    +''.join(arrow(245+40*math.cos(a),150+40*math.sin(a),245+122*math.cos(a),150+122*math.sin(a),TEAL,2) for a in [0,math.pi/2,math.pi,3*math.pi/2])
    +text(415,105,'Dashed: closed surface')+text(415,155,'Flux = Q/ε₀')+text(415,205,'sphere: area = 4πr²'),
    'Outward field arrows cross a spherical imaginary boundary. By symmetry, E is constant and normal on the sphere, so Gauss’s law becomes E(4πr²) = Q/ε₀.',
    'Does zero enclosed charge always mean zero electric field?', 'No. External charges can create a field that enters and leaves the surface with zero net flux.')
register('17-1', 'Field points toward lower electric potential',
    ''.join(line(x,65,x,235,LINE,2,True)+text(x,270,label,anchor='middle') for x,label in [(100,'30 V'),(300,'20 V'),(500,'10 V')])
    +arrow(115,140,565,140,TEAL)+text(320,110,'electric field E →',TEAL,anchor='middle')
    +text(320,35,'Equipotential lines (uniform field)',anchor='middle'),
    'Dashed lines mark equal-potential surfaces seen edge-on. Moving right lowers potential. A positive charge loses potential energy qΔV in that direction; a negative charge gains it.',
    'What is ΔU for +2 C moving from 30 V to 10 V?', 'ΔU = q(V_f − V_i) = 2(10 − 30) = −40 J. The electric force does +40 J of work.')
register('17-2', 'Equipotential motion and cross-field motion differ',
    circle(250,150,25)+text(250,157,'+Q',anchor='middle')+circle(250,150,75,'none',BLUE,True)+circle(250,150,125,'none',BLUE,True)
    +arrow(340,150,405,150,TEAL)+path('M250 75A75 75 0 0 1 325 150',GOLD,4)
    +text(425,110,'Radial E ⟂ circles')+text(425,165,'Gold arc: ΔV = 0')+text(425,215,'No electric work'),
    'The circles are equipotentials around a positive point charge. Moving along one circle keeps r and V fixed. The radial field is perpendicular to that motion.',
    'Is an electron volt a voltage or an energy?', 'An energy: 1 eV is the energy magnitude for one elementary charge crossing 1 volt, about 1.602 × 10⁻¹⁹ J.')
register('17-3', 'A capacitor separates charge across a gap',
    rect(130,55,15,180,'#dbe7f7',BLUE,0)+rect(450,55,15,180,'#f1dfbd',GOLD,0)
    +''.join(text(110,y,'+',BLUE,22,'middle')+text(490,y,'−',GOLD,22,'middle') for y in [90,140,190])
    +''.join(arrow(175,y,420,y,TEAL,2) for y in [95,145,195])+arrow(150,260,450,260,INK,2)
    +text(300,285,'gap d; E from + plate to − plate',anchor='middle')+text(300,35,'Plate area A; voltage magnitude V = Ed',anchor='middle'),
    'Two parallel plates carry equal and opposite charges. Their fields add between the plates. For ideal plates, C = εA/d and Q = CV; a linear dielectric increases ε.',
    'At fixed plate area and dielectric, what happens to capacitance when the gap doubles?', 'It halves. At fixed Q the voltage doubles; at fixed V the stored charge halves.')
register('18-1', 'Electron drift and conventional current point oppositely',
    rect(65,95,510,100,'#f8fafc',LINE)+''.join(circle(x,145,9,'#dbe7f7',BLUE)+text(x,150,'−',BLUE,14,'middle') for x in [145,245,345,445])
    +arrow(150,65,490,65,TEAL)+arrow(490,225,150,225,BLUE)
    +text(320,40,'conventional current I →',TEAL,anchor='middle')+text(320,270,'electron drift ←',BLUE,anchor='middle'),
    'The sketch shows a metal wire. Current direction is defined by positive-charge motion, but its negative electron carriers drift the other way. Random thermal motion is omitted.',
    'Is charge used up as it passes through a resistor in steady state?', 'No. The same steady current enters and leaves. Energy is transferred to the resistor, while charge is conserved.')
register('18-2', 'Geometry affects resistance',
    rect(75,75,210,25)+rect(75,145,420,25)+rect(75,215,210,50)
    +text(330,92,'length ℓ, area A: R')+text(525,163,'2R')+text(330,245,'same ℓ, twice A: R/2')
    +text(320,35,'Same material and temperature: R = ρℓ/A',anchor='middle'),
    'The middle wire is twice as long with the same cross-sectional area, so its resistance doubles. The bottom wire represents twice the area, so its resistance halves. Thickness is schematic.',
    'A wire is twice as long and has twice the area. How does R change?', 'It stays the same if resistivity is unchanged: R_new = ρ(2ℓ)/(2A) = R.')
register('18-3', 'Alternating current still produces positive heating',
    axes('time t', 'current i')+line(75,145,560,145,LINE,1,True)
    +curve(lambda u:math.sin(4*math.pi*u),75,550,145,75,BLUE)
    +text(320,55,'Current reverses; power i²R never becomes negative.',anchor='middle')
    +text(320,290,'I_rms = I_peak/√2 for a sine wave',anchor='middle'),
    'The current oscillates above and below the dashed zero line. Squaring either sign produces positive resistor heating, so average current zero does not mean average power zero.',
    'A sine wave has peak current 2 A. What DC current gives equal average resistor heating?', 'I_rms = 2/√2 ≈ 1.41 A. Its square is the sine wave’s mean squared current.')
register('19-1', 'Series shares current; parallel shares voltage',
    path('M65 105H95M175 105H220M300 105H350',INK,2)+rect(95,90,80,30)+rect(220,90,80,30)
    +text(205,60,'SERIES: one route',anchor='middle')+arrow(85,155,315,155,BLUE)
    +path('M415 85V220M585 85V220M415 110H450M550 110H585M415 195H450M550 195H585',INK,2)
    +rect(450,95,100,30)+rect(450,180,100,30)+circle(415,110,4,INK)+circle(585,110,4,INK)
    +text(500,60,'PARALLEL',anchor='middle')+text(205,245,'I₁ = I₂',BLUE,anchor='middle')+text(500,260,'same two nodes → same V',anchor='middle'),
    'The left resistors have no branch between them. The right resistors both connect to the same two vertical node wires. Trace connectivity rather than judging how the drawing looks.',
    'Which has lower resistance: two equal R in series or in parallel?', 'Series gives 2R. Parallel gives R/2, so the parallel pair draws more current at the same applied voltage.')
register('19-2', 'A junction conserves charge',
    circle(310,145,9,TEAL)+arrow(75,145,295,145,BLUE)+arrow(320,140,500,60,GOLD)+arrow(320,150,500,230,TEAL)
    +text(175,115,'I_in = 5 A',BLUE,anchor='middle')+text(470,35,'I₁ = 2 A',GOLD,anchor='middle')+text(480,270,'I₂ = 3 A',TEAL,anchor='middle'),
    'In a steady circuit, charge does not accumulate at the junction. The incoming 5 coulombs per second divides into 2 and 3 coulombs per second in the two branches.',
    'If the incoming current rises to 7 A while I₁ stays 2 A, what must I₂ be?', '5 A for steady charge balance: I_in = I₁ + I₂.')
register('19-3', 'RC charging approaches a final value gradually',
    axes('time t', 'Q / Q_final')+curve(lambda u:1-math.exp(-4*u),color=BLUE)
    +line(75,65,550,65,LINE,1,True)+line(194,235,194,127,LINE,1,True)+circle(194,127.5,5,BLUE)
    +text(194,265,'τ = RC',anchor='middle')+text(225,145,'0.632 at one τ',BLUE)
    +text(425,85,'final charge Cε',anchor='middle'),
    'The vertical scale is charge divided by its final value. At one time constant τ = RC the capacitor reaches 1 − e⁻¹ ≈ 0.632 of final charge. The ideal curve never jumps instantly to full charge.',
    'After one time constant, is charging complete?', 'No. About 36.8% of the initial charge deficit remains. After each further time constant that deficit is multiplied by e⁻¹.')
register('20-1', 'Current produces circular magnetic field lines',
    circle(240,150,42,'none',BLUE)+circle(240,150,85,'none',BLUE)+circle(240,150,120,'none',BLUE)
    +circle(240,150,13)+circle(240,150,4,TEAL)+arrow(325,150,325,95,BLUE)
    +text(420,100,'⊙ current out of page')+text(420,150,'B counterclockwise')+text(420,200,'Right-hand rule'),
    'The central dot means conventional current comes toward you. Magnetic field circles the wire counterclockwise, as shown by the tangent arrow. Field strength decreases with distance.',
    'What changes if the current goes into the page instead?', 'The circular magnetic-field direction reverses to clockwise. Use a cross ⊗ for current into the page.')
register('20-2', 'Magnetic force bends a moving positive charge',
    ''.join(text(x,y,'×',BLUE,23,'middle') for x in [100,180,260,340,420,500] for y in [65,135,205])
    +circle(280,185,12)+text(280,191,'+',anchor='middle')+arrow(295,185,390,185,TEAL)+arrow(280,172,280,90,GOLD)
    +text(415,240,'B into page: ×',BLUE)+text(380,165,'v',TEAL)+text(300,95,'F',GOLD)
    +text(280,285,'q > 0: v right, B inward → F upward',anchor='middle'),
    'The cross marks indicate a uniform field into the page. For positive q, the right-hand rule gives an upward force perpendicular to rightward velocity. The magnetic force changes direction, not speed.',
    'For an electron moving right in this field, where does the force point?', 'Downward. A negative charge reverses the direction from v × B.')
register('20-3', 'A current loop in a field feels a turning couple',
    ''.join(arrow(70,y,570,y,BLUE,2) for y in [70,150,230])
    +path('M245 95L395 125L395 205L245 175Z',TEAL,3)+text(237,125,'⊙',GOLD,25,'end')+text(405,180,'⊗',GOLD,25)
    +text(470,45,'uniform B →',BLUE,anchor='middle')+text(320,280,'Opposite forces on opposite sides create torque.',anchor='middle'),
    'The loop is shown at an angle to a uniform horizontal field. Gold symbols denote opposite magnetic forces out of and into the page on its vertical sides. These forces make a torque; net force can be zero.',
    'When is loop torque zero?', 'When its magnetic moment, normal to the loop, is parallel or antiparallel to B, because τ = NIAB sin θ.')
register('21-1', 'Flux depends on the angle to the surface normal',
    path('M160 220L330 260L450 140L280 100Z',TEAL,2,PALE)+arrow(305,180,305,40,INK)
    +arrow(305,180,490,75,BLUE)+text(315,45,'normal n')+text(505,75,'B',BLUE)
    +text(330,130,'θ')+text(320,290,'Φ_B = BA cos θ; θ is measured from n, not the plane.',anchor='middle'),
    'The tilted quadrilateral represents a flat loop of area A; its normal is perpendicular to its plane. Only the field component along that normal contributes to signed flux.',
    'Is flux largest when B is parallel to the plane or to its normal?', 'To the normal: θ = 0 and |Φ_B| = BA. Parallel to the plane gives θ = 90° and zero flux.')
register('21-2', 'Lenz’s law opposes the change in flux',
    circle(190,150,80,'none',TEAL)+text(190,163,'⊙',BLUE,45,'middle')
    +arrow(270,150,270,210,GOLD)+text(190,40,'Outward B increasing',anchor='middle')+text(190,270,'Induced field: inward ⊗',anchor='middle')
    +text(390,100,'Required response:')+text(390,145,'oppose the increase')+text(390,190,'clockwise current')+text(390,235,'viewed from this side'),
    'The applied flux points out of the page and grows. The induced current must create an into-page field to oppose that increase, so the induced current is clockwise. The gold arrow at the right edge points downward.',
    'If the outward applied field were decreasing instead, which current direction would be induced?', 'Counterclockwise, creating an outward field to oppose the loss of outward flux.')
register('21-3', 'LC oscillations exchange electric and magnetic energy',
    flow(['Capacitor charged\nU_E = Q²/(2C)', 'Current largest\nU_B = ½LI²', 'Charge reverses\nU_E returns'], 'Ideal LC: total U_E + U_B stays constant; T = 2π√(LC).'),
    'At maximum capacitor charge, current is zero. As the capacitor discharges, its electric energy becomes the inductor’s magnetic energy. The continuing current then charges the capacitor with opposite polarity.',
    'At maximum current in an ideal LC circuit, what is the capacitor charge?', 'Zero at that instant. All the oscillation energy is magnetic, ½LI_max²; charge then continues through zero and reverses.')
register('22-1', 'A plane wave has three perpendicular directions',
    arrow(170,215,560,215,INK)+arrow(170,215,170,55,TEAL)+arrow(170,215,70,280,BLUE)
    +text(565,215,'travel',anchor='end')+text(185,65,'E',TEAL,22)+text(55,275,'B',BLUE,22)
    +text(390,85,'E ⟂ B')+text(390,130,'Both ⟂ travel')+text(390,175,'E/B = c'),
    'The arrows show the local directions of E, B, and propagation, not a particle’s path. For the pictured orientation E × B points along travel. Field values vary together as the wave passes.',
    'Does this electromagnetic wave require air or another material medium?', 'No. Electric and magnetic fields propagate through vacuum, with speed c = 1/√(μ₀ε₀).')
register('22-2', 'The electromagnetic spectrum is one wave family',
    arrow(55,105,585,105,TEAL)+text(320,65,'increasing frequency f and photon energy hf →',anchor='middle')
    +''.join(text(x,160,label,anchor='middle',size=15) for x,label in [(65,'radio'),(150,'micro'),(235,'IR'),(320,'visible'),(405,'UV'),(485,'X-ray'),(565,'gamma')])
    +arrow(585,220,55,220,BLUE)+text(320,265,'← increasing vacuum wavelength λ; c = fλ',anchor='middle'),
    'Moving right means higher frequency and shorter wavelength. All these waves share the same vacuum speed c; names identify parts of a continuous spectrum, with approximate boundaries.',
    'In vacuum, does an X-ray travel faster than a radio wave?', 'No. Both travel at c. The X-ray has higher frequency and a shorter wavelength.')
register('22-3', 'Absorption transfers radiation momentum',
    ''.join(arrow(65,y,375,y,BLUE,3) for y in [95,150,205])+rect(395,55,30,190,'#f1dfbd',GOLD,0)
    +arrow(440,150,570,150,TEAL)+text(215,60,'incident intensity I',BLUE,anchor='middle')
    +text(505,125,'force →',TEAL,anchor='middle')+text(320,280,'Absorber: pressure = I/c. Perfect reflector: 2I/c.',anchor='middle'),
    'Incoming light delivers forward momentum to a surface. An ideal absorber takes that momentum; a perfect reflector reverses the light’s momentum and receives twice as much transfer for normal incidence.',
    'If the field amplitude doubles, how does pressure on an absorber change?', 'It quadruples because intensity is proportional to field amplitude squared, and pressure equals I/c.')

# Optics and modern physics.
register('23-1', 'Measure refraction angles from the normal',
    rect(45,155,550,130,'#edf4fc',LINE,0)+line(45,155,595,155,INK)+line(320,35,320,285,LINE,1,True)
    +arrow(145,50,320,155,BLUE)+arrow(320,155,405,280,TEAL)+arrow(320,155,495,50,GOLD)
    +text(65,130,'n₁ smaller')+text(65,190,'n₂ larger')+text(277,110,'θ₁')+text(330,220,'θ₂')
    +text(320,25,'normal',anchor='middle')+text(485,250,'toward normal',TEAL,anchor='middle'),
    'The blue incident ray reaches a horizontal boundary. The teal refracted ray bends toward the dashed normal on entering the higher-index medium; the gold ray is reflected. Angles and index contrast are schematic.',
    'Which quantities change when the transmitted ray enters the higher-index medium?', 'Speed and wavelength decrease. Frequency stays the same at a stationary boundary.')
register('23-2', 'Two principal rays locate a real inverted image',
    line(35,155,605,155,LINE)+line(330,35,330,270,TEAL,4)
    +arrow(90,155,90,75,INK)+arrow(510,155,510,215,INK)
    +path('M90 75H330L510 215',BLUE,3)+path('M90 75L510 215',GOLD,3)
    +circle(433,155,4,TEAL)+text(433,183,'F',anchor='middle')
    +text(90,50,'object',anchor='middle')+text(330,25,'lens',anchor='middle')+text(510,250,'real image',anchor='middle'),
    'The blue ray enters parallel and leaves through the far focus F. The gold central ray continues straight. Their intersection below the axis locates the inverted image. The drawing is schematic and paraxial.',
    'Why can this real image be projected onto a screen?', 'The transmitted rays physically converge at the image point, so a screen there receives the focused light.')
register('23-3', 'Signed image distance distinguishes real and virtual images',
    line(50,150,590,150,LINE)+line(330,45,330,250,TEAL,3)
    +arrow(330,270,100,270,BLUE)+arrow(330,270,560,270,GOLD)
    +text(185,105,'Virtual image here',BLUE,anchor='middle')+text(185,135,'d_i < 0',BLUE,anchor='middle')
    +text(465,105,'Real image here',GOLD,anchor='middle')+text(465,135,'d_i > 0',GOLD,anchor='middle')
    +arrow(75,45,225,45,INK)+text(150,30,'incoming light →',anchor='middle')+text(330,235,'thin lens',anchor='middle'),
    'For a lens with light arriving from the left, a real image is on the outgoing right side and a virtual image is on the object’s left side. These are alternative outcomes, not simultaneous images.',
    'For a real object and a negative image distance, what is the sign of magnification?', 'Positive, since m = −d_i/d_o and d_o > 0. The virtual image is upright under this convention.')
register('24-1', 'Two paths set the phase difference',
    line(125,35,125,115,INK,5)+line(125,130,125,185,INK,5)+line(125,200,125,270,INK,5)
    +circle(125,122,4,TEAL)+circle(125,192,4,TEAL)+circle(555,85,5,RED)
    +line(125,122,555,85,BLUE)+line(125,192,555,85,GOLD)+line(570,40,570,265,INK,3)
    +text(75,160,'d',anchor='middle')+text(400,55,'screen point P',anchor='middle')
    +text(320,290,'Bright: Δpath = mλ. Dark: Δpath = (m + ½)λ.',anchor='middle'),
    'Blue and gold mark the distances from each slit to the same screen point P. Their difference sets relative phase. Equal-amplitude in-phase sources reinforce when the difference is a whole number of wavelengths.',
    'If the path difference is exactly 1.5λ, is the point bright or dark?', 'Dark in the ideal equal-amplitude model, because the waves arrive half a cycle out of phase.')
register('24-2', 'A narrower slit makes a wider central diffraction peak',
    axes('angle θ', 'relative intensity')+curve(lambda u: (math.sin(12*(u-.5))/(12*(u-.5)))**2 if abs(u-.5)>1e-8 else 1,color=BLUE)
    +curve(lambda u: (math.sin(24*(u-.5))/(24*(u-.5)))**2 if abs(u-.5)>1e-8 else 1,color=GOLD)
    +text(430,70,'narrow slit: blue',BLUE)+text(430,100,'wide slit: gold',GOLD)+text(320,285,'Both have the same central peak height here for comparison.',anchor='middle'),
    'The curves are normalized to the same peak, with a common angle scale. A smaller slit width a moves its first minima farther from zero because sin θ_min = λ/a.',
    'If slit width halves at fixed wavelength, what happens to the small-angle central width?', 'It approximately doubles. The central maximum spans from the first negative minimum to the first positive minimum.')
register('24-3', 'An analyzer passes one electric-field component',
    arrow(140,230,140,45,INK)+arrow(140,230,355,230,INK)+arrow(140,230,320,85,BLUE,4)
    +arrow(140,230,320,230,TEAL,5)+line(320,85,320,230,LINE,1,True)
    +text(315,65,'incident E₀',BLUE,anchor='middle')+text(360,225,'analyzer axis')+text(220,265,'passed E₀ cos θ',TEAL,anchor='middle')
    +text(205,195,'θ')+text(450,110,'I = I₀ cos²θ'),
    'The blue field is tilted by θ from the horizontal analyzer axis. The analyzer transmits the teal projection; squaring the amplitude ratio gives the intensity ratio.',
    'At θ = 60°, what fraction of already polarized input intensity passes?', 'One quarter: cos 60° = ½ and its square is ¼. I₀ is the intensity arriving at this analyzer.')
register('25-1', 'The eye focuses a real image on the retina',
    circle(395,150,105,'#f8fafc',LINE)+path('M325 82Q290 150 325 218Q355 150 325 82',TEAL,2,PALE)
    +path('M70 90L325 110L495 150M70 210L325 190L495 150',BLUE,2)
    +line(495,120,495,180,GOLD,6)+text(320,45,'eye lens',anchor='middle')+text(525,150,'retina',GOLD)
    +text(320,285,'Accommodation changes lens shape to focus on the retina.',anchor='middle'),
    'Rays from one object point converge on the retina. Changing lens curvature changes its focusing power. The diagram shows a schematic cross-section, not anatomically scaled tissues.',
    'For myopia, do distant rays focus before or behind the retina without correction?', 'Before it. A diverging corrective lens reduces the incoming convergence so the eye can focus the distant image on the retina.')
register('25-2', 'A telescope magnifies an angle',
    line(45,150,595,150,LINE)+line(180,45,180,255,TEAL,4)+line(470,75,470,225,TEAL,4)
    +path('M45 67.5L180 90L390 185L470 221.2L595 166.5M45 127.5L180 150L390 185L470 198.3L595 143.6',BLUE,2)
    +circle(390,185,5,RED)+text(180,30,'objective',anchor='middle')+text(470,50,'eyepiece',anchor='middle')
    +text(320,280,'Intermediate image → eyepiece → larger viewing angle',anchor='middle'),
    'A distant point sends nearly parallel rays to the objective. The objective forms an intermediate real image; the eyepiece turns rays from that image into a bundle suitable for relaxed viewing. The optical layout is schematic.',
    'What happens to ideal telescope angular magnification if the eyepiece focal length halves?', 'Its magnitude doubles: |M| = f_objective/f_eyepiece, assuming the instrument is refocused for the same viewing condition.')
register('25-3', 'Resolution is different from magnification',
    circle(155,145,35,'none',BLUE)+circle(220,145,35,'none',GOLD)+circle(155,145,60,'none',LINE)+circle(220,145,60,'none',LINE)
    +circle(445,145,50,'none',BLUE)+circle(465,145,50,'none',GOLD)
    +text(188,65,'two resolved points',anchor='middle')+text(455,65,'blur overlaps strongly',anchor='middle')
    +text(320,270,'Larger aperture D → smaller diffraction angle ≈ 1.22λ/D',anchor='middle'),
    'Each point source makes a diffraction spot rather than a perfect dot. The circles represent central spots and rings schematically. If their angular separation is too small, magnifying the same blur cannot recover detail.',
    'At fixed wavelength, how does doubling aperture diameter affect the diffraction limit?', 'It halves θ_min ≈ 1.22λ/D, so smaller angular separations can be resolved in the ideal instrument.')
register('26-1', 'Light takes a longer path in the frame where the clock moves',
    line(75,55,195,55,INK,4)+line(75,230,195,230,INK,4)+arrow(135,225,135,60,TEAL)
    +line(335,230,435,55,BLUE,3)+line(435,55,535,230,BLUE,3)+line(335,230,535,230,LINE,1,True)
    +text(135,270,'clock rest frame',anchor='middle')+text(435,270,'clock moving right →',anchor='middle')
    +text(320,30,'Both observers measure light speed c.',anchor='middle'),
    'The stationary clock’s pulse goes straight up and down. In the other frame its mirror moves sideways while light travels, giving diagonal legs. At the same light speed, the longer path takes more coordinate time.',
    'Which interval is proper time: the clock’s own tick interval or the other frame’s longer interval?', 'The clock’s own interval, Δτ. The two tick events occur at the same place in that clock’s rest frame.')
register('26-2', 'Moving length requires simultaneous endpoint measurements',
    rect(90,75,440,35)+rect(145,180,330,35,'#dbe7f7',BLUE)
    +text(310,55,'Rod rest frame: L₀',anchor='middle')+text(310,160,'Lab snapshot at one lab time: L = L₀/γ',BLUE,anchor='middle')
    +line(145,165,145,250,LINE,1,True)+line(475,165,475,250,LINE,1,True)+arrow(145,250,475,250,INK,2),
    'The upper bar is the rod at rest. The lower bar represents its length measured parallel to relative motion in another inertial frame. The endpoints must be recorded at one time in that measuring frame.',
    'If γ = 2 and L₀ = 4 m, what length does the moving-frame measurement give?', '2 m. This is a measurement using simultaneous endpoints, not a claim about photographic appearance.')
register('26-3', 'Relativistic kinetic energy grows sharply near c',
    axes('speed v/c', 'K / (mc²)')+curve(lambda u:(1/math.sqrt(1-(.96*u)**2)-1)/2.6,color=BLUE)
    +curve(lambda u:.5*(.96*u)**2/2.6,color=GOLD)+text(330,75,'relativistic',BLUE)+text(425,200,'classical ½mv²',GOLD)
    +text(320,290,'Close at low speed; increasingly different near c.',anchor='middle'),
    'Blue uses K = (γ − 1)mc²; gold uses the classical approximation. Both approach zero together at low speed, but blue rises without bound as speed approaches c. Curves share one scale.',
    'Can a massive object reach c with a finite added energy?', 'No. γ and the required kinetic energy diverge as v approaches c from below.')
register('27-1', 'One photon must supply the electron’s escape energy',
    arrow(65,85,265,155,BLUE)+rect(220,170,320,70,'#f5f4ef',LINE,0)+circle(300,170,8,TEAL)+arrow(310,155,480,65,TEAL)
    +text(130,65,'photon: hf',BLUE,anchor='middle')+text(455,50,'electron: K_max',TEAL,anchor='middle')
    +text(380,215,'metal: work function φ',anchor='middle')+text(320,285,'hf = φ + K_max; no emission if hf < φ.',anchor='middle'),
    'The incoming photon supplies energy hf. Removing the most energetic possible electron still costs the work function φ; its remaining kinetic energy is hf − φ in the single-photon model.',
    'Can more below-threshold photons eject electrons in the simple single-photon model?', 'No. Each individual photon lacks the needed energy. Above threshold, increasing intensity mainly increases the number emitted.')
register('27-2', 'Matter waves connect momentum and interference',
    flow(['electron beam\nmomentum p', 'two paths\nwave amplitudes', 'many detections\ninterference fringes'], 'de Broglie wavelength λ = h/p'),
    'An electron’s state propagates with wave behaviour, allowing path amplitudes to interfere. Each detection is localized, but repeated detections build an interference pattern.',
    'If a nonrelativistic electron’s momentum doubles, what happens to its matter wavelength?', 'It halves because λ = h/p. This is a relation for momentum, not the electron’s physical diameter.')
register('27-3', 'An atomic transition emits a photon of the energy difference',
    line(110,75,420,75,BLUE,3)+line(110,205,420,205,TEAL,3)+arrow(265,85,265,195,RED)
    +text(440,80,'E_high')+text(440,210,'E_low')+arrow(290,140,520,140,GOLD)
    +text(470,115,'photon hf',GOLD,anchor='middle')+text(320,270,'hf = E_high − E_low; only allowed energy gaps.',anchor='middle'),
    'The horizontal lines are two allowed atomic energies. A downward transition releases their difference as one photon; an upward transition must receive that same energy difference.',
    'What happens to photon frequency if the energy gap doubles?', 'It doubles because f = ΔE/h. Its vacuum wavelength halves.')
register('28-1', 'Probability density is not a planetary orbit',
    axes('x', 'probability density |ψ|²')+curve(lambda u:math.sin(math.pi*u)**2,color=BLUE)
    +text(75,260,'0',anchor='middle')+text(550,260,'L',anchor='middle')+text(320,115,'most likely region',anchor='middle')
    +text(320,290,'Example: ground state in an infinite one-dimensional well.',anchor='middle'),
    'The curve gives relative probability density for repeated measurements of identically prepared particles in a box. The probability in a small interval is approximately the curve height times interval width; the full area is one.',
    'Does the peak mean every particle is found exactly at the centre?', 'No. It means intervals of a given small width near the centre are more probable. The possible positions form a distribution.')
register('28-2', 'Stronger localization requires more wave numbers',
    axes('position x', 'wave packet',65,235,300,70)+curve(lambda u:math.exp(-35*(u-.5)**2),65,295,235,125,BLUE)
    +axes('momentum pₓ', 'momentum density',365,235,605,70)+curve(lambda u:math.exp(-7*(u-.5)**2),365,600,235,125,GOLD)
    +text(320,35,'Narrow position spread ↔ broad momentum spread',anchor='middle')
    +text(320,290,'σ_x σ_pₓ ≥ ħ/2; sketches use separate horizontal units.',anchor='middle'),
    'A localized wave packet requires a mixture of wave numbers, hence momenta pₓ = ħkₓ. The two panels show distributions for conjugate quantities, with separate scales.',
    'Is the uncertainty relation only caused by inaccurate measurement equipment?', 'No. It constrains the spreads intrinsic to a quantum state, even for ideal instruments.')
register('28-3', 'Pauli exclusion permits two opposite spins per orbital',
    rect(110,115,90,80)+rect(285,115,90,80)+rect(460,115,90,80)
    +arrow(135,180,135,130,BLUE)+arrow(175,130,175,180,GOLD)+arrow(310,180,310,130,BLUE)
    +text(155,85,'orbital 1',anchor='middle')+text(330,85,'orbital 2',anchor='middle')+text(505,85,'orbital 3',anchor='middle')
    +text(320,255,'A box is a spatial orbital; arrows label spin states.',anchor='middle'),
    'Each box represents one spatial orbital with fixed n, ℓ, and m_ℓ. Its two possible electron spin projections are shown by up and down arrows; they do not mean literal spinning paths.',
    'Can a third electron occupy the first spatial orbital?', 'No. Its two spin states are already occupied. A third electron must have a different set of orbital quantum numbers.')
register('29-1', 'A bond has a stable equilibrium separation',
    axes('separation r', 'potential energy U')+path('M110 55C135 210 210 260 285 195S450 105 550 100',BLUE,4)
    +line(75,100,560,100,LINE,1,True)+circle(222,218,5,RED)+text(222,270,'equilibrium r₀',anchor='middle')
    +text(415,75,'separated atoms: U → 0',anchor='middle')+text(420,220,'near minimum: spring-like'),
    'The lowest point represents stable separation r₀. Moving the nuclei closer or farther raises potential energy locally; the force restores them toward the minimum. The curve is a schematic molecular potential.',
    'Why can a bond be approximated as a spring near its minimum?', 'A smooth potential is approximately quadratic near a stable minimum: U ≈ U_min + ½k(r − r₀)². Its force is approximately linear and restoring.')
register('29-2', 'Energy bands are separated by forbidden gaps',
    rect(150,55,290,65,'#dbe7f7',BLUE,0)+rect(150,210,290,65,'#cce5dc',TEAL,0)
    +arrow(480,210,480,120,GOLD)+text(295,95,'conduction band',anchor='middle')+text(295,250,'valence band',anchor='middle')
    +text(295,170,'forbidden gap E_gap',anchor='middle')+text(500,170,'energy',GOLD),
    'The rectangles represent allowed bands; the white region between them has no allowed bulk electron energies in this ideal model. Moving an electron from the valence edge to the conduction edge requires the band-gap energy.',
    'Is the band gap an empty physical space inside the crystal?', 'No. It is an interval of forbidden electron energies. The vertical direction in this picture means energy, not position.')
register('29-3', 'An LED converts a recombination energy gap into light',
    rect(65,70,200,155,'#dbe7f7',BLUE)+rect(375,70,200,155,'#f1dfbd',GOLD)
    +text(165,105,'n-type: electrons',anchor='middle')+text(475,105,'p-type: holes',anchor='middle')
    +circle(245,155,8,BLUE)+circle(395,155,9,'white',GOLD)+arrow(255,155,385,155,TEAL)
    +arrow(325,145,325,35,RED)+text(340,45,'photon',RED)+text(320,275,'Direct-gap radiative recombination: hf ≈ E_gap',anchor='middle'),
    'In a forward-biased direct-gap LED, injected electrons and holes can recombine. Some of their energy is emitted as a photon. The drawing shows carrier roles rather than the detailed junction electric field.',
    'Would a larger direct band gap tend to emit longer or shorter wavelengths?', 'Shorter, because λ ≈ hc/E_gap. Actual device emission also depends on its material and transition details.')
register('30-1', 'Binding lowers the total rest energy',
    line(90,75,420,75,BLUE,3)+line(90,220,420,220,TEAL,3)+arrow(255,85,255,210,GOLD)
    +text(440,80,'free nucleons')+text(440,225,'bound nucleus')+text(280,155,'binding energy',GOLD)
    +text(320,280,'Δm = mass of free nucleons − nuclear mass > 0',anchor='middle'),
    'The vertical direction is total rest energy. The bound nucleus lies below the separated nucleons by the binding energy Δmc²; that energy must be supplied to separate the nucleus again.',
    'Does a bound nucleus weigh more or less than the same free protons and neutrons?', 'Less. The positive mass defect corresponds to the energy released on binding.')
register('30-2', 'Decay changes proton and nucleon counts in specific ways',
    flow(['α emission\nA → A − 4\nZ → Z − 2', 'β⁻ emission\nA unchanged\nZ → Z + 1', 'γ emission\nA unchanged\nZ unchanged'], 'A counts nucleons; Z counts protons. γ lowers excitation.'),
    'These three alternative decay types have different bookkeeping. Alpha removes two protons and two neutrons; beta-minus converts a neutron to a proton with electron and antineutrino emission; gamma changes excitation only.',
    'After beta-minus decay, is the daughter the same chemical element?', 'No. Its proton number Z increases by one, so its chemical identity changes even though A is unchanged.')
register('30-3', 'Half-life repeatedly halves the survivors',
    ''.join(rect(80+i*130,235-160*(.5**i),70,160*(.5**i),'#dbe7f7',BLUE,0)+text(115+i*130,265,label,anchor='middle')+text(115+i*130,220-160*(.5**i),f'{100*(.5**i):g}%',anchor='middle') for i,label in enumerate(['0','T½','2T½','3T½']))
    +text(320,35,'Expected parent population N/N₀',anchor='middle'),
    'Each column is one half-life later than the previous one. The expected parent fraction is 1, ½, ¼, and ⅛. The same fraction of survivors decays in each interval, not the same number.',
    'After two half-lives, what fraction has decayed?', 'Three quarters. One quarter remains, so the decayed fraction is 1 − ¼ = ¾.')
register('31-1', 'Fission and fusion can both increase binding per nucleon',
    axes('nucleon number A', 'binding energy / nucleon')+path('M90 220Q170 85 290 65Q410 55 550 100',BLUE,4)
    +arrow(130,175,230,95,TEAL)+arrow(520,120,405,90,GOLD)
    +text(165,240,'light nuclei',anchor='middle')+text(475,240,'heavy nuclei',anchor='middle')
    +text(175,130,'fusion →',TEAL)+text(420,155,'← fission',GOLD)+text(320,290,'Toward more tightly bound products → positive released Q.',anchor='middle'),
    'This schematic binding-energy curve peaks near intermediate nuclei. Suitable light nuclei can release energy by combining; suitable heavy nuclei can release energy by splitting. Reaction barriers still matter.',
    'Is released Q positive when total product rest mass is smaller?', 'Yes. Q = (mass_initial − mass_final)c². The decrease in rest energy becomes kinetic energy or radiation.')
register('31-2', 'Dose counts deposited energy per mass',
    rect(90,75,170,150)+rect(385,75,170,150)+text(175,120,'mass m',anchor='middle')+text(470,120,'mass 2m',anchor='middle')
    +arrow(175,30,175,80,RED)+arrow(470,30,470,80,RED)+text(175,175,'dose E/m',anchor='middle')+text(470,175,'dose E/(2m)',anchor='middle')
    +text(320,275,'Same deposited E → larger receiving mass, smaller dose.',anchor='middle'),
    'Each sample receives the same deposited energy E. Absorbed dose divides that energy by the receiving mass, so the larger sample has half the dose. The arrows represent energy transfer, not a medical exposure plan.',
    'Can becquerels alone determine the absorbed dose?', 'No. Activity counts decays per second; dose also depends on emitted energy, absorption, geometry, time, and the mass receiving the energy.')
register('31-3', 'PET detects a pair of annihilation photons',
    circle(320,145,35,'none',TEAL)+circle(305,145,7,BLUE)+circle(335,145,7,GOLD)
    +arrow(280,145,80,145,RED)+arrow(360,145,560,145,RED)+rect(50,95,25,100,'#dbe7f7',BLUE,0)+rect(565,95,25,100,'#dbe7f7',BLUE,0)
    +text(320,65,'e⁻ and e⁺ annihilate',anchor='middle')+text(320,230,'two photons detected in coincidence',anchor='middle')
    +text(320,275,'Near-rest pair: nearly opposite directions, ≈ 511 keV each.',anchor='middle'),
    'For an electron–positron pair annihilating approximately at rest into two photons, momentum conservation makes their directions nearly opposite. Coincident detections identify a line on which the event occurred.',
    'Why do the photons go in opposite directions in the pair’s rest frame?', 'The initial total momentum is zero, so two final photon momenta must cancel. Motion and binding broaden the ideal picture.')
register('32-1', 'Quark charges add to proton and neutron charges',
    circle(175,150,95,'none',LINE)+circle(465,150,95,'none',LINE)
    +''.join(circle(x,y,22)+text(x,y+6,label,anchor='middle') for x,y,label in [(145,115,'u'),(205,115,'u'),(175,180,'d'),(435,115,'u'),(495,115,'d'),(465,180,'d')])
    +text(175,35,'proton: uud',anchor='middle')+text(465,35,'neutron: udd',anchor='middle')
    +text(175,280,'⅔ + ⅔ − ⅓ = +1',anchor='middle')+text(465,280,'⅔ − ⅓ − ⅓ = 0',anchor='middle'),
    'Each u valence quark carries +⅔e and each d carries −⅓e. Adding the three valence charges gives a proton’s +e and a neutron’s zero. Circles show composition, not fixed quark positions.',
    'What is the charge of an antiproton?', '−e. Its valence antiquarks have the opposite charges from the proton’s quarks.')
register('32-2', 'Interactions have different charge and mediator roles',
    flow(['Electromagnetic\nelectric charge\nphoton', 'Strong\ncolour charge\ngluon', 'Weak\nflavour changes\nW and Z'], 'Mediator names summarize the quantum interaction model.'),
    'The three cards organize the Standard Model interactions discussed here. Exchange diagrams are calculation tools for quantum amplitudes, not pictures of classical balls following measurable messenger paths.',
    'Which interaction can change a neutron into a proton in beta decay?', 'The weak interaction. At the quark level a down quark changes to an up quark, with the appropriate emitted leptons.')
register('32-3', 'Centre-of-momentum energy is available for particle creation',
    arrow(60,145,255,145,BLUE)+arrow(580,145,385,145,GOLD)+circle(320,145,22,'#f1dfbd',GOLD)
    +arrow(320,145,430,65,TEAL)+arrow(320,145,430,235,TEAL)
    +text(160,105,'beam p →',BLUE,anchor='middle')+text(480,105,'← beam −p',GOLD,anchor='middle')
    +text(320,285,'Equal opposing momenta: total P = 0, so E_CM = E_total.',anchor='middle'),
    'The incoming beams have equal opposite momenta. Their total centre-of-momentum energy can create final rest masses and motion, provided charge and all other applicable conservation laws also balance.',
    'Is sufficient energy alone enough to make any chosen final particles?', 'No. The reaction must also obey momentum, charge, angular momentum, and the relevant particle conservation rules.')
register('33-1', 'A steady star balances inward gravity with a pressure gradient',
    circle(310,150,95,'#f1dfbd',GOLD)+circle(310,150,35,'#f4c994',GOLD)
    +arrow(310,20,310,65,BLUE)+arrow(310,280,310,235,BLUE)+arrow(180,150,225,150,BLUE)+arrow(440,150,395,150,BLUE)
    +arrow(310,105,310,70,RED)+arrow(310,195,310,230,RED)+text(495,105,'gravity inward',BLUE)
    +text(495,185,'pressure force',RED)+text(495,210,'outward',RED),
    'Blue arrows represent inward gravity. Pressure decreases outward, producing an outward net pressure force on each fluid shell. A star in approximate hydrostatic balance has these effects in equilibrium locally.',
    'Does balance mean gravity has switched off inside a stable star?', 'No. Gravity still acts and is balanced by the pressure gradient. Changes in pressure support can drive contraction or expansion.')
register('33-2', 'Parallax uses a known baseline and a small angular shift',
    circle(95,140,12,'#f1dfbd',GOLD)+circle(95,70,6,BLUE)+circle(95,210,6,BLUE)
    +circle(550,140,8,TEAL)+line(95,70,550,140,BLUE)+line(95,210,550,140,BLUE)+line(95,140,550,140,LINE,1,True)
    +text(65,145,'Sun',anchor='end')+text(95,35,'Earth positions 6 months apart')
    +text(330,120,'distance d')+text(505,136,'p')+text(320,280,'Baseline radius = 1 AU; d(pc) = 1/p(arcsec)',anchor='middle'),
    'Two Earth positions give different apparent directions to a nearby star. Annual parallax p is the half-angle relative to the Sun–star line, not the full six-month shift. Angles are greatly exaggerated.',
    'If parallax falls from 0.2 to 0.1 arcsecond, what happens to inferred distance?', 'It doubles, from 5 to 10 parsecs. Smaller parallax means a more distant star.')
register('33-3', 'Expansion stretches wavelengths with the scale factor',
    curve(lambda u:.15*math.sin(10*math.pi*u),45,260,120,130,BLUE)
    +arrow(280,120,355,120,INK)+curve(lambda u:.15*math.sin(5*math.pi*u),375,605,120,130,RED)
    +text(150,65,'emitted λ',BLUE,anchor='middle')+text(490,65,'observed λ longer',RED,anchor='middle')
    +text(320,220,'1 + z = λ_observed/λ_emitted',anchor='middle')+text(320,270,'Schematic cosmological stretching, not a local speed diagram.',anchor='middle'),
    'The right wave has a larger wavelength. In the cosmological expansion model, wavelengths stretch with the scale factor between emission and reception. Redshift z measures the fractional change.',
    'If observed wavelength is twice emitted wavelength, is z equal to 1 or 2?', 'z = 1, because z = (2λ − λ)/λ. The wavelength ratio is 1 + z = 2.')

# Additional pictures tailored to derivations whose geometry differs from the
# introductory concept picture.
register('box', 'Only whole half-waves fit inside an infinite well',
    line(95,45,95,265,INK,4)+line(555,45,555,265,INK,4)
    +line(95,105,555,105,LINE,1,True)+curve(lambda u:math.sin(math.pi*u),95,555,105,50,BLUE)
    +line(95,220,555,220,LINE,1,True)+curve(lambda u:math.sin(2*math.pi*u),95,555,220,40,TEAL)
    +text(325,35,'Wavefunction ψ = 0 at both walls',anchor='middle')+text(325,160,'n = 1 above; n = 2 below',anchor='middle')
    +text(325,292,'λ_n = 2L/n → p_n = nh/(2L) → E_n = n²h²/(8mL²)',anchor='middle',size=16),
    'The curves are allowed wavefunctions at one phase, not probability densities. Their signs may be positive or negative; |ψ|² gives probability density. Each has nodes at both walls.',
    'Why is n = 0 excluded?', 'It would make ψ zero everywhere, which cannot normalize to probability one. The ground state therefore has nonzero energy.')
register('bragg', 'Bragg reflection adds two extra path segments',
    line(65,110,590,110,LINE,3)+line(65,225,590,225,LINE,3)
    +path('M80 35L225 110L370 35',BLUE,3)+path('M95 100L335 225L575 100',GOLD,3)
    +arrow(610,110,610,225,INK,2)+text(600,180,'d',anchor='end')+text(270,90,'θ')
    +text(320,285,'Adjacent-plane path difference = 2d sin θ = mλ',anchor='middle'),
    'The two horizontal lines are adjacent crystal planes spaced by d. The lower reflected ray travels an extra segment before and after reflection. Their sum is 2d sin θ; θ is measured from a plane.',
    'What condition makes the two reflected contributions reinforce?', 'Their path difference must be a whole wavelength: 2d sin θ = mλ, for integer order m.')

register('rates', 'Slopes and accumulated areas connect motion quantities',
    flow(['position x\nmetres', 'velocity v\nmetres / second', 'acceleration a\nmetres / second²'], '→ take a time derivative; ← integrate and add an initial value.'),
    'Taking the slope of position against time gives velocity; taking velocity’s slope gives acceleration. Reversing a step requires an area integral and an initial value to set the starting condition.',
    'Can acceleration alone determine the position of a particle at a later time?', 'Not without its initial position and velocity. Integrating acceleration first determines changes in velocity, then changes in position.')
register('inductor', 'Building current stores magnetic energy in an inductor',
    path('M60 150H155'+''.join(f'C{x} 75 {x+40} 75 {x+40} 150' for x in range(155,435,40))+'H565',TEAL,3)
    +arrow(100,215,460,215,BLUE)+arrow(460,55,235,55,GOLD)
    +text(320,270,'If I is increasing →, induced emf opposes the increase ←',anchor='middle')
    +text(320,35,'ε_L = −L dI/dt; stored U = ½LI²',anchor='middle'),
    'The coil represents an ideal inductor. Increasing current builds a magnetic field and stores energy; the induced emf opposes that increase. For constant current, the ideal induced emf is zero, while stored energy can remain.',
    'Does doubling current double the stored magnetic energy?', 'No. It quadruples it for constant inductance, because U_L = ½LI².')
register('brightness', 'The same luminosity spreads over larger spherical areas',
    circle(215,150,25,'#f1dfbd',GOLD)+circle(215,150,70,'none',BLUE)+circle(215,150,125,'none',TEAL)
    +arrow(240,150,335,150,GOLD)+text(415,85,'Sphere area = 4πd²')+text(415,140,'At d: flux F')
    +text(415,195,'At 2d: flux F/4')+text(320,290,'Same total power L crosses each sphere: F = L/(4πd²).',anchor='middle'),
    'The circles represent cross-sections through spheres centred on an isotropic source. The same luminosity crosses every sphere, but twice the radius gives four times the area. Absorption is neglected.',
    'If the distance triples, what fraction of the original flux reaches each square metre?', 'One ninth, because received flux varies as 1/d² for the same isotropic luminosity.')

CONCEPT_VISUALS = {n: [f'{n}-{i}' for i in range(1, 4)] for n in range(1, 34)}
DERIVATION_VISUALS = {
    1: ['1-3'], 2: ['2-2', 'rates'], 3: ['3-2'], 4: ['4-3'],
    5: ['5-1', '5-3'], 6: ['6-1', '6-2'], 7: ['7-1'],
    8: ['8-2', '8-3'], 9: ['9-3'], 10: ['10-2', '10-3'],
    11: ['11-1', '11-3'], 12: ['12-1', '12-3'], 13: ['13-1', '13-2'],
    14: ['14-2', '14-3'], 15: ['15-2', '15-3'], 16: ['16-2', '16-3'],
    17: ['17-1', '17-3'], 18: ['18-2', '18-3'], 19: ['19-1', '19-3'],
    20: ['20-2', '20-1'], 21: ['21-1', 'inductor', '21-3'],
    22: ['22-1', '22-3'], 23: ['23-1', '23-2'],
    24: ['24-1', '24-2', '24-3'], 25: ['25-2', 'bragg'],
    26: ['26-1', '26-3'], 27: ['27-1', '27-3'],
    28: ['box', '28-2'], 29: ['29-1', '29-2'],
    30: ['30-3', '30-1'], 31: ['31-1', '31-2'], 32: ['32-1'],
    33: ['brightness', '33-3'],
}


def visual(key, ident):
    item = VISUALS[key]
    esc = html.escape
    return (f'<figure class="teaching-visual" id="{ident}" data-visual-key="{key}">'
            f'<div class="visual-heading"><strong>{esc(item["title"])}</strong>'
            f'<button type="button" class="visual-enlarge" aria-haspopup="dialog" aria-label="Enlarge diagram: {esc(item["title"])}">Enlarge</button></div>'
            f'<svg viewBox="0 0 640 310" role="img" aria-labelledby="{ident}-title {ident}-desc" xmlns="http://www.w3.org/2000/svg">'
            f'<title id="{ident}-title">{esc(item["title"])}</title>'
            f'<desc id="{ident}-desc">{esc(item["guide"])}</desc>'
            f'{item["svg"]}</svg><figcaption><p><strong>Read the picture.</strong> {esc(item["guide"])}</p>'
            f'<p class="visual-prompt"><strong>Predict.</strong> {esc(item["question"])}</p>'
            f'<details class="visual-answer"><summary>Check your prediction</summary><p>{esc(item["answer"])}</p></details>'
            '</figcaption></figure>')


def validate_visuals(chapters):
    for c in chapters:
        n = c['number']
        assert len(CONCEPT_VISUALS[n]) == len(c['concepts']), f'Concept pictures missing in chapter {n}'
        assert len(DERIVATION_VISUALS[n]) == len(c['derivations']['items']), f'Derivation pictures missing in chapter {n}'
        for key in CONCEPT_VISUALS[n] + DERIVATION_VISUALS[n]:
            assert key in VISUALS, f'Missing picture {key}'
