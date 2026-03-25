# Student Grade Analysis

### Objective

The goal of this project is to analyze student performance based on their scores in three subjects. The program calculates each student’s average score, assigns grades, identifies the top-performing student, and provides various statistical insights about the class.

### Tools Used

* Python
* Pandas
* Matplotlib

### Features

1. **Load Dataset**: Reads a CSV file containing student names and their scores in Math, English, and Science.
2. **Calculate Averages**: Computes the average score for each student across the three subjects.
3. **Assign Grades**: Grades are assigned based on the average score:
   * A: 85 and above
   * B: 70–84
   * C: 55–69
   * D: Below 55
4. **Rank Students**: Students are ranked based on their average score.
5. **Identify Top Student**: Displays the student with the highest average.
6. **Top 5 Students**: Lists the top five students in descending order of their averages.
7. **Subject Toppers**: Identifies the highest scorer in each subject.
8. **Class Statistics**: Provides summary statistics for each subject and overall averages.
9. **Grade Distribution**: Counts and visualizes the number of students in each grade.
10. **Visualizations**:
    * Bar chart showing average marks per subject.
    * Histogram showing distribution of student averages.
    * Pie chart showing grade distribution.


### Key Concepts

* DataFrames
* mean()
* max()
* rank()
* value_counts()
* Matplotlib plotting (bar, histogram, pie chart)
