# Physics 12 Tutorial
@page_title: Physics 12 Tutorial | Giancoli Study Companion
@subtitle: A guided study of all 33 chapters in Physics12.pdf.

## 1 Introduction, Measurement & Estimating
> Translate a physical situation into quantities, units, and a defensible estimate.

### Models and evidence
A model keeps the features needed to answer a question. Treating a car as a particle works for travel time, but cannot describe its wheel rotation. Predictions must agree with observations within measurement uncertainty; a useful model also states its limits.

**Picture — A model keeps the features needed for a question:** The car becomes a dot for a travel-time problem. The arrow is its velocity v; this model has no wheel radius or wheel rotation.
**Predict:** Could this dot model predict how fast a wheel spins?
**Check:** No. Add a wheel model with radius and angular velocity to answer that question.

### Units and uncertainty
Use metres, kilograms, and seconds before substituting into equations. A measurement includes uncertainty: 2.50 ± 0.02 m means the last digits are limited by the measurement. Multiplication and division normally retain the fewest significant figures; addition and subtraction retain the least precise decimal place. Keep guard digits until the end.

**Picture — An uncertainty gives a range of plausible values:** The dot is the reported length. The blue interval runs from 2.50 − 0.02 to 2.50 + 0.02 m; it expresses the stated uncertainty, not extra calculator digits.
**Predict:** Is a result of 2.60 m inside this stated interval?
**Check:** No. The interval shown is 2.48 to 2.52 m; investigate the uncertainty assumptions or the measurements.

### Estimate before calculating
Build an order-of-magnitude estimate from plausible assumptions. Dimensional analysis can reject an equation with incompatible units, but matching dimensions alone cannot establish its numerical coefficient or physical validity.

**Picture — Cancel units before calculating:** The middle card contains conversion factors. Their numerator and denominator describe the same length or time, so the physical speed does not change.
**Predict:** Is 36 km/h closer to 1, 10, or 100 m/s?
**Check:** 10 m/s. Dividing 36 by 3.6 is also a useful scale check before using motion equations.

### Essential equations
- `1 km/h = 1/3.6 m/s` — Unit factors equal one; arrange them so unwanted units cancel.
- `[v] = L/T; [a] = L/T²; [F] = ML/T²` — Square brackets here denote dimensions, not a numerical value.

### Equation explanations & derivations
Original explanations mapped to the topic scope of the university review. A derivative is an instantaneous rate; an integral adds small contributions. Definitions and physical laws are stated as starting points.

#### Unit conversion and dimensions
**Concept:** A quantity stays the same when we multiply it by a conversion factor equal to one. Dimensions track the kind of quantity independently of its unit.
**Assumptions:** Use consistent base dimensions: length L, mass M, and time T. Unit conversions below are exact.
**Picture — Cancel units before calculating:** The middle card contains conversion factors. Their numerator and denominator describe the same length or time, so the physical speed does not change.
**Predict:** Is 36 km/h closer to 1, 10, or 100 m/s?
**Check:** 10 m/s. Dividing 36 by 3.6 is also a useful scale check before using motion equations.
1. Start with 1 km/h and multiply by (1000 m / 1 km)(1 h / 3600 s). The km and h cancel.
2. The remaining factor is 1000/3600 m/s = 1/3.6 m/s.
3. Velocity is displacement per time, so [v] = L/T. Acceleration is velocity change per time, so [a] = L/T².
4. From the physical law F = ma, [F] = M(L/T²). Likewise, density defined by ρ = m/V has dimension M/L³.
**Result:** `1 km/h = (1/3.6) m/s; [v] = LT⁻¹; [a] = LT⁻²; [F] = MLT⁻²`
**Check:** Both v₀t and at² have dimension L. Dimensional agreement cannot determine the factor ½ in the displacement equation; that needs the motion model.
**Scope reference:** [1. Measurement](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-1)

### Worked example
A runner covers 125 m in 16.2 s. Find the average speed with appropriate precision.

### Solution
1. Identify speed as distance divided by elapsed time.
2. 125 m ÷ 16.2 s = 7.716… m/s. Both measurements have three significant figures.
3. Round only the final result and retain the unit.
**Answer:** 7.72 m/s (about 28 km/h).

### Common trap
A calculator displays more digits than the measurements justify. Precision and accuracy are different: closely repeated measurements can share a systematic error.

### Self-check
Which expression has the dimensions of a distance?
- v/t
- at²
- a/t
**Answer:** at². Acceleration is L/T², so multiplying by time squared gives L. A coefficient such as ½ has no dimensions.

## 2 Kinematics in One Dimension
> Use signs, motion graphs, and constant-acceleration equations consistently.

### Position, velocity, and acceleration
Choose an origin and a positive direction. Displacement is final position minus initial position; distance counts the entire path. Average velocity uses displacement, whereas average speed uses distance. Instantaneous velocity is the slope of a position–time graph; acceleration is the slope of a velocity–time graph.

**Picture — Displacement records endpoints; distance records the path:** Blue shows the outward leg; gold shows the return. Position x increases rightward. The final position is 2 m to the right of the start, regardless of the detour.
**Predict:** Over 3 s, what are average velocity and average speed?
**Check:** Average velocity is +2/3 m/s. Average speed is 6/3 = 2 m/s. They use different numerators.

### A method for motion problems
Sketch the motion, list known quantities with signs, and choose an equation that avoids unnecessary unknowns. The equations below require constant acceleration during the interval. Split a trip into intervals if acceleration changes. A negative velocity means motion in the negative direction; a negative acceleration need not mean slowing down.

**Picture — Slope gives acceleration; area gives displacement:** The line rises from 2 to 6 m/s in 4 s, so acceleration is +1 m/s². Area is the 2 × 4 rectangle plus the ½ × 4 × 4 triangle: total displacement 16 m.
**Predict:** If the initial velocity were zero, which area would remain?
**Check:** Only the triangle, ½at². The rectangle v₀t would vanish.

### Free fall and graph area
Near Earth, neglecting drag, vertical acceleration is approximately 9.81 m/s² downward. At the top of a vertical throw the velocity is momentarily zero while acceleration remains downward. Signed area under a velocity–time graph is displacement; area under an acceleration–time graph is the change in velocity.

**Picture — Zero velocity at the top does not mean zero acceleration:** The three balls represent successive moments of one vertical throw. Blue velocity changes sign; each equal gold arrow is the same downward gravitational acceleration.
**Predict:** Immediately after the top, which way does the velocity point?
**Check:** Downward. The continuing downward acceleration changes velocity from zero to a negative value.

### Essential equations
- `v = v₀ + at` — v and v₀ are final and initial velocity; a is constant acceleration.
- `Δx = v₀t + ½at²; v² = v₀² + 2aΔx` — Use the same coordinate direction in every term.

### Equation explanations & derivations
Original explanations mapped to the topic scope of the university review. A derivative is an instantaneous rate; an integral adds small contributions. Definitions and physical laws are stated as starting points.

#### Constant acceleration from slopes and graph areas
**Concept:** Acceleration is the slope of a velocity–time graph; displacement is its signed area. A constant slope produces a straight line.
**Assumptions:** One-dimensional motion with constant acceleration a over elapsed time t; x₀ and v₀ are initial values.
**Picture — Slope gives acceleration; area gives displacement:** The line rises from 2 to 6 m/s in 4 s, so acceleration is +1 m/s². Area is the 2 × 4 rectangle plus the ½ × 4 × 4 triangle: total displacement 16 m.
**Predict:** If the initial velocity were zero, which area would remain?
**Check:** Only the triangle, ½at². The rectangle v₀t would vanish.
1. The definition a = (v − v₀)/t rearranges to v = v₀ + at.
2. The area under the straight velocity graph is a rectangle v₀t plus a signed triangle ½(v − v₀)t.
3. Substitute v − v₀ = at into that area to obtain Δx = v₀t + ½at².
4. Equivalently, Δx = ½(v + v₀)t. Multiply 2aΔx = a(v + v₀)t and use at = v − v₀ to get 2aΔx = v² − v₀².
**Result:** `v = v₀ + at; Δx = v₀t + ½at²; v² = v₀² + 2aΔx`
**Check:** At a = 0, displacement reduces to v₀t. These graph areas remain signed when velocity is negative; total distance instead uses the area under |v|.

#### The calculus connection for changing acceleration
**Concept:** A derivative is an instantaneous rate, and an integral adds small changes. The graph interpretation extends to curved graphs.
**Assumptions:** Motion is sufficiently smooth; a(t) may vary. Definite integrals run from the initial time 0 to the current time t.
**Picture — Slopes and accumulated areas connect motion quantities:** Taking the slope of position against time gives velocity; taking velocity’s slope gives acceleration. Reversing a step requires an area integral and an initial value to set the starting condition.
**Predict:** Can acceleration alone determine the position of a particle at a later time?
**Check:** Not without its initial position and velocity. Integrating acceleration first determines changes in velocity, then changes in position.
1. Define v = dx/dt and a = dv/dt. Thus dv = a(t) dt.
2. Adding velocity changes gives v(t) = v₀ + ∫₀ᵗ a(s) ds, where s is a dummy time variable.
3. Adding displacements gives x(t) = x₀ + ∫₀ᵗ v(s) ds. For constant a, integrating v₀ + as produces v₀t + ½at².
**Result:** `v(t) = v₀ + ∫₀ᵗ a(s) ds; x(t) = x₀ + ∫₀ᵗ v(s) ds`
**Check:** The units of each integral are the vertical-axis units times seconds: acceleration area gives m/s, and velocity area gives m.
**Scope reference:** [2. Motion Along a Straight Line](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-2)

### Worked example
A car moves at +12.0 m/s and brakes with a = −3.00 m/s². How long and how far until it stops?

### Solution
1. At the first stop, v = 0. Use v = v₀ + at.
2. t = (0 − 12.0)/(−3.00) = 4.00 s.
3. Δx = 12.0(4.00) + ½(−3.00)(4.00)² = 24.0 m.
**Answer:** 4.00 s and 24.0 m in the original direction.

### Common trap
Do not continue a braking model past the stop unless the stated force really would reverse the motion.

### Self-check
A ball is at the top of its flight. With upward positive and no air resistance, its acceleration is…
- 0
- +g
- −g
**Answer:** −g. Gravity continues acting at the top. Velocity is zero at that instant, not acceleration.

## 3 Kinematics in Two Dimensions; Vectors
> Resolve vectors and connect independent horizontal and vertical motion through time.

### Components and relative motion
A vector has magnitude and direction. Add x components and y components separately, then find the resultant magnitude and quadrant. If θ is measured from +x, Aₓ = A cos θ and Aᵧ = A sin θ. For relative velocity, name both frames: v⃗(A/C) = v⃗(A/B) + v⃗(B/C).

**Picture — A vector is the sum of perpendicular components:** The teal diagonal A equals the blue horizontal component followed by the gold vertical component. The right triangle defines the sine and cosine factors.
**Predict:** For an arrow pointing up and left, what signs do its components have?
**Check:** Aₓ is negative and Aᵧ is positive when right and up are the positive axes.

### Projectile motion
Without air resistance and with nearly constant g, aₓ = 0 and aᵧ = −g when upward is positive. Horizontal velocity stays constant; vertical velocity changes linearly. Solve the vertical equation for flight time, then use that same time in the horizontal equation.

**Picture — Horizontal and vertical motion share one clock:** Each dot is a later position of the same ideal projectile. Equal time intervals give equal horizontal displacement. Gravity changes vertical velocity, including at the top.
**Predict:** Does a larger downward acceleration change vₓ in this model?
**Check:** No. With no horizontal force, aₓ = 0. It changes the flight time and therefore the range.

### When the range shortcut works
The familiar range expression assumes launch and landing at the same height on a horizontal surface. A cliff launch requires the full vertical equation. Equal-height launches at complementary angles have the same ideal range, but different flight times and peak heights.

**Picture — The range shortcut needs equal launch and landing height:** The two endpoint dots lie on the same horizontal line. Setting the vertical displacement to zero gives a nonzero landing time, which determines horizontal range.
**Predict:** Can you use this flight-time shortcut for a launch from a cliff?
**Check:** No. Use the actual landing displacement in Δy = v₀ᵧt − ½gt² and choose the positive physical time.

### Essential equations
- `x − x₀ = v₀ cos(θ)t; y − y₀ = v₀ sin(θ)t − ½gt²` — Ideal projectile equations; x horizontal and y upward.
- `R = v₀² sin(2θ)/g; T = 2v₀ sin(θ)/g` — Equal launch and landing height only, for an upward launch.

### Equation explanations & derivations
Original explanations mapped to the topic scope of the university review. A derivative is an instantaneous rate; an integral adds small contributions. Definitions and physical laws are stated as starting points.

#### Components, relative velocity, and projectile range
**Concept:** Perpendicular vector components can be handled independently, but describe the same elapsed time.
**Assumptions:** Projectile: negligible drag, constant downward g, horizontal x and upward y. Range and flight time shortcuts require equal launch and landing height and 0 < θ < 90°.
**Picture — Horizontal and vertical motion share one clock:** Each dot is a later position of the same ideal projectile. Equal time intervals give equal horizontal displacement. Gravity changes vertical velocity, including at the top.
**Predict:** Does a larger downward acceleration change vₓ in this model?
**Check:** No. With no horizontal force, aₓ = 0. It changes the flight time and therefore the range.
1. Right-triangle projections give v₀ₓ = v₀ cos θ and v₀ᵧ = v₀ sin θ. Apply the one-dimensional motion equations with aₓ = 0 and aᵧ = −g.
2. This gives Δx = v₀ cos(θ)t and Δy = v₀ sin(θ)t − ½gt².
3. At the landing height, 0 = T[v₀ sin θ − ½gT]. Excluding the launch solution T = 0 gives T = 2v₀ sin θ/g.
4. Then R = v₀ cos θ · T = 2v₀² sin θ cos θ/g. Use 2 sin θ cos θ = sin(2θ).
5. For relative motion, positions obey r(A/C) = r(A/B) + r(B/C). Taking their time rates gives the corresponding vector velocity sum.
**Result:** `R = v₀² sin(2θ)/g; T = 2v₀ sin θ/g; v(A/C) = v(A/B) + v(B/C)`
**Check:** At 45°, sin(2θ) is largest. A cliff launch changes the vertical landing condition, so the equal-height range formula no longer applies.
**Scope reference:** [3. Vectors](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-3), [4. Motion in Two and Three Dimensions](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-4)

### Worked example
A ball is launched at 20.0 m/s at 30.0° above horizontal and lands at the same height. Find its flight time and range.

### Solution
1. v₀ₓ = 20.0 cos 30° = 17.32 m/s; v₀ᵧ = 10.0 m/s.
2. Set Δy = 0. The positive, nonzero solution is T = 2(10.0)/9.81 = 2.039 s.
3. R = 17.32(2.039) = 35.31 m.
**Answer:** T = 2.04 s; R = 35.3 m.

### Common trap
Use degrees for angles supplied in degrees. Take care with arctan: component signs determine the quadrant.

### Self-check
Ignoring air resistance, which quantity stays constant during projectile flight?
- Vertical velocity
- Horizontal velocity
- Speed
**Answer:** Horizontal velocity. There is no horizontal acceleration in this model; gravity changes the vertical component.

## 4 Dynamics: Newton’s Laws of Motion
> Draw a free-body diagram and connect net force to acceleration.

### Three laws, three distinct jobs
The first law identifies inertial frames: an object keeps a constant velocity when net force is zero. The second relates the vector sum of external forces on one object to its acceleration. The third pairs interactions between two different objects: their forces on each other are equal and opposite, even if their accelerations differ.

**Picture — Third-law forces act on different objects:** For an attractive interaction, B pulls A rightward and A pulls B leftward. These forces do not cancel in A’s own free-body diagram; only the force on A belongs there.
**Predict:** If A has twice B’s mass, are the interaction forces different?
**Check:** No. The forces have equal magnitude, but the larger mass has the smaller acceleration for this interaction.

### Build the force diagram first
Isolate one object. Add weight, contact forces, tension, and any applied forces that actually act on it. Choose convenient axes, often along and perpendicular to an incline. Write ΣFₓ = maₓ and ΣFᵧ = maᵧ. The normal force is perpendicular to a surface; its magnitude depends on the other forces and acceleration.

**Picture — A free-body diagram isolates one object:** The box slides right on a level floor. The normal force N and weight mg balance vertically; pull minus kinetic friction is the horizontal net force. Arrow lengths are schematic.
**Predict:** Which force changes if the pull tilts upward?
**Check:** The normal force decreases when there is no vertical acceleration: N = mg − F_pull sin θ. Friction then changes too.

### Friction and slopes
Static friction adjusts up to its maximum; kinetic friction is approximately μₖN once sliding occurs. On a slope, weight has downhill component mg sin θ and into-surface component mg cos θ. Friction opposes relative sliding or its tendency, which is not always opposite the object’s velocity in the ground frame.

**Picture — Resolve weight along and perpendicular to a slope:** The gold weight splits into a downhill red component and a blue component into the surface. The normal is perpendicular outward. Components are parts of weight, not additional forces.
**Predict:** On a frictionless slope, what is the downhill acceleration?
**Check:** g sin θ, because the downhill net force is mg sin θ and division by mass cancels m.

### Essential equations
- `ΣF⃗ = ma⃗; W = mg` — W here denotes the magnitude of weight, not work.
- `0 ≤ fₛ ≤ μₛN; fₖ = μₖN` — Use the static maximum only at impending slip.

### Equation explanations & derivations
Original explanations mapped to the topic scope of the university review. A derivative is an instantaneous rate; an integral adds small contributions. Definitions and physical laws are stated as starting points.

#### Newton’s law, weight, normal force, and friction
**Concept:** Newton’s second law is a starting physical law. Weight and contact forces enter its vector sum; friction coefficients summarize measured surface behaviour.
**Assumptions:** Inertial frame, constant mass, nonrelativistic speeds. The friction model approximates dry sliding contact.
**Picture — Resolve weight along and perpendicular to a slope:** The gold weight splits into a downhill red component and a blue component into the surface. The normal is perpendicular outward. Components are parts of weight, not additional forces.
**Predict:** On a frictionless slope, what is the downhill acceleration?
**Check:** g sin θ, because the downhill net force is mg sin θ and division by mass cancels m.
1. The momentum form ΣF = dp/dt becomes ΣF = ma when p = mv and mass is constant. This reformulates the law rather than proving it from algebra.
2. A freely falling object has acceleration g downward. Its gravitational force therefore has magnitude W = mg.
3. For an object on an incline with no other perpendicular force and no perpendicular acceleration, N − mg cos θ = 0, so N = mg cos θ.
4. Static friction supplies the force needed to prevent slip, up to μₛN. If a block rests on the incline, fₛ = mg sin θ and mg sin θ ≤ μₛmg cos θ.
5. At impending slip tan θ = μₛ. Once sliding downhill, the model fₖ = μₖN gives a = g(sin θ − μₖ cos θ).
**Result:** `ΣF = ma; W = mg; fₛ ≤ μₛN; fₖ = μₖN; tan θ_threshold = μₛ`
**Check:** On a horizontal surface with no vertical pull, N = mg. In an accelerating lift or with an angled pull, derive N again from the perpendicular force equation.
**Scope reference:** [5. Force and Motion—I](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-5), [6. Force and Motion—II](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-6)

### Worked example
A 5.00 kg crate is pulled horizontally with 20.0 N across a level floor. μₖ = 0.200. Find its acceleration.

### Solution
1. Vertical acceleration is zero, so N = mg = 49.05 N.
2. Sliding friction is fₖ = 0.200(49.05) = 9.81 N opposite the pull.
3. ΣFₓ = 20.0 − 9.81 = 10.19 N; a = 10.19/5.00.
**Answer:** a = 2.04 m/s² along the pull.

### Common trap
Action and reaction forces cannot cancel in the free-body diagram of one object: they act on different objects.

### Self-check
A book rests on a table. The third-law partner of Earth’s gravitational force on the book is…
- The table’s normal force on the book
- The book’s gravitational force on Earth
- The book’s force on the table
**Answer:** The book’s gravitational force on Earth. The same two bodies exchange a pair of gravitational forces. The normal force belongs to a different interaction.

## 5 Circular Motion & Gravitation
> Identify the inward net force and use gravity to explain orbital motion.

### Changing direction is acceleration
Uniform circular motion has constant speed but changing velocity. The acceleration points toward the circle’s centre. “Centripetal” describes the required inward net force; it is not an extra force to add to the diagram. Tension, friction, gravity, or normal force can supply it.

**Picture — Circular motion needs an inward acceleration:** At the rightmost point, tangent velocity points upward and radial acceleration points left. Their perpendicular directions let the object turn without changing speed.
**Predict:** If speed doubles at fixed radius, how does radial acceleration change?
**Check:** It quadruples because aᵣ = v²/r. The required inward resultant force also quadruples at fixed mass.

### Curves and vertical circles
For a flat road, static friction can provide the inward force. On a banked curve, a component of the normal force can help. In a vertical circle, write a radial force equation at the point of interest; weight may point inward or outward relative to the centre. Nonuniform circular motion also has tangential acceleration.

**Picture — In a vertical circle, inward changes direction:** At the top, both tension and weight point toward the centre. At the bottom, tension points inward but weight points outward. Write a fresh radial equation at each point.
**Predict:** For the same speed at top and bottom, where is the required tension larger?
**Check:** At the bottom: T_bottom = mv²/r + mg, while T_top = mv²/r − mg. A string can pull but cannot supply negative tension.

### Gravity, satellites, and Kepler
Any two masses attract. For spherical bodies outside their surfaces, measure r centre to centre. A circular satellite continually falls while its sideways motion carries it around Earth; apparent weightlessness means little supporting normal force, not zero gravity. For bodies orbiting the same central mass, T² is proportional to orbital size cubed.

**Picture — Radius connects gravity, orbital speed, and period:** Both circular paths orbit the same central mass M. A larger orbital radius weakens gravity, lowers circular speed, and increases the time to complete an orbit.
**Predict:** If orbital radius doubles, by what factor does the period change?
**Check:** T becomes 2^(3/2) ≈ 2.83 times as large, because T² is proportional to r³.

### Essential equations
- `aᵣ = v²/r; v = 2πr/T; ΣFᵣ = mv²/r` — Choose the inward radial direction positive.
- `F = GmM/r²; g = GM/r²; v_orbit = √(GM/r)` — Circular orbit around a much more massive body; G = 6.674 × 10⁻¹¹ N·m²/kg².

### Equation explanations & derivations
Original explanations mapped to the topic scope of the university review. A derivative is an instantaneous rate; an integral adds small contributions. Definitions and physical laws are stated as starting points.

#### Why circular acceleration is v²/r
**Concept:** In uniform circular motion, the speed is constant while the velocity direction rotates through the same angle as the radius.
**Assumptions:** Constant speed on a circle of radius r. Use the limiting geometry of a very short time interval Δt.
**Picture — Circular motion needs an inward acceleration:** At the rightmost point, tangent velocity points upward and radial acceleration points left. Their perpendicular directions let the object turn without changing speed.
**Predict:** If speed doubles at fixed radius, how does radial acceleration change?
**Check:** It quadruples because aᵣ = v²/r. The required inward resultant force also quadruples at fixed mass.
1. Two nearby velocity vectors both have length v. Their difference has magnitude |Δv| = 2v sin(Δθ/2).
2. For a small angle in radians, 2 sin(Δθ/2) approaches Δθ. The arc travelled is Δs = rΔθ = vΔt.
3. Thus |Δv|/Δt approaches vΔθ/Δt = v(v/r) = v²/r. The limiting change points toward the centre.
4. One full lap covers 2πr in period T, so v = 2πr/T. Newton’s law then requires an inward net force mv²/r.
**Result:** `aᵣ = v²/r = ω²r; ΣFᵣ = mv²/r; v = 2πr/T`
**Check:** Doubling speed quadruples the required radial force. The force diagram must identify which actual interactions supply that resultant.

#### Circular orbits, Kepler’s scaling, and gravitational energy
**Concept:** Gravity supplies the inward force for a circular orbit. Its inverse-square form also determines how potential energy changes with separation.
**Assumptions:** Newtonian gravity, spherical central body of mass M, satellite mass m ≪ M, radius r measured from the centre; U = 0 at infinity.
**Picture — Radius connects gravity, orbital speed, and period:** Both circular paths orbit the same central mass M. A larger orbital radius weakens gravity, lowers circular speed, and increases the time to complete an orbit.
**Predict:** If orbital radius doubles, by what factor does the period change?
**Check:** T becomes 2^(3/2) ≈ 2.83 times as large, because T² is proportional to r³.
1. Start with the gravitational law F = GMm/r². Setting F = mg gives g(r) = GM/r².
2. For a circular orbit, GMm/r² = mv²/r. Cancel m and one factor of r to obtain v² = GM/r.
3. Use T = 2πr/v and square to find T² = 4π²r³/(GM). For elliptical orbits the same period relation uses semimajor axis instead of circular radius.
4. The outward radial force component is Fᵣ = −GMm/r². Since dU = −Fᵣ dr, integrating from infinity to r gives U(r) = −GMm/r.
5. Near a surface of radius R, ΔU = GMm(1/R − 1/(R+h)) ≈ (GM/R²)mh = mgh when h ≪ R.
**Result:** `v_orbit = √(GM/r); T² = 4π²r³/(GM); U = −GMm/r`
**Check:** A more distant circular orbit has lower speed and a longer period. The familiar mgh is a local approximation to the inverse-square potential.
**Scope reference:** [4. Motion in Two and Three Dimensions](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-4), [6. Force and Motion—II](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-6), [13. Gravitation](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-13)

### Worked example
A 1000 kg car rounds a flat curve of radius 50.0 m at 10.0 m/s. Find the required friction and minimum static coefficient.

### Solution
1. The inward acceleration is 10.0²/50.0 = 2.00 m/s².
2. Required static friction is maᵣ = 2000 N.
3. N = mg = 9810 N. At the threshold μₛN = 2000 N.
**Answer:** fₛ = 2.00 × 10³ N inward; μₛ,min = 0.204.

