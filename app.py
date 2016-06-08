from flask import Flask, render_template

app = Flask(__name__, static_folder="static")


@app.route('/')
def index():
    coop = {"Type": 0, "Title": "Co-op Status", "Description":
            """✪ Hired by Green Power Labs for a 4-month Co-op position<br>
                ✪ Have completed four of eight academic terms in May 2016<br>
                ✪ Will be available for the second Co-op term in January 2017<br>
                ✪ Will have finished one Co-op term and five of eight academic terms""",
            "Image": False,
            "MoreButton": False,
            "BottomAction": True,
            "BottomActionName": "Find More About My Education",
            "BottomFunction": "/Education"
            }
    contactInfo = {"Type": 1,
                   "Title": "Contact Information",
                   "images": ["images/email.png", "images/in.png", "images/git.png"],
                   "subTitle": ["Email", "LinkedIn", "GitHub"],
                   "subDescription": ["Yaxin.Cheng@Dal.ca", "Yaxin Cheng", "Yaxin Cheng(WatashiJ)"],
                   "buttonTitle": ["Email Me", "Go Check", "Have a look"],
                   "buttonLink": ["mailto:Yaxin.Cheng@Dal.ca?subject=JobOpportunity", "https://ca.linkedin.com/in/yaxincheng", "https://github.com/WatashiJ"],
                   "BottomAction": True,
                   "BottomActionName": "Find More Connections",
                   "BottomFunction": "/Contact"}
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
    return render_template('overview.html', Subject="overview",  Information=[introduction, contactInfo, coop])


@app.route('/Education')
def education():
    NonTech = {"Type": 0, "Title": "Non-Technical Skills", "Description": """✪ Communication: Fluently and properly 
				communicate with people in both written and oral English.<br>
                ✪ Self-motivated: Learned iOS, Python, and Machine Learning independently<br>
                ✪ Time Management: Able to finish projects and assignments before deadlines<br>
                ✪ Team player: Work coherently and efficiently with team members. Good at discovering strength of 
                members and assigning related tasks to them as a team leader"""}
    Other = {"Type": 0, "Title": "Other Techniques", "Description": """✪ Matlab: Used for Machine Learning computing mostly<br>
                ✪ Familiar with design patterns of software<br>
                ✪ Agile development experience<br>
                ✪ Source Control: Git, SVN<br>
                ✪ Microsoft Office: PowerPoint, Word, and Excel"""}
    ML = {"Type": 0, "Title": "Machine Learning", "Description": """✪ This is the area I am still digging, and taking a course for more knowledge about it<br>
                ✪ Some familiarity with supervised and unsupervised learning<br>
                ✪ Understand map-reduce and photo OCR algorithm""", "Image": True, "ImageSource": "images/ml.png"}
    DB = {"Type": 0, "Title": "Database", "Description": """✪ MySQL & SQLite & CoreData & Firebase DB == SQL + NoSQL<br>
	✪ Database building and manipulations at iOS and Flask Python<br> 
                ✪ Familiar with the relational algebra""", "Image": True, "ImageSource": "images/mysql.png"}
    C = {"Type": 0, "Title": "C", "Description": """✪ Familiar with C grammars and experienced with C programming<br>
                ✪ Proficient in memory allocation and pointer manipulations""", "Image": True, "ImageSource": "images/C.png",
         "MoreButton": False, "BottomAction": False}
    Java = {"Type": 0, "Title": "Java", "Description": """
			✪ Have been using Java for more than 2 years for assignments, school projects, and personal projects<br>
                ✪ Familiar with JCF, various of data structures, and sorting algorithms<br>
                ✪ Understand JVM and garbage collection<br>✪ Web Development with Vaadin Framework
			""", "Image": True, "ImageSource": "images/java.png", "MoreButton": False,
            "BottomAction": True, "BottomActionName": "Related Projects", "BottomFunction": "https://github.com/WatashiJ/elmLibrary"}
    Python = {"Type": 0, "Title": "Python", "Description": """
				✪ Flask Web Backend<br>
				✪ Web crawlers<br>
                ✪ Matrix computations<br>
                ✪ Statistics computations<br> By the way, this web page is generated by Flask Python""",
              "Image": True, "ImageSource": "images/python.png", "MoreButton": False, "BottomAction": True,
              "BottomActionName": "Related Projects", "BottomFunction": "https://github.com/WatashiJ/Course-Spider"}
    iOS = {"Type": 0, "Title": "iOS Development", "Description": """✪ Swift + Objective-C<br>
                ✪ UIKit, Foundation<br>
                ✪ CoreData<br>
                ✪ Storyboard + AutoLayout<br>
                ✪ KVC, KVO<br>
                ✪ MVC<br>""", "Image": True, "ImageSource": "images/xcode.png", "MoreButton": False, "BottomAction": True,
           "BottomActionName": "Related Projects", "BottomFunction": "/Projects"}
    general = {"Type": 1, "Title": "Bachelor Of Computer Science",
               "images": ["images/dal.png", "images/date.png", "images/process.png"],
               "subTitle": ["Dalhousie University", "Duration", "Courses Process"],
               "subDescription": ["""6050 University Ave.<br>
                  Halifax, Nova Scotia, Canada""", "Jan 2015 - Present", """Have finished 20 out of 40 courses at Dalhousie University <a>May 2016</a><br>
                  Expected graduate date: <a>August 2018</a><br>"""],
               "buttonTitle": ["Have a look", "Check my projects"],
               "buttonLink": ["http://www.dal.ca", "/Projects"],
               "BottomAction": False}

    return render_template('overview.html', Subject="education", Information=[general, iOS, Python, Java, C, DB, ML, Other, NonTech])


