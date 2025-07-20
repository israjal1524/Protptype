
# LeapLaunch MVP Prototype

**LeapLaunch** is a prototype web application built with Streamlit to help international students in the United States navigate the job market. This MVP focuses on three core features: career path guidance, visa-friendly job listings, and resume scoring.

## Features

### 1. Career Path Navigator

Users can input their degree, skills, and area of interest to receive smart suggestions on career directions based on U.S. market trends and visa constraints.

### 2. Visa-Friendly Job Listings

Displays a curated list of companies and roles known for hiring international students on F1/OPT/CPT/H1B visas.

### 3. Resume Optimizer

A lightweight resume evaluation tool that provides a score and feedback based on the resume’s content and length.

---

## Tech Stack

* **Language:** Python
* **Framework:** [Streamlit](https://streamlit.io)
* **Runtime:** Local machine or Streamlit Cloud

---

## Getting Started

### Prerequisites

Make sure you have Python 3.7+ installed. Install dependencies using:

```bash
pip install streamlit
```

### Running the App

Save the source code as `app.py`, then run:

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

---

## Sample Use Cases

* International students exploring visa-compliant career options
* Career counselors assisting students with resume evaluation
* Quick demonstrations of data-driven career navigation tools

---

## Limitations

* This is a non-production MVP with static job listings
* Resume analysis is rudimentary and based on character length
* No user authentication or data persistence

---

## Next Steps

* Integrate LinkedIn and Handshake APIs for dynamic job listings
* Use AI to enhance resume evaluation and keyword scoring
* Add real-time visa sponsor lookup via government datasets
* Enable personalized dashboards with saved preferences

---

## License

This prototype is developed as part of a case assignment for a Product Management Internship at Leap. Not for commercial use.