### Common trap
For satellites, altitude is measured above the surface; orbital radius is Earth’s radius plus altitude.

### Self-check
If orbital radius doubles for circular orbits around the same mass, orbital speed becomes…
- Twice as large
- 1/√2 of its original value
- Half as large
**Answer:** 1/√2 of its original value. v = √(GM/r), so speed varies as r⁻¹ᐟ².

## 6 Work & Energy
> Choose an energy system and account for transfers without losing track of signs.

### Work transfers energy
A constant force does work equal to its component along displacement times the displacement. A perpendicular force does no work. The signed area under a force-versus-position graph gives work for a variable force. Net work changes kinetic energy, so work can be negative even while an object moves forward.

**Picture — Only the force component along displacement does work:** The applied force is diagonal, but the box’s displacement is horizontal. The blue projection is the component that transfers energy through work.
**Predict:** What is the work if the force is perpendicular to displacement?
**Check:** Zero, because cos 90° = 0. A perpendicular force can still change the direction of motion.

### Potential and conservation
Near Earth, gravitational potential energy changes by mgΔy. A spring stores ½kx² within its elastic range. Choose a zero of potential energy; only differences matter. With only conservative forces doing work, kinetic plus potential energy is constant. Friction transfers mechanical energy into thermal energy rather than destroying total energy.

**Picture — Energy moves between stores without disappearing:** Each panel represents the same total energy, divided into stores. In the first two panels mechanical energy is conserved. The last includes thermal energy produced by friction; bar heights are schematic.
**Predict:** Does friction destroy energy?
**Check:** No. It transfers mechanical energy into thermal and other internal stores. Include those stores when counting total energy.

### Energy or forces?
Energy is useful when the question links speeds and positions without asking for elapsed time. Draw initial and final states and include external work or dissipative work explicitly. Power is the rate of transferring energy, so the same work done faster requires greater average power.

**Picture — Power compares the rate of the same energy transfer:** For equal start and end speeds, each lift increases gravitational energy by mgh. Power measures how quickly this transfer occurs, not just its size.
**Predict:** If a lift takes half the time for the same load and height, what happens to average power?
**Check:** It doubles: P_avg = W/Δt, while the work mgh stays the same.

### Essential equations
- `W = Fd cos θ; W_net = ΔK; K = ½mv²` — θ is the angle between force and displacement.
- `Kᵢ + Uᵢ + W_nc = K_f + U_f; U_g = mgy; U_s = ½kx²` — W_nc is work by nonconservative forces in this mechanical-energy accounting.
- `P_avg = W/Δt; P = Fv cos θ` — The second expression is instantaneous power for a force on a moving object.

### Equation explanations & derivations
Original explanations mapped to the topic scope of the university review. A derivative is an instantaneous rate; an integral adds small contributions. Definitions and physical laws are stated as starting points.

#### Work–energy theorem and kinetic energy
**Concept:** Work accumulates the component of force along displacement. Applying Newton’s law to this accumulated work produces the speed-squared energy expression.
**Assumptions:** A particle of constant mass at nonrelativistic speed; W_net uses all forces acting on it.
**Picture — Only the force component along displacement does work:** The applied force is diagonal, but the box’s displacement is horizontal. The blue projection is the component that transfers energy through work.
**Predict:** What is the work if the force is perpendicular to displacement?
**Check:** Zero, because cos 90° = 0. A perpendicular force can still change the direction of motion.
1. For a constant force, project along displacement: W = (F cos θ)d. For a variable force, add small contributions: W = ∫F · dr.
2. In one dimension, a = dv/dt = v dv/dx. Therefore F dx = ma dx = mv dv.
3. Integrate between the initial and final speeds: W_net = ∫ mv dv = ½mv_f² − ½mv_i². The vector derivation gives the same result.
4. Define K = ½mv², so W_net = ΔK. Dividing a small work increment by dt gives P = F · v = Fv cos θ; over a finite interval P_avg = W/Δt.
**Result:** `K = ½mv²; W_net = ΔK; P = Fv cos θ`
**Check:** A force perpendicular to velocity changes direction without instantaneous work. Work and kinetic energy both have units N·m = J.

#### Potential energy and mechanical energy accounting
**Concept:** For a conservative force, define potential energy so that its decrease equals the work done by that force.
**Assumptions:** Uniform near-Earth gravity and an ideal Hooke-law spring within its elastic range; choose convenient zero levels.
**Picture — Energy moves between stores without disappearing:** Each panel represents the same total energy, divided into stores. In the first two panels mechanical energy is conserved. The last includes thermal energy produced by friction; bar heights are schematic.
**Predict:** Does friction destroy energy?
**Check:** No. It transfers mechanical energy into thermal and other internal stores. Include those stores when counting total energy.
1. Use ΔU = −W_conservative. With upward y, gravity has Fᵧ = −mg, so ΔU_g = −∫(−mg) dy = mgΔy.
2. A spring exerts F = −kx. Thus U_s(x) − U_s(0) = −∫₀ˣ(−ks) ds = ½kx².
3. Split net work into conservative and nonconservative parts: ΔK = −ΔU + W_nc.
4. Rearrange to Kᵢ + Uᵢ + W_nc = K_f + U_f. If W_nc = 0, total mechanical energy stays constant.
**Result:** `U_g = mgy; U_s = ½kx²; Δ(K + U) = W_nc`
**Check:** For sliding friction, W_nc is typically negative and mechanical energy decreases while thermal energy increases. Changing the zero of U cannot change a predicted speed.
**Scope reference:** [7. Kinetic Energy and Work](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-7), [8. Potential Energy and Conservation of Energy](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-8)

### Worked example
A 2.00 kg object slides from rest down a frictionless track through a vertical drop of 5.00 m. Find its final speed.

### Solution
1. Choose the bottom as U_g = 0; initial kinetic energy is zero.
2. mgh = ½mv². The mass cancels.
3. v = √(2 × 9.81 × 5.00) = 9.904… m/s.
**Answer:** 9.90 m/s; the result depends on vertical drop, not track length.

### Common trap
Do not set mechanical energy constant when friction or a motor does unaccounted work.

### Self-check
An object’s speed doubles. Its kinetic energy becomes…
- Twice as large
- Four times as large
- Unchanged
**Answer:** Four times as large. K depends on v², so doubling v multiplies K by four.

## 7 Linear Momentum
> Use impulse for a force over time and momentum conservation for an isolated system.

### Momentum and impulse
Momentum is a vector. The area under a force–time graph is impulse, equal to change in momentum. A longer stopping time can reduce average force for the same momentum change. For constant mass, Newton’s second law follows from F_net = Δp/Δt over an interval with constant or average net force.

**Picture — Impulse is area under a force–time graph:** The rectangles have equal area. The blue stop has twice the average force over half the time; the gold stop produces the same momentum change more gradually.
**Predict:** For the same change in momentum, what happens if stopping time triples?
**Check:** Average net force becomes one third as large: F_avg = Δp/Δt.

### Choose the collision system
For two colliding objects, internal forces exchange momentum between them. Total momentum is conserved when external impulse is negligible during the collision. Momentum may be conserved even when kinetic energy is not: an inelastic collision converts some kinetic energy into other forms.

**Picture — Choose both colliding objects as one system:** Two carts stick. When external impulse is negligible, total momentum before equals total momentum after. Their internal contact forces exchange momentum within the chosen two-cart system.
**Predict:** Do the carts retain all their original kinetic energy when they stick?
**Check:** Generally no. Some becomes deformation, sound, and internal energy, even while total momentum is conserved.

### Elastic, inelastic, and centre of mass
Elastic collisions conserve both momentum and total kinetic energy. Objects that stick together undergo a perfectly inelastic collision and share a final velocity. In two dimensions conserve x and y momentum separately. The centre of mass moves as though total external force acted on the total mass.

**Picture — The centre of mass lies closer to the larger mass:** The red dot is the mass-weighted average position. Three times as much mass on the right shifts the centre of mass toward that side.
**Predict:** Where would the centre of mass be if the two masses were equal?
**Check:** At the midpoint, x = 2 m. The formula averages positions with mass as the weight.

### Essential equations
- `p⃗ = mv⃗; J⃗ = F⃗_avg Δt = Δp⃗` — Use the net external force for impulse–momentum of a system.
- `Σp⃗ᵢ = Σp⃗_f; x_CM = Σ(mᵢxᵢ)/Σmᵢ` — Momentum conservation requires negligible net external impulse.

### Equation explanations & derivations
Original explanations mapped to the topic scope of the university review. A derivative is an instantaneous rate; an integral adds small contributions. Definitions and physical laws are stated as starting points.

#### Impulse, momentum conservation, and centre of mass
**Concept:** Internal forces transfer momentum within a system; only external impulse changes its total momentum.
**Assumptions:** Constant particle masses in an inertial frame. Internal Newton-third-law force pairs cancel in the system sum.
**Picture — Impulse is area under a force–time graph:** The rectangles have equal area. The blue stop has twice the average force over half the time; the gold stop produces the same momentum change more gradually.
**Predict:** For the same change in momentum, what happens if stopping time triples?
**Check:** Average net force becomes one third as large: F_avg = Δp/Δt.
1. Define each momentum by pᵢ = mᵢvᵢ. Newton’s law gives F_net = dp/dt, so integrating gives J = ∫F_net dt = Δp = F_avg Δt.
2. Sum over particles. Each internal force has an equal and opposite partner, leaving dP/dt = ΣF_external.
3. If the external impulse during a collision is negligible, P_f − P_i = 0 even when the collision is inelastic.
4. Define x_CM = Σmᵢxᵢ/M, with M = Σmᵢ. Differentiate to obtain Mv_CM = Σmᵢvᵢ = P, and differentiate again to obtain Ma_CM = ΣF_external.
**Result:** `J = Δp; P_f = P_i if J_external = 0; x_CM = Σmᵢxᵢ/M`
**Check:** Two sticking carts share v_f = (m₁v₁ + m₂v₂)/(m₁+m₂). Their kinetic energy usually changes; the conserved quantity is the system momentum.
**Scope reference:** [9. Center of Mass and Linear Momentum](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-9)

### Worked example
A 0.200 kg cart moving at +3.00 m/s sticks to a stationary 0.300 kg cart. Find their shared speed and kinetic energy loss.

### Solution
1. Initial momentum = 0.200(3.00) = 0.600 kg·m/s.
2. Final speed = 0.600/(0.200 + 0.300) = +1.20 m/s.
3. Kᵢ = ½(0.200)(3.00)² = 0.900 J; K_f = ½(0.500)(1.20)² = 0.360 J.
**Answer:** v_f = +1.20 m/s; 0.540 J of kinetic energy is converted to other forms.

### Common trap
Conservation of momentum does not imply conservation of kinetic energy.

### Self-check
In a perfectly inelastic collision with negligible external impulse, which is conserved?
- Total momentum
- Total kinetic energy
- Each object’s momentum
**Answer:** Total momentum. The system’s momentum is conserved, while the objects exchange momentum and some kinetic energy becomes internal energy.

## 8 Rotational Motion
> Translate between linear and angular quantities and connect torque to rotation.

### Angular kinematics
Angle in radians measures arc length divided by radius. Angular velocity and angular acceleration describe how angle and spin change. At distance r from a fixed axis, tangential speed is rω. The usual constant-acceleration motion equations have angular analogues when α is constant.

**Picture — Radians connect angular and linear motion:** The teal arc has length s and subtends angle θ in radians at the centre. At larger radius, the same angular change corresponds to more travel.
**Predict:** Two points share the same ω; one is twice as far from the axis. How do their speeds compare?
**Check:** The outer point has twice the tangential speed because v_t = rω.

### Torque and rotational inertia
Torque measures a force’s turning effect about a chosen axis. The lever arm is the perpendicular distance from the axis to the force’s line of action. Rotational inertia depends on both mass and its distribution about that axis; placing mass farther away makes angular acceleration harder to produce.

**Picture — Torque uses the perpendicular lever arm:** The force acts upward along the dashed line. Its shortest distance from the pivot is the horizontal lever arm r⊥, so it creates a turning effect.
**Predict:** What happens to torque if the same perpendicular force acts twice as far from the pivot?
**Check:** Torque doubles. For a given rotational inertia I, angular acceleration doubles too.

### Rolling and angular momentum
Rolling without slipping obeys v_CM = Rω and combines translation with rotation. Static friction can enforce rolling without dissipating energy at a stationary contact point. Angular momentum about a fixed axis is conserved if net external torque about that axis is zero. A skater speeds up by reducing rotational inertia.

**Picture — Rolling combines translation and rotation:** The wheel rolls right without slipping on stationary ground. Blue represents translation; gold adds the top point’s rotational velocity. Translation and clockwise rotation cancel at the contact point and add at the top.
**Predict:** Is the ground-frame velocity of the contact point equal to the centre velocity?
**Check:** No. It is momentarily zero for pure rolling. The centre moves at v_CM, and the top moves at 2v_CM.

### Essential equations
- `ω_avg = Δθ/Δt; v_t = rω; a_t = rα; v_CM = Rω` — Use radians; ω_avg is average angular velocity. The rolling relation requires no slipping.
- `τ = rF sin θ; Στ = Iα; K_rot = ½Iω²; L = Iω` — Use the specified fixed/principal axis; Στ = Iα assumes constant I about that axis.

### Equation explanations & derivations
Original explanations mapped to the topic scope of the university review. A derivative is an instantaneous rate; an integral adds small contributions. Definitions and physical laws are stated as starting points.

#### Angular motion, torque, and rotational inertia
**Concept:** A rigid body shares one angular motion, but mass farther from the axis travels faster and contributes more to rotational inertia.
**Assumptions:** Rigid body rotating about a fixed axis with constant I. Angles use radians. The scalar angular momentum formula refers to that axis component or to a principal axis.
**Picture — Torque uses the perpendicular lever arm:** The force acts upward along the dashed line. Its shortest distance from the pivot is the horizontal lever arm r⊥, so it creates a turning effect.
**Predict:** What happens to torque if the same perpendicular force acts twice as far from the pivot?
**Check:** Torque doubles. For a given rotational inertia I, angular acceleration doubles too.
1. Arc length is s = rθ. Taking time rates gives v_t = rω and a_t = rα. For rolling without slip on stationary ground, the contact point has zero velocity, giving v_CM = Rω.
2. For each mass element, tangential force is F_t = m rα. Its axial torque is rF_t = mr²α; summing gives Στ = (Σmr²)α = Iα.
3. Sum particle kinetic energies: K_rot = Σ½m(rω)² = ½Iω².
4. Sum angular momentum components: L_axis = Σr(mv_t) = Σmr²ω = Iω. With zero external axial torque, this component is conserved.
5. For constant α, the straight-line equations carry over: ω = ω₀ + αt and Δθ = ω₀t + ½αt².
**Result:** `I = Σmᵢrᵢ²; Στ = Iα; K_rot = ½Iω²; L_axis = Iω`
**Check:** Moving the same mass twice as far from the axis multiplies its contribution to I by four. For a general force, the lever arm gives τ = rF sin θ.

#### Rolling downhill: translation plus rotation
**Concept:** A rolling object divides its gravitational energy between motion of its centre and rotation about its centre.
**Assumptions:** Rigid body rolling without slipping from rest through height h; fixed incline, no dissipative losses, I = κmR² about its centre.
**Picture — Rolling combines translation and rotation:** The wheel rolls right without slipping on stationary ground. Blue represents translation; gold adds the top point’s rotational velocity. Translation and clockwise rotation cancel at the contact point and add at the top.
**Predict:** Is the ground-frame velocity of the contact point equal to the centre velocity?
**Check:** No. It is momentarily zero for pure rolling. The centre moves at v_CM, and the top moves at 2v_CM.
1. Conservation gives mgh = ½mv_CM² + ½Iω².
2. Insert ω = v_CM/R and I = κmR², so mgh = ½m(1 + κ)v_CM².
3. Cancel mass and solve. For a uniform solid disk κ = ½; for a thin hoop κ = 1.
**Result:** `v_CM = √[2gh/(1 + κ)]`
**Check:** A disk reaches the bottom faster than a hoop from the same height because it needs less rotational energy at a given centre speed. Static friction must be sufficient to enforce the no-slip condition.
**Scope reference:** [10. Rotation](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-10), [11. Rolling, Torque, and Angular Momentum](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-11)

### Worked example
A uniform solid disk of mass 2.00 kg and radius 0.200 m has a tangential 3.00 N force applied at its rim. Find α about its frictionless central axle.

### Solution
1. I = ½MR² = 0.0400 kg·m² for a uniform disk.
2. The force is perpendicular to the radius, so τ = RF = 0.600 N·m.
3. α = τ/I = 0.600/0.0400.
**Answer:** α = 15.0 rad/s².

### Common trap
Torque has units N·m but is not measured in joules. Specify the axis before quoting I or torque.

### Self-check
For conserved angular momentum, halving I causes ω to…
- Halve
- Double
- Stay constant
**Answer:** Double. L = Iω stays fixed, so ω must double. The increase in rotational energy comes from work done while changing shape.

## 9 Static Equilibrium; Elasticity & Fracture
> Balance forces and torques, then distinguish deformation from permanent damage.

### Two equilibrium conditions
Static equilibrium needs both zero net force and zero net torque. Force balance alone could leave an object rotating. Choose a pivot that eliminates unknown forces from the torque equation, then use force balance to find them. A centre-of-mass model often lets a distributed weight act at one point.

**Picture — A balanced beam must balance force and torque:** The upward support balances the total load. Equal forces at equal distances from the pivot also make clockwise and counterclockwise torques cancel. The beam’s own weight is neglected here.
**Predict:** Can two equal opposite forces turn an object?
**Check:** Yes. If they act along different lines, they form a couple: zero net force but nonzero net torque.

### Stability and support
An object tends to return after a small displacement in stable equilibrium. For a body resting on a base, tipping begins when the line of action of its weight passes outside the support region. A low centre of mass and wide base generally improve stability.

**Picture — A support base must contain the weight’s line of action:** On the left, the vertical weight line passes within the base. On the right, the tilted object is supported only at its edge and the weight line lies outside that support, creating a tipping torque.
**Predict:** Why does widening the base usually improve stability?
**Check:** It allows a larger tilt before the weight line passes outside the support region.

### Stress, strain, and limits
Stress is force divided by cross-sectional area; strain is relative deformation. In the linear elastic regime, their ratio is an elastic modulus. Young’s modulus describes stretching, while shear and bulk moduli describe shape and volume changes. Beyond the elastic limit deformation can remain; fracture occurs when the material fails.

**Picture — Stress stretches a material; strain measures the fraction:** The lower bar is the same specimen under tension; the extension is exaggerated. Cross-sectional area A sets stress, while the original length L₀ sets the strain denominator.
**Predict:** For the same material, load, and length, how does doubling area change extension?
**Check:** It halves extension in the linear elastic regime: ΔL = FL₀/(AY).

### Essential equations
- `ΣFₓ = 0; ΣFᵧ = 0; Στ = 0` — Planar static equilibrium.
- `stress = F/A; strain = ΔL/L₀; Y = (F/A)/(ΔL/L₀)` — Small axial elastic deformations; Y is measured in pascals.

### Equation explanations & derivations
Original explanations mapped to the topic scope of the university review. A derivative is an instantaneous rate; an integral adds small contributions. Definitions and physical laws are stated as starting points.

#### Equilibrium conditions and elastic extension
**Concept:** An object that remains at rest has neither translational nor angular acceleration. A linear elastic material has stress proportional to strain.
**Assumptions:** Planar rigid-body equilibrium; a uniform rod or wire under small axial elastic deformation.
**Picture — Stress stretches a material; strain measures the fraction:** The lower bar is the same specimen under tension; the extension is exaggerated. Cross-sectional area A sets stress, while the original length L₀ sets the strain denominator.
**Predict:** For the same material, load, and length, how does doubling area change extension?
**Check:** It halves extension in the linear elastic regime: ΔL = FL₀/(AY).
1. Set a_CM = 0 in ΣF = Ma_CM. Set α = 0 in the fixed-axis torque equation. In a plane this gives ΣFₓ = 0, ΣFᵧ = 0, and Στ = 0.
2. Define stress = F/A and strain = ΔL/L₀. Young’s modulus is their ratio in the linear elastic regime: Y = (F/A)/(ΔL/L₀).
3. Rearrange to ΔL = FL₀/(AY). This has the spring form F = k_eff ΔL with k_eff = AY/L₀.
4. Similarly, linear bulk response uses bulk modulus B = −ΔP/(ΔV/V), with the minus sign accounting for compression when pressure rises.
**Result:** `ΣFₓ = ΣFᵧ = Στ = 0; ΔL = FL₀/(AY); B = −VΔP/ΔV`
**Check:** Doubling wire length doubles its extension under the same force; doubling cross-sectional area halves it. Force balance alone cannot rule out rotation.
**Scope reference:** [12. Equilibrium and Elasticity](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-12)

### Worked example
A uniform 4.00 m beam weighs 200 N and is supported at both ends. A 300 N load sits 1.00 m from the left end. Find both upward supports.

### Solution
1. Take torques about the left end: R_right(4.00) − 200(2.00) − 300(1.00) = 0.
2. R_right = 700/4.00 = 175 N.
3. Vertical force balance gives R_left + 175 − 200 − 300 = 0.
**Answer:** Left support: 325 N; right support: 175 N.

### Common trap
Use perpendicular lever arms. A force passing through the pivot creates zero torque about that pivot.

### Self-check
An object has zero net force. Must it be in static equilibrium?
- Yes, always
- No; net torque may be nonzero
- Only if it is heavy
**Answer:** No; net torque may be nonzero. A pair of opposite forces at different lines of action can have zero resultant force and a nonzero turning effect.

## 10 Fluids
> Relate pressure, buoyancy, and ideal flow to forces and energy.

### Pressure at rest
Pressure is normal force per area. In a fluid of uniform density at rest, pressure increases by ρgh below a reference level. Absolute pressure includes the pressure at the top; gauge pressure subtracts atmospheric pressure. Pascal’s principle transmits an applied pressure change through an enclosed fluid.

**Picture — Pressure increases with depth:** Depth h is measured downward from the surface, where pressure is P₀. The weight of water above a point accounts for the additional pressure ρgh. Density ρ and g are constant here.
**Predict:** At twice the depth, does the absolute pressure always double?
**Check:** No. The gauge pressure ρgh doubles, but absolute pressure also includes the unchanged surface pressure P₀.

### Buoyancy
The buoyant force equals the weight of displaced fluid. An object floating in equilibrium displaces its own weight of fluid, not necessarily its entire volume. Compare average object density with fluid density to predict floating. The upward force results from pressure being greater on the lower surface.

**Picture — Floating means buoyancy balances weight:** The immersed part of the object occupies the volume that fluid would otherwise fill. In floating equilibrium, the weight of that displaced fluid equals the object’s whole weight.
**Predict:** An object has half the fluid’s average density. What fraction of its volume floats below the surface?
**Check:** One half: V_sub/V = ρ_object/ρ_fluid = ½, for equilibrium in the uniform fluid.

### Flow and its assumptions
In steady incompressible flow through a tube, volume flow rate Av is constant. Bernoulli’s equation expresses mechanical energy per unit volume along a streamline for ideal steady flow. Viscosity causes pressure losses and can make this ideal model inadequate; narrow tubes can strongly resist flow.

**Picture — A narrow flow section needs a larger speed:** The same fluid volume crosses each section every second. With smaller cross-sectional area A₂, speed v₂ must rise. At equal height, ideal Bernoulli flow has lower static pressure in the narrow section.
**Predict:** If the cross-sectional area halves, how does the speed change?
**Check:** It doubles for steady incompressible flow, because Av must remain constant.

### Essential equations
- `P = P₀ + ρgh; F_b = ρ_fluid V_displaced g` — ρ is mass density in kg/m³; pressure is in Pa.
- `A₁v₁ = A₂v₂; P + ½ρv² + ρgy = constant` — Bernoulli: steady, incompressible, nonviscous flow along a streamline.

### Equation explanations & derivations
Original explanations mapped to the topic scope of the university review. A derivative is an instantaneous rate; an integral adds small contributions. Definitions and physical laws are stated as starting points.

#### Hydrostatic pressure and buoyancy
**Concept:** A fluid at rest must balance the weight of each small fluid element. Pressure differences then produce the upward buoyant force.
**Assumptions:** Uniform density ρ, constant g, static fluid, depth h measured downward from pressure P₀.
**Picture — Floating means buoyancy balances weight:** The immersed part of the object occupies the volume that fluid would otherwise fill. In floating equilibrium, the weight of that displaced fluid equals the object’s whole weight.
**Predict:** An object has half the fluid’s average density. What fraction of its volume floats below the surface?
**Check:** One half: V_sub/V = ρ_object/ρ_fluid = ½, for equilibrium in the uniform fluid.
1. Take a vertical fluid column with area A and height h. Its weight is ρAhg.
2. Vertical balance gives P_bottom A − P₀A − ρAhg = 0. Dividing by A gives P = P₀ + ρgh.
3. For a submerged rectangular volume, the bottom–top pressure difference is ρg(height). Multiplying by its area gives F_b = ρgV_displaced; side forces cancel.
4. The same displaced-fluid argument works for other shapes. For a floating object, ρ_fluid V_sub g = mg, so V_sub/V_object = ρ_object/ρ_fluid.
**Result:** `P = P₀ + ρgh; F_b = ρ_fluid V_displaced g`
**Check:** A fully submerged rigid object in an incompressible liquid displaces the same volume at different depths, so its buoyant force is unchanged.

