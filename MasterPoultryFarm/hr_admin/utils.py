from .models import *


MODEL_MAP = {
    
    'basic': EmployeeBasic,
    'contact': EmployeeContact,
    'access': EmployeeAccess,
    
    
    'job': EmployeeJob,
    'promotion': Promotions,
    'history': EmployeeHistory,
    'termination': EmployeeTermination,
    
    
    'payroll': EmployeePayroll,
    'bank': EmployeeBank,
    'tax': EmployeeTax,
    'insurance': EmployeeInsurance,
    
    'attendance': EmployeeAttendance,
    'performance': EmployeePerformance,
    'leave': EmployeeLeave,
    
    'training-programs': EmployeeTrainingPrograms,
    'training-records': EmployeeTrainingRecords,
    
    'address': OwnerAddress,
    'branches': Branches,
}

def get_model_by_name(name):
    return MODEL_MAP.get(name)