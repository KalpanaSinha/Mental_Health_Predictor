

sugg1 = """
<strong>Value yourself:</strong> 
<ol>
	<li>Treat yourself with kindness and respect, and avoid self-criticism. </li>
	<li>Make time for your hobbies. Do plant a garden, take dance lessons.</li>
	<li>Learn to play an instrument and spread happiness.</li>
</ol>"""

sugg2 = """
<strong>Take care of your body.Taking care of yourself physically can improve your mental health. Be sure to:</strong> 
<ol>
	<li>Eat nutritious meals </li>
	<li>Avoid smoking and vaping</li>
	<li>Drink plenty of water</li>
	<li>Exercise, which helps decrease depression and anxiety. </li>
	<li>Get enough sleep, as lack of sleep contributes to a high rate of depression.</li>
</ol>"""

sugg3 = """
<strong>Surround yourself with good people:</strong> 
<ol>
	<li>Eat nutritious meals </li>
	<li>People with strong family or social connections are generally healthier than those who lack a support network.</li>
	<li>Make plans with supportive family members and friends, or seek out activities where you can meet new people, </li>
	<li>People with strong family or social connections are generally healthier than those who lack a support network, ;such as a club, class or support group. </li>
</ol>"""

sugg4 = """
<strong>Give yourself time:</strong> 
<ol>
	<li>Volunteer your time and energy to help someone else.  </li>
	<li>You'll feel good about doing something tangible to help someone in need — and it's a great way to meet new people.</li>
</ol>"""

sugg5 = """
<strong> Learn how to deal with stress:</strong> 
<ol>
	<li>Like it or not, stress is a part of life.  </li>
	<li>Practice good coping skills.</li>
	<li>Try One-Minute Stress Strategies, do Tai Chi, exercise, take a nature walk, play with your pet or try journal writing as a stress reducer.  </li>
	<li>Also, remember to smile and see the humor in life.  </li>
</ol>"""


sugg6 = """
<strong> Quiet your mind:</strong> 
<ol>
	<li>Try meditating, Mindfulness and/or prayer.  </li>
	<li>Relaxation exercises and prayer can improve your state of mind and outlook on life.</li>
	<li>meditation may help you feel calm and enhance the effects of therapy.  </li>
</ol>"""

sugg7 = """
<strong> Set realistic goals:</strong> 
<ol>
	<li>Decide what you want to achieve academically, professionally and personally, and write down the steps you need to realize your goals. </li>
	<li>Aim high, but be realistic and don't over-schedule. </li>
	<li>You'll enjoy a tremendous sense of accomplishment and self-worth as you progress toward your goal.  </li>
</ol>"""

sugg8 = """
<strong>Break up the monotony:</strong> 
<ol>
	<li>Although our routines make us more efficient and enhance our feelings of security and safety, a little change of pace can perk up a tedious schedule.</li>
	<li>Alter your jogging route, plan a road-trip, take a walk in a different park, hang some new pictures or try a new restaurant </li>
</ol>"""

sugg9 = """
<strong>Avoid alcohol and other drugs:</strong> 
<ol>
	<li>Keep alcohol use to a minimum and avoid other drugs.</li>
	<li>Sometimes people use alcohol and other drugs to "self-medicate" but in reality, alcohol and other drugs only aggravate problems.  </li>
</ol>"""

sugg10 = """
<strong> Get help when you need it:</strong> 
<ol>
	<li>Seeking help is a sign of strength — not a weakness. </li>
	<li>And,it is important to remember that treatment is effective.</li>
	<li>People who get appropriate care can recover from mental illness and addiction and lead full, rewarding lives.</li>
</ol>"""

import random

def suggestion(age):
	print(type(sugg1))
	rand = random.randint(1, 10) 
	if rand == 1:
		return sugg1
	elif rand == 2:
		return sugg2
	elif rand == 3:
		return sugg3
	elif rand == 4:
		return sugg4
	elif rand == 5:
		return sugg5
	elif rand == 6:
		return sugg6
	elif rand == 7:
		return sugg7
	elif rand == 8:
		return sugg8
	elif rand == 9:
		return sugg9
	else:
		return sugg10