#### Continuity and Bernoulli from conservation
**Concept:** Steady flow conserves mass. Pressure work changes the kinetic and gravitational energy of a parcel.
**Assumptions:** Steady, incompressible, nonviscous flow along a streamline, with no pump or turbine between the chosen points.
**Picture — A narrow flow section needs a larger speed:** The same fluid volume crosses each section every second. With smaller cross-sectional area A₂, speed v₂ must rise. At equal height, ideal Bernoulli flow has lower static pressure in the narrow section.
**Predict:** If the cross-sectional area halves, how does the speed change?
**Check:** It doubles for steady incompressible flow, because Av must remain constant.
1. In time Δt, volume A₁v₁Δt enters a tube segment and A₂v₂Δt leaves. With no accumulation, A₁v₁ = A₂v₂.
2. Follow a parcel of volume ΔV. Upstream pressure does P₁ΔV work; downstream pressure removes P₂ΔV.
3. The net work equals ½ρΔV(v₂² − v₁²) + ρgΔV(y₂ − y₁).
4. Divide by ΔV and regroup each point’s terms to obtain Bernoulli’s equation.
**Result:** `A₁v₁ = A₂v₂; P + ½ρv² + ρgy = constant along a streamline`
**Check:** All three Bernoulli terms have units J/m³ = Pa. A horizontal constriction raises ideal flow speed and lowers static pressure.
**Scope reference:** [14. Fluids](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-14)

### Worked example
A sealed object has volume 2.00 × 10⁻³ m³ and mass 1.50 kg. What fraction of its volume is submerged when floating in water of density 1000 kg/m³?

### Solution
1. Floating requires ρ_water V_sub g = mg.
2. V_sub = m/ρ_water = 1.50 × 10⁻³ m³.
3. Divide by total volume: 1.50 × 10⁻³ / (2.00 × 10⁻³) = 0.750.
**Answer:** 75.0% is submerged.

### Common trap
Buoyancy depends on displaced volume and fluid density, not simply on the depth of a fully submerged rigid object.

### Self-check
At the same depth in connected stationary water, the pressure is…
- Greater in the wider part
- The same
- Greater in the narrower part
**Answer:** The same. For the same density and surface pressure, hydrostatic pressure depends on depth, not container shape.

## 11 Oscillations & Waves
> Connect restoring forces, oscillation periods, and the transport of wave energy.

### Simple harmonic motion
A displacement-proportional restoring force produces simple harmonic motion. For a mass on an ideal spring, acceleration points toward equilibrium. Speed is largest at equilibrium and zero at the turning points. The amplitude sets energy, while the ideal mass–spring period depends on mass and spring stiffness.

**Picture — A spring’s restoring force points toward equilibrium:** The three dots are three positions of one oscillator. At either end, F = −kx points back toward x = 0. A larger displacement produces a larger restoring force.
**Predict:** Is acceleration zero where speed is greatest?
**Check:** Yes, in ideal spring SHM it is zero at x = 0 because the restoring force vanishes there. Speed is changing least rapidly at that instant.

### Pendulums, damping, resonance
A simple pendulum approximates SHM only for small angles. Damping removes mechanical energy, reducing amplitude. A periodic driving force can produce a large steady response near a natural frequency; damping controls the resonance peak and prevents unlimited growth in a real oscillator.

**Picture — A pendulum restores; damping removes energy:** Left: gravity has a tangential component back toward the lowest point. Right: the oscillation amplitude decreases as damping transfers mechanical energy to other stores. The sketch is schematic.
**Predict:** Does making an ideal small-angle pendulum heavier change its period?
**Check:** No. Mass cancels from the equation of motion; T ≈ 2π√(ℓ/g). Length and g set the period.

### Travel, superposition, and standing waves
A wave moves a disturbance and energy while medium particles oscillate locally. Frequency is set by the source; wavelength follows from wave speed. Displacements add where waves overlap. Opposite travelling waves can make standing waves with fixed nodes and antinodes. Reflection, refraction, and diffraction change how waves propagate.

**Picture — Standing-wave nodes fix the allowed wavelengths:** Each curve shows one instant of a standing wave. Nodes never move. The fundamental fits half a wavelength; the second mode fits a full wavelength in the same length L.
**Predict:** At the same wave speed, how do these mode frequencies compare?
**Check:** The n = 2 frequency is twice the fundamental because its wavelength is half as long.

### Essential equations
- `F = −kx; T_spring = 2π√(m/k); T_pendulum ≈ 2π√(ℓ/g)` — Ideal spring; small-angle pendulum, respectively.
- `v = fλ; f = 1/T; E_spring = ½kA²` — A is oscillation amplitude; T denotes period here.
- `f_n = nv/(2L), n = 1, 2, …` — Standing waves on a uniform string fixed at both ends.

### Equation explanations & derivations
Original explanations mapped to the topic scope of the university review. A derivative is an instantaneous rate; an integral adds small contributions. Definitions and physical laws are stated as starting points.

#### Spring and pendulum periods from restoring forces
**Concept:** Simple harmonic motion occurs when acceleration is proportional to displacement and points back toward equilibrium.
**Assumptions:** Ideal undamped spring with mass m; simple pendulum with length ℓ and small angle θ in radians.
**Picture — A spring’s restoring force points toward equilibrium:** The three dots are three positions of one oscillator. At either end, F = −kx points back toward x = 0. A larger displacement produces a larger restoring force.
**Predict:** Is acceleration zero where speed is greatest?
**Check:** Yes, in ideal spring SHM it is zero at x = 0 because the restoring force vanishes there. Speed is changing least rapidly at that instant.
1. Hooke’s empirical law F = −kx and Newton’s law give d²x/dt² = −(k/m)x.
2. For x = A cos(ωt + φ), the second derivative is −ω²x. Matching coefficients yields ω² = k/m; since ω = 2π/T, T = 2π√(m/k).
3. A pendulum’s tangential acceleration is ℓ d²θ/dt². Its tangential force is −mg sin θ ≈ −mgθ, so d²θ/dt² = −(g/ℓ)θ.
4. The same comparison gives T ≈ 2π√(ℓ/g). At a spring turning point, E = ½kA²; at equilibrium E = ½mv_max², hence v_max = A√(k/m).
**Result:** `T_spring = 2π√(m/k); T_pendulum ≈ 2π√(ℓ/g); v_max = A√(k/m)`
**Check:** The ideal period does not depend on spring amplitude. A large-angle pendulum violates sin θ ≈ θ, and its period increases with amplitude.

#### Wave speed and standing-wave frequencies
**Concept:** A fixed wave phase moves one wavelength in one period. Standing-wave modes must also satisfy the boundaries.
**Assumptions:** Linear sinusoidal waves; a uniform string of length L fixed at both ends. Tension F_T and linear mass density μ are constant.
**Picture — Standing-wave nodes fix the allowed wavelengths:** Each curve shows one instant of a standing wave. Nodes never move. The fundamental fits half a wavelength; the second mode fits a full wavelength in the same length L.
**Predict:** At the same wave speed, how do these mode frequencies compare?
**Check:** The n = 2 frequency is twice the fundamental because its wavelength is half as long.
1. Write y(x,t) = A sin(kx − ωt), with k = 2π/λ and ω = 2πf. Holding phase fixed gives k dx/dt − ω = 0, so v = ω/k = fλ.
2. For a small string element dx, the difference between endpoint transverse tension components is F_T(∂²y/∂x²)dx.
3. Newton’s law with element mass μdx gives ∂²y/∂t² = (F_T/μ)∂²y/∂x². Substitution of the sinusoid gives v² = F_T/μ.
4. Fixed ends require nodes at both boundaries, so L = nλ/2 with n = 1, 2, … . Substitute λ_n = 2L/n into f = v/λ.
**Result:** `v = fλ = √(F_T/μ); f_n = nv/(2L); f = 1/T`
**Check:** Higher string tension raises all mode frequencies. The medium particles oscillate transversely; their speed is different from the phase speed v.
**Scope reference:** [15. Oscillations](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-15), [16. Waves—I](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-16)

### Worked example
A 0.500 kg mass on a spring with k = 200 N/m oscillates with amplitude 0.100 m. Find its period and maximum speed.

### Solution
1. T = 2π√(0.500/200) = 0.3142 s.
2. At a turning point E = ½kA² = 1.00 J.
3. At equilibrium ½mv_max² = 1.00 J, so v_max = √(2.00/0.500).
**Answer:** T = 0.314 s; v_max = 2.00 m/s.

### Common trap
Wave speed is not particle speed. A particle of the medium need not travel with the moving wave crest.

### Self-check
Doubling the amplitude of an ideal mass–spring oscillator multiplies its total energy by…
- 1
- 2
- 4
**Answer:** 4. E = ½kA², so the energy becomes four times as large, while the ideal period is unchanged.

## 12 Sound
> Explain pitch, loudness, resonance, interference, and Doppler shifts.

### Sound as a pressure wave
In air, sound is a longitudinal mechanical wave: compressions and rarefactions travel through the medium. Frequency chiefly determines pitch. Intensity is power per area and is related to perceived loudness, but the ear’s response also depends on frequency. For an ideal point source spreading uniformly, intensity decreases as 1/r².

**Picture — Sound carries compressions through a medium:** Close lines represent high-pressure compressions; spread lines represent lower-pressure rarefactions. The pattern travels, while a small parcel of air oscillates around its local equilibrium.
**Predict:** Do the same air molecules travel all the way from the speaker to your ear?
**Check:** No. Local oscillations pass the disturbance and energy along; bulk transport of the air is not required.

### Resonance and beats
A vibrating string or air column supports particular standing-wave patterns. An open pipe has displacement antinodes at both ends; a pipe closed at one end has a displacement node there and supports odd harmonics in the ideal model. Two close frequencies produce a beat frequency equal to their difference.

**Picture — Closed and open ends impose different boundaries:** The closed left end is a displacement node; the open right end is a displacement antinode. The curves show displacement amplitude patterns, not the path taken by air through the pipe.
**Predict:** Why is the second allowed frequency 3f₁ rather than 2f₁?
**Check:** A node-to-antinode pipe must contain an odd number of quarter wavelengths. Its ideal modes are f₁, 3f₁, 5f₁, and so on.

### Motion of sources and listeners
The Doppler effect changes the received frequency when source and listener move relative to the medium. Approaching motion increases received frequency; recession lowers it. Source motion changes the wavelength in the medium. A source moving faster than sound generates a shock wave.

**Picture — A moving source crowds wavefronts ahead:** Each circle is a wavefront emitted when the source was farther left. The source moves right slower than sound, so front wavefronts are closer together while rear wavefronts are farther apart.
**Predict:** Which side hears a higher frequency if listeners are at rest in the medium?
**Check:** The side ahead. Sound speed in the medium is unchanged, so the shorter wavelength gives larger f = v/λ.

### Essential equations
- `β = 10 log₁₀(I/I₀); I₀ = 10⁻¹² W/m²` — β is sound level in dB; this I₀ is the reference intensity.
- `f_beat = |f₁ − f₂|; f_n = nv/(4L), n = 1, 3, 5, …` — Second expression: ideal pipe closed at one end.
- `f_observed = f_source (v + v_o)/(v − v_s)` — v_o is positive toward the source; v_s is positive toward the observer; speeds are relative to the medium.

### Equation explanations & derivations
Original explanations mapped to the topic scope of the university review. A derivative is an instantaneous rate; an integral adds small contributions. Definitions and physical laws are stated as starting points.

#### Sound level, spreading, and beats
**Concept:** Intensity is energy flow per area. Decibels compare intensities logarithmically, while beats arise from superposing nearby frequencies.
**Assumptions:** For inverse-square spreading, an isotropic source in a lossless open medium; for beats, two coherent tones with close frequencies.
**Picture — Sound carries compressions through a medium:** Close lines represent high-pressure compressions; spread lines represent lower-pressure rarefactions. The pattern travels, while a small parcel of air oscillates around its local equilibrium.
**Predict:** Do the same air molecules travel all the way from the speaker to your ear?
**Check:** No. Local oscillations pass the disturbance and energy along; bulk transport of the air is not required.
1. A source of acoustic power P sends that power through a sphere of area 4πr², giving I = P/(4πr²).
2. Sound level is defined as β = 10 log₁₀(I/I₀), with I₀ = 10⁻¹² W/m². Therefore a tenfold intensity increase adds 10 dB; doubling adds about 3 dB.
3. Use cos(2πf₁t) + cos(2πf₂t) = 2 cos[π(f₁ − f₂)t] cos[π(f₁ + f₂)t].
4. The magnitude of the slow envelope has successive loud peaks separated by 1/|f₁ − f₂|, so f_beat = |f₁ − f₂|.
**Result:** `I = P/(4πr²); β = 10 log₁₀(I/I₀); f_beat = |f₁ − f₂|`
**Check:** Doubling distance quarters intensity and lowers level by about 6 dB under the spreading assumptions. A zero frequency difference gives no beats.

#### Pipe modes and the Doppler equation
**Concept:** Pipe boundaries fix allowed wavelengths. Relative source and observer motion changes the spacing and arrival rate of sound wavefronts.
**Assumptions:** Ideal pipe with one closed end; one-dimensional classical sound in a stationary medium. Speeds are relative to the medium; source motion stays subsonic.
**Picture — A moving source crowds wavefronts ahead:** Each circle is a wavefront emitted when the source was farther left. The source moves right slower than sound, so front wavefronts are closer together while rear wavefronts are farther apart.
**Predict:** Which side hears a higher frequency if listeners are at rest in the medium?
**Check:** The side ahead. Sound speed in the medium is unchanged, so the shorter wavelength gives larger f = v/λ.
1. A closed end is a displacement node, and an open end is approximately a displacement antinode. Thus L = nλ/4 for n = 1, 3, 5, …, giving f_n = nv/(4L).
2. A source emits crests every T_s = 1/f_s. Moving toward the observer by v_sT_s shortens their spacing to λ_front = (v − v_s)T_s.
3. An observer moving toward the source meets those crests at relative speed v + v_o. Divide the encounter speed by λ_front.
4. This yields f_observed = f_s(v + v_o)/(v − v_s), with v_o positive toward the source and v_s positive toward the observer.
**Result:** `f_n = nv/(4L), n odd; f_observed = f_s(v + v_o)/(v − v_s)`
**Check:** For stationary source and observer, the observed frequency equals f_s. End corrections and real pipe geometry shift the ideal mode frequencies.
**Scope reference:** [17. Waves—II](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-17)

### Worked example
A sound has intensity 1.00 × 10⁻⁶ W/m². Find its level and the level when intensity doubles.

### Solution
1. I/I₀ = 10⁶; β = 10 log₁₀(10⁶) = 60.0 dB.
2. Doubling intensity adds 10 log₁₀2 = 3.01 dB.
3. Levels are logarithmic, so double intensity does not mean double decibels.
**Answer:** 60.0 dB initially; 63.0 dB after doubling.

### Common trap
Do not add decibel levels directly. Add the corresponding intensities for independent sound sources.

### Self-check
Two tones are 440 Hz and 444 Hz. Their beat frequency is…
- 442 Hz
- 4 Hz
- 884 Hz
**Answer:** 4 Hz. The amplitude envelope repeats at the frequency difference, |444 − 440| = 4 Hz.

## 13 Temperature & Kinetic Theory
> Connect temperature and pressure to a microscopic model of matter.

### Temperature and expansion
Thermal equilibrium means that bodies in contact have no net heat transfer and share a temperature. Kelvin temperature is used in gas laws; a temperature interval of 1 K equals 1 °C. Most materials expand when warmed. Linear and volume expansion coefficients describe small changes, but water near 0–4 °C is an important exception to simple expansion behaviour.

**Picture — Thermal expansion is a small fractional length change:** The warmer bar is slightly longer in a material with positive expansion coefficient α. The extra length depends on the original length and temperature increase, not just on final temperature.
**Predict:** For equal material and temperature rise, which expands more: a 1 m or a 2 m bar?
**Check:** The 2 m bar has twice the extension because ΔL is proportional to L₀ in this model.

### The ideal gas model
An ideal gas treats molecules as tiny particles with negligible intermolecular forces except during collisions. Pressure results from impacts on the container walls. The model is most useful at low density, away from condensation. Distinguish n, the amount in moles, from N, the number of molecules; N = nN_A.

**Picture — Molecular collisions exert pressure on a wall:** The molecule reverses its perpendicular velocity in an elastic wall collision. The wall receives the opposite momentum change; many impacts per second produce a steady average pressure.
**Predict:** At fixed volume and molecule count, why does heating an ideal gas raise pressure?
**Check:** Molecules have larger mean squared speed. Their faster, stronger momentum transfers increase P = Nm⟨v²⟩/(3V).

### Molecular energy and phase behaviour
Temperature measures average translational kinetic energy in this model, rather than the speed of each molecule. At a fixed temperature different gases have the same average translational energy, but lighter molecules have higher rms speeds. Real gases, vapour pressure, humidity, and phase changes require attention to intermolecular interactions.

**Picture — Equal temperature means equal average translational energy:** Compare two ideal gases at the same temperature. A molecule four times heavier has half the rms speed, so ½m⟨v²⟩ is unchanged. Arrows compare rms values, not individual trajectories.
**Predict:** Do all molecules in one gas have exactly the rms speed?
**Check:** No. There is a distribution of speeds; rms is the square root of the mean squared speed.

### Essential equations
- `T(K) = T(°C) + 273.15; ΔL = αL₀ΔT` — α is a linear expansion coefficient; use a small enough temperature interval for it to be approximately constant.
- `PV = nRT = Nk_B T; ⟨K_trans⟩ = 3k_B T/2` — P is absolute pressure; R = 8.314 J/(mol·K).
- `v_rms = √(3k_B T/m)` — m is the mass of one molecule, not the mass of the entire gas.

### Equation explanations & derivations
Original explanations mapped to the topic scope of the university review. A derivative is an instantaneous rate; an integral adds small contributions. Definitions and physical laws are stated as starting points.

#### Temperature scales and thermal expansion
**Concept:** Temperature conversion is a scale definition. Expansion coefficients quantify a measured fractional change per degree.
**Assumptions:** A uniform object over a small temperature interval where the linear expansion coefficient α is approximately constant.
**Picture — Thermal expansion is a small fractional length change:** The warmer bar is slightly longer in a material with positive expansion coefficient α. The extra length depends on the original length and temperature increase, not just on final temperature.
**Predict:** For equal material and temperature rise, which expands more: a 1 m or a 2 m bar?
**Check:** The 2 m bar has twice the extension because ΔL is proportional to L₀ in this model.
1. The Kelvin and Celsius scales have equal increments and offset zero points: T(K) = T(°C) + 273.15.
2. Define α ≈ (ΔL/L₀)/ΔT. Rearranging gives ΔL = αL₀ΔT.
3. For an isotropic solid, V = L³. A small fractional change gives ΔV/V ≈ 3ΔL/L, so the volume expansion coefficient is approximately 3α.
**Result:** `T(K) = T(°C) + 273.15; ΔL = αL₀ΔT; ΔV ≈ 3αV₀ΔT`
**Check:** A temperature difference of 10°C is 10 K. An absolute temperature in an ideal-gas equation must be in kelvins.

#### Gas pressure, molecular energy, and rms speed
**Concept:** Pressure comes from repeated molecular momentum transfers to container walls. Temperature measures the mean translational kinetic energy of an ideal gas.
**Assumptions:** Dilute classical ideal gas in thermal equilibrium, isotropic molecular velocities, elastic wall collisions, negligible interaction energy.
**Picture — Molecular collisions exert pressure on a wall:** The molecule reverses its perpendicular velocity in an elastic wall collision. The wall receives the opposite momentum change; many impacts per second produce a steady average pressure.
**Predict:** At fixed volume and molecule count, why does heating an ideal gas raise pressure?
**Check:** Molecules have larger mean squared speed. Their faster, stronger momentum transfers increase P = Nm⟨v²⟩/(3V).
1. In a cubical box of side L, a molecule with x-speed vₓ reverses momentum by 2mvₓ every 2L/|vₓ|. Its average x-force contribution is mvₓ²/L.
2. Divide the sum of forces by wall area L²: P = Nm⟨vₓ²⟩/V. Isotropy gives ⟨vₓ²⟩ = ⟨v²⟩/3, so PV = Nm⟨v²⟩/3.
3. Combine this mechanical result with the ideal-gas equation of state PV = Nk_B T. Then ½m⟨v²⟩ = 3k_B T/2.
4. By definition v_rms = √⟨v²⟩, hence v_rms = √(3k_B T/m). With N = nN_A and R = N_Ak_B, PV = nRT.
**Result:** `PV = nRT = Nk_B T; ⟨K_trans⟩ = 3k_B T/2; v_rms = √(3k_B T/m)`
**Check:** At the same temperature, lighter molecules have larger rms speed but the same mean translational kinetic energy. The wall argument alone does not define an absolute temperature scale.
**Scope reference:** [18. Temperature, Heat, and the First Law of Thermodynamics](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-18), [19. The Kinetic Theory of Gases](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-19)

### Worked example
One mole of ideal gas occupies 0.0240 m³ at 293 K. Find its pressure.

### Solution
1. Use absolute Kelvin temperature and volume in m³.
2. P = nRT/V = (1.00)(8.314)(293)/0.0240.
3. The units J/m³ are equivalent to Pa.
**Answer:** P = 1.02 × 10⁵ Pa, approximately one atmosphere.

### Common trap
Celsius temperatures and gauge pressures cannot be substituted directly into PV = nRT.

### Self-check
At fixed volume and amount of ideal gas, doubling Kelvin temperature makes pressure…
- Double
- Halve
- Unchanged
**Answer:** Double. With n and V constant, P is proportional to absolute temperature.

## 14 Heat
> Account for heating, phase changes, and the three mechanisms of heat transfer.

### Heat, temperature, internal energy
Heat is energy transferred because of a temperature difference. Internal energy is the microscopic energy stored in a system. Temperature is not a measure of the total energy: a large cool object can contain more internal energy than a small hot one.

**Picture — Heat is a transfer, not a substance stored inside a body:** Internal energy U belongs to each body’s microscopic state. The arrow Q denotes energy crossing the boundary because the bodies have different temperatures.
**Predict:** When both bodies reach the same temperature, is all internal energy gone?
**Check:** No. Net heat transfer stops at thermal equilibrium, but both bodies still have internal energy.

### Calorimetry and phase changes
Away from a phase change, heat changes temperature according to mass and specific heat. During melting or boiling at fixed pressure, energy can change phase at approximately constant temperature. Break a multistage process into warming, phase change, and further warming steps; add each energy contribution. For an insulated mixture, energy lost by warm parts equals energy gained by cool parts, including the container if needed.

**Picture — During a phase change, heating need not raise temperature:** This ideal fixed-pressure heating curve has a plateau while solid becomes liquid. Energy supplied on the plateau changes the phase fraction rather than the temperature.
**Predict:** Should you use mcΔT to calculate the energy needed on the melting plateau?
**Check:** No. ΔT is zero there but energy is still required; use the latent heat term mL for the amount that melts.

### How energy travels
Conduction transfers energy through matter without bulk flow. Convection involves bulk fluid motion. Radiation is electromagnetic transfer and can cross a vacuum. Net thermal radiation depends on both the object and its surroundings, not just on the object’s emission.

**Picture — Three ways to transfer thermal energy:** Conduction transfers energy through microscopic interactions without bulk flow. Convection carries energy with a moving fluid. Radiation transports energy as electromagnetic waves and needs no material medium.
**Predict:** Which mechanism carries sunlight across space to Earth?
**Check:** Radiation. Conduction and convection require matter along the transfer route.

### Essential equations
- `Q = mcΔT; Q_phase = mL; ΣQ = 0 (isolated calorimeter)` — c is specific heat; L is latent heat for the stated phase change.
- `P_conduction = kAΔT/ℓ; P_rad,net = εσA(T⁴ − T_surr⁴)` — Steady one-dimensional conduction; radiative surroundings at uniform T_surr. Radiation temperatures are in kelvins.

### Equation explanations & derivations
Original explanations mapped to the topic scope of the university review. A derivative is an instantaneous rate; an integral adds small contributions. Definitions and physical laws are stated as starting points.

#### Heating, phase changes, and calorimetry
**Concept:** Specific heat and latent heat are material properties defined by how much energy a process transfers.
**Assumptions:** Approximately constant specific heat c or latent heat L over the interval; an isolated calorimeter includes every participating body and container.
**Picture — During a phase change, heating need not raise temperature:** This ideal fixed-pressure heating curve has a plateau while solid becomes liquid. Energy supplied on the plateau changes the phase fraction rather than the temperature.
**Predict:** Should you use mcΔT to calculate the energy needed on the melting plateau?
**Check:** No. ΔT is zero there but energy is still required; use the latent heat term mL for the amount that melts.
1. Define c = (1/m)dQ/dT for the specified process. Integrating with constant c gives Q = mc(T_f − T_i).
2. During a specified equilibrium phase change, transferred energy changes the phase fraction at nearly fixed temperature. Define L = Q_phase/m, giving Q_phase = mL.
3. Energy conservation for an isolated set of bodies requires ΣQ = 0. Assign positive Q to energy gained and negative Q to energy lost.
4. For two bodies with no phase change, m₁c₁(T_f − T₁) + m₂c₂(T_f − T₂) = 0. Solve for their shared final temperature.
**Result:** `Q = mcΔT; Q_phase = mL; ΣQ = 0`
**Check:** Without a phase change or reaction, the final isolated equilibrium temperature lies between the starting temperatures. Include separate warming, phase-change, and cooling terms when needed.

#### Conduction and net thermal radiation
**Concept:** Heat-flow laws describe measured material response. Geometry and energy balance convert them into useful power formulas.
**Assumptions:** Steady one-dimensional conduction through a uniform slab; grey-body radiation to large surroundings of uniform temperature, with an appropriate emissivity ε.
**Picture — Three ways to transfer thermal energy:** Conduction transfers energy through microscopic interactions without bulk flow. Convection carries energy with a moving fluid. Radiation transports energy as electromagnetic waves and needs no material medium.
**Predict:** Which mechanism carries sunlight across space to Earth?
**Check:** Radiation. Conduction and convection require matter along the transfer route.
1. Fourier’s empirical conduction law is P = −kA dT/dx, with the sign indicating flow toward lower temperature.
2. For constant k, no internal heat generation, and steady flow through thickness ℓ, temperature varies linearly, so the magnitude is P = kA(T_hot − T_cold)/ℓ.
3. Stefan–Boltzmann emission is P_emit = εσAT⁴. Absorption from the specified surroundings contributes εσAT_surr⁴ under the grey-body model.
4. Subtract absorbed power from emitted power to find net outward radiative transfer.
**Result:** `P_conduction = kAΔT/ℓ; P_rad,net = εσA(T⁴ − T_surr⁴)`
**Check:** At T = T_surr, net radiation is zero even though both bodies continue emitting. The fourth powers require absolute temperatures.
**Scope reference:** [18. Temperature, Heat, and the First Law of Thermodynamics](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-18)

