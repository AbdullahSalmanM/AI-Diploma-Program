# AIAT 115 - Scalable Data Science | علم البيانات القابل للتوسع

## 🚀 NEW STUDENTS: START HERE! | الطلاب الجدد: ابدأ من هنا!

**👉 If you're a new student, read `START_HERE.md` FIRST!**  
**👉 إذا كنت طالباً جديداً، اقرأ `START_HERE.md` أولاً!**

The `START_HERE.md` file contains:
- ✅ Day 1 setup instructions
- ✅ Step-by-step installation guide
- ✅ Learning sequence
- ✅ Progress tracker
- ✅ Troubleshooting tips

**Don't skip it!** It will save you time and confusion.

---

## Course Overview | نظرة عامة على الدورة

This course provides comprehensive training in scalable data science techniques using Python and NVIDIA RAPIDS. Students will learn to process, clean, visualize, and model data at scale through hands-on coding examples and exercises.

**Course Code:** AIAT 115  
**Language:** Bilingual (Arabic/English)
**Credit Hours:** 4  
**Lecture Hours:** 2  
**Practical Hours:** 4  
**Total Hours:** 64 (32 theoretical + 32 practical)

**Unit Breakdown:**
- Unit 1: 6 theoretical + 6 practical = 12 hours
- Unit 2: 6 theoretical + 6 practical = 12 hours
- Unit 3: 6 theoretical + 6 practical = 12 hours
- Unit 4: 7 theoretical + 7 practical = 14 hours
- Unit 5: 7 theoretical + 7 practical = 14 hours

---

## Prerequisites | المتطلبات الأساسية

**Python Version**: Python 3.8+ required (3.10 or 3.11 recommended)

**Knowledge**: Students should have:
- Basic Python programming knowledge (variables, functions, classes)
- Familiarity with NumPy and Pandas (helpful but will be covered)

**Setup**: See `DOCS/` folder for detailed guides and `../requirements.txt` for dependencies

---

## 📁 Clean Folder Structure | هيكل المجلد النظيف

```
📦 Course Root
│
├── 📄 README.md                        📖 This file
├── 📄 START_HERE.md                    ⭐ READ THIS FIRST!
├── 📄 STUDENT_PROGRESS_CHECKLIST.md    ✅ Track progress
├── 📄 ../requirements.txt              📦 Dependencies (in root directory)
│
├── 📂 unit1-introduction/              📚 Unit 1 (7 examples)
├── 📂 unit2-cleaning/                  📚 Unit 2 (6 examples)
├── 📂 unit3-visualization/             📚 Unit 3 (7 examples)
├── 📂 unit4-ml-intro/                 📚 Unit 4 (12 examples)
├── 📂 unit5-scaling/                   📚 Unit 5 (7 examples)
├── 📖 DOCS/                            📄 Documentation
└── 📊 META/                            📈 Course Metadata
```

---

## Quick Start | البدء السريع

1. **Read:** `START_HERE.md`
2. **Install:** Libraries (see `DOCS/SETUP_INSTRUCTIONS.md`)
3. **Start:** `unit1-introduction/examples/01_data_science_intro.py` (or `.ipynb`)
4. **Track:** Use `STUDENT_PROGRESS_CHECKLIST.md`

---

## Course Learning Outcomes (CLOs) | مخرجات التعلم

**The detailed objectives of the training program are: For the trainee to be able to:**

*Note: Detailed CLOs for Course 05 (Scalable Data Science) are not explicitly listed in the PDF extraction. The course focuses on scalable data processing, cleaning, visualization, and modeling techniques using Python and NVIDIA RAPIDS.*

---

## 📚 Course Content | محتوى الدورة

### Unit 1: Introduction to Data Science | مقدمة في علم البيانات
**Folder**: `unit1-introduction/`

**Topics Covered:**
- Data science lifecycle
- Pandas DataFrame operations
- NumPy array operations
- cuDF introduction (GPU-accelerated DataFrame)
- Basic data exploration and statistics

**Start Here**: `unit1-introduction/examples/01_data_science_intro.py` (or `.ipynb`)

---

### Unit 2: Data Cleaning and Preparation | تنظيف البيانات وتحضيرها
**Folder**: `unit2-cleaning/`

**Topics Covered:**
- Advanced data loading techniques
- Missing value handling strategies
- Duplicate detection and removal
- Outlier detection and treatment
- Data transformation and normalization

---

