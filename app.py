from flask import Flask, render_template

app = Flask(__name__,static_folder="static")

@app.route('/')
def index():
	contactInfo = { "Type": 1,
					"Title": "Contact Information",
					"images": ["images/email.png", "images/in.png"],
					"subTitle": ["Email", "LinkedIn"],
					"subDescription": ["Yaxin.Cheng@Dal.ca", "Yaxin Cheng"],
					"buttonTitle": ["Email Me", "Go Check"],
					"buttonLink": ["mailto:Yaxin.Cheng@Dal.ca?subject=Job Opportunity", "https://ca.linkedin.com/in/yaxincheng"]}
	introduction = {"Type": 0, "Title": "Introduction", "Description":
				"""✪ My Name: <a>Yaxin Cheng</a><br>
                ✪ An international student taking Computer Science at Dalhousie University<br>
                ✪ Habit: Coding &amp; Game of Thrones<br>
                ✪ Originally from Sichuan, a south-western province in China. Just remember, we have panda bears and we love spicy food<br>
                ✪ Recent update: I got a job at <a href="http://www.greenpowerlabs.com">Green Power Labs</a><br>
                ✪ Don't ask me if I wanna stay in Canada after graduation. I do""",
                "Image": False, 
                "MoreButton": True, 
                "ButtonOptions": ["This guy is cool!", "He is not cool..."], 
                "ButtonEnable": [True, False]}
	return render_template('overview.html', Information = [introduction, contactInfo])

if __name__ == "__main__":
	app.run()