### Worked example
How much energy heats 0.200 kg of liquid water from 20.0 °C to 60.0 °C? Use c = 4186 J/(kg·K), with no losses or phase change.

### Solution
1. ΔT = 60.0 − 20.0 = 40.0 K.
2. Q = (0.200)(4186)(40.0) = 33,488 J.
3. The positive sign indicates energy transferred into the water.
**Answer:** Q = 33.5 kJ.

### Common trap
Do not use mcΔT to account for melting at constant temperature; use latent heat for that part.

### Self-check
Ice at 0 °C melts at constant pressure. During the phase change its temperature…
- Must rise
- Stays approximately constant
- Must fall
**Answer:** Stays approximately constant. Energy changes the molecular arrangement and phase rather than raising temperature during equilibrium melting.

## 15 The Laws of Thermodynamics
> Apply energy conservation with a stated work convention and recognize thermodynamic limits.

### The first law
Use the book’s convention: Q is positive into the system, and W is positive when the system does work on its surroundings. Expansion against a piston can lower internal energy unless heat enters. On a pressure–volume diagram the area under a quasistatic path is work done by the gas; a cycle’s enclosed signed area is net work.

**Picture — The first law accounts for energy crossing a boundary:** Heat entering the boundary adds internal energy; work done by the system transfers energy outward. The equation uses W > 0 for work done by the system.
**Predict:** If Q = +80 J enters and W = +30 J leaves as work, what is ΔU?
**Check:** +50 J. The system gains the energy that enters minus the energy it sends out.

### Recognize the process
An isothermal ideal-gas process has constant temperature and therefore no internal-energy change. Adiabatic means no heat exchange, not constant temperature. Isochoric means constant volume and no boundary work; isobaric means constant pressure. Internal energy is a state quantity, but heat and work depend on the path.

**Picture — The area on a P–V diagram is expansion work:** For this quasistatic constant-pressure expansion, each small volume increase contributes P dV. The shaded rectangle has area PΔV and units joules.
**Predict:** What is the boundary work on a vertical constant-volume P–V path?
**Check:** Zero. With ΔV = 0, there is no area under the path in the volume direction and no piston boundary work.

### Engines and entropy
A cyclic heat engine accepts heat from a hot reservoir, does work, and rejects heat to a cold reservoir. The second law limits the efficiency below one for finite positive reservoir temperatures. Entropy of a system can decrease if its surroundings gain enough; total entropy of an isolated system cannot decrease in a macroscopic process.

**Picture — An engine must reject some heat:** The engine returns to its initial state each cycle, so W_out = Q_H − Q_C. Heat rejected to the cold reservoir is required by the second law; a reversible engine sets the maximum efficiency.
**Predict:** Can a reversible engine between 600 K and 300 K have 75% efficiency?
**Check:** No. Its Carnot limit is 1 − 300/600 = 50%. A real engine is no more efficient than this limit.

### Essential equations
- `ΔU = Q − W; W = PΔV (constant P)` — Work convention: positive for work done by the system.
- `η = W_out/Q_H = 1 − Q_C/Q_H; η_Carnot = 1 − T_C/T_H` — For engine bookkeeping Q_H and Q_C are positive magnitudes. Use Kelvin temperatures.
- `ΔS = Q_rev/T` — For reversible isothermal transfer; use a reversible comparison path to find entropy changes.

### Equation explanations & derivations
Original explanations mapped to the topic scope of the university review. A derivative is an instantaneous rate; an integral adds small contributions. Definitions and physical laws are stated as starting points.

#### First law and ideal-gas work
**Concept:** Internal energy changes through heat entering a system and work leaving it. Gas expansion does mechanical work against external pressure.
**Assumptions:** Closed system with work positive when done by the system; quasistatic ideal-gas paths when gas pressure is used in the work integral.
**Picture — The area on a P–V diagram is expansion work:** For this quasistatic constant-pressure expansion, each small volume increase contributes P dV. The shaded rectangle has area PΔV and units joules.
**Predict:** What is the boundary work on a vertical constant-volume P–V path?
**Check:** Zero. With ΔV = 0, there is no area under the path in the volume direction and no piston boundary work.
1. A piston displacement dx changes volume by dV = A dx. Pressure force PA does work dW = PA dx = P dV.
2. Energy conservation therefore gives ΔU = Q − W, with W = ∫P dV. At constant pressure this becomes PΔV.
3. On a reversible isothermal ideal-gas path, P = nRT/V. Integrate to get W = nRT ln(V_f/V_i). Since ideal-gas internal energy depends only on T, ΔU = 0 and Q = W.
4. For an ideal gas with constant heat capacities on a reversible adiabatic path, Q = 0 and dU = nC_V dT = −P dV.
5. Insert P = nRT/V and integrate C_V dT/T = −R dV/V. With γ = C_P/C_V and C_P − C_V = R, obtain TV^(γ−1) = constant, or PV^γ = constant.
**Result:** `ΔU = Q − W; W = ∫P dV; W_isothermal = nRT ln(V_f/V_i); PV^γ = constant (reversible adiabatic)`
**Check:** Expansion work is positive. An irreversible free expansion cannot be evaluated by inserting the gas pressure into a quasistatic work integral.

#### Heat-engine efficiency, entropy, and the Carnot limit
**Concept:** A cyclic engine cannot turn all absorbed heat into work while also obeying the second law. Entropy accounts for the direction of the heat transfers.
**Assumptions:** Engine operates between reservoirs at fixed T_H > T_C > 0 K; Q_H and Q_C are positive heat magnitudes.
**Picture — An engine must reject some heat:** The engine returns to its initial state each cycle, so W_out = Q_H − Q_C. Heat rejected to the cold reservoir is required by the second law; a reversible engine sets the maximum efficiency.
**Predict:** Can a reversible engine between 600 K and 300 K have 75% efficiency?
**Check:** No. Its Carnot limit is 1 − 300/600 = 50%. A real engine is no more efficient than this limit.
1. Over one cycle, ΔU = 0, so W_out = Q_H − Q_C. Divide by Q_H to get η = 1 − Q_C/Q_H.
2. Entropy change is defined along a reversible comparison path by dS = δQ_rev/T. For reversible isothermal transfer, ΔS = Q_rev/T.
3. A reversible cyclic engine has zero total reservoir entropy change: −Q_H/T_H + Q_C/T_C = 0. Hence Q_C/Q_H = T_C/T_H.
4. Substitute to get η_Carnot = 1 − T_C/T_H. An irreversible engine produces entropy, so Q_C/T_C ≥ Q_H/T_H and η ≤ η_Carnot.
5. At constant volume, heating an ideal gas with constant C_V gives ΔS = ∫nC_V dT/T = nC_V ln(T_f/T_i). A gas entropy change can be calculated this way even if the actual path is irreversible.
**Result:** `η = 1 − Q_C/Q_H ≤ 1 − T_C/T_H; ΔS = ∫δQ_rev/T; ΔS_universe ≥ 0`
**Check:** As reservoir temperatures approach equality, maximum efficiency approaches zero. A subsystem may lose entropy while the total entropy still increases.
**Scope reference:** [18. Temperature, Heat, and the First Law of Thermodynamics](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-18), [19. The Kinetic Theory of Gases](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-19), [20. Entropy and the Second Law of Thermodynamics](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-20)

### Worked example
A gas absorbs 500 J of heat while doing 200 J of work. Find ΔU. Then find the Carnot efficiency between 600 K and 300 K.

### Solution
1. First law: ΔU = 500 − 200 = +300 J.
2. The reservoir temperatures are already absolute temperatures.
3. η_Carnot = 1 − 300/600 = 0.500. Real engines between these reservoirs have lower efficiency.
**Answer:** ΔU = +300 J; the ideal limiting efficiency is 50.0%.

### Common trap
An adiabatic expansion can cool a gas even though no heat leaves it: the gas does work at the expense of internal energy.

### Self-check
In an adiabatic process, which is necessarily zero?
- Temperature change
- Heat transfer Q
- Work W
**Answer:** Heat transfer Q. Adiabatic specifies Q = 0. Work and internal-energy change can both be nonzero.

## 16 Electric Charge & Electric Field
> Use vector superposition to relate charges, fields, and electric forces.

### Charge and materials
Electric charge is conserved and occurs in integer multiples of the elementary charge. Electrons can transfer between materials; a positively charged object has a deficit of electrons. Conductors allow mobile charge to redistribute, while insulators restrict that motion. Charging by induction uses redistribution and, if a net charge is desired, a suitable grounding sequence.

**Picture — Charging transfers electrons and conserves total charge:** The two objects initially have equal positive and negative charge overall. Transferring electrons rightward leaves a positive deficit on the left and an equal negative excess on the right. Positive ion cores are omitted.
**Predict:** Does rubbing create a new net charge for the isolated pair?
**Check:** No. It redistributes charge. The total charge of the two-object isolated system is unchanged.

### Coulomb force and field
Like charges repel and unlike charges attract. Compute the force from each source separately and add the vectors. Electric field at a point is force per unit positive test charge; its direction describes what a positive test charge would experience. A negative charge feels force opposite the field.

**Picture — Electric-field direction uses a positive test charge:** A positive source creates an outward electric field at the marked point. The field belongs to the source configuration; the force on a test particle is F = qE and depends on its charge sign.
**Predict:** Which way does an electron accelerate at this point if the electric force is the only force?
**Check:** Left, toward +Q, because its negative charge makes its force opposite the rightward field.

### Field lines and electrostatic conductors
Field lines point away from positive charges and toward negative ones; closer spacing represents stronger field. They do not cross because the field at a point has a single direction. Inside the material of a conductor in electrostatic equilibrium, the field is zero and excess charge lies on surfaces. Gauss’s law relates total electric flux through a closed surface to enclosed charge.

**Picture — A Gaussian surface counts enclosed charge through flux:** Outward field arrows cross a spherical imaginary boundary. By symmetry, E is constant and normal on the sphere, so Gauss’s law becomes E(4πr²) = Q/ε₀.
**Predict:** Does zero enclosed charge always mean zero electric field?
**Check:** No. External charges can create a field that enters and leaves the surface with zero net flux.

### Essential equations
- `F = k_e |q₁q₂|/r²; E = k_e |Q|/r²; F⃗ = qE⃗` — Point charges or appropriate spherical distributions; k_e = 8.988 × 10⁹ N·m²/C².
- `Φ_E = EA cos θ; ∮E⃗·dA⃗ = Q_enclosed/ε₀` — First: uniform field on a flat surface, θ to its normal. Second: Gauss’s law.

### Equation explanations & derivations
Original explanations mapped to the topic scope of the university review. A derivative is an instantaneous rate; an integral adds small contributions. Definitions and physical laws are stated as starting points.

#### Coulomb force, field, and superposition
**Concept:** Electric field describes the force per unit test charge from a source configuration. Coulomb’s inverse-square law is an experimental starting law.
**Assumptions:** Electrostatic point charges in vacuum; a test charge small enough not to disturb the source distribution.
**Picture — Electric-field direction uses a positive test charge:** A positive source creates an outward electric field at the marked point. The field belongs to the source configuration; the force on a test particle is F = qE and depends on its charge sign.
**Predict:** Which way does an electron accelerate at this point if the electric force is the only force?
**Check:** Left, toward +Q, because its negative charge makes its force opposite the rightward field.
1. Coulomb’s law gives force magnitude F = k_e|Qq|/r². Define E = F/q for a positive test charge, including its direction.
2. Cancel test-charge magnitude to obtain E = k_e|Q|/r²; the direction is outward for Q > 0 and inward for Q < 0.
3. For any test charge, the vector force is F = qE. A negative q reverses the direction.
4. The superposition principle adds vector field contributions: E_total = ΣEᵢ. Resolve components before summing magnitudes.
**Result:** `E_point = k_e|Q|/r²; F = qE; E_total = ΣEᵢ`
**Check:** At the midpoint of two equal positive charges, the vector fields cancel even though the scalar electric potentials add.

#### Gauss’s law: spherical, line, and sheet symmetry
**Concept:** Electric flux counts the normal field through a surface. A closed-surface flux is fixed by the enclosed charge; symmetry is what lets us extract E from that flux.
**Assumptions:** Vacuum electrostatics. Spherical, infinitely long line, and infinite-sheet results require their stated symmetries; θ is between field and area normal.
**Picture — A Gaussian surface counts enclosed charge through flux:** Outward field arrows cross a spherical imaginary boundary. By symmetry, E is constant and normal on the sphere, so Gauss’s law becomes E(4πr²) = Q/ε₀.
**Predict:** Does zero enclosed charge always mean zero electric field?
**Check:** No. External charges can create a field that enters and leaves the surface with zero net flux.
1. For a uniform field on a flat area, Φ_E = EA cos θ. Gauss’s law states ∮E · dA = Q_enclosed/ε₀.
2. For spherical symmetry, E is radial and constant on a sphere: E(4πr²) = Q_enclosed/ε₀. Outside the source, E = Q/(4πε₀r²).
3. For a line with charge per length λ_q, use a cylinder of radius r and length ℓ. End flux is zero and side flux is E(2πrℓ), giving E = |λ_q|/(2πε₀r).
4. For a sheet of surface charge density σ_q, a pillbox has flux EA on each cap, so 2EA = |σ_q|A/ε₀ and E = |σ_q|/(2ε₀).
5. For a conductor in electrostatic equilibrium the interior field vanishes. A pillbox across its surface then gives E_outside = |σ_q|/ε₀.
**Result:** `∮E · dA = Q_enclosed/ε₀; E_sphere = k_e|Q|/r²; E_sheet = |σ_q|/(2ε₀)`
**Check:** Zero enclosed charge means zero net flux; it does not by itself imply zero field. An external uniform field can enter one side of a closed surface and leave the other.
**Scope reference:** [21. Coulomb’s Law](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-21), [22. Electric Fields](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-22), [23. Gauss’ Law](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-23)

### Worked example
Find the field 0.300 m to the right of an isolated +2.00 μC point charge, and the force on a −1.00 nC charge placed there.

### Solution
1. Convert +2.00 μC to 2.00 × 10⁻⁶ C.
2. E = (8.988 × 10⁹)(2.00 × 10⁻⁶)/(0.300)² = 1.997 × 10⁵ N/C, rightward.
3. F⃗ = qE⃗. The negative test charge reverses the force direction.
**Answer:** E = 2.00 × 10⁵ N/C right; force = 2.00 × 10⁻⁴ N left.

### Common trap
Electric field is a property of the source arrangement; electric force also depends on the sign and size of the charge placed there.

### Self-check
At the midpoint between equal positive charges, the total electric field is…
- Zero
- Directed toward either charge
- Twice the single-charge field
**Answer:** Zero. The equal-magnitude fields point in opposite directions and cancel at that point.

## 17 Electric Potential
> Distinguish scalar potential from vector field and account for energy stored electrically.

### Potential and energy
Potential difference is change in electric potential energy per unit charge. Potential is a scalar, so add contributions algebraically, keeping the signs of source charges. The electric field points toward decreasing potential. A positive charge released from rest accelerates toward lower potential; an electron can move toward higher potential while still losing potential energy.

**Picture — Field points toward lower electric potential:** Dashed lines mark equal-potential surfaces seen edge-on. Moving right lowers potential. A positive charge loses potential energy qΔV in that direction; a negative charge gains it.
**Predict:** What is ΔU for +2 C moving from 30 V to 10 V?
**Check:** ΔU = q(V_f − V_i) = 2(10 − 30) = −40 J. The electric force does +40 J of work.

### Equipotentials and electron volts
Moving a charge along an equipotential changes no electric potential energy. Field lines cross equipotentials at right angles. One electron volt is an energy unit equal to the energy change associated with moving one elementary charge through one volt. It is not a unit of voltage.

**Picture — Equipotential motion and cross-field motion differ:** The circles are equipotentials around a positive point charge. Moving along one circle keeps r and V fixed. The radial field is perpendicular to that motion.
**Predict:** Is an electron volt a voltage or an energy?
**Check:** An energy: 1 eV is the energy magnitude for one elementary charge crossing 1 volt, about 1.602 × 10⁻¹⁹ J.

### Capacitors and dielectrics
A capacitor stores equal and opposite separated charges. Its capacitance is charge magnitude per potential difference. A dielectric can increase capacitance through polarization. If the battery remains connected, voltage stays fixed; if an ideal charged capacitor is isolated, charge stays fixed. These different constraints lead to different energy changes.

**Picture — A capacitor separates charge across a gap:** Two parallel plates carry equal and opposite charges. Their fields add between the plates. For ideal plates, C = εA/d and Q = CV; a linear dielectric increases ε.
**Predict:** At fixed plate area and dielectric, what happens to capacitance when the gap doubles?
**Check:** It halves. At fixed Q the voltage doubles; at fixed V the stored charge halves.

### Essential equations
- `ΔU = qΔV; W_electric = −ΔU; V_point = k_e Q/r` — Point-charge potential uses V = 0 at infinity.
- `ΔV = −EΔx; C = Q/ΔV; C_parallel-plate = εA/d` — First relation is along a uniform field; ideal plates neglect edge effects.
- `U_C = ½C(ΔV)² = Q²/(2C); 1 eV = 1.602 × 10⁻¹⁹ J` — Q is the magnitude of charge on either plate.

### Equation explanations & derivations
Original explanations mapped to the topic scope of the university review. A derivative is an instantaneous rate; an integral adds small contributions. Definitions and physical laws are stated as starting points.

#### Potential from electric work
**Concept:** Potential difference is the potential-energy change per charge. It is related to the field by accumulated work, not by a vector sum of potential values.
**Assumptions:** Electrostatic fields; point-charge potential uses zero at infinity. The uniform-field formula uses displacement along the chosen field axis.
**Picture — Field points toward lower electric potential:** Dashed lines mark equal-potential surfaces seen edge-on. Moving right lowers potential. A positive charge loses potential energy qΔV in that direction; a negative charge gains it.
**Predict:** What is ΔU for +2 C moving from 30 V to 10 V?
**Check:** ΔU = q(V_f − V_i) = 2(10 − 30) = −40 J. The electric force does +40 J of work.
1. Electric work is W_e = ∫qE · dr. Since ΔU = −W_e, divide by q to obtain ΔV = −∫E · dr and ΔU = qΔV.
2. Along a uniform field in the +x direction, the integral gives ΔV = −EΔx. Potential falls in the field direction.
3. For a source Q, the outward radial field is k_eQ/r². Integrate V(r) − V(∞) = −∫∞ʳ k_eQ/s² ds to get V = k_eQ/r.
4. A charge e through 1 V changes energy by e × 1 J/C, defining 1 eV = 1.602 × 10⁻¹⁹ J.
**Result:** `ΔU = qΔV; ΔV = −∫E · dr; V_point = k_eQ/r`
**Check:** A positive charge released in an electric field tends toward lower potential. For a negative charge, lower potential energy instead means higher potential.

#### Capacitance, stored energy, and capacitor combinations
**Concept:** Capacitance connects stored separated charge to voltage. Charging progressively costs more work because the existing charge raises the voltage.
**Assumptions:** Ideal parallel plates, separation d much smaller than plate dimensions, linear dielectric of permittivity ε, negligible edge fields.
**Picture — A capacitor separates charge across a gap:** Two parallel plates carry equal and opposite charges. Their fields add between the plates. For ideal plates, C = εA/d and Q = CV; a linear dielectric increases ε.
**Predict:** At fixed plate area and dielectric, what happens to capacitance when the gap doubles?
**Check:** It halves. At fixed Q the voltage doubles; at fixed V the stored charge halves.
1. Oppositely charged sheets produce E = Q/(εA) between the plates. Voltage magnitude is V = Ed = Qd/(εA).
2. Using the definition C = Q/V gives C = εA/d.
3. During charging, a small charge dq moves through V(q) = q/C, so dU = (q/C)dq. Integrate from 0 to Q: U = Q²/(2C) = ½CV².
4. Parallel capacitors share V and add charge: Q_total = ΣCᵢV, so C_parallel = ΣCᵢ.
5. Series capacitors with initially neutral isolated intermediate conductors carry equal charge magnitudes. Voltages add: V_total = ΣQ/Cᵢ, so 1/C_series = Σ1/Cᵢ.
**Result:** `C = εA/d; U_C = Q²/(2C) = ½CV²; C_parallel = ΣCᵢ; 1/C_series = Σ1/Cᵢ`
**Check:** For fixed voltage, inserting a dielectric increases stored charge and energy; for an isolated fixed-charge capacitor it lowers voltage and energy. State which constraint applies.
**Scope reference:** [24. Electric Potential](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-24), [25. Capacitance](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-25)

### Worked example
A 4.00 μF capacitor is connected across 12.0 V. Find charge magnitude on each plate and stored energy.

### Solution
1. C = 4.00 × 10⁻⁶ F.
2. Q = CΔV = (4.00 × 10⁻⁶)(12.0) = 48.0 × 10⁻⁶ C.
3. U_C = ½(4.00 × 10⁻⁶)(12.0)² = 2.88 × 10⁻⁴ J.
**Answer:** Q = 48.0 μC per plate; stored energy = 0.288 mJ.

### Common trap
Zero potential at a point does not imply zero electric field there; potential depends on a chosen reference.

### Self-check
A positive charge moves to a point 5 V higher in potential. Its electric potential energy…
- Increases
- Decreases
- Must be unchanged
**Answer:** Increases. ΔU = qΔV is positive when both charge and potential change are positive.

## 18 Electric Currents
> Connect charge flow, resistance, and electrical power.

### Current and convention
Current is the rate at which charge crosses a section of wire. Conventional current follows positive-charge motion; conduction electrons in a metal drift in the opposite direction. Charge is not used up by a resistor. The electric field establishes a slow net drift superimposed on much faster random electron motion.

**Picture — Electron drift and conventional current point oppositely:** The sketch shows a metal wire. Current direction is defined by positive-charge motion, but its negative electron carriers drift the other way. Random thermal motion is omitted.
**Predict:** Is charge used up as it passes through a resistor in steady state?
**Check:** No. The same steady current enters and leaves. Energy is transferred to the resistor, while charge is conserved.

### Resistance and resistivity
An ohmic device has an approximately constant voltage-to-current ratio at fixed physical conditions. Resistance depends on geometry and material: a longer wire has more resistance and a wider wire less. Resistivity can change with temperature, so a glowing filament need not have a constant resistance.

**Picture — Geometry affects resistance:** The middle wire is twice as long with the same cross-sectional area, so its resistance doubles. The bottom wire represents twice the area, so its resistance halves. Thickness is schematic.
**Predict:** A wire is twice as long and has twice the area. How does R change?
**Check:** It stays the same if resistivity is unchanged: R_new = ρ(2ℓ)/(2A) = R.

### Power and alternating current
A resistor transfers electrical energy into internal energy. Electrical energy used over time is power times time; a kilowatt-hour is an energy unit. In sinusoidal AC, rms values give the same average resistor heating as equal DC values. Superconductivity and biological signal conduction extend the simple conductor model.

**Picture — Alternating current still produces positive heating:** The current oscillates above and below the dashed zero line. Squaring either sign produces positive resistor heating, so average current zero does not mean average power zero.
**Predict:** A sine wave has peak current 2 A. What DC current gives equal average resistor heating?
**Check:** I_rms = 2/√2 ≈ 1.41 A. Its square is the sine wave’s mean squared current.

### Essential equations
- `I = ΔQ/Δt; V = IR; R = ρℓ/A` — ρ here is electrical resistivity in Ω·m, rather than mass density.
- `P = IV = I²R = V²/R; E_used = PΔt` — The last two power forms apply to resistive elements obeying V = IR.
- `V_rms = V_peak/√2; I_rms = I_peak/√2` — Sinusoidal AC; average resistor power is V_rms I_rms.

### Equation explanations & derivations
Original explanations mapped to the topic scope of the university review. A derivative is an instantaneous rate; an integral adds small contributions. Definitions and physical laws are stated as starting points.

#### Current, resistance, and electrical power
**Concept:** Current measures charge flow, while resistance connects the field driving that flow to the material response.
**Assumptions:** Uniform wire of length ℓ and area A, constant resistivity ρ, steady current; the material is ohmic over the operating range.
**Picture — Geometry affects resistance:** The middle wire is twice as long with the same cross-sectional area, so its resistance doubles. The bottom wire represents twice the area, so its resistance halves. Thickness is schematic.
**Predict:** A wire is twice as long and has twice the area. How does R change?
**Check:** It stays the same if resistivity is unchanged: R_new = ρ(2ℓ)/(2A) = R.
1. Current is I = dQ/dt, or average I = ΔQ/Δt. With carrier number density n_c, charge magnitude |q|, and drift-speed magnitude v_d, I = n_c|q|Av_d.
2. The local material law is E = ρJ, with current density J = I/A. For uniform E, V = Eℓ = ρIℓ/A.
3. Comparing V = IR gives R = ρℓ/A. This depends on the material law rather than being a universal law for every component.
4. A small charge dQ transferring through voltage V transfers energy dE = V dQ. Divide by dt: P = VI. Substitute V = IR to obtain P = I²R = V²/R.
5. When power is constant, total transferred energy is E_used = PΔt.
**Result:** `I = dQ/dt; R = ρℓ/A; P = IV = I²R = V²/R`
**Check:** For the same material and length, a thicker wire has less resistance. Electrical resistivity ρ here has units Ω·m, unlike mass density.

