#I'm making a list of my professional goals.
goal_certifications = ["Linux+", "AWS Certified Solutions Architect", 
                       "Certified Kubernetes Administrator",
                       "Comptia Security+", 
                       "Robotics Process Automation (RPA) Certification"
                       ]
print("My professional goals are: ", goal_certifications)

# I want to add a new certification to my list of goals.
other_certifications = input("What other certifications do you want to achieve? ")
goal_certifications.append(other_certifications)
print("I've added a new certification to your goals: ", goal_certifications)