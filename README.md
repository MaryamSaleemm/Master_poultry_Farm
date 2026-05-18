# Master Poultry Farm Management System

A comprehensive, AI-powered web application designed to digitize and optimize operations for commercial wholesale egg production facilities. 

This system replaces legacy operational tracking by providing a secure administrative web dashboard for HR, finance, and asset management, while leveraging Machine Learning to forecast yields and optimize resources.

##  Key Features

*   **Centralized Administration:** A secure, web-based dashboard to manage daily farm operations, staff, and financial metrics.
*   **Predictive AI Integration:** Built-in machine learning pipelines that analyze daily operational logs (feed, water, mortality rates) to provide actionable insights.
    *   *Egg Production Model:* Forecasts daily yield outcomes using Linear Regression.
    *   *Feed Prediction Model:* Optimizes feed consumption based on flock health.
    *   *Environmental Monitoring:* Classifies health anomalies using Support Vector Machines (SVM) and Decision Trees.
*   **RESTful API Architecture:** A decoupled Django backend that serves database queries and AI predictions directly to the web interface via standardized API endpoints for real-time visualization.
<img width="1878" height="760" alt="image" src="https://github.com/user-attachments/assets/222b5c6a-fdd6-4b4f-9f66-79d6df7e66e7" />

##  Tech Stack

*   **Backend Framework:** Python, Django
*   **API Layer:** Django REST Framework (DRF)
*   **Machine Learning:** Scikit-learn, Pandas, NumPy
*   **Frontend / UI:** HTML5, CSS3, JavaScript
*   **Database:** SQLite

##  Installation & Setup

Follow these steps to run the project locally on your machine.

**1. Clone the repository**
```bash
git clone [https://github.com/yourusername/master-poultry-farm.git](https://github.com/yourusername/master-poultry-farm.git)
cd master-poultry-farm
