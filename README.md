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

<img width="1070" height="809" alt="image" src="https://github.com/user-attachments/assets/8be0f6ac-2ecb-4773-8f1a-176720745f79" />
<img width="788" height="727" alt="image" src="https://github.com/user-attachments/assets/9c63fd82-3589-4566-9d3a-012902aeb06c" />
<img width="872" height="541" alt="image" src="https://github.com/user-attachments/assets/4a0469b5-9113-4787-97b0-a3bdb620cda8" />
<img width="828" height="356" alt="image" src="https://github.com/user-attachments/assets/ea37e40d-e1fb-4ba3-9f0d-600529881bb1" />
<img width="1919" height="807" alt="image" src="https://github.com/user-attachments/assets/7d4aa364-8d9c-4b0e-833e-e08be8be72ef" />
<img width="1893" height="778" alt="image" src="https://github.com/user-attachments/assets/7a2dbfed-d38e-48ec-978a-7aac71774d8a" />
<img width="1502" height="574" alt="image" src="https://github.com/user-attachments/assets/61d05089-2a0f-49a3-b1cf-90a13c8f4279" />
<img width="1704" height="598" alt="image" src="https://github.com/user-attachments/assets/60fd0851-458e-4b0b-9075-ad8179c55339" />
*   **Predictive AI Integration:**
<img width="1346" height="742" alt="image" src="https://github.com/user-attachments/assets/e392ff2b-4e0e-4c3b-82c4-30e4843b1296" />

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