@app.route('/Projects')
def projects():
    courseSpider = {"Type": 0, "Title": """Course Spider(2016)<h5><font color="grey">Personal Project</font></h5>""",
                    "Description": """✪ Started from the desire to build a course selecting App, web crawler may be the most convinient way to get data<br>
                ✪ Analyzed the web API of Dalhousie University, and built a simple demo to parse all information<br>
                ✪ Implemented a Python package: BeautifulSoup, to parse the html file returned by the server<br>
                ✪ Built the DalCourse class to store processed data, and encapsulated crawler functions to CourseSpider class<br>
                ✪ Installed Flask micro-framework, and built RESTful APIs to open the crawler to other users<br>
                ✪ Host the program on Heroku (https://course-spider.herokuapp.com), and wrote documentations""",
                    "Image": True, "ImageSource": "images/spider.png", "BottomAction": True, "BottomActionName": "Give it a try",
                    "BottomFunction": "https://github.com/WatashiJ/Course-Spider"}
    elm = {"Type": 0, "Title": """Elm Library(2016)<h5><font color="grey">Group Project</font></h5>""",
               "Description": """✪ Analyzed the requirements and established 17 user stories to negotiate with the client<br>
                ✪ Grouped the uesr stories into 3 iterations so that the final goal can be reached iteratively<br>
                ✪ Broke tasks and assigned to each team-mate through communications<br>
                ✪ Doing pair programming to keep the app as a team property<br>
                ✪ Build unit test before coding to ensure the code quality (TDD)<br>
                ✪ Followed the MVC structure to separate the logic and representation which ensures the code reuse<br>
                ✪ Applied SVN to keep the continuous integrity (Now on Github)<br>
                ✪ Refactoring code at the begining of each iteration to optimize the readability and extensibility<br>""",
               "Image": True, "ImageSource": "images/elm.png", "BottomAction": True,
               "BottomActionName": "Check on github", "BottomFunction": "https://github.com/WatashiJ/elmLibrary#elmlibrary"}
    iMoney = {"Type": 0, "Title": """iMoney(2016)<h5><font color="grey">Personal Project</font></h5>""",
                  "Description": """✪ Analyzed and categorized classes by drawing UML diagrams at the beginning<br>
                ✪ Applied open-sourced libraries to optimize the user experience<br>
                ✪ Stored and secured users’ records by CoreData database technique<br>
                ✪ Built the program structure with MVC architecture which enables the readability and reusability of code<br>
                ✪ Added iCloud support for users’ records to keep data synchronized and secured<br>
                ✪ Implemented animations with CoreAnimation APIs to polish the user interface<br>
                ✪ Deployed Git to backup each version in order to keep the code integrity""",
                  "Image": True, "ImageSource": "images/imoney.png", "BottomAction": True, "BottomActionName": "Check On Github",
                  "BottomFunction": "https://github.com/WatashiJ/iMoney"}
    ApartmentSearch = {"Type": 0, "Title": """Apartment Prices Checking System for Halifax
	(2015)<h5><font color="grey">Group Project</font></h5>""", "Description": """✪ Analyzed and divided requirements into tasks
	 in order to establish a features list<br>
                ✪ Utilized ER diagrams to determine the relations and framework of the program<br>
                ✪ Assigned tasks to teammates based on their skill levels and experience, so that the whole team can
                 run efficiently and coherently<br>
                ✪ Designed a relational database by MySQL which stores the house pricing information of Halifax<br>
                ✪ Programmed a Python web crawler which downloads the information of house pricing from the Internet<br>
                ✪ Consulted and pair programmed with the team member who was working on the web part to connect the backend (database) 
                to the frontend (Web Interface)"""}
    return render_template('overview.html', Subject="projects", Information=[courseSpider, elm, iMoney, ApartmentSearch])


