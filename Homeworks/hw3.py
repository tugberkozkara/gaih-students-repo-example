#Homework-3
#Course Grade Application
#Create 5 students. Ask these students from the user.
#Each of these students should have a midterm grade, project grade and final grade.
#Each student will have a course passing grade.
#passingGrade = midterm * (0.3) + project * (0.3) + final * (0.4) passing grade should be determined like this.
#Create a dictionary that keeps these students' information.
#Calculate the students' grades and transfer them to the list with the help of indexing.
#Finally, set the students with the highest grade to be in the first index and the student with the lowest grade to be in the last index of the list.

studdict = {}
studlist = []

for i  in range(1,6):
    name, midterm, project, final = input("Enter the Student" + str(i) + "'s name, midterm grade, project and final grade (with spaces between them): ").split()
    passingGrade = int(midterm) * (0.3) + int(project) * (0.3) + int(final) * (0.4)
    studdict['name',i] = name
    studdict['midterm grade' ,i] = midterm
    studdict['project grade',i] = project    
    studdict['final grade',i] = final
    studdict['passing grade',i] = passingGrade
    studlist.append([passingGrade, name])
    i += 1

#print(studdict)
studlist.sort(reverse=True)
print(studlist)

#because of my being late, couldn't send the quiz4 :(