### Unit 3: Data Visualization | تصوير البيانات
**Folder**: `unit3-visualization/`

**Topics Covered:**
- Matplotlib basics and customization
- Seaborn statistical visualizations
- Plotly interactive visualizations
- Dashboard creation
- 3D visualizations

---

### Unit 4: Machine Learning Introduction | مقدمة في تعلم الآلة
**Folder**: `unit4-ml-intro/`

**Topics Covered:**
- Linear regression
- Classification algorithms
- Model evaluation metrics
- CPU vs GPU performance comparison
- Learning curves

---

### Unit 5: Scaling and Production | التوسع والإنتاج
**Folder**: `unit5-scaling/`

**Topics Covered:**
- Dask for distributed computing
- NVIDIA RAPIDS workflows
- Production pipelines
- Performance optimization
- Large dataset handling
- Model deployment

---

## Learning Path | مسار التعلم

```
Python Basics (Prerequisites)
    ↓
Unit 1: Introduction to Data Science
    ↓
Unit 2: Data Cleaning and Preparation
    ↓
Unit 3: Data Visualization
    ↓
Unit 4: Machine Learning Introduction
    ↓
Unit 5: Scaling and Production
    ↓
Advanced Topics (Deep Learning, NLP, etc.)
```

---

## 📖 Documentation | التوثيق

All documentation is in the `DOCS/` folder:
- **SETUP_INSTRUCTIONS.md** - Installation and setup guide
- **INSTRUCTOR_GUIDE.md** - Teaching guide
- **QUICK_START.md** - Quick start guide
- **STUDENT_LEARNING_GUIDE.md** - Student learning guide

---

## 📄 Course Summary | ملخص الدورة

**Quick Reference:** `COURSE_SUMMARY.md` contains a comprehensive text summary of all course materials (PDFs/PPTX files).  
**مرجع سريع:** يحتوي `COURSE_SUMMARY.md` على ملخص نصي شامل لجميع مواد الدورة (ملفات PDF/PPTX).

This summary allows you to:
- Read course content without opening PDF/PPTX files
- Search through all materials quickly
- Review key concepts in text format
- Use as a study guide

---

## 📝 Assessment | التقييم

- **Quizzes:** `QUIZZES/` folder (all quizzes centralized)
- **Tests:** Each unit contains tests
- **Exercises:** Practice problems in each unit's `exercises/` folder

---

## 🆘 Need Help? | تحتاج مساعدة?

- **Installation issues?** → Check `DOCS/` folder
- **Questions?** → See `START_HERE.md` troubleshooting section
- **Progress tracking?** → Use `STUDENT_PROGRESS_CHECKLIST.md`

---

## 📦 Required Libraries | المكتبات المطلوبة

- **Data Processing:** pandas, numpy
- **Machine Learning:** scikit-learn
- **Visualization:** matplotlib, seaborn, plotly
- **Distributed Computing:** dask
- **Utilities:** jupyter, ipython
- **GPU Acceleration (Optional):** cuDF, RAPIDS (requires NVIDIA GPU)

See `../requirements.txt` for complete list with versions.

---

## 🖥️ GPU Requirements | متطلبات GPU

**Important:** This course works perfectly **WITHOUT a GPU**!

- **GPU is OPTIONAL** - All notebooks have pandas fallbacks
- **NVIDIA GPU recommended** for best performance with large datasets
- **CPU works fine** - You can complete the entire course using pandas (CPU)
- **cuDF/RAPIDS** are optional enhancements, not requirements

**If you don't have NVIDIA GPU:**
- ✅ Course works perfectly with pandas (CPU)
- ✅ All concepts are taught the same way
- ✅ You'll learn GPU benefits even without GPU hardware
- ✅ Performance will be slower on large datasets, but functionality is identical

**If you have NVIDIA GPU:**
- ✅ Install RAPIDS for GPU acceleration
- ✅ See 10-100x speedup on large datasets
- ✅ Experience production-level performance

**Installation (Optional):**
```bash
# Only if you have NVIDIA GPU
conda install -c rapidsai -c conda-forge cudf cuml
```

---

## 📊 Course Status | حالة الدورة

**Status:** ✅ Complete

- ✅ All 5 units present with examples and exercises
- ✅ All documentation complete
- ✅ All assessment materials ready
- ✅ Clean folder structure

---

**Created for**: AIAT 115 - Scalable Data Science  
**Language Support**: Arabic & English  
**Last Updated**: 2025