#### Why sinusoidal rms values contain √2
**Concept:** An rms value is the DC current or voltage that would produce the same average heating in a resistor.
**Assumptions:** Sinusoidal steady state, purely resistive load R, average over a whole number of cycles.
**Picture — Alternating current still produces positive heating:** The current oscillates above and below the dashed zero line. Squaring either sign produces positive resistor heating, so average current zero does not mean average power zero.
**Predict:** A sine wave has peak current 2 A. What DC current gives equal average resistor heating?
**Check:** I_rms = 2/√2 ≈ 1.41 A. Its square is the sine wave’s mean squared current.
1. Let i(t) = I_peak sin(ωt). Instantaneous resistor power is i²R = I_peak²R sin²(ωt).
2. The cycle average of sin² is ½, so P_avg = I_peak²R/2.
3. Set this equal to I_rms²R. Taking the positive root gives I_rms = I_peak/√2, and the same argument gives V_rms = V_peak/√2.
**Result:** `I_rms = I_peak/√2; V_rms = V_peak/√2; P_avg = V_rms I_rms (resistor)`
**Check:** The average sinusoidal current is zero, but its rms value and heating are positive. A reactive AC circuit requires a power factor as well.
**Scope reference:** [26. Current and Resistance](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-26), [31. Electromagnetic Oscillations and Alternating Current](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-31)

### Worked example
A 6.00 Ω resistor has 12.0 V across it for 30.0 s. Find current, power, and transferred energy.

### Solution
1. I = 12.0/6.00 = 2.00 A.
2. P = VI = 12.0(2.00) = 24.0 W.
3. E = PΔt = 24.0(30.0) = 720 J.
**Answer:** 2.00 A; 24.0 W; 720 J.

### Common trap
A kilowatt-hour is 3.6 × 10⁶ J, not a unit of power.

### Self-check
A uniform wire’s length doubles while its cross-sectional area stays fixed. Its resistance…
- Doubles
- Halves
- Stays fixed
**Answer:** Doubles. R = ρℓ/A, so resistance doubles if resistivity and area stay unchanged.

## 19 DC Circuits
> Reduce series and parallel networks and use junction and loop rules.

### Series and parallel reasoning
Series elements carry the same current because there is no branch between them. Parallel elements connect across the same two nodes and have the same potential difference. Identify the nodes rather than relying on a drawing’s visual arrangement. Adding a parallel resistor reduces equivalent resistance; adding a series resistor increases it.

**Picture — Series shares current; parallel shares voltage:** The left resistors have no branch between them. The right resistors both connect to the same two vertical node wires. Trace connectivity rather than judging how the drawing looks.
**Predict:** Which has lower resistance: two equal R in series or in parallel?
**Check:** Series gives 2R. Parallel gives R/2, so the parallel pair draws more current at the same applied voltage.

### Kirchhoff and real batteries
The junction rule expresses charge conservation. The loop rule expresses energy conservation per unit charge. Choose current directions; a negative solved current simply means the true direction is opposite. A battery delivering current loses some terminal voltage across its internal resistance. Ideal ammeters go in series and ideal voltmeters in parallel.

**Picture — A junction conserves charge:** In a steady circuit, charge does not accumulate at the junction. The incoming 5 coulombs per second divides into 2 and 3 coulombs per second in the two branches.
**Predict:** If the incoming current rises to 7 A while I₁ stays 2 A, what must I₂ be?
**Check:** 5 A for steady charge balance: I_in = I₁ + I₂.

### Capacitors and transients
Capacitor combinations reverse the resistor rules: capacitances add in parallel and reciprocals add in series. In a charging RC circuit the current is largest initially and falls as capacitor voltage grows. The time constant RC sets the approach rate; one time constant is not a complete charge.

**Picture — RC charging approaches a final value gradually:** The vertical scale is charge divided by its final value. At one time constant τ = RC the capacitor reaches 1 − e⁻¹ ≈ 0.632 of final charge. The ideal curve never jumps instantly to full charge.
**Predict:** After one time constant, is charging complete?
**Check:** No. About 36.8% of the initial charge deficit remains. After each further time constant that deficit is multiplied by e⁻¹.

### Essential equations
- `R_series = ΣRᵢ; 1/R_parallel = Σ(1/Rᵢ)` — Resistors in series share current; those in parallel share voltage.
- `ΣI_in = ΣI_out; ΣΔV_loop = 0; V_terminal = ε − Ir` — Last relation: battery discharging through internal resistance r.
- `τ = RC; Q_charge(t) = Cε(1 − e^(−t/RC)); Q_discharge(t) = Q₀e^(−t/RC)` — Ideal single-resistor, single-capacitor circuits.

### Equation explanations & derivations
Original explanations mapped to the topic scope of the university review. A derivative is an instantaneous rate; an integral adds small contributions. Definitions and physical laws are stated as starting points.

#### Kirchhoff rules, resistor networks, and real batteries
**Concept:** Circuit junctions conserve charge, and a complete electrostatic loop accounts for energy per charge.
**Assumptions:** Lumped DC circuit with negligible charge accumulation at junctions, ideal wires, and no unaccounted changing magnetic flux through a loop.
**Picture — Series shares current; parallel shares voltage:** The left resistors have no branch between them. The right resistors both connect to the same two vertical node wires. Trace connectivity rather than judging how the drawing looks.
**Predict:** Which has lower resistance: two equal R in series or in parallel?
**Check:** Series gives 2R. Parallel gives R/2, so the parallel pair draws more current at the same applied voltage.
1. Charge balance at a junction gives ΣI_in = ΣI_out. Returning around a loop to the same potential gives ΣΔV_loop = 0.
2. In series, current is shared and voltages add: V = ΣIRᵢ = IΣRᵢ. Therefore R_series = ΣRᵢ.
3. In parallel, voltage is shared and currents add: I = ΣV/Rᵢ = VΣ(1/Rᵢ). Therefore 1/R_parallel = Σ1/Rᵢ.
4. A discharging battery with emf ε and internal resistance r has loop equation ε − Ir − V_terminal = 0, giving V_terminal = ε − Ir.
**Result:** `ΣI_in = ΣI_out; ΣΔV_loop = 0; R_series = ΣRᵢ; 1/R_parallel = Σ1/Rᵢ; V_terminal = ε − Ir`
**Check:** Parallel equivalent resistance is smaller than the smallest positive branch resistance. Battery terminal voltage equals its emf when current is zero.

#### RC charging and discharging
**Concept:** As a capacitor charges, its growing voltage reduces the resistor’s voltage and current. The remaining voltage difference decays by a constant fraction per unit time.
**Assumptions:** Ideal single resistor R and capacitor C; charging from Q(0) = 0 with constant emf ε, or discharging from initial charge Q₀ with the battery removed.
**Picture — RC charging approaches a final value gradually:** The vertical scale is charge divided by its final value. At one time constant τ = RC the capacitor reaches 1 − e⁻¹ ≈ 0.632 of final charge. The ideal curve never jumps instantly to full charge.
**Predict:** After one time constant, is charging complete?
**Check:** No. About 36.8% of the initial charge deficit remains. After each further time constant that deficit is multiplied by e⁻¹.
1. For charging, Kirchhoff’s loop rule gives ε − IR − Q/C = 0. Since I = dQ/dt, dQ/dt = (Cε − Q)/(RC).
2. Define the charge deficit u = Cε − Q. Then du/dt = −u/(RC), so du/u = −dt/(RC).
3. Integration gives u(t) = Cεe^(−t/RC), hence Q(t) = Cε[1 − e^(−t/RC)].
4. For discharge, the remaining capacitor charge obeys dQ/dt = −Q/(RC); therefore Q(t) = Q₀e^(−t/RC). The discharge-current sign depends on the chosen loop direction.
**Result:** `τ = RC; Q_charge = Cε(1 − e^(−t/RC)); Q_discharge = Q₀e^(−t/RC)`
**Check:** At one time constant, charging reaches about 63.2% of its final charge and discharging retains about 36.8%. At t = 0 the charging formula gives zero.
**Scope reference:** [27. Circuits](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-27)

### Worked example
Two resistors, 6.00 Ω and 3.00 Ω, are connected in parallel across an ideal 12.0 V battery. Find equivalent resistance and branch currents.

### Solution
1. 1/R_eq = 1/6.00 + 1/3.00 = 1/2.00, so R_eq = 2.00 Ω.
2. Both branches have 12.0 V: I₁ = 12.0/6.00 = 2.00 A; I₂ = 12.0/3.00 = 4.00 A.
3. The battery current is 6.00 A. Check: 12.0/2.00 = 6.00 A.
**Answer:** R_eq = 2.00 Ω; branch currents 2.00 A and 4.00 A; total 6.00 A.

### Common trap
Do not assume equal current in parallel branches with different resistances.

### Self-check
Two identical resistors R in parallel have equivalent resistance…
- 2R
- R
- R/2
**Answer:** R/2. There are two equal current paths, so conductance doubles and equivalent resistance halves.

## 20 Magnetism
> Predict magnetic fields and forces with the correct geometry and sign.

### Sources of magnetic field
Magnets and electric currents produce magnetic fields. Field lines form closed loops; outside a bar magnet they run from north to south. A straight wire produces circular field lines. Curl the fingers of the right hand around the wire with the thumb in the conventional-current direction to determine the field direction.

**Picture — Current produces circular magnetic field lines:** The central dot means conventional current comes toward you. Magnetic field circles the wire counterclockwise, as shown by the tangent arrow. Field strength decreases with distance.
**Predict:** What changes if the current goes into the page instead?
**Check:** The circular magnetic-field direction reverses to clockwise. Use a cross ⊗ for current into the page.

### Magnetic forces on moving charges
A moving charge experiences a force perpendicular to both its velocity and the magnetic field. Use the right-hand cross-product direction for a positive charge and reverse it for a negative charge. A magnetic field alone does no work on a point charge, so it can turn the velocity without changing speed. A perpendicular velocity gives circular motion; a parallel component adds helical motion.

**Picture — Magnetic force bends a moving positive charge:** The cross marks indicate a uniform field into the page. For positive q, the right-hand rule gives an upward force perpendicular to rightward velocity. The magnetic force changes direction, not speed.
**Predict:** For an electron moving right in this field, where does the force point?
**Check:** Downward. A negative charge reverses the direction from v × B.

### Wires, coils, and materials
A current-carrying wire can feel a magnetic force; a loop can feel a torque. These effects underlie motors and moving-coil meters. A long solenoid produces a nearly uniform internal field. Parallel currents in the same direction attract. Ferromagnetic domains and hysteresis explain material magnetization beyond the simple vacuum field model.

**Picture — A current loop in a field feels a turning couple:** The loop is shown at an angle to a uniform horizontal field. Gold symbols denote opposite magnetic forces out of and into the page on its vertical sides. These forces make a torque; net force can be zero.
**Predict:** When is loop torque zero?
**Check:** When its magnetic moment, normal to the loop, is parallel or antiparallel to B, because τ = NIAB sin θ.

### Essential equations
- `F⃗ = q(v⃗ × B⃗); F = |q|vB sin θ; F_wire = IℓB sin θ` — θ is between velocity (or wire current direction) and field.
- `r = mv/(|q|B); B_wire = μ₀I/(2πr); B_solenoid ≈ μ₀nI` — First: nonrelativistic perpendicular motion. Others: long straight wire and long air-core solenoid.
- `τ_loop = NIAB sin θ` — θ is between the loop’s area normal and field; n in the solenoid formula is turns per metre.

### Equation explanations & derivations
Original explanations mapped to the topic scope of the university review. A derivative is an instantaneous rate; an integral adds small contributions. Definitions and physical laws are stated as starting points.

#### Magnetic force, wire force, orbit radius, and loop torque
**Concept:** The magnetic part of the Lorentz-force law is perpendicular to velocity. Summing it over moving charges produces the force on a current-carrying wire.
**Assumptions:** Uniform B; nonrelativistic perpendicular motion for the circular-orbit formula; straight active wire length ℓ; planar coil with N turns.
**Picture — Magnetic force bends a moving positive charge:** The cross marks indicate a uniform field into the page. For positive q, the right-hand rule gives an upward force perpendicular to rightward velocity. The magnetic force changes direction, not speed.
**Predict:** For an electron moving right in this field, where does the force point?
**Check:** Downward. A negative charge reverses the direction from v × B.
1. Start with the physical law F = q(v × B), whose magnitude is |q|vB sin θ. Since F · v = 0, a magnetic field alone does no work on the charge.
2. For v perpendicular to B, set |q|vB = mv²/r to obtain r = mv/(|q|B). Charge sign determines the direction of curvature.
3. In a wire segment, the number of mobile carriers is n_cAℓ. Sum their magnetic forces and use I = n_c|q|Av_d to obtain F_wire = IℓB sin θ.
4. The opposite forces on a rectangular loop make a couple. Force times perpendicular separation gives τ = IAB sin θ for one turn, or τ = NIAB sin θ.
5. Define the magnetic moment magnitude μ = NIA, directed by the current right-hand rule. The vector torque is μ × B and orientation energy is U = −μ · B.
**Result:** `F = q(v × B); r = mv/(|q|B); F_wire = IℓB sin θ; τ_loop = NIAB sin θ`
**Check:** A charge moving parallel to B feels no magnetic force. In the coil torque formula, θ refers to the area normal, not to the plane of the loop.

#### Fields from currents using Ampère’s law
**Concept:** A symmetric current distribution lets us evaluate the magnetic circulation law without adding every current-element contribution separately.
**Assumptions:** Steady currents in vacuum or air; an effectively infinite straight wire, or the central interior of a tightly wound long solenoid.
**Picture — Current produces circular magnetic field lines:** The central dot means conventional current comes toward you. Magnetic field circles the wire counterclockwise, as shown by the tangent arrow. Field strength decreases with distance.
**Predict:** What changes if the current goes into the page instead?
**Check:** The circular magnetic-field direction reverses to clockwise. Use a cross ⊗ for current into the page.
1. For steady currents, Ampère’s law states ∮B · dℓ = μ₀I_enclosed.
2. Around a long straight wire, symmetry makes B tangent and constant on a circular path: B(2πr) = μ₀I.
3. For a long solenoid, choose a rectangular path with one long side inside and one outside. The outside field is approximately zero and the crosswise sides contribute negligibly.
4. If n is turns per unit length, a path of internal length ℓ encloses nℓ currents: Bℓ ≈ μ₀(nℓ)I.
**Result:** `B_wire = μ₀I/(2πr); B_solenoid ≈ μ₀nI`
**Check:** These are symmetry-specific results. A short coil or a point near the solenoid ends requires a more complete field calculation.
**Scope reference:** [28. Magnetic Fields](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-28), [29. Magnetic Fields Due to Currents](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-29)

### Worked example
A proton enters a uniform 0.200 T magnetic field at 1.00 × 10⁶ m/s perpendicular to the field. Find its orbit radius; use m_p = 1.673 × 10⁻²⁷ kg.

### Solution
1. Magnetic force supplies inward acceleration: qvB = mv²/r.
2. r = mv/(qB). Use |q| = 1.602 × 10⁻¹⁹ C.
3. r = (1.673 × 10⁻²⁷)(1.00 × 10⁶)/[(1.602 × 10⁻¹⁹)(0.200)].
**Answer:** r = 0.0522 m = 5.22 cm.

### Common trap
A stationary charge experiences no magnetic force from a static magnetic field. A charge moving parallel to B also has zero magnetic force.

### Self-check
A magnetic field alone bends a charged particle’s path. What happens to its speed?
- It must increase
- It must decrease
- It stays constant
**Answer:** It stays constant. The magnetic force is perpendicular to velocity and does no work. This assumes no accompanying electric field or other energy transfer.

## 21 Electromagnetic Induction & Faraday’s Law
> Track changes in magnetic flux and connect them to induced emf and current.

### Flux and Faraday
Magnetic flux measures field threading an oriented surface. It can change because field strength, loop area, or orientation changes. Faraday’s law gives induced emf from the rate of change of flux linkage. A nonzero emf can exist around a loop even before a conducting wire is placed there; a current additionally requires a conducting path.

**Picture — Flux depends on the angle to the surface normal:** The tilted quadrilateral represents a flat loop of area A; its normal is perpendicular to its plane. Only the field component along that normal contributes to signed flux.
**Predict:** Is flux largest when B is parallel to the plane or to its normal?
**Check:** To the normal: θ = 0 and |Φ_B| = BA. Parallel to the plane gives θ = 90° and zero flux.

### Lenz’s law is energy accounting
The induced current creates a magnetic effect that opposes the change in flux, not necessarily the original field. If outward flux increases, induced current produces inward flux. If outward flux decreases, the induced field is outward. The opposing mechanical effects explain why generators require work and eddy currents can provide braking.

**Picture — Lenz’s law opposes the change in flux:** The applied flux points out of the page and grows. The induced current must create an into-page field to oppose that increase, so the induced current is clockwise. The gold arrow at the right edge points downward.
**Predict:** If the outward applied field were decreasing instead, which current direction would be induced?
**Check:** Counterclockwise, creating an outward field to oppose the loss of outward flux.

### Devices and circuit extensions
A moving conductor can develop a motional emf. Generators rotate coils, motors develop back emf, and transformers use changing flux to change AC voltage. An ideal transformer conserves power, so stepping voltage up steps current down. Inductors store magnetic energy and resist rapid changes of current; AC reactance and resonance extend the DC circuit model.

**Picture — LC oscillations exchange electric and magnetic energy:** At maximum capacitor charge, current is zero. As the capacitor discharges, its electric energy becomes the inductor’s magnetic energy. The continuing current then charges the capacitor with opposite polarity.
**Predict:** At maximum current in an ideal LC circuit, what is the capacitor charge?
**Check:** Zero at that instant. All the oscillation energy is magnetic, ½LI_max²; charge then continues through zero and reverses.

### Essential equations
- `Φ_B = BA cos θ; ε_avg = −NΔΦ_B/Δt` — Uniform B over each turn; θ is measured to the area normal.
- `|ε_motion| = Bℓv; V_s/V_p = N_s/N_p; V_p I_p = V_s I_s` — Motional emf assumes perpendicular geometry; transformer relations assume ideal operation.
- `ε_L = −LΔI/Δt; U_L = ½LI²` — L is self-inductance in henries; the emf formula is an average-rate form for constant L.

### Equation explanations & derivations
Original explanations mapped to the topic scope of the university review. A derivative is an instantaneous rate; an integral adds small contributions. Definitions and physical laws are stated as starting points.

#### Flux, motional emf, and ideal transformers
**Concept:** Faraday’s law connects induced emf to changing magnetic flux. Lenz’s sign makes the induced response oppose the change, consistent with energy conservation.
**Assumptions:** Uniform field over each planar turn for Φ_B = BA cos θ; perpendicular rod motion for Bℓv; ideal transformer with common time-varying flux and negligible losses.
**Picture — Flux depends on the angle to the surface normal:** The tilted quadrilateral represents a flat loop of area A; its normal is perpendicular to its plane. Only the field component along that normal contributes to signed flux.
**Predict:** Is flux largest when B is parallel to the plane or to its normal?
**Check:** To the normal: θ = 0 and |Φ_B| = BA. Parallel to the plane gives θ = 90° and zero flux.
1. Define flux by Φ_B = ∫B · dA; for a uniform field and flat loop, Φ_B = BA cos θ. Faraday’s law states ε = −N dΦ_B/dt.
2. For a rod of length ℓ sliding at speed v across parallel rails in perpendicular B, swept area changes at dA/dt = ℓv. Thus |ε| = Bℓv.
3. Equivalently, magnetic force separates rod charges until |q|E = |q|vB, so the open-circuit voltage is Eℓ = Bℓv.
4. Each ideal transformer turn links the same flux, so voltage magnitudes have ratio V_s/V_p = N_s/N_p. With no losses, input and output power match: V_pI_p = V_sI_s.
**Result:** `ε = −N dΦ_B/dt; |ε_motion| = Bℓv; V_s/V_p = N_s/N_p`
**Check:** A steady flux gives zero induced emf. Increasing transformer voltage decreases available current by the inverse ratio under ideal power conservation.

#### Inductance and magnetic energy
**Concept:** An inductor’s changing current changes its own linked flux, creating an emf that resists the current change.
**Assumptions:** Linear constant inductance L; negligible winding resistance when calculating stored field energy.
**Picture — Building current stores magnetic energy in an inductor:** The coil represents an ideal inductor. Increasing current builds a magnetic field and stores energy; the induced emf opposes that increase. For constant current, the ideal induced emf is zero, while stored energy can remain.
**Predict:** Does doubling current double the stored magnetic energy?
**Check:** No. It quadruples it for constant inductance, because U_L = ½LI².
1. Define flux linkage NΦ_B = LI. Faraday’s law gives ε_L = −d(LI)/dt = −L dI/dt for constant L.
2. An external source raising the current must provide voltage V_L = L dI/dt. Its delivered power is P = IV_L = LI dI/dt.
3. Thus dU = LI dI. Integrate from current 0 to I to obtain U_L = ½LI². Over a finite interval, average self-induced emf is −LΔI/Δt.
**Result:** `ε_L = −L dI/dt; U_L = ½LI²`
**Check:** A constant current has zero ideal self-induced emf while retaining magnetic energy. If L depends strongly on current, the simple quadratic energy formula needs revision.

#### LC oscillations and series RLC resonance
**Concept:** A capacitor stores electric energy and an inductor stores magnetic energy. Their exchange follows the same mathematics as a mass on a spring.
**Assumptions:** Ideal lumped L and C; first take R = 0 and no source, then consider a series resistor and sinusoidal drive.
**Picture — LC oscillations exchange electric and magnetic energy:** At maximum capacitor charge, current is zero. As the capacitor discharges, its electric energy becomes the inductor’s magnetic energy. The continuing current then charges the capacitor with opposite polarity.
**Predict:** At maximum current in an ideal LC circuit, what is the capacitor charge?
**Check:** Zero at that instant. All the oscillation energy is magnetic, ½LI_max²; charge then continues through zero and reverses.
1. Let i = dQ/dt with a consistent passive circuit convention. The unforced loop equation is L d²Q/dt² + Q/C = 0.
2. Compare with the oscillator equation x″ + ω₀²x = 0: ω₀ = 1/√(LC), so Q = Q_max cos(ω₀t + φ). Energy Q²/(2C) + ½Li² is constant.
3. Adding resistance gives LQ″ + RQ′ + Q/C = ε(t). The term RQ′ dissipates energy and damps free oscillations.
4. For sinusoidal steady state, differentiating current gives inductor reactance X_L = ωL, while integrating current gives capacitor reactance X_C = 1/(ωC). Their voltages are opposite in phase.
5. The resistor voltage is in phase with current. The phasor right triangle gives Z = √[R² + (X_L − X_C)²] and I_rms = V_rms/Z. Reactances cancel at ω₀ = 1/√(LC).
**Result:** `ω₀ = 1/√(LC); Z = √[R² + (ωL − 1/(ωC))²]; P_avg = I_rms²R`
**Check:** At series resonance Z = R and the driven current is largest for a fixed source voltage. Individual L and C voltages can still be large; they cancel in the loop sum.
**Scope reference:** [30. Induction and Inductance](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-30), [31. Electromagnetic Oscillations and Alternating Current](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-31)

### Worked example
A 100-turn coil of area 0.0100 m² is perpendicular to a field that falls uniformly from 0.500 T to zero in 0.200 s. Find average emf magnitude.

### Solution
1. The area normal is parallel to B, so initial flux per turn is BA = 0.00500 Wb.
2. ΔΦ_B = −0.00500 Wb.
3. |ε_avg| = 100(0.00500)/0.200 = 2.50 V. The induced field supports the original field direction as it decreases.
**Answer:** Average emf magnitude = 2.50 V.

### Common trap
A large steady flux produces no Faraday emf in a stationary loop. Flux must change.

### Self-check
Flux through a stationary coil is constant and nonzero. Its Faraday-induced emf is…
- Zero
- Always positive
- Proportional to the steady flux
**Answer:** Zero. Faraday’s law depends on flux change per unit time, which is zero here.

## 22 Electromagnetic Waves
> Link electromagnetic fields to light, energy flow, and the spectrum.

### Fields that propagate
Maxwell’s synthesis connects electric and magnetic fields, including a magnetic effect associated with a changing electric field. Accelerating charges can radiate electromagnetic waves. In a plane wave in vacuum, electric and magnetic fields oscillate perpendicular to one another and to the travel direction. No material medium is required.

**Picture — A plane wave has three perpendicular directions:** The arrows show the local directions of E, B, and propagation, not a particle’s path. For the pictured orientation E × B points along travel. Field values vary together as the wave passes.
**Predict:** Does this electromagnetic wave require air or another material medium?
**Check:** No. Electric and magnetic fields propagate through vacuum, with speed c = 1/√(μ₀ε₀).

### One spectrum
Radio, microwave, infrared, visible, ultraviolet, X-ray, and gamma radiation are electromagnetic waves classified by frequency and wavelength. In vacuum all travel at c. A higher frequency means a shorter vacuum wavelength; entering a material changes wavelength and speed while frequency stays fixed at a stationary boundary.

**Picture — The electromagnetic spectrum is one wave family:** Moving right means higher frequency and shorter wavelength. All these waves share the same vacuum speed c; names identify parts of a continuous spectrum, with approximate boundaries.
**Predict:** In vacuum, does an X-ray travel faster than a radio wave?
**Check:** No. Both travel at c. The X-ray has higher frequency and a shorter wavelength.

### Energy and momentum transport
Intensity is average energy flow per unit area. For a sinusoidal plane wave it is proportional to the square of field amplitude. Waves also carry momentum: absorption exerts radiation pressure and ideal normal reflection doubles that pressure for the same incident intensity. Wireless communication encodes information in controlled changes of a carrier wave.

**Picture — Absorption transfers radiation momentum:** Incoming light delivers forward momentum to a surface. An ideal absorber takes that momentum; a perfect reflector reverses the light’s momentum and receives twice as much transfer for normal incidence.
**Predict:** If the field amplitude doubles, how does pressure on an absorber change?
**Check:** It quadruples because intensity is proportional to field amplitude squared, and pressure equals I/c.

