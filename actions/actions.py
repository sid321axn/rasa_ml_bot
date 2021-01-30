from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import json

class ActionSearchResult(Action):
	def name(self):
		return "action_result"
		
	def run(self, dispatcher, tracker, domain):
		item = tracker.get_slot('item')
		item = item.lower()
		
		
		if item =="book":
			dispatcher.utter_message("These are top 5 books that you should follow for machine learning- \n 1.[The Hundred-Page Machine Learning Book](https://www.amazon.in/Hundred-Page-Machine-Learning-Book/dp/1999579542/ref=sr_1_3?crid=2496N4X3IKOPH&dchild=1&keywords=best+machine+learning+books&qid=1610976961&sprefix=best+machine+%2Caps%2C325&sr=8-3) by Andriy Burkov  \n 2.[Machine Learning For Absolute Beginners](https://www.amazon.in/Machine-Learning-Absolute-Beginners-Introduction-ebook/dp/B07335JNW1/ref=sr_1_8?crid=2496N4X3IKOPH&dchild=1&keywords=best+machine+learning+books&qid=1610976961&sprefix=best+machine+%2Caps%2C325&sr=8-8) by Oliver Theobald  \n 3.[Approaching (Almost) Any Machine Learning Problem](https://www.amazon.in/Approaching-Almost-Machine-Learning-Problem-ebook/dp/B089P13QHT/ref=sr_1_2?crid=34SPFM2QIC5YX&dchild=1&keywords=approaching+almost+any+machine+learning+problem&qid=1610977145&sprefix=approaching%2Caps%2C326&sr=8-2) by Abhishek thakur  \n 4.[Hands-On Machine Learning with Scikit-Learn, Keras and Tensor Flow](https://www.amazon.in/Hands-Machine-Learning-Scikit-Learn-Tensor/dp/9352139054/ref=sr_1_1?crid=2496N4X3IKOPH&dchild=1&keywords=best+machine+learning+books&qid=1610977180&sprefix=best+machine+%2Caps%2C325&sr=8-1) by Aurelien Geron  \n 5.[Pattern Recognition and Machine Learning (Information Science and Statistics)](https://www.amazon.in/Pattern-Recognition-Learning-Information-Statistics/dp/0387310738/ref=sr_1_7?crid=2496N4X3IKOPH&dchild=1&keywords=best+machine+learning+books&qid=1610977180&sprefix=best+machine+%2Caps%2C325&sr=8-7) by Christopher M. Bishop ")
		elif item =="course":
			dispatcher.utter_message("The top 5 machine learning courses that you should follow are- \n 1. [Machine Learning by Stanford University (Coursera)](https://www.coursera.org/learn/machine-learning) \n 2. [Machine Learning with Python by IBM (Coursera)](https://www.coursera.org/learn/machine-learning-with-python) \n 3. [Machine Learning Specialization by University of Washington (Coursera)](https://www.coursera.org/specializations/machine-learning) \n 4. [Machine Learning A-Z Hands-On Python & R In Data Science (Udemy)](https://www.udemy.com/course/machinelearning/) \n 5. [Machine Learning by HarvardX (edX)](https://www.edx.org/course/data-science-machine-learning) \n")
		elif item =="skill":
			dispatcher.utter_message("A __Machine Learning Engineer__ must have following skills- \n 1. Expertise in languages like Python/C++/R/Java. \n 2. Probability and statistics.\n 3. Data modelling and Evaluation. \n 4. Machine learning Algorithms. \n 5. Advanced Signal Processing Techniques. \n 6. Distributed Computing. \n Apart from that following are prerequisites- \n 1. Linear Algebra. \n 2. Programming knowledge. \n 3. Calculus.")

class ActionGenMLQuery(Action):
    def name(self):
        return "action_genml_query"

    def run(self,dispatcher,tracker,domain):
        intent = tracker.latest_message["intent"].get("name")

        

        if intent in ["ml_query"]:
            message = {
                "type": "video",
                "payload": {
                    "title": "Machine Learning Video",
                    "src": "https://www.youtube.com/embed/9Ay4u7OYOhA",
                },
            }
            dispatcher.utter_message(
                text="Machine learning is an application of artificial intelligence (AI) that provides systems the ability to automatically learn and improve from experience without being explicitly programmed. \nMachine learning focuses on the development of computer programs that can access data and use it to learn for themselves.",
                attachment=message,
            )
        elif intent in ["dl_query"]:
            message = {
                "type": "video",
                "payload": {
                    "title": "Deep Learning Video",
                    "src": "https://www.youtube.com/embed/6M5VXKLf4D4",
                },
            }
            dispatcher.utter_message(
                text="Deep learning is the subset of machine learning. Deep learning works with artificial neural networks, which are designed to imitate how humans think and learn. \nUntil recently, neural networks were limited by computing power and thus were limited in complexity. \nHowever, advancements in Big Data analytics have permitted larger, sophisticated neural networks, allowing computers to observe, learn, and react to complex situations faster than humans. Deep learning has aided image classification, language translation, speech recognition. \nIt can be used to solve any pattern recognition problem and without human intervention.\nYou can watch above video to understand basics of deep learning.\n",
                attachment=message,
            )
        return []