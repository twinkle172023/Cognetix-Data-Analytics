# Student Performance Analysis

## Cognetix Technology — Data Analyst Internship

### Project 2 — Level 1

## 1. Project Overview

This project analyzes student academic performance using the **Students Performance in Exams** dataset. The analysis focuses on Mathematics, Reading, and Writing scores to calculate subject-wise averages, identify the top-performing students, validate the dataset, and visualize performance patterns.

The project demonstrates the use of Python, Pandas, and Matplotlib for basic data analysis and visualization.

---

## 2. Objective

The main objectives of this project are:

- Load and analyze student performance data using Pandas.
- Calculate average marks for Mathematics, Reading, and Writing.
- Identify the top 5 performing student records based on overall average score.
- Validate the dataset for missing and negative marks.
- Analyze score distributions.
- Compare academic performance based on test preparation.
- Generate clear visualizations and derive meaningful insights.

---

## 3. Dataset

**Dataset:** Students Performance in Exams

**Source:** Kaggle — Students Performance in Exams

**Dataset Size:**
- 1,000 student records
- 8 attributes

### Dataset Attributes

| Attribute | Description |
|---|---|
| `gender` | Student gender |
| `race/ethnicity` | Student group |
| `parental level of education` | Parent's education level |
| `lunch` | Type of lunch program |
| `test preparation course` | Test preparation status |
| `math score` | Mathematics score |
| `reading score` | Reading score |
| `writing score` | Writing score |

---

## 4. Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## 5. Data Validation

The dataset was validated before performing the analysis.

| Validation Check | Result |
|---|---:|
| Total Records | 1,000 |
| Missing Math Scores | 0 |
| Missing Reading Scores | 0 |
| Missing Writing Scores | 0 |
| Negative Scores | 0 |
| Scores Outside 0–100 | 0 |
| Duplicate Rows | 0 |

The dataset passed all required validation checks.

---

## 6. Subject-wise Performance

| Subject | Average Score |
|---|---:|
| Mathematics | 66.09 |
| Reading | 69.17 |
| Writing | 68.05 |

**Reading** achieved the highest average score, while **Mathematics** had the lowest average score.

---

## 7. Top 5 Performing Students

Students were ranked using the average of their Mathematics, Reading, and Writing scores.

| Rank | Dataset Index | Gender | Group | Math | Reading | Writing | Overall Average |
|---:|---:|---|---|---:|---:|---:|---:|
| 1 | 916 | Male | E | 100 | 100 | 100 | 100.00 |
| 2 | 962 | Female | E | 100 | 100 | 100 | 100.00 |
| 3 | 458 | Female | E | 100 | 100 | 100 | 100.00 |
| 4 | 114 | Female | E | 99 | 100 | 100 | 99.67 |
| 5 | 712 | Female | D | 98 | 100 | 99 | 99.00 |

Since the dataset does not contain student names or unique student IDs, the original dataset index is used to identify the records.

---

## 8. Test Preparation Analysis

A comparison was performed between students who completed the test preparation course and those who did not.

| Test Preparation | Students | Math | Reading | Writing |
|---|---:|---:|---:|---:|
| Completed | 358 | 69.70 | 73.89 | 74.42 |
| None | 642 | 64.08 | 66.53 | 64.50 |

Students who completed the test preparation course achieved higher average scores across all three subjects.

---

## 9. Visualizations

The project includes the following visualizations:

1. **Average Score by Subject**
   - Compares average Mathematics, Reading, and Writing scores.

2. **Top 5 Students by Overall Average**
   - Displays the highest-performing student records.

3. **Distribution of Student Scores**
   - Shows the score distribution across the three subjects.

4. **Average Scores by Test Preparation Course**
   - Compares subject performance between students who completed and did not complete the preparation course.

5. **Distribution of Overall Student Scores**
   - Shows the distribution of students based on their overall average score.

All visualization files are available in the `visuals/` directory.

---

## 10. Key Insights

- Reading recorded the highest subject average at **69.17**.
- Mathematics recorded the lowest subject average at **66.09**.
- Three students achieved a perfect overall average of **100.00**.
- Students who completed the test preparation course performed better across Mathematics, Reading, and Writing.
- **358 students** completed the preparation course, while **642 students** did not.
- Most overall student scores are concentrated in the middle-to-upper score range.
- Four of the five top-performing records belong to **Group E**.

---

## 11. Recommendations

- Provide additional academic support and practice resources for Mathematics.
- Encourage students to complete available test preparation programs.
- Continue effective learning strategies for Reading and Writing.
- Identify students with lower overall averages and provide targeted academic support.
- Monitor subject-wise and overall performance regularly to identify changes in student outcomes.

---

## 12. Project Structure

```text
Project-2-Student-Performance/
│
├── data/
│   └── StudentsPerformance.csv
│
├── notebooks/
│   └── student_performance_analysis.ipynb
│
├── visuals/
│   ├── average_subject_scores.png
│   ├── top_5_students.png
│   ├── score_distribution.png
│   ├── test_preparation_performance.png
│   └── overall_score_distribution.png
│
└── README.md
```

---

## 13. Conclusion

The Student Performance Analysis successfully analyzed 1,000 student records using Python and Pandas. The dataset was validated for missing values, negative marks, invalid scores, and duplicate records, with no data quality issues identified.

The analysis showed that Reading had the highest average score, while Mathematics had the lowest. The project also identified the top five performing student records using their overall average across the three subjects.

The comparison of test preparation groups showed that students who completed the preparation course achieved higher average scores in all three subjects. The visualizations further helped identify subject-wise performance patterns, score distributions, top performers, and differences associated with test preparation.

This project demonstrates a complete basic data analysis workflow involving data validation, statistical analysis, visualization, and interpretation of academic performance data.