### Essential equations
- `c = 1/√(μ₀ε₀) = fλ; E₀ = cB₀` — Relations for electromagnetic waves in vacuum.
- `I_avg = ½cε₀E₀²; p_rad = I/c (absorption); p_rad = 2I/c (reflection)` — Sinusoidal plane wave; normal incidence on an ideal absorber or reflector.

### Equation explanations & derivations
Original explanations mapped to the topic scope of the university review. A derivative is an instantaneous rate; an integral adds small contributions. Definitions and physical laws are stated as starting points.

#### Maxwell’s equations and the speed of light
**Concept:** Changing magnetic fields accompany circulating electric fields, and changing electric fields accompany circulating magnetic fields. Maxwell’s equations predict travelling waves.
**Assumptions:** Vacuum, no free charges or conduction currents in the wave region; plane wave travelling along x, with E along y and B along z.
**Picture — A plane wave has three perpendicular directions:** The arrows show the local directions of E, B, and propagation, not a particle’s path. For the pictured orientation E × B points along travel. Field values vary together as the wave passes.
**Predict:** Does this electromagnetic wave require air or another material medium?
**Check:** No. Electric and magnetic fields propagate through vacuum, with speed c = 1/√(μ₀ε₀).
1. Gauss’s electric law is ∮E · dA = Q/ε₀, and its magnetic counterpart is ∮B · dA = 0. Faraday’s law is ∮E · dℓ = −dΦ_B/dt.
2. Ampère–Maxwell law adds the changing-electric-flux term: ∮B · dℓ = μ₀I + μ₀ε₀ dΦ_E/dt. This term permits waves even where I = 0.
3. For the stated plane-wave components, the curl equations reduce to ∂E_y/∂x = −∂B_z/∂t and ∂B_z/∂x = −μ₀ε₀∂E_y/∂t.
4. Differentiate the first with respect to x and substitute the second to obtain ∂²E_y/∂x² = μ₀ε₀∂²E_y/∂t². Compare with the wave equation coefficient 1/c².
5. For sinusoidal waves, kE₀ = ωB₀, so E₀/B₀ = ω/k = c. One wavelength passes per period, giving c = fλ.
**Result:** `c = 1/√(μ₀ε₀); E₀ = cB₀; c = fλ`
**Check:** E, B, and propagation are mutually perpendicular for this plane wave. The result predicts light speed from electromagnetic constants.

#### Intensity and radiation pressure
**Concept:** Electromagnetic waves transport both energy and momentum. Intensity is the average energy flux; pressure is momentum flux delivered to a surface.
**Assumptions:** Sinusoidal vacuum plane wave; normal incidence on an ideal fully absorbing or reflecting surface.
**Picture — Absorption transfers radiation momentum:** Incoming light delivers forward momentum to a surface. An ideal absorber takes that momentum; a perfect reflector reverses the light’s momentum and receives twice as much transfer for normal incidence.
**Predict:** If the field amplitude doubles, how does pressure on an absorber change?
**Check:** It quadruples because intensity is proportional to field amplitude squared, and pressure equals I/c.
1. The Poynting-vector magnitude is S = EB/μ₀. Substitute B = E/c to get S = cε₀E².
2. For E = E₀ sin(kx − ωt), the cycle average of E² is E₀²/2, so I_avg = ½cε₀E₀².
3. Radiation energy U carries forward momentum U/c. Absorbing energy I A dt delivers momentum I A dt/c, giving force IA/c and pressure I/c.
4. Perfect reflection reverses the radiation momentum and doubles the momentum transfer, giving pressure 2I/c.
**Result:** `I_avg = ½cε₀E₀²; p_rad = I/c (absorption); p_rad = 2I/c (reflection)`
**Check:** Pressure units are (W/m²)/(m/s) = N/m². Doubling electric-field amplitude quadruples intensity and radiation pressure.
**Scope reference:** [32. Maxwell’s Equations; Magnetism of Matter](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-32), [33. Electromagnetic Waves](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-33)

### Worked example
A radio signal has frequency 100 MHz. Find its vacuum wavelength.

### Solution
1. 100 MHz = 1.00 × 10⁸ Hz.
2. λ = c/f = (2.998 × 10⁸)/(1.00 × 10⁸).
3. A frequency in s⁻¹ divided into m/s produces metres.
**Answer:** λ ≈ 3.00 m.

### Common trap
Do not confuse an electromagnetic wave’s oscillating field direction with its direction of propagation.

### Self-check
Which needs a material medium to propagate?
- Radio waves
- Visible light
- Sound
**Answer:** Sound. Sound is a mechanical disturbance of matter; electromagnetic waves can cross a vacuum.

## 23 Light: Geometric Optics
> Trace rays and calculate refraction and image formation with consistent signs.

### Reflection and refraction
At a smooth reflecting surface, incidence and reflection angles are equal, measured from the normal. Refraction follows Snell’s law. Light entering a higher refractive index bends toward the normal and has lower speed. Total internal reflection is possible only from higher to lower index above the critical angle.

**Picture — Measure refraction angles from the normal:** The blue incident ray reaches a horizontal boundary. The teal refracted ray bends toward the dashed normal on entering the higher-index medium; the gold ray is reflected. Angles and index contrast are schematic.
**Predict:** Which quantities change when the transmitted ray enters the higher-index medium?
**Check:** Speed and wavelength decrease. Frequency stays the same at a stationary boundary.

### Images and ray diagrams
A real image forms where rays actually converge and can be projected onto a screen. A virtual image is found by extending diverging rays backward. For a thin converging lens, a parallel incident ray refracts through the far focus and a central ray continues approximately straight. Sketch rays before solving to predict image orientation and location.

**Picture — Two principal rays locate a real inverted image:** The blue ray enters parallel and leaves through the far focus F. The gold central ray continues straight. Their intersection below the axis locates the inverted image. The drawing is schematic and paraxial.
**Predict:** Why can this real image be projected onto a screen?
**Check:** The transmitted rays physically converge at the image point, so a screen there receives the focused light.

### A stated sign convention
For the single-element problems here, a real object has d_o > 0; a real image has d_i > 0 and a virtual image d_i < 0. A converging lens or concave mirror has f > 0; a diverging lens or convex mirror has f < 0. Negative magnification denotes an inverted image. Thin-lens and spherical-mirror formulas assume paraxial rays.

**Picture — Signed image distance distinguishes real and virtual images:** For a lens with light arriving from the left, a real image is on the outgoing right side and a virtual image is on the object’s left side. These are alternative outcomes, not simultaneous images.
**Predict:** For a real object and a negative image distance, what is the sign of magnification?
**Check:** Positive, since m = −d_i/d_o and d_o > 0. The virtual image is upright under this convention.

### Essential equations
- `n = c/v; n₁ sin θ₁ = n₂ sin θ₂; sin θ_c = n₂/n₁` — Angles from the normal; critical-angle formula requires n₁ > n₂.
- `1/f = 1/d_o + 1/d_i; m = h_i/h_o = −d_i/d_o` — Thin lens or paraxial spherical mirror with the stated convention; f_mirror = R/2.

### Equation explanations & derivations
Original explanations mapped to the topic scope of the university review. A derivative is an instantaneous rate; an integral adds small contributions. Definitions and physical laws are stated as starting points.

#### Refraction and total internal reflection
**Concept:** A wave must keep the same phase along an interface. Different wave speeds change its direction and wavelength while frequency stays fixed.
**Assumptions:** Flat stationary interface between transparent media; n = c/v; angles measured from the surface normal.
**Picture — Measure refraction angles from the normal:** The blue incident ray reaches a horizontal boundary. The teal refracted ray bends toward the dashed normal on entering the higher-index medium; the gold ray is reflected. Angles and index contrast are schematic.
**Predict:** Which quantities change when the transmitted ray enters the higher-index medium?
**Check:** Speed and wavelength decrease. Frequency stays the same at a stationary boundary.
1. Wave crests must match along the boundary, so their tangential wave-number components agree: k₁ sin θ₁ = k₂ sin θ₂.
2. Since k = 2πf/v = 2πfn/c and f is unchanged at the interface, cancel the shared factor to get n₁ sin θ₁ = n₂ sin θ₂.
3. The transmitted wavelength is λ_medium = v/f = λ_vacuum/n.
4. For n₁ > n₂, the limiting transmitted angle is 90°. Setting sin θ₂ = 1 gives sin θ_c = n₂/n₁. Larger incidence angles have no propagating refracted ray in the second medium.
**Result:** `n₁ sin θ₁ = n₂ sin θ₂; λ_medium = λ_vacuum/n; sin θ_c = n₂/n₁`
**Check:** Entering a higher-index medium bends a ray toward the normal. Total internal reflection requires travel from higher to lower index.

#### Thin-lens equation and magnification from similar triangles
**Concept:** Two principal rays locate the image. Similar triangles connect image size to object distance and focal length.
**Assumptions:** Thin converging lens, small paraxial angles, real object beyond its positive focal length for the geometric derivation; extend using signed distances for virtual images.
**Picture — Two principal rays locate a real inverted image:** The blue ray enters parallel and leaves through the far focus F. The gold central ray continues straight. Their intersection below the axis locates the inverted image. The drawing is schematic and paraxial.
**Predict:** Why can this real image be projected onto a screen?
**Check:** The transmitted rays physically converge at the image point, so a screen there receives the focused light.
1. Let object height be h_o, real image height h_i < 0, and positive object and image distances d_o and d_i. The central ray gives h_i/h_o = −d_i/d_o.
2. A ray entering parallel to the axis leaves through the far focal point. Its slope is −h_o/f, so at the image plane h_i = h_o(1 − d_i/f).
3. Equate the two height ratios: −d_i/d_o = 1 − d_i/f. Divide by d_i and rearrange to 1/f = 1/d_o + 1/d_i.
4. Thus magnification m = h_i/h_o = −d_i/d_o. For a spherical mirror, a near-axis normal tilts by approximately h/R; reflection doubles the tilt, making f ≈ R/2 and giving the analogous paraxial imaging equation.
**Result:** `1/f = 1/d_o + 1/d_i; m = −d_i/d_o; f_mirror ≈ R/2`
**Check:** At d_o = 2f, the real image has d_i = 2f and m = −1. As d_o approaches f from above, the image distance grows without bound in the ideal model.
**Scope reference:** [33. Electromagnetic Waves](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-33), [34. Images](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-34), [35. Interference](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-35)

### Worked example
An object is 30.0 cm in front of a converging thin lens with focal length +10.0 cm. Find the image position and magnification.

### Solution
1. 1/d_i = 1/10.0 − 1/30.0 = 1/15.0 cm⁻¹.
2. d_i = +15.0 cm, so the image is real and on the outgoing side of the lens.
3. m = −15.0/30.0 = −0.500.
**Answer:** A real inverted image, 15.0 cm beyond the lens and half the object’s height.

### Common trap
Angles for Snell’s law are measured to the normal, not the surface. Draw and label that normal.

### Self-check
Total internal reflection can occur when light travels…
- From any lower index to a higher index
- From higher index to lower index above θ_c
- Only through a vacuum
**Answer:** From higher index to lower index above θ_c. The refracted angle reaches 90° at θ_c; beyond it there is no propagating refracted ray in the simple ray model.

## 24 The Wave Nature of Light
> Explain interference, diffraction, and polarization as wave effects.

### Coherence and interference
Superposed light waves interfere according to their relative phase. Two coherent slits produce bright fringes when path difference is an integer number of wavelengths, and dark fringes halfway between for equal-amplitude illumination. For a distant screen and small angles, fringe positions depend linearly on wavelength and screen distance.

**Picture — Two paths set the phase difference:** Blue and gold mark the distances from each slit to the same screen point P. Their difference sets relative phase. Equal-amplitude in-phase sources reinforce when the difference is a whole number of wavelengths.
**Predict:** If the path difference is exactly 1.5λ, is the point bright or dark?
**Check:** Dark in the ideal equal-amplitude model, because the waves arrive half a cycle out of phase.

### Diffraction and gratings
A finite-width slit spreads light. Interference among contributions across that slit makes a broad central maximum with dark minima. A narrower slit gives a wider central maximum. A diffraction grating uses many regularly spaced slits to produce sharp principal maxima useful for identifying wavelengths.

**Picture — A narrower slit makes a wider central diffraction peak:** The curves are normalized to the same peak, with a common angle scale. A smaller slit width a moves its first minima farther from zero because sin θ_min = λ/a.
**Predict:** If slit width halves at fixed wavelength, what happens to the small-angle central width?
**Check:** It approximately doubles. The central maximum spans from the first negative minimum to the first positive minimum.

### Films and polarization
Thin-film interference includes both travel through the film and phase changes on reflection. Reflection toward a higher refractive index produces a half-cycle phase reversal; count reversals before choosing a bright or dark condition. Polarization describes transverse-field orientation and confirms that light is transverse. A linear analyzer transmits according to Malus’s law.

**Picture — An analyzer passes one electric-field component:** The blue field is tilted by θ from the horizontal analyzer axis. The analyzer transmits the teal projection; squaring the amplitude ratio gives the intensity ratio.
**Predict:** At θ = 60°, what fraction of already polarized input intensity passes?
**Check:** One quarter: cos 60° = ½ and its square is ¼. I₀ is the intensity arriving at this analyzer.

### Essential equations
- `d sin θ = mλ; y_m ≈ mλL/d; Δy ≈ λL/d` — Two-slit bright fringes, or grating principal maxima; screen formulas require small angles and L ≫ d.
- `a sin θ = mλ, m = ±1, ±2, …` — Single-slit dark minima, with slit width a. Do not use this for double-slit bright fringes.
- `I = I₀ cos² θ` — Malus’s law: linearly polarized incident light at angle θ to the analyzer axis.

### Equation explanations & derivations
Original explanations mapped to the topic scope of the university review. A derivative is an instantaneous rate; an integral adds small contributions. Definitions and physical laws are stated as starting points.

#### Double-slit fringes from path difference
**Concept:** Phase differences arise when waves travel different distances. Whole-wavelength differences align crests; half-integer differences reverse them.
**Assumptions:** Two coherent in-phase narrow slits, separation d, same wavelength λ in the propagation medium; far field, and small angles for screen-position formulas.
**Picture — Two paths set the phase difference:** Blue and gold mark the distances from each slit to the same screen point P. Their difference sets relative phase. Equal-amplitude in-phase sources reinforce when the difference is a whole number of wavelengths.
**Predict:** If the path difference is exactly 1.5λ, is the point bright or dark?
**Check:** Dark in the ideal equal-amplitude model, because the waves arrive half a cycle out of phase.
1. Far from the slits, the path difference is Δ = d sin θ. Phase difference is δ = 2πΔ/λ.
2. Constructive interference occurs when δ = 2πm, hence d sin θ = mλ for integer m. Destructive interference occurs at Δ = (m + ½)λ.
3. On a screen distance L away, tan θ = y/L. For small angles sin θ ≈ tan θ, giving y_m ≈ mλL/d.
4. Subtract adjacent bright-fringe positions to obtain Δy ≈ λL/d. A multi-slit grating has the same principal-maximum condition, with sharper maxima.
**Result:** `d sin θ = mλ; y_m ≈ mλL/d; Δy ≈ λL/d`
**Check:** Increasing wavelength widens fringes; increasing slit separation narrows them. At larger angles use the exact sine condition and y = L tan θ.

#### Single-slit minima and the diffraction envelope
**Concept:** Every part of a finite-width slit contributes a wave. At certain angles those contributions cancel across the width.
**Assumptions:** Uniformly illuminated slit of width a in the far field; scalar wave approximation.
**Picture — A narrower slit makes a wider central diffraction peak:** The curves are normalized to the same peak, with a common angle scale. A smaller slit width a moves its first minima farther from zero because sin θ_min = λ/a.
**Predict:** If slit width halves at fixed wavelength, what happens to the small-angle central width?
**Check:** It approximately doubles. The central maximum spans from the first negative minimum to the first positive minimum.
1. At the first minimum, divide the slit into two equal halves. Pair points separated by a/2. Their path difference is (a/2)sin θ.
2. When a sin θ = λ, each pair differs by λ/2 and cancels. For higher nonzero integer m, split the slit into 2|m| equal strips and pair adjacent strips to obtain a sin θ = mλ.
3. Adding all phase contributions across the slit by integration gives amplitude proportional to sin u/u, with u = πa sin θ/λ.
4. Intensity is proportional to squared amplitude, so I = I_central(sin u/u)². For two finite slits, multiply this envelope by the two-slit interference factor.
**Result:** `a sin θ = mλ, m = ±1, ±2, …; I/I_central = (sin u/u)²`
**Check:** At θ = 0 the ratio approaches 1, so m = 0 is the central maximum, not a minimum. Slit width a and slit separation d play different roles.

#### Polarization and Malus’s law
**Concept:** An ideal analyzer passes the electric-field component along its transmission axis. Intensity depends on the square of that component.
**Assumptions:** Linearly polarized incident light and ideal linear analyzer; θ is the angle between polarization and transmission axes.
**Picture — An analyzer passes one electric-field component:** The blue field is tilted by θ from the horizontal analyzer axis. The analyzer transmits the teal projection; squaring the amplitude ratio gives the intensity ratio.
**Predict:** At θ = 60°, what fraction of already polarized input intensity passes?
**Check:** One quarter: cos 60° = ½ and its square is ¼. I₀ is the intensity arriving at this analyzer.
1. Project the incident field amplitude onto the analyzer axis: E_transmitted = E_incident cos θ.
2. Since intensity is proportional to E², divide transmitted by incident intensity to get I/I₀ = cos²θ.
3. For initially unpolarized light, averaging cos²θ over all directions gives ½, so a first ideal polarizer passes half the incident intensity.
**Result:** `I = I₀ cos²θ; I_after_first_polarizer = ½I_unpolarized`
**Check:** Parallel axes transmit all of the already polarized input; crossed ideal axes transmit zero. I₀ in Malus’s law is the intensity arriving at the analyzer.
**Scope reference:** [33. Electromagnetic Waves](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-33), [35. Interference](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-35), [36. Diffraction](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-36)

### Worked example
Light of wavelength 600 nm passes through two slits 0.200 mm apart onto a screen 2.00 m away. Find adjacent bright-fringe spacing.

### Solution
1. λ = 600 × 10⁻⁹ m; d = 0.200 × 10⁻³ m.
2. Δy ≈ λL/d = (600 × 10⁻⁹)(2.00)/(2.00 × 10⁻⁴).
3. The small-angle result is appropriate near the central fringe.
**Answer:** Δy ≈ 0.00600 m = 6.00 mm.

### Common trap
The integer m = 0 labels a bright central double-slit maximum; it is excluded from the single-slit dark-minimum condition.

### Self-check
If double-slit separation increases with wavelength and screen distance fixed, fringe spacing…
- Increases
- Decreases
- Is unchanged
**Answer:** Decreases. Δy = λL/d, so increasing d makes fringes closer together.

## 25 Optical Instruments
> Explain how lenses form useful images and why resolution limits magnification.

### Cameras and eyes
A camera forms a real image on film or a sensor. Aperture controls light collection and affects depth of field; exposure time controls how long light is collected. The eye forms a real image on the retina and accommodates mainly by changing lens shape. Myopia is corrected with a diverging lens; hyperopia and reduced near focusing can require a converging correction.

**Picture — The eye focuses a real image on the retina:** Rays from one object point converge on the retina. Changing lens curvature changes its focusing power. The diagram shows a schematic cross-section, not anatomically scaled tissues.
**Predict:** For myopia, do distant rays focus before or behind the retina without correction?
**Check:** Before it. A diverging corrective lens reduces the incoming convergence so the eye can focus the distant image on the retina.

### Magnifiers, telescopes, microscopes
A magnifying glass increases angular size by allowing a close object to be seen comfortably. A telescope’s objective forms an image that the eyepiece magnifies. A compound microscope combines objective and eyepiece magnifications. Angular magnification is a ratio of viewing angles, not simply the ratio of physical image height to object height.

**Picture — A telescope magnifies an angle:** A distant point sends nearly parallel rays to the objective. The objective forms an intermediate real image; the eyepiece turns rays from that image into a bundle suitable for relaxed viewing. The optical layout is schematic.
**Predict:** What happens to ideal telescope angular magnification if the eyepiece focal length halves?
**Check:** Its magnitude doubles: |M| = f_objective/f_eyepiece, assuming the instrument is refocused for the same viewing condition.

### Diffraction and aberration
Aberrations blur an image because different rays or colours focus differently. Even a perfect instrument has diffraction limits set by wavelength and aperture. Increasing magnification beyond the available resolution enlarges blur without revealing new details. X-ray diffraction uses short wavelengths to probe crystal spacing; CT combines many projections to reconstruct internal structure.

**Picture — Resolution is different from magnification:** Each point source makes a diffraction spot rather than a perfect dot. The circles represent central spots and rings schematically. If their angular separation is too small, magnifying the same blur cannot recover detail.
**Predict:** At fixed wavelength, how does doubling aperture diameter affect the diffraction limit?
**Check:** It halves θ_min ≈ 1.22λ/D, so smaller angular separations can be resolved in the ideal instrument.

### Essential equations
- `P_lens = 1/f; f-number = f/D` — Lens power in dioptres requires f in metres; D is aperture diameter.
- `M_telescope = −f_objective/f_eyepiece; M_magnifier ≈ D_near/f` — Relaxed-eye viewing; D_near is the chosen near-point distance, often 25 cm.
- `θ_min ≈ 1.22λ/D; 2d sin θ = mλ` — First: Rayleigh criterion for a circular aperture in radians. Second: Bragg diffraction from crystal planes.

### Equation explanations & derivations
Original explanations mapped to the topic scope of the university review. A derivative is an instantaneous rate; an integral adds small contributions. Definitions and physical laws are stated as starting points.

#### Lens power, magnifiers, and telescopes
**Concept:** Optical instruments change the angular size of an object at the eye. Their magnification follows from small-angle geometry.
**Assumptions:** Thin lenses, paraxial rays, relaxed-eye viewing; near-point distance D_near is a chosen reference.
**Picture — A telescope magnifies an angle:** A distant point sends nearly parallel rays to the objective. The objective forms an intermediate real image; the eyepiece turns rays from that image into a bundle suitable for relaxed viewing. The optical layout is schematic.
**Predict:** What happens to ideal telescope angular magnification if the eyepiece focal length halves?
**Check:** Its magnitude doubles: |M| = f_objective/f_eyepiece, assuming the instrument is refocused for the same viewing condition.
1. Lens power is defined by P_lens = 1/f with f in metres, giving dioptres. Aperture ratio is defined by f-number = f/D_aperture.
2. An unaided object of height h at the near point subtends θ₀ ≈ h/D_near. A magnifier with the object at its focal plane sends parallel rays with angle θ ≈ h/f.
3. Their angular ratio gives M_magnifier ≈ D_near/f.
4. For a distant object at angular position θ, a telescope objective forms an intermediate image of height h ≈ f_objective θ. An eyepiece sends this image out at angle θ′ ≈ −h/f_eyepiece.
5. Thus M_telescope = θ′/θ = −f_objective/f_eyepiece; the minus sign indicates inversion.
**Result:** `P_lens = 1/f; f-number = f/D; M_magnifier ≈ D_near/f; M_telescope = −f_o/f_e`
**Check:** A longer objective focal length and shorter eyepiece focal length increase telescope angular magnification. Magnification by itself cannot overcome the diffraction resolution limit.

#### Diffraction resolution and Bragg’s law
**Concept:** A finite aperture spreads a point source into a diffraction pattern. Crystal-plane reflections interfere according to their path difference.
**Assumptions:** Circular aperture of diameter D; small angular separation; for Bragg reflection, parallel lattice planes separated by d with θ measured from the planes.
**Picture — Bragg reflection adds two extra path segments:** The two horizontal lines are adjacent crystal planes spaced by d. The lower reflected ray travels an extra segment before and after reflection. Their sum is 2d sin θ; θ is measured from a plane.
**Predict:** What condition makes the two reflected contributions reinforce?
**Check:** Their path difference must be a whole wavelength: 2d sin θ = mλ, for integer order m.
1. The circular-aperture diffraction solution has its first dark ring at sin θ ≈ 1.22λ/D. The coefficient 1.22 comes from adding waves over a circle, not from dimensional analysis.
2. Rayleigh’s criterion takes the peak of one point image at the first minimum of the other, giving θ_min ≈ 1.22λ/D in radians.
3. For rays reflected from adjacent crystal planes, the lower ray travels an extra d sin θ on entering and d sin θ on leaving.
4. Constructive interference requires the total extra distance 2d sin θ to equal mλ.
**Result:** `θ_min ≈ 1.22λ/D; 2d sin θ = mλ`
**Check:** Doubling aperture diameter halves the diffraction-limited angular separation. In Bragg’s law the angle is to the crystal planes, unlike a refraction angle measured from a normal.
**Scope reference:** [34. Images](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-34), [36. Diffraction](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-36)

### Worked example
An astronomical telescope has an objective focal length of 1.00 m and an eyepiece focal length of 0.0250 m. Find angular magnification.

### Solution
1. Use both focal lengths in the same unit.
2. M = −1.00/0.0250 = −40.0.
3. The magnitude gives enlargement of angular size; the minus sign identifies inversion in this ideal telescope.
**Answer:** Angular magnification −40.0, or a 40× inverted view.

### Common trap
Greater magnification does not automatically improve resolution. Aperture and wavelength set a separate limit.

### Self-check
For fixed wavelength, doubling a telescope’s aperture diameter makes its diffraction-limited minimum angular separation…
- Twice as large
- Half as large
- Unchanged
**Answer:** Half as large. θ_min ≈ 1.22λ/D, so a larger aperture can distinguish smaller angular separations.

## 26 The Special Theory of Relativity
> Identify proper quantities and apply relativistic time, length, and energy relations.

### Two postulates
The laws of physics have the same form in all inertial frames, and the speed of light in vacuum is the same for all inertial observers. These statements require new relations between measurements of space and time. Events simultaneous in one frame need not be simultaneous in another.

