from flask import Flask, render_template, request
# some_file.py
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'C:/Users/ASUS/Desktop/my_test')

from my_test import test_model


contexts= ['Building construction is the process of adding structure to real property or construction of buildings. The majority of building construction jobs are small renovations, such as addition of a room, or renovation of a bathroom. Often, the owner of the property acts as laborer, paymaster, and design team for the entire project. Although building construction projects typically include various common elements, such as design, financial, estimating and legal considerations, many projects of varying sizes reach undesirable end results, such as structural collapse, cost overruns, and/or litigation. For this reason, those with experience in the field make detailed plans and maintain careful oversight during the project to ensure a positive outcome.','According to PolitiFact the top 400 richest Americans "have more wealth than half of all Americans combined." According to the New York Times on July 22, 2014, the "richest 1 percent in the United States now own more wealth than the bottom 90 percent". Inherited wealth may help explain why many Americans who have become rich may have had a "substantial head start". In September 2012, according to the Institute for Policy Studies, "over 60 percent" of the Forbes richest 400 Americans "grew up in substantial privilege".','Newton s First Law of Motion states that objects continue to move in a state of constant velocity unless acted upon by an external net force or resultant force. This law is an extension of Galileo s insight that constant velocity was associated with a lack of net force (see a more detailed description of this below). Newton proposed that every object with mass has an innate inertia that functions as the fundamental equilibrium "natural state" in place of the Aristotelian idea of the "natural state of rest". That is, the first law contradicts the intuitive Aristotelian belief that a net force is required to keep an object moving with constant velocity. By making rest physically indistinguishable from non-zero constant velocity, Newton s First Law directly connects inertia with the concept of relative velocities. Specifically, in systems where objects are moving with different velocities, it is impossible to determine which object is "in motion" and which object is "at rest". In other words, to phrase matters more technically, the laws of physics are the same in every inertial frame of reference, that is, in all frames related by a Galilean transformation.','Forces act in a particular direction and have sizes dependent upon how strong the push or pull is. Because of these characteristics, forces are classified as "vector quantities". This means that forces follow a different set of mathematical rules than physical quantities that do not have direction (denoted scalar quantities). For example, when determining what happens when two forces act on the same object, it is necessary to know both the magnitude and the direction of both forces to calculate the result. If both of these pieces of information are not known for each force, the situation is ambiguous. For example, if you know that two people are pulling on the same rope with known magnitudes of force but you do not know which direction either person is pulling, it is impossible to determine what the acceleration of the rope will be. The two people could be pulling against each other as in tug of war or the two people could be pulling in the same direction. In this simple one-dimensional example, without knowing the direction of the forces it is impossible to decide whether the net force is the result of adding the two force magnitudes or subtracting one from the other. Associating forces with vectors avoids such problems.','There is evidence that there have been significant changes in Amazon rainforest vegetation over the last 21,000 years through the Last Glacial Maximum (LGM) and subsequent deglaciation. Analyses of sediment deposits from Amazon basin paleolakes and from the Amazon Fan indicate that rainfall in the basin during the LGM was lower than for the present, and this was almost certainly associated with reduced moist tropical vegetation cover in the basin. There is debate, however, over how extensive this reduction was. Some scientists argue that the rainforest was reduced to small, isolated refugia separated by open forest and grassland; other scientists argue that the rainforest remained largely intact but extended less far to the north, south, and east than is seen today. This debate has proved difficult to resolve because the practical limitations of working in the rainforest mean that data sampling is biased away from the center of the Amazon basin, and both explanations are reasonably well supported by the available data.','Oxygen is a chemical element with symbol O and atomic number 8. It is a member of the chalcogen group on the periodic table and is a highly reactive nonmetal and oxidizing agent that readily forms compounds (notably oxides) with most elements. By mass, oxygen is the third-most abundant element in the universe, after hydrogen and helium. At standard temperature and pressure, two atoms of the element bind to form dioxygen, a colorless and odorless diatomic gas with the formula O2. Diatomic oxygen gas constitutes 20.8% of the Earth s atmosphere. However, monitoring of atmospheric oxygen levels show a global downward trend, because of fossil-fuel burning. Oxygen is the most abundant element by mass in the Earth s crust as part of oxide compounds such as silicon dioxide, making up almost half of the crust s mass.','The role of teacher is often formal and ongoing, carried out at a school or other place of formal education. In many countries, a person who wishes to become a teacher must first obtain specified professional qualifications or credentials from a university or college. These professional qualifications may include the study of pedagogy, the science of teaching. Teachers, like other professionals, may have to continue their education after they qualify, a process known as continuing professional development. Teachers may use a lesson plan to facilitate student learning, providing a course of study which is called the curriculum.','Martin Luther was born to Hans Luder (or Ludher, later Luther) and his wife Margarethe (née Lindemann) on 10 November 1483 in Eisleben, Saxony, then part of the Holy Roman Empire. He was baptized as a Catholic the next morning on the feast day of St. Martin of Tours. His family moved to Mansfeld in 1484, where his father was a leaseholder of copper mines and smelters and served as one of four citizen representatives on the local council. The religious scholar Martin Marty describes Luther s mother as a hard-working woman of "trading-class stock and middling means" and notes that Luther s enemies later wrongly described her as a whore and bath attendant. He had several brothers and sisters, and is known to have been close to one of them, Jacob. Hans Luther was ambitious for himself and his family, and he was determined to see Martin, his eldest son, become a lawyer. He sent Martin to Latin schools in Mansfeld, then Magdeburg in 1497, where he attended a school operated by a lay group called the Brethren of the Common Life, and Eisenach in 1498. The three schools focused on the so-called "trivium": grammar, rhetoric, and logic. Luther later compared his education there to purgatory and hell.','The French and Indian War (1754–1763) was the North American theater of the worldwide Seven Years War. The war was fought between the colonies of British America and New France, with both sides supported by military units from their parent countries of Great Britain and France, as well as Native American allies. At the start of the war, the French North American colonies had a population of roughly 60,000 European settlers, compared with 2 million in the British North American colonies. The outnumbered French particularly depended on the Indians. Long in conflict, the metropole nations declared war on each other in 1756, escalating the war from a regional affair into an intercontinental conflict.']




app= Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():

	if request.method == 'POST':
		context= request.form['context']
		question= request.form['question']
		print(context)
		print(question)
		dict = test_model([question], context)
		for el in dict:
			print(el, dict[el])
	return render_template('index.html', contexts=contexts , len=len(contexts))

