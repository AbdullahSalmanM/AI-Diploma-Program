# 🎓 START HERE - Welcome Students! | ابدأ من هنا - مرحباً بالطلاب!

## 👋 Welcome to Scalable Data Science Course | مرحباً بك في دورة علم البيانات القابل للتوسع

**If you're a new student, READ THIS FIRST!**  
**إذا كنت طالباً جديداً، اقرأ هذا أولاً!**

This file tells you exactly what to do on **Day 1** and how to navigate this course.  
هذا الملف يخبرك بالضبط ماذا تفعل في **اليوم الأول** وكيف تتنقل في هذه الدورة.

---

## ✅ Day 1 Checklist | قائمة اليوم الأول

Follow these steps in order. Don't skip any!  
اتبع هذه الخطوات بالترتيب. لا تتخطى أي خطوة!

### Step 1: Check Prerequisites | الخطوة 1: تحقق من المتطلبات الأساسية

**Before starting this course, you should have:**
- [ ] **Python 3.8 or higher** (Python 3.10 or 3.11 recommended)
- [ ] **Basic Python programming knowledge**: Variables, data types, functions, classes
- [ ] **Familiarity with NumPy and Pandas** (will be covered, but prior knowledge helps)

**If you're new to Python:**  
⚠️ Complete a Python basics course first! This course assumes you know Python fundamentals.

**If you don't have Python or have an old version:**  
Install Python 3.10 or 3.11 from [python.org](https://www.python.org/downloads/)

---

### Step 2: Check Python Version | الخطوة 2: تحقق من إصدار بايثون

Open your terminal/command prompt and type:

```bash
python --version
```

**You need:** Python 3.8 or higher (3.10 or 3.11 recommended)

**If you don't have Python or have an old version:**  
Install Python 3.10 or 3.11 from [python.org](https://www.python.org/downloads/)

---

### Step 3: Install Libraries | الخطوة 3: تثبيت المكتبات

**Follow the installation guide:** See `DOCS/` folder for detailed instructions.

**Quick method (if you're comfortable with terminal):**

```bash
# 1. Create virtual environment (recommended)
python -m venv venv

# 2. Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 3. Upgrade pip
pip install --upgrade pip

# 4. Install all libraries
pip install -r ../requirements.txt

# 5. Verify installation
pip check
```

**🖥️ GPU Installation (OPTIONAL):**
- **GPU is NOT required** - Course works perfectly on CPU!
- If you have NVIDIA GPU and want GPU acceleration:
  ```bash
  conda install -c rapidsai -c conda-forge cudf cuml
  ```
- All notebooks have pandas fallbacks - you can complete the course without GPU

**If you see errors:** Read `DOCS/SETUP_INSTRUCTIONS.md` for troubleshooting.

---

### Step 4: Read the Course Overview | الخطوة 4: اقرأ نظرة عامة على الدورة

**Open and read:** `README.md`

This file explains:
- What this course covers
- The 5 course units
- The learning path
- How units connect to each other

**Don't skip this!** It's only 5-10 minutes to read and will save you hours of confusion later.

---

### Step 5: Start with Unit 1 | الخطوة 5: ابدأ بالوحدة الأولى

**Open:** `unit1-introduction/examples/01_data_science_intro.py` (or `.ipynb`)

**Why this unit FIRST?**
- All other units use pandas and NumPy extensively
- You need to learn these libraries BEFORE learning data cleaning/visualization
- This unit teaches you the tools you'll use in all other units

**Don't jump ahead!** Each unit builds on the previous one.

---

## 📚 Learning Sequence | تسلسل التعلم

**Follow this exact order:**

```
1. ✅ Check Prerequisites (Python 3.8+)
   ↓
2. ✅ Install Libraries (Step 3 above)
   ↓
3. 📓 Unit 1: Introduction to Data Science
   ↓
4. 📓 Unit 2: Data Cleaning and Preparation
   ↓
5. 📓 Unit 3: Data Visualization
   ↓
6. 📓 Unit 4: Machine Learning Introduction
   ↓
7. 📓 Unit 5: Scaling and Production
```

**Important:** Each unit builds on the previous one. Don't skip units!

---

## 📋 Progress Tracker | متتبع التقدم

Use this checklist to track your progress:

### Setup & Preparation
- [ ] Python 3.8+ installed and verified
- [ ] Libraries installed successfully (`pip check` shows no errors)
- [ ] Read README.md
- [ ] Read this START_HERE.md file

### Units
- [ ] **Unit 1**: Introduction to Data Science
- [ ] **Unit 2**: Data Cleaning and Preparation
- [ ] **Unit 3**: Data Visualization
- [ ] **Unit 4**: Machine Learning Introduction
- [ ] **Unit 5**: Scaling and Production

**For detailed progress tracking, use:** `STUDENT_PROGRESS_CHECKLIST.md`

---

## 🆘 Need Help? | تحتاج مساعدة?

### Common Issues:

**Problem:** "No module named 'pandas'" or "No module named 'numpy'"  
**Solution:** You haven't installed libraries. Go back to Step 3.

**Problem:** "Python version too old"  
**Solution:** Install Python 3.10 or 3.11 from python.org

**Problem:** "I don't understand the notebook"  
**Solution:** 
1. Check if you have Python basics knowledge
2. Make sure you're doing units in order (1 → 2 → 3...)
3. Read the README.md in each unit folder

**Problem:** "Libraries conflict with each other"  
**Solution:** Use virtual environment (see Step 3)

---

## 📖 File Guide | دليل الملفات

**What each file/folder is for:**

| File/Folder | Purpose | When to Use |
|-------------|---------|-------------|
| `START_HERE.md` | **This file** - First thing to read | **Day 1, before anything else** |
| `README.md` | Course overview and structure | After reading START_HERE |
| `STUDENT_PROGRESS_CHECKLIST.md` | Track your progress | Throughout the course |
| `../requirements.txt` | List of libraries to install | During installation (Step 3) |
| `unit1-introduction/` | Unit 1 materials | Start here after setup |
| `unit2-cleaning/` | Unit 2 materials | After completing Unit 1 |
| `unit3-visualization/` | Unit 3 materials | After completing Unit 2 |
| `unit4-ml-intro/` | Unit 4 materials | After completing Unit 3 |
| `unit5-scaling/` | Unit 5 materials | After completing Unit 4 |
| `DOCS/` | Documentation and guides | When you need help |

---

## 🎯 Quick Start Summary | ملخص البدء السريع

**For students who want the shortest path:**

1. ✅ Check Python version (3.8+)
2. ✅ Install libraries: `pip install -r ../requirements.txt`
3. ✅ Read `README.md` (5 minutes)
4. ✅ Open `unit1-introduction/examples/01_data_science_intro.py` and start learning!

**That's it!** Everything else is in the unit folders.

---

## 💡 Tips for Success | نصائح للنجاح

1. **Don't rush:** Each unit builds on the previous one
2. **Practice:** Complete all exercises in each unit
3. **Experiment:** Try modifying the code examples
4. **Take notes:** Write down concepts you find difficult
5. **Review:** Before starting a new unit, review the previous one

---

## ✅ Ready to Start? | جاهز للبدء؟

If you've completed all steps above, you're ready!

**Next action:** Open `unit1-introduction/examples/01_data_science_intro.py` and begin your data science journey!

**Good luck!** 🚀  
**حظاً موفقاً!** 🚀

---

**Last Updated:** 2025  
**Course:** AIAT 115 - Scalable Data Science  
**Language Support:** Arabic & English