**Picture — Light takes a longer path in the frame where the clock moves:** The stationary clock’s pulse goes straight up and down. In the other frame its mirror moves sideways while light travels, giving diagonal legs. At the same light speed, the longer path takes more coordinate time.
**Predict:** Which interval is proper time: the clock’s own tick interval or the other frame’s longer interval?
**Check:** The clock’s own interval, Δτ. The two tick events occur at the same place in that clock’s rest frame.

### Proper time and proper length
Proper time is measured by a clock present at both events in its own rest frame. Other inertial frames assign a longer interval to that clock’s ticks. Proper length is the object’s length in its rest frame; a moving observer measures a shorter length parallel to motion, with endpoints measured simultaneously in that observer’s frame. Perpendicular dimensions do not contract in this relation.

**Picture — Moving length requires simultaneous endpoint measurements:** The upper bar is the rod at rest. The lower bar represents its length measured parallel to relative motion in another inertial frame. The endpoints must be recorded at one time in that measuring frame.
**Predict:** If γ = 2 and L₀ = 4 m, what length does the moving-frame measurement give?
**Check:** 2 m. This is a measurement using simultaneous endpoints, not a claim about photographic appearance.

### Momentum and energy
At low speeds, relativistic expressions approach Newtonian ones. Rest energy belongs to mass even at rest. Total energy includes rest and kinetic energy, and energy–momentum accounting applies to reactions. A massive object cannot be accelerated to c with finite energy. Relativistic velocity addition replaces ordinary addition when speeds are large.

**Picture — Relativistic kinetic energy grows sharply near c:** Blue uses K = (γ − 1)mc²; gold uses the classical approximation. Both approach zero together at low speed, but blue rises without bound as speed approaches c. Curves share one scale.
**Predict:** Can a massive object reach c with a finite added energy?
**Check:** No. γ and the required kinetic energy diverge as v approaches c from below.

### Essential equations
- `γ = 1/√(1 − v²/c²); Δt = γΔτ; L = L₀/γ` — Δτ is proper time; L₀ is proper length.
- `p = γmv; E = γmc²; K = (γ − 1)mc²; E² = p²c² + m²c⁴` — m is invariant rest mass; E is total energy.
- `u = (u′ + v)/(1 + u′v/c²)` — Collinear velocity transformation between frames in standard configuration.

### Equation explanations & derivations
Original explanations mapped to the topic scope of the university review. A derivative is an instantaneous rate; an integral adds small contributions. Definitions and physical laws are stated as starting points.

#### Time dilation and length contraction
**Concept:** The same light pulse has speed c in every inertial frame. Different path lengths therefore require different elapsed times.
**Assumptions:** Inertial frames with relative speed v < c; proper time is measured where the two clock events occur at one location; lengths use simultaneous endpoint measurements in the measuring frame.
**Picture — Light takes a longer path in the frame where the clock moves:** The stationary clock’s pulse goes straight up and down. In the other frame its mirror moves sideways while light travels, giving diagonal legs. At the same light speed, the longer path takes more coordinate time.
**Predict:** Which interval is proper time: the clock’s own tick interval or the other frame’s longer interval?
**Check:** The clock’s own interval, Δτ. The two tick events occur at the same place in that clock’s rest frame.
1. A light clock has mirror spacing d perpendicular to its motion. In its rest frame, half a round trip takes Δτ/2 = d/c.
2. In a frame where the clock moves at v, a half-trip is diagonal: (cΔt/2)² = d² + (vΔt/2)².
3. Insert d = cΔτ/2 and solve: Δt = Δτ/√(1 − v²/c²) = γΔτ.
4. To measure a moving rod of rest length L₀, record endpoints simultaneously in the lab: Δt = 0. The Lorentz transformation gives Δx′ = γ(Δx − vΔt), so L₀ = γL.
5. For a particle, the inverse transformations give dx = γ(dx′ + vdt′) and dt = γ(dt′ + vdx′/c²). Divide to obtain u = (u′ + v)/(1 + u′v/c²).
**Result:** `γ = 1/√(1 − v²/c²); Δt = γΔτ; L = L₀/γ; u = (u′ + v)/(1 + u′v/c²)`
**Check:** As v/c approaches zero, γ approaches one and the velocity rule approaches u′ + v. If u′ = c, the transformed velocity is still c.

#### Relativistic energy and the classical limit
**Concept:** Relativistic energy and momentum form a consistent pair. Their invariant relation separates rest energy from kinetic energy.
**Assumptions:** Free particle of invariant rest mass m; p = γmv and E = γmc² are relativistic physical relations.
**Picture — Relativistic kinetic energy grows sharply near c:** Blue uses K = (γ − 1)mc²; gold uses the classical approximation. Both approach zero together at low speed, but blue rises without bound as speed approaches c. Curves share one scale.
**Predict:** Can a massive object reach c with a finite added energy?
**Check:** No. γ and the required kinetic energy diverge as v approaches c from below.
1. Substitute E and p into E² − p²c²: γ²m²c⁴ − γ²m²v²c² = γ²m²c⁴(1 − v²/c²) = m²c⁴.
2. At rest γ = 1, so E_rest = mc². Subtract rest energy to obtain K = (γ − 1)mc².
3. For v ≪ c, expand γ ≈ 1 + ½v²/c². Then K ≈ ½mv², recovering the classical equation.
4. For a massless particle, the invariant relation reduces to E = pc. A photon therefore has momentum despite zero rest mass.
**Result:** `E² = p²c² + m²c⁴; K = (γ − 1)mc²; E_photon = pc`
**Check:** The low-speed limit is a check of consistency. E = pc applies to a massless particle; it is not the general energy equation for a massive body.
**Scope reference:** [37. Relativity](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-37)

### Worked example
A spacecraft passes Earth at 0.800c. Its own clock measures 3.00 years between two ticks. What interval does Earth’s inertial frame assign?

### Solution
1. γ = 1/√(1 − 0.800²) = 1/0.600 = 1.6667.
2. The spacecraft clock measures proper time: Δτ = 3.00 years.
3. Δt = γΔτ = 1.6667(3.00).
**Answer:** 5.00 years in Earth’s frame for this constant-speed comparison.

### Common trap
Decide which clock is present at both events before applying time dilation; do not choose a formula solely from the word “moving.”

### Self-check
A spacecraft moves at 0.800c. Its length along motion is measured in Earth’s frame as…
- 0.600 times its rest length
- 1.667 times its rest length
- Its rest length
**Answer:** 0.600 times its rest length. γ = 1.667 and L = L₀/γ = 0.600L₀.

## 27 Early Quantum Theory & Models of the Atom
> Use photons and quantized energy levels to explain observations classical models cannot.

### Why introduce quanta?
Planck’s quantization accounted for blackbody spectra, and Einstein’s photon model explained the photoelectric effect. A photon has energy hf. In the simple photoelectric model, one photon transfers energy to one electron; an electron can escape only if photon energy exceeds the material’s work function.

**Picture — One photon must supply the electron’s escape energy:** The incoming photon supplies energy hf. Removing the most energetic possible electron still costs the work function φ; its remaining kinetic energy is hf − φ in the single-photon model.
**Predict:** Can more below-threshold photons eject electrons in the simple single-photon model?
**Check:** No. Each individual photon lacks the needed energy. Above threshold, increasing intensity mainly increases the number emitted.

### Wave–particle behaviour
Light produces wave interference and discrete absorption events. Matter also has a de Broglie wavelength related to momentum; electron diffraction is evidence for this wave behaviour. Increasing photoelectric light intensity at fixed frequency above threshold mainly increases the number of emitted electrons, not their maximum kinetic energy. Compton scattering and pair production require photon energy and momentum accounting.

**Picture — Matter waves connect momentum and interference:** An electron’s state propagates with wave behaviour, allowing path amplitudes to interfere. Each detection is localized, but repeated detections build an interference pattern.
**Predict:** If a nonrelativistic electron’s momentum doubles, what happens to its matter wavelength?
**Check:** It halves because λ = h/p. This is a relation for momentum, not the electron’s physical diameter.

### Atomic spectra and Bohr’s model
Discrete spectral lines show that atomic energies are quantized. The Bohr model predicts hydrogen energy levels and one-electron ion spectra, but is not a general description of many-electron atoms. Emission occurs when the atom drops to a lower energy state and releases a photon equal to the energy difference. Absorption requires an allowed energy difference.

**Picture — An atomic transition emits a photon of the energy difference:** The horizontal lines are two allowed atomic energies. A downward transition releases their difference as one photon; an upward transition must receive that same energy difference.
**Predict:** What happens to photon frequency if the energy gap doubles?
**Check:** It doubles because f = ΔE/h. Its vacuum wavelength halves.

### Essential equations
- `E_photon = hf = hc/λ; p_photon = h/λ; λ_matter = h/p` — h = 6.626 × 10⁻³⁴ J·s; use p ≈ mv only for nonrelativistic matter.
- `K_max = hf − φ; eV_stop = K_max; f_threshold = φ/h` — Emission requires hf ≥ φ; V_stop denotes a positive stopping-potential magnitude.
- `E_n = −13.6 Z²/n² eV; hf = |E_f − E_i|` — Approximate hydrogen-like, one-electron energy levels; Z is nuclear charge number.

### Equation explanations & derivations
Original explanations mapped to the topic scope of the university review. A derivative is an instantaneous rate; an integral adds small contributions. Definitions and physical laws are stated as starting points.

#### Photons, matter waves, and the photoelectric equation
**Concept:** Photon energy and matter wavelength are quantum starting relations. Energy conservation then determines photoelectron energies.
**Assumptions:** Single-photon photoelectric model for a clean surface with work function φ; V_stop is a positive stopping-voltage magnitude.
**Picture — One photon must supply the electron’s escape energy:** The incoming photon supplies energy hf. Removing the most energetic possible electron still costs the work function φ; its remaining kinetic energy is hf − φ in the single-photon model.
**Predict:** Can more below-threshold photons eject electrons in the simple single-photon model?
**Check:** No. Each individual photon lacks the needed energy. Above threshold, increasing intensity mainly increases the number emitted.
1. Use the quantum relation E = hf and the vacuum wave relation c = fλ to obtain E_photon = hc/λ.
2. For a photon E = pc, so p = E/c = h/λ. Matter waves obey the de Broglie relation λ = h/p as a separate quantum principle.
3. A photon supplies hf; at least φ is needed to remove the electron. The largest remaining electron kinetic energy is K_max = hf − φ.
4. A stopping potential removes kinetic energy eV_stop, so eV_stop = K_max. At the emission threshold K_max = 0, giving f_threshold = φ/h.
**Result:** `E_photon = hf = hc/λ; λ_matter = h/p; K_max = hf − φ = eV_stop`
**Check:** Below threshold this model predicts no emission even if intensity increases. Above threshold, greater intensity mainly increases electron count; greater frequency increases K_max.

#### Hydrogen-like energy levels in the Bohr model
**Concept:** Coulomb attraction supplies circular acceleration, while Bohr’s historical angular-momentum postulate selects allowed orbits.
**Assumptions:** One electron around charge +Ze; nonrelativistic Bohr model with a very heavy stationary nucleus. Modern quantum mechanics replaces the literal orbit picture.
**Picture — An atomic transition emits a photon of the energy difference:** The horizontal lines are two allowed atomic energies. A downward transition releases their difference as one photon; an upward transition must receive that same energy difference.
**Predict:** What happens to photon frequency if the energy gap doubles?
**Check:** It doubles because f = ΔE/h. Its vacuum wavelength halves.
1. Force balance gives m_ev²/r = k_eZe²/r². Bohr’s postulate is m_evr = nħ for n = 1, 2, … .
2. Eliminate v to obtain r_n = n²ħ²/(m_ek_eZe²).
3. Kinetic energy is ½m_ev² = k_eZe²/(2r), while potential energy is −k_eZe²/r. Thus E = −k_eZe²/(2r).
4. Insert r_n to obtain E_n = −m_ek_e²Z²e⁴/(2n²ħ²) ≈ −13.6 Z²/n² eV.
5. For a transition, energy conservation requires hf = |E_f − E_i|, with emission for a downward transition and absorption for an upward one.
**Result:** `E_n ≈ −13.6 Z²/n² eV; hf = |E_f − E_i|`
**Check:** The negative energy means the electron is bound relative to the zero at infinite separation. The formula does not describe general many-electron atoms.
**Scope reference:** [38. Photons and Matter Waves](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-38), [40. All About Atoms](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-40)

### Worked example
A 400 nm photon strikes a surface with work function 2.00 eV. Find the maximum photoelectron kinetic energy. Use hc ≈ 1240 eV·nm.

### Solution
1. E_photon = 1240/400 = 3.10 eV.
2. Since 3.10 eV exceeds 2.00 eV, emission is possible.
3. K_max = 3.10 − 2.00 = 1.10 eV.
**Answer:** K_max = 1.10 eV; corresponding stopping-potential magnitude is 1.10 V.

### Common trap
Below threshold frequency, simply increasing intensity does not eject electrons in the single-photon photoelectric model.

### Self-check
At fixed frequency above threshold, increasing light intensity chiefly increases…
- Maximum photoelectron energy
- The number of photoelectrons emitted per second
- The work function
**Answer:** The number of photoelectrons emitted per second. More incident photons create more opportunities for emission; energy per photon stays hf.

## 28 Quantum Mechanics of Atoms
> Replace definite electron orbits with quantum states and probability distributions.

### Wave functions and probability
A quantum state is described by a wave function; its squared magnitude gives probability density for a position measurement. An orbital is a spatial state, not a little planetary path. Repeated preparation and measurement reveal a distribution of outcomes. Interference patterns arise from probability amplitudes, while detections occur as localized events.

**Picture — Probability density is not a planetary orbit:** The curve gives relative probability density for repeated measurements of identically prepared particles in a box. The probability in a small interval is approximately the curve height times interval width; the full area is one.
**Predict:** Does the peak mean every particle is found exactly at the centre?
**Check:** No. It means intervals of a given small width near the centre are more probable. The possible positions form a distribution.

### Uncertainty and quantum numbers
Position and momentum cannot both have arbitrarily narrow distributions in the same state. This is intrinsic to the quantum description rather than merely a limitation of instruments. Hydrogen states are labelled by n, ℓ, m_ℓ, and electron spin projection m_s. Allowed values restrict which combinations are possible and how many states a shell contains.

**Picture — Stronger localization requires more wave numbers:** A localized wave packet requires a mixture of wave numbers, hence momenta pₓ = ħkₓ. The two panels show distributions for conjugate quantities, with separate scales.
**Predict:** Is the uncertainty relation only caused by inaccurate measurement equipment?
**Check:** No. It constrains the spreads intrinsic to a quantum state, even for ideal instruments.

### Exclusion, spectra, and lasers
The Pauli exclusion principle prevents two electrons in an atom from sharing all four quantum numbers. Filling available states explains shells and patterns in the periodic table. Atomic transitions generate spectra. Stimulated emission produces a matching photon; a laser requires suitable excitation and population inversion, with feedback often supplied by an optical cavity. Metastable states help explain delayed phosphorescence.

**Picture — Pauli exclusion permits two opposite spins per orbital:** Each box represents one spatial orbital with fixed n, ℓ, and m_ℓ. Its two possible electron spin projections are shown by up and down arrows; they do not mean literal spinning paths.
**Predict:** Can a third electron occupy the first spatial orbital?
**Check:** No. Its two spin states are already occupied. A third electron must have a different set of orbital quantum numbers.

### Essential equations
- `σ_x σ_pₓ ≥ ħ/2; ħ = h/(2π)` — Precise standard-deviation form; the textbook also uses order-of-magnitude uncertainty estimates.
- `n = 1, 2, …; ℓ = 0, …, n−1; m_ℓ = −ℓ, …, +ℓ; m_s = ±½` — Allowed quantum numbers for a bound electron in the atomic model.
- `L = √[ℓ(ℓ+1)] ħ; L_z = m_ℓ ħ` — Orbital angular momentum magnitude and its chosen-axis component.

### Equation explanations & derivations
Original explanations mapped to the topic scope of the university review. A derivative is an instantaneous rate; an integral adds small contributions. Definitions and physical laws are stated as starting points.

#### Confinement and the particle-in-a-box spectrum
**Concept:** A confined matter wave must satisfy boundary conditions. Only certain wavelengths fit, so only certain momenta and energies are allowed.
**Assumptions:** One nonrelativistic particle of mass m in a one-dimensional infinite square well from x = 0 to x = L.
**Picture — Only whole half-waves fit inside an infinite well:** The curves are allowed wavefunctions at one phase, not probability densities. Their signs may be positive or negative; |ψ|² gives probability density. Each has nodes at both walls.
**Predict:** Why is n = 0 excluded?
**Check:** It would make ψ zero everywhere, which cannot normalize to probability one. The ground state therefore has nonzero energy.
1. The wavefunction vanishes at both walls. As for a fixed-end standing wave, L = nλ/2, so λ_n = 2L/n.
2. Use p = h/λ to find momentum magnitude p_n = nh/(2L). Then E_n = p_n²/(2m) = n²h²/(8mL²).
3. The stationary wavefunction is ψ_n = A sin(nπx/L). Normalization requires ∫₀ᴸ|ψ_n|²dx = 1. The integral of sin² over this interval is L/2, so A = √(2/L).
4. If a photon drives a transition, its energy must equal the difference between the two allowed levels.
**Result:** `E_n = n²h²/(8mL²); ψ_n(x) = √(2/L) sin(nπx/L), n = 1, 2, …`
**Check:** The lowest allowed energy is positive. Halving the well width quadruples every level energy; tighter confinement raises the kinetic-energy scale.

#### Uncertainty and counting atomic states
**Concept:** A localized matter wave combines a spread of wave numbers. Atomic angular-momentum values and quantum numbers follow from quantum wave mechanics.
**Assumptions:** σ denotes standard deviation. Atomic state counting uses the central-field quantum numbers and two electron spin states.
**Picture — Stronger localization requires more wave numbers:** A localized wave packet requires a mixture of wave numbers, hence momenta pₓ = ħkₓ. The two panels show distributions for conjugate quantities, with separate scales.
**Predict:** Is the uncertainty relation only caused by inaccurate measurement equipment?
**Check:** No. It constrains the spreads intrinsic to a quantum state, even for ideal instruments.
1. Fourier wave analysis gives σ_xσ_k ≥ ½. With pₓ = ħkₓ, multiply by ħ to obtain σ_xσ_pₓ ≥ ħ/2. This is a quantum wave result, not an effect of poor instruments.
2. Angular wave solutions have L² eigenvalues ℓ(ℓ+1)ħ² and L_z eigenvalues m_ℓħ. Taking the positive square root gives |L| = √[ℓ(ℓ+1)]ħ.
3. For fixed principal quantum number n, allowed ℓ values are 0 through n−1. For each ℓ, m_ℓ runs from −ℓ to +ℓ, giving 2ℓ+1 orbital states.
4. Each orbital permits two spin states m_s = ±½. Sum 2Σ(2ℓ+1) from ℓ = 0 to n−1 to get a shell capacity of 2n² electrons under the Pauli principle.
**Result:** `σ_xσ_pₓ ≥ ħ/2; |L| = √[ℓ(ℓ+1)]ħ; L_z = m_ℓħ; shell capacity = 2n²`
**Check:** The Bohr value nħ is not the modern orbital magnitude formula. An s orbital has ℓ = 0 and zero orbital angular momentum even though its electron has nonzero kinetic energy.
**Scope reference:** [38. Photons and Matter Waves](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-38), [39. More About Matter Waves](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-39), [40. All About Atoms](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-40)

### Worked example
How many distinct electron states can occupy a 2p subshell?

### Solution
1. The principal quantum number is n = 2 and p means ℓ = 1.
2. Allowed m_ℓ values are −1, 0, and +1: three orbitals.
3. Each orbital has two possible spin projections, so 3 × 2 = 6 distinct states.
**Answer:** Six electrons can occupy the 2p subshell, with no duplicate set of all four quantum numbers.

### Common trap
Do not draw an orbital as a known electron trajectory. It describes a state and a position probability distribution.

### Self-check
For n = 2, which orbital quantum number ℓ is allowed?
- 2 only
- 0 or 1
- Any positive integer
**Answer:** 0 or 1. ℓ runs from 0 through n − 1, so n = 2 permits ℓ = 0 and ℓ = 1.

## 29 Molecules & Solids
> Connect bonding and energy bands to the behaviour of materials and semiconductor devices.

### Bonding and molecular energy
Covalent bonds involve shared electrons; ionic bonding emphasizes electrostatic attraction after electron transfer; metallic bonding involves mobile electrons among positive ion cores. A potential-energy minimum gives an equilibrium separation. Molecules can rotate and vibrate as well as change electronic states, producing closely spaced spectral structures.

**Picture — A bond has a stable equilibrium separation:** The lowest point represents stable separation r₀. Moving the nuclei closer or farther raises potential energy locally; the force restores them toward the minimum. The curve is a schematic molecular potential.
**Predict:** Why can a bond be approximated as a spring near its minimum?
**Check:** A smooth potential is approximately quadratic near a stable minimum: U ≈ U_min + ½k(r − r₀)². Its force is approximately linear and restoring.

### From atomic levels to bands
When many atoms form a solid, their interacting states produce energy bands separated by forbidden gaps. Conductivity depends on available occupied and empty states, not merely on the existence of electrons. Insulators have a large gap; semiconductors have a smaller gap, allowing carrier populations to respond strongly to temperature and impurities.

**Picture — Energy bands are separated by forbidden gaps:** The rectangles represent allowed bands; the white region between them has no allowed bulk electron energies in this ideal model. Moving an electron from the valence edge to the conduction edge requires the band-gap energy.
**Predict:** Is the band gap an empty physical space inside the crystal?
**Check:** No. It is an interval of forbidden electron energies. The vertical direction in this picture means energy, not position.

### Doping and devices
Donor doping creates n-type material with mobile electrons; acceptor doping creates p-type material with holes as carriers. A pn junction responds differently to forward and reverse bias. LEDs emit light when carriers recombine, solar cells separate photogenerated carriers, and transistors use electrical control to switch or amplify signals. These are applications of quantum states and charge transport.

**Picture — An LED converts a recombination energy gap into light:** In a forward-biased direct-gap LED, injected electrons and holes can recombine. Some of their energy is emitted as a photon. The drawing shows carrier roles rather than the detailed junction electric field.
**Predict:** Would a larger direct band gap tend to emit longer or shorter wavelengths?
**Check:** Shorter, because λ ≈ hc/E_gap. Actual device emission also depends on its material and transition details.

### Essential equations
- `E_vib = (ν + ½)hf, ν = 0, 1, 2, …` — Ideal quantum harmonic vibration; level spacing is hf.
- `E_rot = ℓ(ℓ + 1)ħ²/(2I); E_photon ≈ E_gap` — Rigid-rotor model; the band-gap photon relation is an ideal estimate for direct-gap emission.

### Equation explanations & derivations
Original explanations mapped to the topic scope of the university review. A derivative is an instantaneous rate; an integral adds small contributions. Definitions and physical laws are stated as starting points.

#### Molecular vibration and rotation
**Concept:** Near a stable bond length, a molecule behaves approximately like a spring. Rotation contributes a separate quantized energy.
**Assumptions:** Diatomic molecule near equilibrium; harmonic vibration, rigid-rotor approximation, no strong vibration–rotation coupling.
**Picture — A bond has a stable equilibrium separation:** The lowest point represents stable separation r₀. Moving the nuclei closer or farther raises potential energy locally; the force restores them toward the minimum. The curve is a schematic molecular potential.
**Predict:** Why can a bond be approximated as a spring near its minimum?
**Check:** A smooth potential is approximately quadratic near a stable minimum: U ≈ U_min + ½k(r − r₀)². Its force is approximately linear and restoring.
1. For displacement x of the bond length, approximate U(x) = U_min + ½kx². The relative coordinate uses reduced mass μ = m₁m₂/(m₁+m₂).
2. The classical vibration frequency is f = (1/2π)√(k/μ). Solving the quantum harmonic oscillator gives E_vib = (ν + ½)hf with ν = 0, 1, 2, … .
3. A rigid rotor has classical energy L²/(2I). Substitute the quantum value L² = ℓ(ℓ+1)ħ² to obtain E_rot = ℓ(ℓ+1)ħ²/(2I).
4. Allowed transitions require energy matching ΔE = hf_photon; additional selection rules determine which transitions actually occur.
**Result:** `E_vib = (ν + ½)hf; E_rot = ℓ(ℓ+1)ħ²/(2I)`
**Check:** Harmonic vibrational levels have equal spacing hf, while rotor spacings grow with ℓ. The vibration ground state retains zero-point energy.

#### Band gaps, emitted light, and conduction
**Concept:** In a solid, many atomic states form bands. An electron changing bands transfers an energy approximately set by the band gap.
**Assumptions:** Simple band model; E_photon ≈ E_gap applies to ideal direct-gap radiative transitions near band edges. The one-carrier drift model is a simplified conduction model.
**Picture — Energy bands are separated by forbidden gaps:** The rectangles represent allowed bands; the white region between them has no allowed bulk electron energies in this ideal model. Moving an electron from the valence edge to the conduction edge requires the band-gap energy.
**Predict:** Is the band gap an empty physical space inside the crystal?
**Check:** No. It is an interval of forbidden electron energies. The vertical direction in this picture means energy, not position.
1. For an electron dropping from the conduction-band edge to a hole at the valence-band edge, energy conservation gives E_photon ≈ E_gap.
2. Use E_photon = hc/λ to find λ ≈ hc/E_gap, or λ(nm) ≈ 1240/E_gap(eV).
3. For one carrier species, current density magnitude is J = n_c|q|v_d. If v_d = μ_dE with mobility μ_d, then J = n_c|q|μ_dE.
4. Compare with J = E/ρ to find resistivity ρ = 1/(n_c|q|μ_d). A semiconductor with both electrons and holes requires their conductivity contributions to be added.
**Result:** `E_photon ≈ E_gap; λ ≈ hc/E_gap; ρ = 1/(n_c|q|μ_d) (one carrier type)`
**Check:** A larger direct band gap produces shorter-wavelength light. Carrier density and mobility both affect conductivity; a band-gap value alone does not determine a material’s resistance.
**Scope reference:** [40. All About Atoms](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-40), [41. Conduction of Electricity in Solids](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-41)