@app.route('/Experience')
def experience():
    GPL = {"Type": 0, "Title": """Green Power Labs.Inc<h5><font color="grey">Junior Programmer, Buildings(May 2016 - Aug 2016)</font>""",
            "Description": """✪ Read and analyzed APIs from building control companies<br>
            ✪ Built adapters to bridging from Predictive Building Control(PBC) system to buildings by Java based on the APIs<br>
            ✪ Ensured the communications between PBC and buildings by doing regular maintenance<br>
            ✪ Wrote documents and records about new functions added and modifications made during development<br>
            ✪ Doing researches about dashboard interface, and may involve in the development of a dashboard""",
            "Image": True, "ImageSource": "images/gpl.png", "BottomAction": True, "BottomActionName": "Check GPL", 
            "BottomFunction": "http://www.greenpowerlabs.com"}
    IC = {"Type": 0, "Title": """Dalhousie International Centre<h5><font color="grey">Student Coordinator(Jul 2015 &amp; Jan 2016)</font>""",
          "Description": """✪ Registered new students for the orientation by corresponding with them<br>
                ✪ Picked up new students, and directed them to their accommondations in order to ensure that their arrive on campus safely<br>
                ✪ Arranged meeting rooms during the orientation day to provide new students a welcoming space<br>
                ✪ Conducted campus orientation as well as answered student questions in order to introduce the campus life to the students""",
          "Image": False}
    Buskers = {"Type": 0, "Title": """Halifax Buskers' Festival<h5><font color="grey">Stage Manager and Program Seller(Oct 2015)</font></h5>""",
               "Description": """✪ Ensured the artists' performances by keeping stage clear and helping to install their equipment<br>
                ✪ Balanced the budget for the organizer by selling the programs<br>
                ✪ Promoted the festival by introducing features and highlights<br>
                ✪ Maintained the order by organizing people to stay in certain areas<br>
                ✪ Ensured the public security by reporting lost children and dangerous behaviours""", "Image": True,
               "ImageSource": "images/hbf.png"}
    return render_template('overview.html', Subject="experience", Information=[GPL, IC, Buskers])


@app.route('/Contact')
def contact():
    Contact = {"Type": 1, "Title": "Contact Information", "images":
               ["images/email.png", "images/phone.png", "images/git.png", "images/in.png"], "subTitle":
               ["Email", "Phone", "GitHub", "LinkedIn"], "subDescription": ["Yaxin.Cheng@Dal.ca", "(902)877-9707", "Yaxin Cheng (WatashiJ)", "Yaxin Cheng on LinkedIn"],
               "buttonTitle": ["Email me", "", "Have a look", "Go check"],
               "buttonLink": ["mailto:Yaxin.Cheng@Dal.ca?subject=JobOpportunity", "", "https://github.com/WatashiJ", "https://ca.linkedin.com/in/yaxincheng"]}
    return render_template('overview.html', Subject="contact", Information=[Contact])

if __name__ == "__main__":
    app.run()