### Worked example
Estimate the emission wavelength of an ideal LED with a 2.00 eV transition. Use hc = 1240 eV·nm.

### Solution
1. Treat the emitted photon energy as the transition energy.
2. λ = hc/E = 1240/2.00 nm.
3. Real devices can have a spread in wavelengths and nonradiative losses.
**Answer:** λ ≈ 620 nm, in the visible red–orange region.

### Common trap
A hole is a mobile absence of an electron in an otherwise filled band; it behaves as a positive carrier, not as a proton moving through the crystal.

### Self-check
In an n-type semiconductor, the added majority mobile carriers are…
- Protons
- Electrons
- Neutrons
**Answer:** Electrons. Donor impurities supply electrons that can readily enter conducting states.

## 30 Nuclear Physics & Radioactivity
> Track nuclear composition, binding energy, and exponential decay.

### Nuclei and binding
Atomic number Z counts protons; mass number A counts protons plus neutrons. Isotopes share Z but differ in neutron number. Bound nuclei have less mass than their separated constituents, and the mass difference corresponds to binding energy. Use consistent atomic or nuclear mass conventions when calculating mass defects.

**Picture — Binding lowers the total rest energy:** The vertical direction is total rest energy. The bound nucleus lies below the separated nucleons by the binding energy Δmc²; that energy must be supplied to separate the nucleus again.
**Predict:** Does a bound nucleus weigh more or less than the same free protons and neutrons?
**Check:** Less. The positive mass defect corresponds to the energy released on binding.

### Alpha, beta, and gamma
Alpha decay emits a helium nucleus, reducing A by 4 and Z by 2. In beta-minus decay a neutron becomes a proton while emitting an electron and an antineutrino: A is unchanged and Z rises by 1. Beta-plus emission lowers Z by 1. Gamma emission lowers nuclear excitation energy without changing A or Z. Balance charge, nucleon number, and energy–momentum.

**Picture — Decay changes proton and nucleon counts in specific ways:** These three alternative decay types have different bookkeeping. Alpha removes two protons and two neutrons; beta-minus converts a neutron to a proton with electron and antineutrino emission; gamma changes excitation only.
**Predict:** After beta-minus decay, is the daughter the same chemical element?
**Check:** No. Its proton number Z increases by one, so its chemical identity changes even though A is unchanged.

### Statistics and half-life
A decay constant specifies the probability rate for each surviving nucleus. The population follows exponential decay statistically; no schedule predicts a particular nucleus’s decay. Activity is the number of decays per second, measured in becquerels. After every half-life, half of the remaining parent nuclei survive. Dating uses a decay model plus assumptions about the initial sample and its history.

**Picture — Half-life repeatedly halves the survivors:** Each column is one half-life later than the previous one. The expected parent fraction is 1, ½, ¼, and ⅛. The same fraction of survivors decays in each interval, not the same number.
**Predict:** After two half-lives, what fraction has decayed?
**Check:** Three quarters. One quarter remains, so the decayed fraction is 1 − ¼ = ¾.

### Essential equations
- `N(t) = N₀e^(−λt) = N₀2^(−t/T½); T½ = ln 2/λ` — λ is the decay constant; T½ is half-life; time units must agree.
- `A_activity = λN; E_binding = Δmc²; 1 u·c² ≈ 931.5 MeV` — Activity is measured in Bq = s⁻¹. A_activity is distinct from mass number A.

### Equation explanations & derivations
Original explanations mapped to the topic scope of the university review. A derivative is an instantaneous rate; an integral adds small contributions. Definitions and physical laws are stated as starting points.

#### Exponential decay, activity, and half-life
**Concept:** Each surviving nucleus has the same decay probability per unit time. The number decaying per unit time is therefore proportional to the number still present.
**Assumptions:** One parent species, constant decay constant λ, no replenishment; N is a large-sample expectation.
**Picture — Half-life repeatedly halves the survivors:** Each column is one half-life later than the previous one. The expected parent fraction is 1, ½, ¼, and ⅛. The same fraction of survivors decays in each interval, not the same number.
**Predict:** After two half-lives, what fraction has decayed?
**Check:** Three quarters. One quarter remains, so the decayed fraction is 1 − ¼ = ¾.
1. Write dN/dt = −λN. Separate variables: dN/N = −λdt.
2. Integrate from N₀ at 0 to N at t: ln(N/N₀) = −λt. Exponentiate to obtain N = N₀e^(−λt).
3. At t = T½, N/N₀ = ½. Thus ln(½) = −λT½ and T½ = ln 2/λ.
4. Insert λ = ln 2/T½ to rewrite N = N₀2^(−t/T½). Activity counts decays per second: A_activity = −dN/dt = λN.
**Result:** `N = N₀e^(−λt) = N₀2^(−t/T½); T½ = ln 2/λ; A_activity = λN`
**Check:** After three half-lives, one eighth of the original parent population remains. Half-life is a population statistic, not a scheduled lifetime of an individual nucleus.

#### Nuclear size and binding energy
**Concept:** Nuclei have approximately constant interior nucleon density. A bound nucleus also has less mass than its separated nucleons because energy was released on binding.
**Assumptions:** Spherical nuclear-size estimate; use consistent nuclear masses, or neutral atomic masses with electron contributions properly accounted for.
**Picture — Binding lowers the total rest energy:** The vertical direction is total rest energy. The bound nucleus lies below the separated nucleons by the binding energy Δmc²; that energy must be supplied to separate the nucleus again.
**Predict:** Does a bound nucleus weigh more or less than the same free protons and neutrons?
**Check:** Less. The positive mass defect corresponds to the energy released on binding.
1. If nuclear volume is proportional to nucleon count A, then (4/3)πR³ is proportional to A. Hence R = r₀A^(1/3), with empirical r₀ about 1.2 fm.
2. For Z protons and N neutrons, the separated nuclear mass is Zm_p + Nm_n. Define mass defect Δm = Zm_p + Nm_n − M_nucleus.
3. Mass–energy equivalence gives binding energy E_binding = Δmc². Dividing by A gives binding energy per nucleon.
4. A mass difference of 1 u corresponds to about 931.5 MeV/c², so E_binding(MeV) ≈ Δm(u) × 931.5.
**Result:** `R ≈ r₀A^(1/3); E_binding = Δmc²; 1 u·c² ≈ 931.5 MeV`
**Check:** Binding energy is positive for a stable bound nucleus. Mixing neutral atomic masses with bare proton masses introduces electron-mass errors.
**Scope reference:** [42. Nuclear Physics](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-42)

### Worked example
A sample initially contains 8.00 × 10⁶ parent nuclei with a 6.00 h half-life. Find the expected number remaining after 18.0 h and its activity then.

### Solution
1. 18.0/6.00 = 3.00 half-lives, so N = (8.00 × 10⁶)/2³ = 1.00 × 10⁶.
2. Convert half-life: 6.00 h = 21,600 s. λ = ln 2/21,600 = 3.209 × 10⁻⁵ s⁻¹.
3. Activity = λN = 32.09 s⁻¹.
**Answer:** Expected parent population: 1.00 × 10⁶; activity: 32.1 Bq.

### Common trap
After two half-lives, one quarter of the original parent nuclei remain. Half-life does not mean half the original population decays during every equal interval.

### Self-check
After three half-lives, the fraction of parent nuclei remaining is…
- 1/3
- 1/6
- 1/8
**Answer:** 1/8. Multiply the surviving fraction by ½ three times: (½)³ = ⅛.

## 31 Nuclear Energy; Effects & Uses of Radiation
> Use mass–energy accounting and distinguish radiation quantities and applications.

### Nuclear reactions and energy
For a reaction, compare total initial and final rest masses. A positive mass decrease releases energy as kinetic energy or radiation. Fission splits a heavy nucleus, potentially releasing neutrons that continue a chain reaction. Fusion combines light nuclei; high temperatures and confinement help overcome electrical repulsion. In both cases, a rise in binding energy per nucleon can release energy.

**Picture — Fission and fusion can both increase binding per nucleon:** This schematic binding-energy curve peaks near intermediate nuclei. Suitable light nuclei can release energy by combining; suitable heavy nuclei can release energy by splitting. Reaction barriers still matter.
**Predict:** Is released Q positive when total product rest mass is smaller?
**Check:** Yes. Q = (mass_initial − mass_final)c². The decrease in rest energy becomes kinetic energy or radiation.

### Radiation quantities
Activity counts decays per second; absorbed dose measures energy deposited per mass; equivalent dose includes a radiation weighting factor. These quantities answer different questions and cannot be substituted for one another. This lesson explains their units and physical meaning rather than making exposure or treatment recommendations.

**Picture — Dose counts deposited energy per mass:** Each sample receives the same deposited energy E. Absorbed dose divides that energy by the receiving mass, so the larger sample has half the dose. The arrows represent energy transfer, not a medical exposure plan.
**Predict:** Can becquerels alone determine the absorbed dose?
**Check:** No. Activity counts decays per second; dose also depends on emitted energy, absorption, geometry, time, and the mass receiving the energy.

### Imaging and other uses
Radioactive tracers allow emitted radiation to map a substance’s distribution. PET detects pairs of photons associated with positron annihilation; SPECT uses emitted gamma photons. MRI uses nuclear magnetic resonance in magnetic fields and radiofrequency signals; it is not an X-ray technique. Radiation interactions can ionize matter, which underlies both detection and biological effects.

**Picture — PET detects a pair of annihilation photons:** For an electron–positron pair annihilating approximately at rest into two photons, momentum conservation makes their directions nearly opposite. Coincident detections identify a line on which the event occurred.
**Predict:** Why do the photons go in opposite directions in the pair’s rest frame?
**Check:** The initial total momentum is zero, so two final photon momenta must cancel. Motion and binding broaden the ideal picture.

### Essential equations
- `Q_reaction = (Σm_initial − Σm_final)c²` — Positive Q is released energy. Mass and charge conventions must be consistent.
- `D_abs = E_deposited/m; H_equiv = w_R D_abs` — Absorbed dose in Gy = J/kg; equivalent dose in Sv. Sum contributions for mixed radiation types.

### Equation explanations & derivations
Original explanations mapped to the topic scope of the university review. A derivative is an instantaneous rate; an integral adds small contributions. Definitions and physical laws are stated as starting points.

#### Reaction energy, fission, and fusion
**Concept:** The change in total rest mass sets the energy available to products. Fission or fusion releases energy when it leads to more tightly bound products.
**Assumptions:** Consistent initial and final mass conventions; include every reaction product and relevant excitation state.
**Picture — Fission and fusion can both increase binding per nucleon:** This schematic binding-energy curve peaks near intermediate nuclei. Suitable light nuclei can release energy by combining; suitable heavy nuclei can release energy by splitting. Reaction barriers still matter.
**Predict:** Is released Q positive when total product rest mass is smaller?
**Check:** Yes. Q = (mass_initial − mass_final)c². The decrease in rest energy becomes kinetic energy or radiation.
1. Energy conservation reads Σm_initial c² + K_initial = Σm_final c² + K_final when all included energy terms are counted.
2. Rearrange: Q_reaction = (Σm_initial − Σm_final)c² = K_final − K_initial. Positive Q means released rest energy.
3. Expressing masses through nucleon masses minus binding energies shows Q = total final binding energy − total initial binding energy when nucleon counts are unchanged.
4. The binding-energy-per-nucleon curve rises toward intermediate nuclei. Splitting suitable heavy nuclei or combining suitable light nuclei can therefore give positive Q. Charge, momentum, and other conservation laws still apply.
**Result:** `Q_reaction = (Σm_initial − Σm_final)c²`
**Check:** A positive Q does not remove a reaction barrier. Fusion still requires overcoming or tunnelling through electrostatic repulsion.

#### Absorbed and equivalent radiation dose
**Concept:** Absorbed dose counts deposited energy per mass. Equivalent dose applies a specified radiation weighting factor to that absorbed dose.
**Assumptions:** Energy deposited in the stated tissue mass; w_R is the specified radiation-type weighting factor. These definitions are for physics bookkeeping.
**Picture — Dose counts deposited energy per mass:** Each sample receives the same deposited energy E. Absorbed dose divides that energy by the receiving mass, so the larger sample has half the dose. The arrows represent energy transfer, not a medical exposure plan.
**Predict:** Can becquerels alone determine the absorbed dose?
**Check:** No. Activity counts decays per second; dose also depends on emitted energy, absorption, geometry, time, and the mass receiving the energy.
1. Divide deposited energy E_deposited by irradiated mass m: D_abs = E_deposited/m, with 1 Gy = 1 J/kg.
2. For one radiation type, define H_equiv = w_R D_abs in sieverts.
3. For mixed radiation, add contributions: H_equiv = Σw_R D_R. Activity in becquerels counts decays per second and cannot be converted to dose without deposition and exposure information.
**Result:** `D_abs = E_deposited/m; H_equiv = Σw_R D_R`
**Check:** The same deposited energy in twice the mass gives half the absorbed dose. Equivalent dose and effective dose are different quantities; the latter also uses tissue weighting.
**Scope reference:** [42. Nuclear Physics](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-42), [43. Energy from the Nucleus](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-43)

### Worked example
A hypothetical nuclear reaction has an initial-to-final rest-mass decrease of 0.200 u. Find the released energy.

### Solution
1. The initial rest mass is larger, so Q is positive.
2. Use 1 u·c² = 931.5 MeV.
3. Q = 0.200(931.5) = 186.3 MeV.
**Answer:** Q = 186 MeV per reaction, or about 2.98 × 10⁻¹¹ J.

### Common trap
A becquerel does not specify absorbed dose: radiation type, emitted energy, geometry, absorption, and elapsed time also matter.

### Self-check
Which unit directly measures absorbed energy per kilogram?
- Becquerel
- Gray
- Coulomb
**Answer:** Gray. One gray equals one joule deposited per kilogram. The becquerel is one decay per second.

## 32 Elementary Particles
> Classify particles and use conservation laws to test proposed interactions.

### Families of matter
Quarks and leptons are elementary matter particles in the Standard Model. Protons and neutrons are composite baryons made of three valence quarks; mesons contain a valence quark–antiquark pair. Electrons and neutrinos are leptons. Antiparticles have the same mass and reversed relevant additive quantum numbers, such as electric charge.

**Picture — Quark charges add to proton and neutron charges:** Each u valence quark carries +⅔e and each d carries −⅓e. Adding the three valence charges gives a proton’s +e and a neutron’s zero. Circles show composition, not fixed quark positions.
**Predict:** What is the charge of an antiproton?
**Check:** −e. Its valence antiquarks have the opposite charges from the proton’s quarks.

### Interactions and exchange
Electromagnetic interactions involve photons, strong interactions involve gluons and colour charge, and weak interactions involve W and Z bosons. Gravity is not included as a quantum interaction in the Standard Model. An exchange-particle picture is a model for calculating interactions, not a literal classical trajectory of a little ball between objects.

**Picture — Interactions have different charge and mediator roles:** The three cards organize the Standard Model interactions discussed here. Exchange diagrams are calculation tools for quantum amplitudes, not pictures of classical balls following measurable messenger paths.
**Predict:** Which interaction can change a neutron into a proton in beta decay?
**Check:** The weak interaction. At the quark level a down quark changes to an up quark, with the appropriate emitted leptons.

### Testing reactions and models
Check electric charge, energy, momentum, angular momentum, and the relevant particle quantum numbers. Accelerators convert collision energy into other particles, provided conservation laws permit the process. Neutrinos help account for missing energy and momentum in beta decay. The book also discusses grand unification, supersymmetry, and strings; those proposals should be distinguished from the established classification used in this lesson.

**Picture — Centre-of-momentum energy is available for particle creation:** The incoming beams have equal opposite momenta. Their total centre-of-momentum energy can create final rest masses and motion, provided charge and all other applicable conservation laws also balance.
**Predict:** Is sufficient energy alone enough to make any chosen final particles?
**Check:** No. The reaction must also obey momentum, charge, angular momentum, and the relevant particle conservation rules.

### Essential equations
- `q_u = +⅔e; q_d = −⅓e; proton = uud; neutron = udd` — Valence-quark charge accounting; antiquarks carry opposite electric charge.
- `E² = p²c² + m²c⁴; E_CM ≥ Σm_final c²` — The second relation is a necessary energy threshold in the centre-of-momentum frame; other conservation laws must also hold.

### Equation explanations & derivations
Original explanations mapped to the topic scope of the university review. A derivative is an instantaneous rate; an integral adds small contributions. Definitions and physical laws are stated as starting points.

#### Quark charges and particle-production thresholds
**Concept:** Composite-particle charges add. Collision energy available in the centre-of-momentum frame sets a necessary threshold for making massive products.
**Assumptions:** Valence-quark charge accounting; special-relativistic energy and momentum conservation for the complete initial state.
**Picture — Quark charges add to proton and neutron charges:** Each u valence quark carries +⅔e and each d carries −⅓e. Adding the three valence charges gives a proton’s +e and a neutron’s zero. Circles show composition, not fixed quark positions.
**Predict:** What is the charge of an antiproton?
**Check:** −e. Its valence antiquarks have the opposite charges from the proton’s quarks.
1. Use q_u = +⅔e and q_d = −⅓e. A proton uud has charge ⅔e + ⅔e − ⅓e = +e; a neutron udd has charge ⅔e − ⅓e − ⅓e = 0.
2. Antiquarks have opposite charges. These fractions are physical inputs to the quark model, not consequences of the arithmetic.
3. For total initial lab energy E_total and total momentum P_total, the invariant centre-of-momentum energy obeys E_CM² = E_total² − c²|P_total|².
4. At the ideal threshold, final particles have no relative kinetic energy in that frame. Therefore E_CM must be at least Σm_final c²; additional conservation laws may forbid a proposed final state.
**Result:** `q_proton = +e; q_neutron = 0; E_CM = √(E_total² − c²|P_total|²) ≥ Σm_final c²`
**Check:** Opposing equal-momentum collider beams have P_total = 0. A fixed-target beam generally spends some lab energy on overall product motion, so lab energy alone is not the available creation energy.
**Scope reference:** [44. Quarks, Leptons, and the Big Bang](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-44)

### Worked example
Use valence quark charges to find the charges of a proton and a neutron.

### Solution
1. Proton uud: +⅔e + ⅔e − ⅓e = +e.
2. Neutron udd: +⅔e − ⅓e − ⅓e = 0.
3. A zero total charge does not mean an object lacks charged constituents.
**Answer:** Proton charge +e; neutron charge 0.

### Common trap
“Elementary” and “small” are different ideas: a proton is very small but has internal quark and gluon structure.

### Self-check
Which particle is a lepton?
- Proton
- Electron
- Neutron
**Answer:** Electron. An electron is elementary in the Standard Model; protons and neutrons are composite baryons.

## 33 Astrophysics & Cosmology
> Connect gravity, spectra, and distance measurements to stars and cosmic expansion.

### Stars and stellar evolution
Gravity compresses stellar matter while pressure supports it. Fusion changes composition and releases energy during major stages of stellar evolution. A star’s mass strongly affects its lifetime and eventual remnant. Spectra reveal composition and motion; surface temperature affects emitted colour, while luminosity measures total emitted power.

**Picture — A steady star balances inward gravity with a pressure gradient:** Blue arrows represent inward gravity. Pressure decreases outward, producing an outward net pressure force on each fluid shell. A star in approximate hydrostatic balance has these effects in equilibrium locally.
**Predict:** Does balance mean gravity has switched off inside a stable star?
**Check:** No. Gravity still acts and is balanced by the pressure gradient. Changes in pressure support can drive contraction or expansion.

### Measuring the universe
Parallax uses the change in a nearby star’s apparent position as Earth orbits. Standard-candle reasoning compares an estimated luminosity with observed flux. Redshift measures fractional wavelength increase. For nearby galaxies, a roughly linear relation between recession speed and distance describes cosmic expansion. The numerical Hubble constant used in the example is an assumed teaching value.

**Picture — Parallax uses a known baseline and a small angular shift:** Two Earth positions give different apparent directions to a nearby star. Annual parallax p is the half-angle relative to the Sun–star line, not the full six-month shift. Angles are greatly exaggerated.
**Predict:** If parallax falls from 0.2 to 0.1 arcsecond, what happens to inferred distance?
**Check:** It doubles, from 5 to 10 parsecs. Smaller parallax means a more distant star.

### Relativity and cosmological models
General relativity describes gravity through spacetime geometry, with light and freely falling objects following paths shaped by that geometry. Expansion, the cosmic microwave background, and light-element abundances support a hot early-universe model. Dark matter describes gravitating matter inferred beyond luminous material; dark energy describes the component associated with accelerated expansion. The chapter provides historical context, not a live survey of current measurements.

**Picture — Expansion stretches wavelengths with the scale factor:** The right wave has a larger wavelength. In the cosmological expansion model, wavelengths stretch with the scale factor between emission and reception. Redshift z measures the fractional change.
**Predict:** If observed wavelength is twice emitted wavelength, is z equal to 1 or 2?
**Check:** z = 1, because z = (2λ − λ)/λ. The wavelength ratio is 1 + z = 2.

### Essential equations
- `F_received = L/(4πd²); d(parsecs) = 1/p(arcseconds)` — Isotropic emission without intervening absorption; stellar parallax p is the annual parallax angle.
- `z = (λ_observed − λ_emitted)/λ_emitted; v ≈ cz; v ≈ H₀d` — The speed approximation is for small redshift; the linear distance law is a nearby-universe approximation.
- `r_s = 2GM/c²` — Schwarzschild radius of a nonrotating, uncharged black hole.

### Equation explanations & derivations
Original explanations mapped to the topic scope of the university review. A derivative is an instantaneous rate; an integral adds small contributions. Definitions and physical laws are stated as starting points.

#### Inverse-square brightness and parallax distance
**Concept:** Luminosity spreads over a growing spherical area. Parallax instead finds distance from a geometric baseline and a small angular shift.
**Assumptions:** Isotropic emission without absorption; source distance much larger than its size. Annual stellar parallax p uses a baseline radius of 1 astronomical unit.
**Picture — The same luminosity spreads over larger spherical areas:** The circles represent cross-sections through spheres centred on an isotropic source. The same luminosity crosses every sphere, but twice the radius gives four times the area. Absorption is neglected.
**Predict:** If the distance triples, what fraction of the original flux reaches each square metre?
**Check:** One ninth, because received flux varies as 1/d² for the same isotropic luminosity.
1. A source with luminosity L sends that power through a sphere of area 4πd², so received flux is F = L/(4πd²).
2. For a small parallax angle, p_radians ≈ 1 AU/d. By definition, 1 parsec is the distance where 1 AU subtends 1 arcsecond.
3. Using the same angular units therefore gives d(parsecs) = 1/p(arcseconds).
**Result:** `F_received = L/(4πd²); d(pc) = 1/p(arcsec)`
**Check:** Doubling distance quarters received flux and halves parallax. Apparent brightness alone cannot give distance unless luminosity is known or estimated.

#### Redshift, Hubble’s law, and an escape-speed analogy
**Concept:** Redshift measures a wavelength ratio. Nearby expansion admits a linear speed–distance approximation; black-hole horizons require general relativity.
**Assumptions:** Small redshift for v ≈ cz; nearby-universe Hubble approximation; a nonrotating uncharged black hole for r_s.
**Picture — Expansion stretches wavelengths with the scale factor:** The right wave has a larger wavelength. In the cosmological expansion model, wavelengths stretch with the scale factor between emission and reception. Redshift z measures the fractional change.
**Predict:** If observed wavelength is twice emitted wavelength, is z equal to 1 or 2?
**Check:** z = 1, because z = (2λ − λ)/λ. The wavelength ratio is 1 + z = 2.
1. Define z = (λ_observed − λ_emitted)/λ_emitted. For small relative recession speeds, the Doppler expansion gives z ≈ v/c, hence v ≈ cz.
2. The observed nearby expansion relation is v ≈ H₀d. Combining the approximations gives d ≈ cz/H₀. This estimates distance only within the approximation’s range.
3. Newtonian escape energy sets ½mv_escape² − GMm/r = 0, giving v_escape = √(2GM/r).
4. Formally setting this Newtonian expression equal to c gives r = 2GM/c². This reproduces the Schwarzschild radius algebraically, but the existence and meaning of an event horizon follow from general relativity.
**Result:** `z = Δλ/λ_emitted; v ≈ cz ≈ H₀d (nearby); r_s = 2GM/c²`
**Check:** H₀ has dimensions inverse time. At large cosmological redshift, interpreting cz as a physical recession speed fails; the simple nearby distance conversion must be replaced.
**Scope reference:** [13. Gravitation](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-13), [44. Quarks, Leptons, and the Big Bang](https://cghuisunshine.github.io/Physics_uni/Physics_Review_and_Summary_Tutorial.html#chapter-44)

### Worked example
For a nearby galaxy with redshift z = 0.0100, estimate distance using c ≈ 3.00 × 10⁵ km/s and an assumed H₀ = 70.0 km/s/Mpc.

### Solution
1. Use the small-redshift approximation v ≈ cz = 3000 km/s.
2. Use the local linear relation d ≈ v/H₀.
3. d ≈ 3000/70.0 = 42.86 Mpc. This is an approximate model calculation.
**Answer:** d ≈ 42.9 Mpc for the stated assumed H₀.

### Common trap
At large cosmological redshift, do not treat v = cz as an exact velocity or d = cz/H₀ as an exact distance.

### Self-check
For an isotropic star with unchanged luminosity, doubling distance makes received flux…
- Twice as large
- Half as large
- One quarter as large
**Answer:** One quarter as large. The same power spreads over a sphere whose area scales as d², so received flux falls by a factor of four.
